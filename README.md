L'application app_taxis vise à connaître le nombre de courses de taxis dans chaque quartier et affiche les 5 premières courses de la liste
L'application app_dataviz affiche le nombre de passagers sur une période définie par l'utilisateur à l'aide d'un curseur (pour les années) et d'un menu déroulant (pour les mois). Elle affiche également une courbe montrant l'évolution du nombre de passagers sur la période définie, et une heatmap à la demande de l'utilisateur.
L'application app_securisee affiche le contenu d'un site (ici une galerie photo) après authentification. Nous avons ici créé un accès sécurisé au contenu. 

Pour créer un environnement virtuel sur Mac: 
python3 -m venv nom_env 

cela crée un environnement virtuel avec la version par défaut de python déjà installée (que l'on peut vérifier avec python3 --version)

Pour l'activer : 
source nom_env/bin/activate

Pour installer les dépendances listées dans le fichier requirements.txt : 
pip install -r requirements.txt

Pour lancer l'application en local : 
streamlit run nom_application
