import requests
import requests_cache

requests_cache.install_cache()
requests_cache.install_cache('qwant_cache')


def normalisation(mot):
    """
    Fonction permettant de normaliser une chaîne de caractères pour améliorer le recoupement entre les mêmes mots
    :param mot: chaîne de caractères correspondant au mot-clé
    :type mot: str
    :return: le mot normalisé
    :rtype: str
    """
    # remplacement des lettres minuscules et majuscules accentuées par des lettres non accentuées
    e = ["é","è","ê","ë", "È", "É", "Ê", "Ë"]
    for lettre in e:
        if lettre in mot:
            mot = mot.replace(lettre, "e")

    a = ["à", "â", "ä", "À", "Â", "Ä"]
    for lettre in a:
        if lettre in mot:
            mot = mot.replace(lettre, "a")

    i = ["Î", "Ï", "î", "ï"]
    for lettre in i:
        if lettre in mot:
            mot = mot.replace(lettre, "i")

    c = ["Ç", "ç"]
    for lettre in c:
        if lettre in mot:
            mot = mot.replace(lettre, "c")

    o = ["Ô", "ô", "ö", "Ö"]
    for lettre in o:
        if lettre in mot:
            mot = mot.replace(lettre, "o")

    oe = ["Œ", "œ"]
    for lettre in oe:
        if lettre in mot:
            mot = mot.replace(lettre, "oe")

    ae = ["Æ", "æ"]
    for lettre in ae:
        if lettre in mot:
            mot = mot.replace(lettre, "ae")

    u = ["ü", "û", "ù", "Ù", "Û", "Ü"]
    for lettre in u:
        if lettre in mot:
            mot = mot.replace(lettre, "u")

    y = ["ÿ", "Ÿ"]
    for lettre in y:
        if lettre in mot:
            mot = mot.replace(lettre, "y")

    # transformation du mot en majuscules
    mot_normalise = mot.upper()

    return mot_normalise

def get_first_image(tag):
    """
    Fonction permettant de renvoyer une seule url d'image à partir d'un tag
    :param tag: chaîne de caractères correspondant au mot clé d'un post
    :type tag: str
    :return: une url
    :rtype: str
    """

    # normalisation du mot entré
    tag = normalisation(tag)

    # requête
    r = requests.get("https://api.qwant.com/api/search/images",
        params={
            'count': 1,
            'q': tag,
            't': 'images',
            'safesearch': 1,
            'locale': 'fr_FR',
            'uiv': 4
        },
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    )

    reponse = r.json().get('data').get('result').get('items')
    if len(reponse):
        return reponse[0]["media"]
    return None