from ..app import app, db
from flask import render_template, flash, redirect, request, url_for, abort
from flask_login import current_user, login_required
from ..modeles.utilisateurs import PostForm, CommentForm
from ..modeles.donnees import Post, User, Comment
from ..constantes import POSTS_PAR_PAGE, COMMENTS_PAR_PAGE

# routes présentes dans l'ordre:
# /poster
# /editer_post
# /post


@app.route('/fil', methods=['GET', 'POST'])
def poster():
    """
    Permet de rendre le template d'édition d'un message sur le forum
    :return: template publier.html
    :rtype: template
    """
    # utilisation du formulaire PostForm()
    form = PostForm()
    # validate_on_submit n'admet que les méthodes POST, PUT, PATCH et DELETE; ici la méthode est donc POST
    if form.validate_on_submit():
        # récupération des données du formulaire dans la variable post; ces données sont assignées à chacun des champs de la base de données
        nouveau_post = Post(post_titre = form.titre.data,
                    post_message = form.message.data,
                    auteur = current_user)
        nouveau_post.nettoyer_mot(form.indexation.data)
        # ajout et commit des données dans la base de données
        db.session.add(nouveau_post)
        db.session.commit()
        flash("Votre message est maintenant publié")
        return redirect(url_for('poster'))

    # gestion de la pagination des posts
    page = request.args.get('page', 1, type=int)
    # récupération de l'ensemble des posts ordonnés par date de publication
    posts = Post.query.order_by(Post.post_date.desc()).paginate(page=int(page), per_page=int(POSTS_PAR_PAGE))

    # pour afficher la date du dernier commentaire
    # création d'un dictionnaire vide dans lequel seront insérés l'id du post en clé, et l'id du dernier commentaire en valeur
    dernier_commentaire = {}
    liste_posts = Post.query.all()
    for post in liste_posts:
        last_comment = post.comments.order_by(Comment.comment_date.desc()).first()
        dernier_commentaire[post.post_id] = last_comment

    return render_template('pages//posts/publier.html',
                           nom="Publier",
                           dernier_commentaire=dernier_commentaire,
                           form=form,
                           posts=posts.items,
                           pagination=posts)


@app.route('/editer_post/<int:id>', methods=['GET', 'POST'])
@login_required
def editer_post(id):
    """
    Route permettant de modifier ses propres posts; ce n'est possible qu'en étant connecté et en étant le créateur initial du post
    :param id: id du post concerné par la modification
    :type id: int
    :return: template editer_post.html
    :rtype: template
    """
    # récupération du post dont l'id a été fourni en paramètre dans la variable post
    post = Post.query.get_or_404(id)
    # vérification que l'utilisateur actuel(qui souhaite modifier) est bien l'auteur du post
    if current_user != post.auteur:
        abort(403)

    # utilisation du formulaire PostForm
    form = PostForm()
    # validate_on_submit n'admet que les méthodes POST, PUT, PATCH et DELETE; ici la méthode est donc POST
    if form.validate_on_submit():
        # récupération des données du formulaire dans la variable post; ces données sont assignées à chacun des champs de la base de données
        post.post_titre = form.titre.data
        post.post_message = form.message.data
        post.nettoyer_mot(form.indexation.data)

        # ajout et commit dans la base de données des modifications
        db.session.add(post)
        db.session.commit()
        flash("Le post a bien été mis à jour")
        return redirect(url_for('post', id=post.post_id))
    # remplissage des champs du formulaire
    form.titre.data = post.post_titre
    form.message.data = post.post_message
    form.indexation.data = post.post_indexation
    return render_template('pages/posts/editer_post.html',
                           form=form)


@app.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    """
    Fonction renvoyant le template Post avec un seul post désigné par l'id: permet de créer des liens pour chaque post de manière à pouvoir les partager
    :param id: id du post concerné
    :type id: int
    :return: template post.html
    :rtype: template
    """
    # récupération du post dont l'id a été fourni en paramètre dans la variable post
    post = Post.query.get_or_404(id)
    # récupération de l'utilisateur
    utilisateur = User.query.filter_by(user_name=current_user.user_name).first_or_404()

    # utilisation du formulaire CommentForm
    form = CommentForm()
    # validate_on_submit n'admet que les méthodes POST, PUT, PATCH et DELETE; ici la méthode est donc POST
    if form.validate_on_submit():
        # récupération des données du formulaire dans la variable post; ces données sont assignées à chacun des champs de la base de données
        comment = Comment(comment_message=form.message.data,
                          comment_post=post.post_id,
                          comment_auteur=current_user.id)
        # ajout et commit dans la base de données
        db.session.add(comment)
        db.session.commit()
        flash("Votre commentaire a été publié")
        return redirect(url_for('post', id=post.post_id))

    # gestion de la pagination
    page = request.args.get('page', 1, type=int)
    # récupération des commentaires de l'utilisateur
    comments = post.comments.order_by(Comment.comment_date.desc()).paginate(page=int(page), per_page=int(COMMENTS_PAR_PAGE))

    return render_template('pages/posts/post.html',
                           nom='Post',
                           posts=[post],
                           post=post.post_id,
                           form=form,
                           comments=comments.items,
                           pagination=comments)