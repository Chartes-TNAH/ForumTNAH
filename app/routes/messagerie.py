from ..app import app, db
from flask import render_template, flash, redirect, request, url_for, abort
from flask_login import current_user, login_required
from ..modeles.utilisateurs import AddConversationForm
from ..modeles.donnees import User, Message
from ..constantes import  POSTS_PAR_PAGE

# routes présentes dans l'ordre
# /messagerie
# /messagerie/<user_name>

@app.route('/messagerie', methods=['GET', 'POST'])
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
    # # je récupère ici tous les utilisateurs de manière à faire cette jointure tout de même
    users = User.query.all()

    return render_template('pages/messagerie/messagerie.html',
                           nom='Messagerie personnelle',
                           form=form,
                           utilisateurs=utilisateurs.items,
                           pagination=utilisateurs,
                           users=users)