# Projet Apprentissage par Renforcement - Highway Environment
Ce dépôt contient le code et la documentation pour le projet d'Apprentissage par Renforcement (RL), réalisé dans le cadre du cours "RL - Apprentissage par renforcement - CS - PARIS - SACLAY (2023-2024)". 
<p align="center">
  <img src="./assets/cs.png" alt="Logo CentraleSupélec">
</p>
 

## Organisation

Le projet est divisé en 3 tâches principales ainsi que l'exploration d'un aspect/question intéressante sur l'une des tâches précédentes:

### Tâche 1 : Environnement prédéfini - Highway-env

- Implémentation d'un algorithme DQN (Deep Q-Network) à partir de zéro pour résoudre l'environnement Highway-env
- Configuration spécifique:
  - Observation: Grille d'occupation avec 7 caractéristiques par véhicule (présence, position, vitesse, orientation)
  - Actions discrètes (changements de voie, accélération/décélération)
  - 4 voies avec 15 véhicules et épisodes de 60 secondes
  - Système de récompenses favorisant:
    - Évitement des collisions (pénalité de -1)
    - Conduite sur la voie de droite (+0.5)
    - Maintien d'une vitesse élevée entre 20-30 m/s (+0.1)
- Documentation des performances d'apprentissage et analyse du comportement de l'agent dans différentes situations de trafic
- Étude de l'évolution de l'apprentissage et des stratégies développées par l'agent pour naviguer efficacement

### Tâche 2 : Actions continues - Racetrack-v0

- Choix et configuration de l'environnement racetrack-v0 pour des actions continues
- Configuration spécifique:
  - Observation: Grille d'occupation simplifiée (présence et statut sur route)
  - Actions continues limitées au contrôle latéral (direction)
  - Épisodes plus longs (300 secondes) permettant d'observer le comportement sur la durée
  - Système de récompenses axé sur:
    - Évitement des collisions (-1)
    - Centrage sur la voie (coût de 4 pour les déviations)
    - Pénalisation des actions brusques (-0.3)
- Implémentation d'un algorithme adapté aux espaces d'actions continues
- Étude comparative entre les performances avec actions discrètes vs continues
- Analyse de la précision et fluidité du contrôle latéral sur circuit

### Tâche 3 : Environnement roundabout-v0 avec Stable-Baselines

- Utilisation de la bibliothèque Stable-Baselines pour entraîner un algorithme existant sur l'environnement roundabout-v0
- Configuration spécifique:
  - Observation basée sur le temps jusqu'à collision (TimeToCollision)
  - Actions discrètes pour naviguer dans le rond-point
  - Sessions courtes (11 secondes) centrées sur la prise de décision critique
  - Focus sur la sécurité et l'évitement des collisions dans un contexte de trafic plus complexe
- Comparaison des performances entre algorithmes implémentés manuellement et ceux de Stable-Baselines
- Analyse de l'efficacité des différentes stratégies d'apprentissage dans un environnement plus complexe nécessitant des prises de décision rapides

## Structure du projet
```
RL-highway/
├── assets/                  # image
├── Config1/                 # Notebooks,configs et scripts pour la Tâche 1
├── Config2/                 # Tâche 2
├── Config3/                 # Tâche 3 
└── README.md                
```

## Auteurs 
- Rayane Bouaita
- Pierre El Anati
- Gabriel Trier