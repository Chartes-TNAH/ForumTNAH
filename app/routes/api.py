from flask import request, url_for, jsonify
from urllib.parse import urlencode

from ..app import app
from ..constantes import POSTS_PAR_PAGE, API_ROUTE
from ..modeles.donnees import Post


def Json_404():
    response = jsonify({"erreur": "Unable to perform the query"})
    response.status_code = 404
    return response


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
        resultats = query.paginate(page=page, per_page=POSTS_PAR_PAGE)
    except Exception:
        return Json_404()

    dict_resultats = {
        "links": {
            "self": request.url
        },
        "data": [
            post.post_to_json()
            for post in resultats.items
        ]
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
    return response