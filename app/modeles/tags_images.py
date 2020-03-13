import requests


def get_first_image(tag):
    """
    Fonction permettant de renvoyer une seule url à partir d'un tag
    :param tag: chaîne de caractères correspondant au mot clé d'un post
    :type tag: str
    :return: une url
    :rtype: str
    """

    r = requests.get("https://api.qwant.com/api/search/images",
        params={
            'count': 1,
            'q': tag,
            't': 'images',
            'safesearch': 1,
            'locale': 'en_US',
            'uiv': 4
        },
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    )

    response = r.json().get('data').get('result').get('items')
    return response[0]["media"]