users = 'INSERT INTO User(user_name, user_firstname, user_surname, user_mail, user_birthyear, user_promotion_date, user_description, user_last_seen, user_linkedin, user_github, user_password_hash, user_inscription_date)\
               VALUES ("Marie", "Marie", "Lefevre", "marie.lefevre@gmail.com", 1998, "2019-2021", "Je suis étudiante en M1 TNAH cette année, en Livres et Médias. Je suis inscrite ici pour en apprendre plus sur les domaines sur lesquels nous allons travailler en M2", "2020-02-17 23:58:44.761000", "https://www.linkedin.com/in/marie-lefevre", "https://www.github.com/marie-lefevre", "pbkdf2:sha256:150000$koCdnv2k$8cb86eb892afe0931cb2515daaac22c1a29655d55b1b57d028d17db354bcf23a", "2020-01-28 09:58:47.761000"),\
                      ("John", "John", "Dupont", "john.dupont@chartes.psl.eu", 1990, "2012-2014", "Je suis sorti en 2014 du M2 et je suis aujourd\'hui intervenant pour le cours de bases de données SQL dans ce même master. Si vous avez des questions, n\'hésitez pas.", "2020-03-24 12:58:47.761000", "https://www.linkedin.com/in/john-dupont", "https://www.github.com/john-dupont", "pbkdf2:sha256:150000$koCdnv2k$8cb86eb992afe0931cb2315dvfac22c1a29655d55b1b57d028d17db354bcf23a", "2015-08-26 21:57:26.729436"),\
                      ("Maxime", "Maxime", "Challon", "un_email@gmail.com", 1997, "2018-2020", "Les cours sont finis depuis quelques semaines. Ceci est le devoir de Python", "2020-03-31 15:31:54.000000", "https://www.linkedin.com/in/maxime-challon", "https://www.github.com/MaximeChallon", "pbkdf2:sha256:150000$koCdnv2k$8cb86eb992afe0931cb2315daaac22c1a29655d55b1b57d028d17db354bcf23a", "2020-01-01 00:00:00.000000"),\
                      ("Sarah", "Sarah", "Leconte", "sarahLeconte@free.fr", 1980, "2013-2015", "Je suis sortie en 2015 du master, puis j\'ai eu un CDD dans le public, où je suis encore actuellement. Ponctuellement, j\'enseigne l\'EAD aux M2.", "2020-03-08 21:25:44.761000", "https://www.linkedin.com/in/sarah-leconte", "https://www.github.com/sarah-leconte", "", "2018-04-25 21:10:25.2563247"),\
                      ("Jean", "Jean", "Du Chêne", "jean.duchene@chartes.psl.eu", 1997, "2018-2020", "Je suis encore étudiant en M2 cette année, mais la fin est proche. Je fais normalement (si la santé le permet) mon stage dans une bibliothèque de province, à Rodez. Je suis plutôt axé Bibliothèques.", "2020-03-15 12:45:44.761000", "https://www.linkedin.com/in/duchene-jean", "https://www.github.com/leCheneAveyronnais", "", "2020-02-12 21:55:28.2563247"),\
                      ("Fleur", "Fleur", "DesChamps", "fleur.deschamps@chartes.psl.eu", 1997, "2018-2020", "Je suis étudiante en M2 cette année. J\'ai une préférence pour les archives, donc je vais en stage à Lille aux archives départementales.", "2020-03-23 09:36:44.761000", "https://www.linkedin.com/in/fleurdeschamps", "https://www.github.com/fleurDeschamps", "", "2020-03-15 08:52:28.2563247"),\
                      ("Alice", "Alice", "Bourgeois", "bourgeois.a@yahoo.fr", 1997, "2018-2020", "Je suis comme beaucoup ici étudiante en M2 TNAH. J\'ai comme Fleur une préférence pour les archives. Mon stage sera en Italie, à Rome, aux archives pontificales, pendant 4 mois.", "2020-02-02 13:32:17.761000", "https://www.linkedin.com/in/aliceB", "https://www.github.com/BourgeoisAlice", "", "2020-01-14 08:52:28.2563247"),\
                      ("François", "François", "LeCoq", "lecoq_francois@gmail.com", 1994, "2015-2017", "Il y a peu, j\'étais encore en master. Ce cursus m\'a beaucoup plu donc si vous avez des questions sur son déroulement, je répondrai avec plaisir. Actuellement, je travaille sur des bases de données NO-SQL dans une entreprise. J\'utilise aussi beaucoup Python pour les traitements de données.", "2020-03-30 13:54:36.761000", "https://www.linkedin.com/in/lecoqf", "https://www.github.com/LecoqDeParis", "", "2019-05-25 13:54:36.761000")'

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
                VALUES ("Python"), ("HTML"), ("JavaScript"), ("JSON"), ("CSS"), ("SQL"),\
                 ("NO-SQL"), ("SPARQL"), ("RDF"), ("XML-EAD"), ("XML-TEI"), ("XML-Path"),\
                 ("GitHub"), ("XML-Schema"), ("XSLT"), ("IIIF")'

skills = 'INSERT INTO skills\
         VALUES (1, 2), (1, 5),\
          (2, 6), (2, 1), (2, 10), (2, 11), (2, 12), (2, 14), (2, 15),\
          (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16),\
          (4, 1), (4, 10), (4, 12), (4, 14), (4, 2), (4, 16),\
          (5, 1), (5, 2), (5, 6), (5, 8), (5, 9), (5, 13), (5, 16),\
          (6, 1), (6, 4), (6, 7), (6, 10), (6, 15), (6, 16),\
          (7, 2), (7, 3), (7, 4), (7, 5), (7, 7), (7, 8), (7, 9), (7, 10), (7, 12), (7, 13), (7, 14), (7, 15),\
          (8, 12), (8, 9), (8, 8), (8, 6), (8, 1), (8, 7)'

followers = 'INSERT INTO followers\
                VALUES (1, 2), (1, 4), (1, 6),\
                 (2, 1), (2, 3), (2, 4), (2, 5),\
                 (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),\
                 (4, 1), (4, 2), (4, 6), (4, 7),\
                 (5, 2), (5, 3), (5, 4), (5, 6), (5, 8),\
                 (6, 1), (6, 2), (6, 3), (6, 5), (6, 7), (6, 8),\
                 (7, 4), (7, 6), (7, 8), (7, 3),\
                 (8, 1), (8, 2), (8, 3), (8, 7), (8, 6)'

messages = 'INSERT INTO Message(message_message, message_html, message_date, message_expediteur_id, message_destinataire_id)\
           VALUES ("#Bonjour\n Mon **message** est très important", "<h1>Bonjour</h1><br><p>Mon <i>message</i> est très important</p>","2020-03-19 10:00:44.761000", 1, 3),\
            ("#Bonjour\n Mon **message** est très peu important", "<h1>Bonjour</h1><br><p>Mon <i>message</i> est très peu important</p>","2020-02-20 10:00:44.761000", 3, 1),\
             ("#Bonjour\n Mon **message** est très très important", "<h1>Bonjour</h1><br><p>Mon <i>message</i> est très très important</p>","2020-01-18 10:00:44.761000", 1, 3)'