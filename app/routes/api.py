from flask import request, url_for, jsonify
from urllib.parse import urlencode

from ..app import app
from ..constantes import RESULTATS_PAR_PAGE, API_ROUTE
from ..modeles.donnees import Post, User

# routes dans l'ordre
# /api/posts/<int:post_id>
# /api/posts
# /api/utilisateurs
# /api/utilisateurs/<int:user_id>

def Json_404():
    response = jsonify({"erreur": "Unable to perform the query"})
    response.status_code = 404
    return response


@app.route(API_ROUTE+"/posts/<int:post_id>")
def api_posts_single(post_id):
    """ Route permettant la recherche d'un post en particulier selon son id
    On s'inspirera de http://jsonapi.org/ faute de pouvoir trouver temps d'y coller à 100%
    :param post_id: id du post demandé
    :type post_id: int
    """
    try:
        query = Post.query.get(post_id)
        return jsonify(query.post_to_json())
    except:
        return Json_404()


@app.route(API_ROUTE+"/posts")
def api_posts_browse():
    """ Route permettant la recherche plein-texte et la navigation classique
    On s'inspirera de http://jsonapi.org/ faute de pouvoir trouver temps d'y coller à 100%
    """
    # q est très souvent utilisé pour indiquer une capacité de recherche
    motclef = request.args.get("q", None)
    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    if motclef:
        query = Post.query.filter(
            Post.post_message.like("%{}%".format(motclef))
        )
    else:
        query = Post.query

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
            post.post_to_json()
            for post in resultats.items
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
def api_utilisateurs_browse():
    """ Route permettant le retour des données des utilisateurs
    On s'inspirera de http://jsonapi.org/ faute de pouvoir trouver temps d'y coller à 100%
    """
    # q est très souvent utilisé pour indiquer une capacité de recherche
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