users = 'INSERT INTO User(user_name, user_firstname, user_surname, user_mail, user_birthyear, user_promotion_date, user_description, user_last_seen, user_linkedin, user_github, user_password_hash, user_inscription_date)\
               VALUES ("Marie", "Marie", "Lefevre", "marie.lefevre@gmail.com", 1998, "2019-2021", "Je suis étudiante en M1 TNAH cette année, en Livres et Médias. Je suis inscrite ici pour en apprendre plus sur les domaines sur lesquels nous allons travailler en M2", "2020-02-29 23:58:44.761000", "https://www.linkedin.com/in/marie-lefevre", "https://www.github.com/marie-lefevre", "pbkdf2:sha256:150000$koCdnv2k$8cb86eb892afe0931cb2515daaac22c1a29655d55b1b57d028d17db354bcf23a", "2020-01-28 09:58:47.761000"),\
                      ("John", "John", "Dupont", "john.dupont@chartes.psl.eu", 1990, "2012-2014", "Je suis sorti en 2014 du M2 et je suis aujourd\'hui intervenant pour le cours de bases de données SQL dans ce même master. Si vous avez des questions, n\'hésitez pas.", "2020-03-24 12:58:47.761000", "https://www.linkedin.com/in/john-dupont", "https://www.github.com/john-dupont", "pbkdf2:sha256:150000$koCdnv2k$8cb86eb992afe0931cb2315dvfac22c1a29655d55b1b57d028d17db354bcf23a", "2015-08-26 21:57:26.729436"),\
                      ("Maxime", "Maxime", "Challon", "un_email@gmail.com", 1997, "2018-2020", "Les cours sont finis depuis quelques semaines. Ceci est le devoir de Python", "2020-03-31 15:31:54.000000", "https://www.linkedin.com/in/maxime-challon", "https://www.github.com/MaximeChallon", "pbkdf2:sha256:150000$koCdnv2k$8cb86eb992afe0931cb2315daaac22c1a29655d55b1b57d028d17db354bcf23a", "2020-01-01 00:00:00.000000"),\
                      ("Sarah", "Sarah", "Leconte", "sarahLeconte@free.fr", 1980, "2013-2015", "Je suis sortie en 2015 du master, puis j\'ai eu un CDD dans le public, où je suis encore actuellement. Ponctuellement, j\'enseigne l\'EAD aux M2.", "2020-03-08 21:25:44.761000", "https://www.linkedin.com/in/sarah-leconte", "https://www.github.com/sarah-leconte", "", "2018-04-25 21:10:25.2563247"),\
                      ("Jean", "Jean", "Du Chêne", "jean.duchene@chartes.psl.eu", 1997, "2018-2020", "Je suis encore étudiant en M2 cette année, mais la fin est proche. Je fais normalement (si la santé le permet) mon stage dans une bibliothèque de province, à Rodez. Je suis plutôt axé Bibliothèques.", "2020-03-15 12:45:44.761000", "https://www.linkedin.com/in/duchene-jean", "https://www.github.com/leCheneAveyronnais", "", "2020-02-12 21:55:28.2563247"),\
                      ("Fleur", "Fleur", "DesChamps", "fleur.deschamps@chartes.psl.eu", 1997, "2018-2020", "Je suis étudiante en M2 cette année. J\'ai une préférence pour les archives, donc je vais en stage à Lille aux archives départementales.", "2020-03-23 09:36:44.761000", "https://www.linkedin.com/in/fleurdeschamps", "https://www.github.com/fleurDeschamps", "", "2020-03-15 08:52:28.2563247"),\
                      ("Alice", "Alice", "Bourgeois", "bourgeois.a@yahoo.fr", 1997, "2018-2020", "Je suis comme beaucoup ici étudiante en M2 TNAH. J\'ai comme Fleur une préférence pour les archives. Mon stage sera en Italie, à Rome, aux archives pontificales, pendant 4 mois.", "2020-02-02 13:32:17.761000", "https://www.linkedin.com/in/aliceB", "https://www.github.com/BourgeoisAlice", "", "2020-01-14 08:52:28.2563247"),\
                      ("François", "François", "LeCoq", "lecoq_francois@gmail.com", 1994, "2015-2017", "Il y a peu, j\'étais encore en master. Ce cursus m\'a beaucoup plu donc si vous avez des questions sur son déroulement, je répondrai avec plaisir. Actuellement, je travaille sur des bases de données NO-SQL dans une entreprise. J\'utilise aussi beaucoup Python pour les traitements de données.", "2020-03-30 13:54:36.761000", "https://www.linkedin.com/in/lecoqf", "https://www.github.com/LecoqDeParis", "", "2019-05-25 13:54:36.761000")'

posts = 'INSERT INTO Post(post_titre, post_message, post_date, html, post_auteur, post_indexation)\
               VALUES ("Recherche de stage pour l\'an prochain", "Bonjour à tous, \n Je cherche un stage pour le M2 l\'an prochain. J\'ai une préférence pour les **bibliothèques**. Auriez-vous des pistes? \n Merci pour vos réponses!", "2020-02-18 12:58:24.236587", "<p>Bonjour à tous, \n Je cherche un stage pour le M2 l\'an prochain. J\'ai une préférence pour les <strong>bibliothèques</strong>. Auriez-vous des pistes? \n Merci pour vos réponses!</p>", 1, "stage"),\
                      ("IIIF et la BNF", "Bonjour à tous, \n J\'ai entendu parlé de la possibilité de récupérer des images de la *BNF* par une URL spéciale. Quelqu\'un connaîtrait-il des ressources permettant d\'apprendre à se servir de IIIF? ", "2020-02-27 18:32:24.236587", "<p>Bonjour à tous, \n J\'ai entendu parlé de la possibilité de récupérer des images de la <em>BNF</em> par une URL spéciale. Quelqu\'un connaîtrait-il des ressources permettant d\'apprendre à se servir de IIIF? </p>", 1, "IIIF"),\
                      ("Offres d\'emploi", "Bonjour à tous, \n Je pense qu\'il serait intéressant de pouvoir poster sur ce forum des offres d\'emploi, notamment de la part des anciens, pour que les nouveaux étudiants sortants et les autres membres puissent être au courant des offres en cours.", "2020-01-28 22:52:24.236587", "<p>Bonjour à tous, <br> Je pense qu\'il serait intéressant de pouvoir poster sur ce forum des offres d\'emploi, notamment de la part des anciens, pour que les nouveaux étudiants sortants et les autres membres puissent être au courant des offres en cours.</p>", 1, "emploi"),\
                      ("Devoir d\'Olivier Canteaut", "Bonjour à tous, Peut-être vous en souvenez-vous, mais nous avons un devoir de culture numérique à rendre pour Oliver Canteaut. Quelqu\'un aurait-il des idées de sujet? \n Merci d\'avance", "2020-02-03 09:18:24.236587", "<p>Bonjour à tous,<br> Peut-être vous en souvenez-vous, mais nous avons un devoir de culture numérique à rendre pour Oliver Canteaut. <br> Quelqu\'un aurait-il des idées de sujet? \n Merci d\'avance</p>", 1, "humanites_numeriques"),\
                      ("Une offre d\'emploi intéressante", "Bonjour à tous, \n Je viens de tomber par hasard sur une offre d\'emploi qui peut peut-être intéresser certains d\'entre vous, les plus bibliophiles. \n [Voici le lien](http://www.jobculture.fr/emploi-culture/une-bibliothecaire-ludothecaire-chelles-77/) \ Bonne journée", "2020-02-13 21:18:35.258741", "<p>Bonjour à tous, </p><p> Je viens de tomber par hasard sur une offre d\'emploi qui peut peut-être intéresser certains d\'entre vous, les plus bibliophiles. </p><p> <a href=\'http://www.jobculture.fr/emploi-culture/une-bibliothecaire-ludothecaire-chelles-77/\'>Voici le lien</a> </p><p> Bonne journée</p>", 1, "emploi"),\
                      ("Gallica", "Bonjour, \n De passage sur Gallica, j\'ai remarqué que la navigation entre les pages est laborieuse avec leur menu déroulant. Quelqu\'un sait-il si cela sera bientôt corrigé car comment trouver la bonne page quand tout est marqué `NP`?", "2020-02-14 21:18:35.258741", "<p>Bonjour, </p><p> De passage sur Gallica, j\'ai remarqué que la navigation entre les pages est laborieuse avec leur menu déroulant. Quelqu\'un sait-il si cela sera bientôt corrigé car comment trouver la bonne page quand tout est marqué <code>NP</code>?</p>", 1, "Gallica"),\
                      ("bibliothèques", "Bonjour, \n La création de *bibliothèques numériques* est aujourd\'hui très répandue. Est-ce une tendance dans laquelle il faut s\'engager? Ou bien n\'est-ce qu\'un phénomène qui risque de disparaître dans quelques années. Je me pose cette question car de toutes petites bibliothèques s\'engagent dans cette aventure avec ~~notre~~ l\'argent public, et on peut s\'interroger sur leur utilité dans des communes de 1000 habitants.", "2020-02-16 23:18:35.258741", "<p>Bonjour, </p><p> La création de <em>bibliothèques numériques</em> est aujourd\'hui très répandue. Est-ce une tendance dans laquelle il faut s\'engager? Ou bien n\'est-ce qu\'un phénomène qui risque de disparaître dans quelques années. Je me pose cette question car de toutes petites bibliothèques s\'engagent dans cette aventure avec <del>notre</del> l\'argent public, et on peut s\'interroger sur leur utilité dans des communes de 1000 habitants.</p>", 1, "bibliotheques"),\
                      ("Du nouveau aux AN", "Les Archives Nationales ont récemment mis en ligne de nouveaux inventaires sur les DeThou! \n Allez les consulter, ils sont très intéressants!", "2020-02-16 08:12:28.258964", "<p>Les Archives Nationales ont récemment mis en ligne de nouveaux inventaires sur les DeThou! <br> Allez les consulter, ils sont très intéressants!</p>", 1, "archives"),\
                      ("Total embauche une nouvelle fois!", "# Une offre très intéressante \n Si vous rêvez de quitter le public pour rejoindre le privé, vous allez être ravis par cette offre d\'emploi chez Total: ils recrutent un **chef de projet numérique** pour leur bibliothèque numérique au *Cananda*. \n N\'hésitez plus, les chartistes, et encore mieux, les chartistes TNAH, sont les bienvenus!", "2016-08-16 08:18:28.258964", "<h1>Une offre très intéressante</h1><p> Si vous rêvez de quitter le public pour rejoindre le privé, vous allez être ravis par cette offre d\'emploi chez Total: ils recrutent un <strong>chef de projet numérique</strong> pour leur bibliothèque numérique au <em>Cananda</em>. </p><p> N\'hésitez plus, les chartistes, et encore mieux, les chartistes TNAH, sont les bienvenus!</p>", 2, "emploi"),\
                      ("SQL/NOSQL", "Bonjour tout le monde, \n Un collègue m\'a demandé hier une liste de système de bases de données NOSQL. J\'en profite pour vous faire partager cette information également: une liste non exhaustive peut être trouvée [ici](https://www.ambient-it.net/top-meilleures-db-nosql-2019/)", "2019-04-22 08:58:28.258964", "<p>Bonjour tout le monde, </p><p>Un collègue m\'a demandé hier une liste de système de bases de données NOSQL. J\'en profite pour vous faire partager cette information également: une liste non exhaustive peut être trouvée <a href=\'https://www.ambient-it.net/top-meilleures-db-nosql-2019/\'>ici</a></p>", 2, "databases"),\
                      ("A destination des M1, stage d\'été", "Bonjour les M1 \n Peut-être cherchez-vous un stage pour cet été. Voici une offre qui peut-être intéressante pour une première approche: [ici](http://www.jobculture.fr/emploi-culture/offre-de-stage-gratifie-4-stagiaires-au-service-culture-art-et-territoire/)", "2018-04-30 01:25:36.235789", "<p>Bonjour les M1 </p><p> Peut-être cherchez-vous un stage pour cet été. Voici une offre qui peut-être intéressante pour une première approche: <a href=\'http://www.jobculture.fr/emploi-culture/offre-de-stage-gratifie-4-stagiaires-au-service-culture-art-et-territoire/\'>ici</a></p>", 2, "stage"),\
                      ("Archives départementales de l\'Aude", "A tous les passionnés d\'archivistique, et aux rares venant de l\'Aude, notez bien que [l\'ancien site des archives départementales](http://audealaculture.fr) est devenu [http://audealaculture.fr/archives/nouveau-site-archives-departementales](http://audealaculture.fr/archives/nouveau-site-archives-departementales).", "2020-03-13 21:25:36.235789", "<p>A tous les passionnés d\'archivistique, et aux rares venant de l\'Aude, notez bien que <a href=\'http://audealaculture.fr\'>l\'ancien site des archives départementales</a> est devenu <a href=\'http://audealaculture.fr/archives/nouveau-site-archives-departementales\'>http://audealaculture.fr/archives/nouveau-site-archives-departementales</a>.</p>", 2, "archives"),\
                      ("Colloque de TEI", "Je vous signale à tous **le** colloque de l\'année à Lyon sur la TEI : [https://www.msh-lse.fr/evenements/tei-connect-animate-innovate](https://www.msh-lse.fr/evenements/tei-connect-animate-innovate). J\'y serai bien évidemment présent.", "2015-10-01 06:24:53.789654", "<p>Je vous signale à tous <strong>le</strong> colloque de l\'année à Lyon sur la TEI : <a href=\'https://www.msh-lse.fr/evenements/tei-connect-animate-innovate\'>https://www.msh-lse.fr/evenements/tei-connect-animate-innovate</a>. J\'y serai bien évidemment présent.</p>", 2, "humanites_numeriques"),\
                      ("De l\'intérêt des bibliothèques numériques", "Avec cette crise sanitaire, Gallica propose avec l\'Education nationale des EPUB éducatifs pour pallier la fermeture des écoles. C\'est très intéressant. \n [lien](https://gallica.bnf.fr/blog/18012018/150-epub-gallica-selectionnes-par-le-ministere-de-leducation-nationale?mode=desktop)", "2020-03-24 17:42:35.852741", "<p>Avec cette crise sanitaire, Gallica propose avec l\'Education nationale des EPUB éducatifs pour pallier la fermeture des écoles. C\'est très intéressant. </p><p> <a href=\'https://gallica.bnf.fr/blog/18012018/150-epub-gallica-selectionnes-par-le-ministere-de-leducation-nationale?mode=desktop\'>lien</a></p>", 2, "Gallica"),\
                      ("Un projet chinois", "Une fois n\'est pas coutume, sortons un peu de France. Il y a quelques semaines, l\'équipe de WuHan a mis en ligne son [site](http://dh.whu.edu.cn/dh/web/index.html) qui va recevoir bientôt leur magnifique travail. Vous y verrez: \n * des peintures murales \n * des manuscrits \n * le sens des peintures retrouvé grâce aux manuscrits.", "2020-03-21 14:45:25.236589", "<p>Une fois n\'est pas coutume, sortons un peu de France. Il y a quelques semaines, l\'équipe de WuHan a mis en ligne son <a href=\'http://dh.whu.edu.cn/dh/web/index.html\'>site</a> qui va recevoir bientôt leur magnifique travail. Vous y verrez: </p><ul><li>des peintures murales </li><li>des manuscrits </li><li>le sens des peintures retrouvé grâce aux manuscrits.</li></ul>", 3, "humanites_numeriques"),\
                      ("Un stage très intéressant", "Bonjour à tous \n Je viens de tomber par hasard sur cette offre de stage à la BILIPO de Paris, la bibliothèque des **littératures policières**. Vous y serez très bien accueilli! [Lien vers l\'offre de stage](https://stage-apprentissage.paris.fr/?_3x931S1Z2U3Kfbeaa589-5f59-4e7d-96c5-374d6bbf95c9&offerid=2777)", "2019-12-24 21:25:53.896523", "<p>Bonjour à tous </p><p> Je viens de tomber par hasard sur cette offre de stage à la BILIPO de Paris, la bibliothèque des <strong>littératures policières</strong>. Vous y serez très bien accueilli! <a href=\'https://stage-apprentissage.paris.fr/?_3x931S1Z2U3Kfbeaa589-5f59-4e7d-96c5-374d6bbf95c9&amp;offerid=2777\'>Lien vers l\'offre de stage</a></p>", 3, "stage"),\
                      ("Un peu de réconfort dans ces temps troublés", "Une très jolie peinture d\'un manuscrit de Valenciennes: [peinture](https://gallica.bnf.fr/ark:/12148/btv1b84525958/f33.image.r=regiacarol%20peintures).", "2020-03-21 15:02:26.234596", "<p>Une très jolie peinture d\'un manuscrit de Valenciennes: <a href\'https://gallica.bnf.fr/ark:/12148/btv1b84525958/f33.image.r=regiacarol%20peintures\'>peinture</a>.</p>", 3, "Gallica"),\
                      '

comments = 'INSERT INTO Comment(comment_message, comment_html, comment_date, comment_auteur, comment_post)\
                VALUES ("Bonjour Marie. \n Tu n\'as pas à t\'inquiéter pour les stages de l\'an prochain car: \n * tu ne peux pas savoir quels sujets t\'intéresseront \n * la scolarité fournit une liste avec des stages à pourvoir car ce sont des stages sûrs. \n \n Bien à toi, Sarah", "<p>Bonjour Marie. <br> Tu n\'as pas à t\'inquiéter pour les stages de l\'an prochain car: </p><ul><li>tu ne peux pas savoir quels sujets t\'intéresseront </li><li>la scolarité fournit une liste avec des stages à pourvoir car ce sont des stages sûrs. </li></ul><p>Bien à toi, Sarah</p>", "2020-02-19 13:58:24.236587", 4, 1),\
                ("Bonjour Sarah, \n Merci beaucoup pour ces informations. \n A bientôt", "<p>Bonjour Sarah,  <br> Merci beaucoup pour ces informations.</p><p>A bientôt</p>", "2020-02-19 14:14:24.236587", 1, 1),\
                ("Bonjour Marie, \n Tu trouveras [ici](http://api.bnf.fr/api-iiif-de-recuperation-des-images-de-gallica) toutes les informations qu\'il te faut pour bien utiliser IIIF sur la BNF.", "<p>Bonjour Marie, \n Tu trouveras <a href=\'http://api.bnf.fr/api-iiif-de-recuperation-des-images-de-gallica\'>ici</a> toutes les informations qu\'il te faut pour bien utiliser IIIF sur la BNF.</p>", "2020-02-27 18:34:24.236587", 2, 2),\
                ("Bonjour Marie, \n Je suis d\'accord avec toi. C\'est une fonctionnalité qui devrait arriver dans les prochains mois, car il faut que ce soit efficace. \n Bonne soirée", "<p>Bonjour Marie, <br> Je suis d\'accord avec toi. C\'est une fonctionnalité qui devrait arriver dans les prochains mois, car il faut que ce soit efficace. <br> Bonne soirée</p>", "2020-01-29 10:02:20.236587", 3, 3),\
                ("Bonjour Marie, \n Il faudrait que ce soient des anciens du master qui répondent car ils sont au quotidien avec ces projets numériques qu\'il faut étudier.", "<p>Bonjour Marie, <br> Il faudrait que ce soient des anciens du master qui répondent car ils sont au quotidien avec ces projets numériques qu\'il faut étudier</p>", "2020-02-03 10:02:20.236587", 3, 4),\
                ("Bonjour Marie, \n Il existe de nombreux projets numériques. Regarde peut-être l\'**International Dunhuang Project** qui est très intéressant. \n Bonne journée", "<p>Bonjour Marie, <br> Il existe de nombreux projets numériques. Regarde peut-être l\'<strong>International Dunhuang Project</strong> qui est très intéressant. <br> Bonne journée</p>", "2020-02-04 10:02:20.236587", 6, 4),\
                ("# Merci à tous pour vos réponses!", "<h1>Merci à tous pour vos réponses!</h1>", "2020-02-04 13:04:29.236587", 1, 4),\
                ("Merci pour cette information Marie", "<p>Merci pour cette information Marie</p>", "2020-02-14 15:12:54.369852", 7, 5),\
                ("Bonjour Marie, \n C\'est une réflexion très courante dans les discussions dans les bibliothèques. Mais on peut considérer les bibliothèques comme un service public, et aujourd\'hui les services publics ont tendance à proposer une part de dématérialisation.", "<p>Bonjour Marie,</p><p>C\'est une réflexion très courante dans les discussions dans les bibliothèques. Mais on peut considérer les bibliothèques comme un service public, et aujourd\'hui les services publics ont tendance à proposer une part de dématérialisation.</p>", "2020-02-31- 15:12:54.369852", 4, 7),\
                ("Je suis tout à fait d\'accord avec Sarah, c\'est une question qui ne devrait même pas se poser dans les institutions,  mais on connaît les beosins d\'économies.", "<p>Je suis tout à fait d\'accord avec Sarah, c\'est une question qui ne devrait même pas se poser dans les institutions,  mais on connaît les beosins d\'économies.</p>", "2020-03-16 06:52:32.145236", 5, 7),\
                ("Je les avais aussi remarqué, ils ont fait du super travail! Félicitations à eux!", "<p>Je les avais aussi remarqué, ils ont fait du super travail! Félicitations à eux!</p>", "2020-02-16 09:28:54.214563", 2, 8),\
                ("Bonjour John, \n A tout hasard, sais-tu si cette offre a trouvé preneur? (deux ans après)", "<p>Bonjour John</p><br><p>A tout hasard, sais-tu si cette offre a trouvé preneur? (deux ans après)</p>", "2018-06-26 16:36:36.214563", 4, 9),\
                ("Bonjour Sarah, \n Cette offre a rapidement été pourvue. Si tu cherches un poste dans le privé, je sais qu\'EDF rechecrhe une personne pour un poste similaire, mais en France cette fois-ci. \n Bonne journée", "<p>Bonjour Sarah, </p><br><p>Cette offre a rapidement été pourvue. Si tu cherches un poste dans le privé, je sais qu\'EDF rechecrhe une personne pour un poste similaire, mais en France cette fois-ci.</p><br><p>Bonne journée</p>", "2018-06-27 12:36:36.214563", 2, 9),\
                ("Merci pour cette information, je vais me renseigner!", "<p>Merci pour cette information, je vais me renseigner!</p>", "2018-06-27 14:38:36.214563", 4, 9),\
                ("J\'ai obtenu un entretien pour la semaine prochaine, je vous tiens tous au courant.", "<p>J\'ai obtenu un entretien pour la semaine prochaine, je vous tiens tous au courant.</p>", "2018-06-29 07:28:32.214563", 4, 9),\
                ("Enfin une liste utile, merci John!", "<p>Enfin une liste utile, merci John!</p>", "2019-05-25 09:26:35.214563", 8, 10),\
                ("# Mise à jour \n J\'ai oublié de mettre le [lien vers le nouveau site](archivesdepartementales.aude.fr)", "<h1>Mise à jour</h1><p>J\'ai oublié de mettre le <a href=\'archivesdepartementales.aude.fr\'>lien vers le nouveau site</a>.</p>",  "2020-03-13 21:27:36.235789", 2, 12),\
                ("Bonjour John, savez-vous si l\'événement se déroule chaque année à Lyon, ou bien s\'il n\'y était que de passage?", "<p>Bonjour John, savez-vous si l\'événement se déroule chaque année à Lyon, ou bien s\'il n\'y était que de passage?</p>", "2020-03-16 09:52:45.235478", 6, 13),\
                ("Bonjour Je ne saurai pas te répondre. Il se déroule certainement chaque année, mais peut-être pas chaque année. internet sauras certainement te répondre. Bonne journée", "<p>Bonjour Je ne saurai pas te répondre. Il se déroule certainement chaque année, mais peut-être pas chaque année. internet sauras certainement te répondre. Bonne journée</p>", "2020-03-17 19:52:45.235478", 2, 13),\
                ("Merci pour votre réponse. \n J\'ai trouvé ce qu\'il me faut sur internet.", "<p>Merci pour votre réponse. </p><br><p> J\'ai trouvé ce qu\'il me faut sur internet.</p>", "2020-03-18 06:28:45.235478", 6, 13),\
                ("Merci beaucoup John, \n Cela va me permettre de faire école aux enfants tout en les divertissant. \n Bonne journée", "<p>Merci beaucoup John, </p><br><p> Cela va me permettre de faire école aux enfants tout en les divertissant. </p><br><p> Bonne journée</p>", "2020-03-24 20:20:20.235478", 4, 14),\
                ("A partir de quel endroit ont-ils fait ce travail? (Je ne parle pas chinois)", "<p>A partir de quel endroit ont-ils fait ce travail? (Je ne parle pas chinois)</p>", "2020-03-21 14:52:25.321456", 5, 15),\
                ("A partir des Grottes de Mogao, à DunHuang. Ce sont des grottes très célèbres et classées au Patrimoine de l\'Unesco.", "<p>A partir des Grottes de Mogao, à DunHuang. Ce sont des grottes très célèbres et classées au Patrimoine de l\'Unesco.</p>", "2020-03-21 14:58:25.321456", 3, 15),\
                ("Un projet international, l\'[IDP](http://idp.bl.uk/), existe justement et rassemble déjà tous les manuscrits chinois retrouvés dans les grottes et conservés dans le monde.", "<p>Un projet international, l\'<a href=\'http://idp.bl.uk/\'>IDP</a>, existe justement et rassemble déjà tous les manuscrits chinois retrouvés dans les grottes et conservés dans le monde.</p>", "2020-03-21 14:59:25.321456", 3, 15),\
                ("Merci pour toutes ces informations, je vais aller voir.", "<p>Merci pour toutes ces informations, je vais aller voir.</p>", "2020-03-21 15:02:25.321456", 5, 15),\
                ("Merci pour cette veille, elle m\'intéresse beaucoup pour cet été, en plus c\'est une bibliothèque.", "<p>Merci pour cette veille, elle m\'intéresse beaucoup pour cet été, en plus c\'est une bibliothèque.</p>", "2019-12-28 21:25:53.896523", 1, 16),\
                ("J\'ai personnellement une plus grande préférence pour cette [page-ci](https://gallica.bnf.fr/ark:/12148/btv1b84525958/f63.image.r=regiacarol%20peintures), elle est totalement peinte.", "<p>J\'ai personnellement une plus grande préférence pour cette <a href=\'https://gallica.bnf.fr/ark:/12148/btv1b84525958/f63.image.r=regiacarol%20peintures\'>page-ci</a>, elle est totalement peinte.</p>", "2020-03-21 17:02:26.234596", 5, 17),\
                ("Il est toujours diffcile de faire un choix parmi toutes les images de Gallica, qui sont d\'une très belle qualité!", "<p>Il est toujours diffcile de faire un choix parmi toutes les images de Gallica, qui sont d\'une très belle qualité!</p>", "2020-03-21 18:02:26.234596", 8, 17),\
                            '

cvs = 'INSERT INTO CV(cv_nom_poste, cv_nom_employeur, cv_ville, cv_annee_debut, cv_annee_fin, cv_description_poste, cv_utilisateur)\
          VALUES ("Stagiaire à la bibliothèque nationale de France, site de l\'Arsenal", "BNF", "Paris", 2019, 2019, "Je me suis occupée du catalogage des nouveaux manuscrits acquis par la BNF Arsenal, ainsi que des reprises de cotes des incunables (en refaisant par la même occasion les notices). Le stage a duré quatre mois.", 1),\
                 ("Ingénieur de la donnée", "Total", "Paris", 2017, 2019, "Dans le groupe Total, j\'étais en charge des bases de données documentaires relatives aux fonds historiques de l\'entreprise. La migration des données vers un nouveau modèle relationnel a été engagé en 2017 et s\'est achevée en 2019 à mon départ", 2),\
                 ("Bibliothécaire", "Bibliothèque d\'études et du patrimoine", "Toulouse", 2014, 2017, "Pour mon premier poste professionnel, j\'ai passé le concours de bibliothécaire puis ai obtenu un poste à la BEP de Toulouse où je me suis occupé principalement du catalogage du fonds ancien, ainsi que de l\'accueil du public.", 2),\
                 ("Ingénieur de la donnée", "Bibliothèque nationale et universitaire de Strasbourg", "Strasbourg", 2019, 2020, "Je suis actuellement responsable de la bibliothèque numérique de la BNU, ainsi que du portail des ressources numériques. J\'ai une équipe de 4 personnes qui travaille à mes côtés pour établir les nouveaux modèles de données nécessaires au fonctionnement futur de la bibliothèque numérique nouvelle génération.", 2),\
                 ("Stagiaire bibliothécaire", "Bibliothèque du musée national des arts asiatiques Guimet", "Paris", 2019, 2019, "Catalogue du fonds chinois de la bibliothèque, fonds ancien ou contemporain; accueil du public. Stage de quatre mois pendant l\'été.", 3),\
                 ("Stagiaire", "Institut national de l\'Audiovisuel", "Bry-sur-Marne", 2020, 2020, "Stage de fin de master prévu d\'avril(?) à juillet sur la migration des données juridiques de l\'INA.", 3),\
                 ("Chargée documentaire", "Archives départementales de l\'Aveyron", "Rodez", 2015, 2016, "A la sortie du master, j\'ai obtenu un cours CDD pour le classement des archives industrielles de l\'Aveyron aux AD du département. Durée du contrat: 3 mois.", 4),\
                 ("Chargée documentaire", "Archives départementales du Nord", "Lille", 2016, 2016, "Rapidement après le premier poste, j\'ai obtenu un poste similaire aux AD du Nord, pour la description archivistique des fonds miniers du département. C\'était un contrat de 10 mois.", 4),\
                 ("Encodeuse archivistique", "Archives du Parlement européen de Strasbourg", "Strasbourg", 2017, 2017, "Après une première expérience réussie avec l\'EAD aux AD du Nord, j\'ai obtenu un nouveau poste d\'un an au Parlement européen de Strasbourg pour décrire les archives produites quotidiennement dans l\'institution.", 4),\
                 ("Directrice des Archives Départementales", "Archives départementales de Haute-Garonne", "Toulouse", 2018, 2018, "Ayant réussi le concours de conservatrice en 2016, j\'obtiens mon premier poste à responsabilités en 2018 en devenant directrice des AD de Haute-Garonne. Je pratique moins l\'encodage archivistique, mais je connais mieux l\'ensemble des fonds conservés.", 4),\
                 ("Directrice des Archives de la Défense", "Service des archives de la défense", "Paris", 2019, 2019, "Après plusieurs années en province, j\'ai réussi à obtenir un poste dans la région parisienne, au SAD.", 4),\
                 ("Archiviste auprès du Ministre de l\'Intérieur", "Cabinet du ministre de l\'Intérieur", "Paris", 2020, 2020, "Depuis cette année, je suis auprès du Ministre pour effectuer l\'archivage de ses documents courants.", 4),\
                 ("Stagiaire à la bibliothèque municipale Vaclav Havel", "Bibliothèques de Paris", "Paris", 2019, 2019, "Pendant ce stage d\'été de 4 mois, j\'ai aidé à la mise en place du portail numérique de la bibliothèque du 18è arrondissement; j\'ai également participé à la réflexion autour de la politique documentaire qu\'il faut offrir dans cet arrondissement", 5),\
                 ("Stagiaire à la bibliothèque municipale de Rodez", "Bibliothèque municipale de Rodez", "Rodez", 2020, 2020, "Ce stage est le stage de fin de M2. J\'effectuerai dans la médiathèque municipale la mise en place de Gallica blanche pour valoriser les documents patrimoniaux de la ville.", 5),\
                 ("Stagiaire aux archives départementales de Lille dans le Nord", "Archives départementales de Lille", "Lille", 2020, 2020, "Pour mon stage de fin de master, j\'ai choisi d\'aller aux AD du Nord car il s\'y effectue un gros travail de numérisation et de valorisation des collections, industrielles notamment. Il ne durera que trois mois, mais il semble être très intéressant.", 6),\
                 ("Stagiaire aux archives départementales du Bas-Rhin", "Archives du Bas-Rhin", "Strasbourg", 2019, 2019, "Lors d\'un stage d\'été, j\'ai découvert les archives grâce aux AD du Bas-Rhin. J\'ai effectué des tâches banales d\'inventoriage des collections pendant deux mois seulement. Je me suis découvert une passion pour l\'EAD.", 6),\
                 ("Stagiaire aux archives pontificales du Saint-Siège", "Archives pontificales du Saint-Siège", "Rome", 2020, 2020, "Pour le stage de M2, je pars en Italie à Rome aux archives pontificales. J\'aiderai à la mise en ligne des plus beaux fonds, et à leur valorisation auprès du plus grand nombre.", 7),\
                 ("Bibliothécaire à l\'EFEO", "Ecole Française d\'Extrême-Orient", "Paris", 2019, 2020, "J\'ai trouvé un poste de bibliothécaire à l\'EFEO pour cette année, mais je me suis rendue compte que ce ne sont pas les bibliothèques qui m\'intéressent. J\'y ai effectué du catalogage des ouvrages récemment achetés, 15 heures par semaine.", 7),\
                 ("Ingénieur de la donnée", "INA", "Bry-sur-Marne", 2020, 2020, "Dans le cadre du grand projet sur les données de l\'INA, je participe à leur migration dans le nouveau modèle de données, en utilisant notamment des technologies SQL et NO-SQL, ainsi que beaucoup de Python, pour parvenir aux résultats souhaités.", 8),\
                 ("Chargé documentaire", "Ministère des affaires étrangères", "Paris", 2017, 2017, "Mon premier poste a été dans un projet institutionnel au MAE, où j\'ai ouvert la bibliothèque numérique de la bibliothèque du ministère", 8),\
                 ("Employé dans un fonds privé", "Famille noble strasbourgeoise", "Strasbourg", 2018, 2018, "Après le premier poste, j\'ai travaillé dans un château pour une grande famille de la région de Strasbourg de manière à classer, cataloguer et inventorier les fonds possédés.", 8),\
                 ("Ingénieur", "Université Jean Jaurès - Toulouse II", "Toulouse", 2019, 2019, "Dans le cadre du projet de migration des données du département d\'archéologie de la faculté d\'histoire et d\'archéologie, j\'ai initié cette migration en proposant des modèles de données correspondant au cahier des charges. Ce projet est actuellement encore en cours.", 8)'

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