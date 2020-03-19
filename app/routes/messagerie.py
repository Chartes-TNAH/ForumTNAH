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
    # récupération des conversations de l'utilisateur
    messages = Message.query.filter(Message.message_destinataire_id == current_user.id).order_by(Message.message_date.desc()).paginate(page=int(page), per_page=int(POSTS_PAR_PAGE))

    return render_template('pages/messagerie/messagerie.html',
                           nom='Messagerie personnelle',
                           form=form,
                           messages=messages.items,
                           pagination=messages)