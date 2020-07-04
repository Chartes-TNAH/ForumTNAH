from ..app import app, db
from flask import render_template, flash, redirect, request, url_for, abort
from flask_login import current_user, login_required
from sqlalchemy import or_
from ..modeles.utilisateurs import AddConversationForm, PrivateMessageForm
from ..modeles.donnees import User, Message
from ..constantes import  POSTS_PAR_PAGE

"""
routes présentes dans l'ordre
/messagerie
/messagerie/<user_name>
"""

@app.route('/messagerie', methods=['GET', 'POST'])
@login_required
def messagerie():
    # gestion du formulaire de premier message privé avec un utilisateur
    utilisateurs_disponibles = User.query.all()
    # création de la liste de tuples pour le SelectField du formulaire
    utilisateurs_liste = [(u.id, u.user_name) for u in utilisateurs_disponibles]
    form = AddConversationForm()
    # passage de la liste dans le formulaire
    form.destinataire_id.choices = utilisateurs_liste
    if form.validate_on_submit():
        destinataire = Message(message_destinataire_id=form.destinataire_id.data,
                               message_expediteur_id=current_user.id,
                               message_message=form.message.data)
        db.session.add(destinataire)
        db.session.commit()
        flash("Message envoyé")
        return redirect(url_for('messagerie'))

    # gestion de la pagination des posts
    page = request.args.get('page', 1, type=int)
    # récupération des personnes distinctes de conversation
    utilisateurs  = Message.query.filter(Message.message_destinataire_id == current_user.id).\
        group_by(Message.message_expediteur_id).paginate(page=int(page), per_page=int(POSTS_PAR_PAGE))

    # en raisons de difficultés à effectuer la double jointure sur User à partir de Message (erreur AmbiguousForeignKeys),
    # je récupère ici tous les utilisateurs de manière à faire cette jointure tout de même
    users = User.query.all()

    return render_template('pages/messagerie/messagerie.html',
                           nom='Messagerie personnelle',
                           form=form,
                           utilisateurs=utilisateurs.items,
                           pagination=utilisateurs,
                           users=users)


@app.route('/messagerie/<user_name>', methods=['GET', 'POST'])
@login_required
def conversation(user_name):
    # le choix a été fait de ne pas paginer cette page car c'est un fil de discussion
    # récupération de l'id de l'utilisateur
    utilisateur = User.query.filter(User.user_name == user_name).first()
    # récupération des messages concernés, ordonnés dans l'ordre chronologique descendant
    messages = Message.query.filter(or_(Message.message_destinataire_id == current_user.id, Message.message_destinataire_id == utilisateur.id))\
        .filter(or_(Message.message_expediteur_id == utilisateur.id, Message.message_expediteur_id == current_user.id))\
        .order_by(Message.message_date.desc()).all()

    # formulaire de discussion
    form = PrivateMessageForm()
    if form.validate_on_submit():
        message = Message(message_message=form.message.data,
                          message_expediteur_id=current_user.id,
                          message_destinataire_id=utilisateur.id)
        db.session.add(message)
        db.session.commit()
        flash("Votre message a bien été envoyé")
        return redirect(url_for('conversation', user_name=user_name))

    return render_template('pages/messagerie/conversation.html',
                           nom="Conversation avec "+user_name,
                           messages=messages,
                           utilisateur=utilisateur,
                           form=form)