from warnings import warn

DEBUG = True

POSTS_PAR_PAGE = 3
POSTS_PAR_PAGE_DISCUSSION = 10
COMMENTS_PAR_PAGE = 5

SECRET_KEY = "JE SUIS UN SECRET !"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)