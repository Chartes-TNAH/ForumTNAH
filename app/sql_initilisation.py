users = 'INSERT INTO User(user_name, user_firstname, user_surname, user_mail, user_birthyear, user_promotion_date,\
                        user_description, user_last_seen, user_linkedin, user_github, user_password_hash)\
                      VALUES ("John", "John", "DUPONT", "john@example.com", "1995", "2016-2018",\
                                "Je suis un employé lambda", "2020-02-17 23:58:44.761000",\
                                "https://www.linkedin.com/in/john-dupont", "https://www.github.com/john-dupont", ""),\
                      ("Marie", "Marie", "LEFEVRE", "marie@chartes.psl.eu", "1992", "2014-2016",\
                        "Je suis fonctionnaire dans un ministère", "2020-02-24 12:58:47.761000",\
                        "https://www.linkedin.com/in/marie-lefevre", "https://www.github.com/marie-lefevre", ""),\
                      ("Maxime", "Maxime", "CHALLON", "maxime.challon@undomaine.com", "1997", "2018-2020",\
                        "Je suis encore étudiant pour quelques mois.", "2020-03-11 09:58:47.761000",\
                        "https://www.linkedin.com/in/maxime-challon", "https://www.github.com/MaximeChallon",\
                        "pbkdf2:sha256:150000$koCdnv2k$8cb86eb992afe0931cb2315daaac22c1a29655d55b1b57d028d17db354bcf23a")'

posts = 'INSERT INTO Post(post_titre, post_message, post_date, html, post_auteur, post_indexation)\
                      VALUES ("Un renseignement serait le bienvenu", "#Bonjour, voici mon titre \n Mon message ici.",\
                                "2020-03-08 21:25:44.761000", "<h1>Bonjour, voici mon titre</h1><br/><p>Mon message ici</p>", 1, "BNF"),\
                      ("Un nouveau message sur le forum", "#Bonjour, voici un nouveau message \n Mon message ici.",\
                        "2020-03-12 08:25:44.761000", "<h1>Bonjour, voici un nouveau message</h1><br/><p>Mon message ici</p>", 2, "BNF"),\
                      ("Quelque chose", "#RE \n Mon message ici.",\
                        "2020-03-14 08:28:44.761000", "<h1>RE</h1><br/><p>Mon message ici</p>", 2, "Archives")'

comments = 'INSERT INTO Comment(comment_message, comment_html, comment_date, comment_auteur, comment_post)\
                          VALUES ("#Bonjour \n Mon commentaire est utile.", "<h1>Bonjour</h1><br/><p>Mon commentaire est utile</p>",\
                                    "2020-03-02 21:32:44.761000", 1, 2),\
                          ("#Bonjour \n Mon commentaire est utile et novateur.", "<h1>Bonjour</h1><br/><p>Mon commentaire est utile et novateur.</p>",\
                            "2020-02-27 10:00:44.761000", 2, 1)'

cvs = 'INSERT INTO CV(cv_nom_poste, cv_nom_employeur, cv_ville, cv_annee_debut, cv_annee_fin, cv_description_poste, cv_utilisateur)\
                              VALUES ("Ingénieur de la donnée", "BNF", "Paris", "2019", "2020",\
                                        "Je traite certaines des métadonnées de la BNF",1),\
                              ("Chef de projet numérique", "Ministère X", "Paris", "2017", "2019",\
                                "Je gère des gens et je fais un peu de tout", 2),\
                              ("Ingénieur", "Une entreprise", "Strasbourg", "2019","",\
                               "Je traite beaucoup de données en tant que prestataire dans les institutions", 2)'

competences ='INSERT INTO Competences(competence_label)\
                VALUES ("IIIF"), ("Python"), ("SQL") '

skills = 'INSERT INTO skills\
         VALUES (1, 1), (1, 3), (2, 2)'

messages = 'INSERT INTO Message(message_message, message_html, message_date, message_expediteur_id, message_destinataire_id)\
           VALUES ("#Bonjour\n Mon **message** est très important", "<h1>Bonjour</h1><br><p>Mon <i>message</i> est très important</p>","2020-03-19 10:00:44.761000", 1, 3),\
            ("#Bonjour\n Mon **message** est très peu important", "<h1>Bonjour</h1><br><p>Mon <i>message</i> est très peu important</p>","2020-02-20 10:00:44.761000", 3, 1),\
             ("#Bonjour\n Mon **message** est très très important", "<h1>Bonjour</h1><br><p>Mon <i>message</i> est très très important</p>","2020-01-18 10:00:44.761000", 1, 3)'