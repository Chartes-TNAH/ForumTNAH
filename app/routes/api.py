from flask import request, url_for, jsonify, render_template
from flask_login import login_required
from urllib.parse import urlencode

from ..app import app
from ..constantes import RESULTATS_PAR_PAGE, API_ROUTE
from ..modeles.donnees import Post, User

"""
routes dans l'ordre:
/api/posts/<int:post_id>
/api/posts
/api/utilisateurs
/api/utilisateurs/<int:user_id>
"""

# gestion des erreurs 404 pour l'API
def Json_404():
    response = jsonify({"erreur": "Unable to perform the query"})
    response.status_code = 404
    return response


@app.route(API_ROUTE)
@login_required
def api():
    return render_template('pages/api.html',
                           nom='Accueil API')


@app.route(API_ROUTE+"/posts/<int:post_id>")
@login_required
def api_posts_single(post_id):
    """
    Route permettant la recherche d'un post en particulier selon son id.
    :param post_id: id du post demandé
    :type post_id: int
    """
    try:
        query = Post.query.get(post_id)
        return jsonify(query.post_to_json())
    except:
        return Json_404()


@app.route(API_ROUTE+"/posts")
@login_required
def api_posts_browse():
    """
    Route permettant la recherche plein-texte et la navigation classique.
    """
    # q est le paramètre d'URL prenant la recherche utilisateur
    motclef = request.args.get("q", None)
    # comme il y a un nombre maximal de résultats par page(RESULTATS_PAR_PAGE), plusieurs pages de réponses peuvent exister
    # lors d'une recherche; leur numéro est donc défini à 1 au départ
    page = request.args.get("page", 1)

    # si page est une chaîne de caractères et qu'il est possible de la passer en nombre, alors on le fait, sinon, page est définie sur 1
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    # on cherche à retourner les résultats pour le mot-clé donné; s'il n'y a rien, on retourne l'ensemble des posts
    if motclef:
        query = Post.query.filter(
            Post.post_message.like("%{}%".format(motclef))
        )
    else:
        query = Post.query

    # récupération des résultats
    try:
        resultats = query.paginate(page=page, per_page=RESULTATS_PAR_PAGE)
    except Exception:
        return Json_404()

    # création du dictionnaire accueillant les données récupérées
    dict_resultats = {
        "jsonapi": {
            "version": "1.0"
        },
        "links": {
            "self": request.url
        },
        "data": [
            post.post_to_json()
            for post in resultats.items
        ],
        "meta": {
            "copyright": "2020 - Ecole nationale des Chartes",
            "results": resultats.total
        }
    }

    # gestion des multi-pages (précédentes et suivantes)
    if resultats.has_next:
        arguments = {
            "page": resultats.next_num
        }
        if motclef:
            arguments["q"] = motclef
        dict_resultats["links"]["next"] = url_for("api_posts_browse", _external=True)+"?"+urlencode(arguments)

    if resultats.has_prev:
        arguments = {
            "page": resultats.prev_num
        }
        if motclef:
            arguments["q"] = motclef
        dict_resultats["links"]["prev"] = url_for("api_posts_browse", _external=True)+"?"+urlencode(arguments)

    response = jsonify(dict_resultats)
    response.headers['Content-Type'] = 'application/vnd.api+json'
    return response


@app.route(API_ROUTE+"/utilisateurs")
@login_required
def api_utilisateurs_browse():
    """
    Route permettant le retour des données des utilisateurs
    """
    # les commentaires sont similaires à ceux de la route api_posts_browse
    motclef = request.args.get("q", None)
    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    if motclef:
        query = User.query.filter(
            User.user_name.like("%{}%".format(motclef))
        )
    else:
        query = User.query

    try:
        resultats = query.paginate(page=page, per_page=RESULTATS_PAR_PAGE)
    except Exception:
        return Json_404()

    dict_resultats = {
        "jsonapi": {
            "version": "1.0"
        },
        "links": {
            "self": request.url
        },
        "data": [
            user.user_to_json()
            for user in resultats.items
        ],
        "meta": {
            "copyright": "2020 - Ecole nationale des Chartes",
            "results": resultats.total
        }
    }

    if resultats.has_next:
        arguments = {
            "page": resultats.next_num
        }
        if motclef:
            arguments["q"] = motclef
        dict_resultats["links"]["next"] = url_for("api_utilisateurs_browse", _external=True)+"?"+urlencode(arguments)

    if resultats.has_prev:
        arguments = {
            "page": resultats.prev_num
        }
        if motclef:
            arguments["q"] = motclef
        dict_resultats["links"]["prev"] = url_for("api_utilisateurs_browse", _external=True)+"?"+urlencode(arguments)

    response = jsonify(dict_resultats)
    response.headers['Content-Type'] = 'application/vnd.api+json'
    return response


@app.route(API_ROUTE+"/utilisateurs/<int:user_id>")
@login_required
def api_utilisateurs_single(user_id):
    """
    Route permettant la recherche d'un utilisateur en particulier selon son id
    :param post_id: id de l'utilisateur demandé
    :type post_id: int
    """
    try:
        query = User.query.get(user_id)
        return jsonify(query.user_to_json())
    except:
        return Json_404()