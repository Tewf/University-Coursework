# Introduction to AI

> [Read in English](README.md)

**Cours :** Introduction to AI, M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes
**Équipe pédagogique :** Nguyen Kim Thang (apprentissage automatique), Sylvain Bouveret (IA symbolique)

Deux moitiés et neuf TP. La moitié apprentissage automatique va de l'évaluation
des modèles aux réseaux récurrents en sept notebooks ; la moitié symbolique
écrit des programmes logiques en Datalog et des modèles de contraintes avec
OR-Tools. Chaque TP est un notebook ou un script à compléter, donc chaque TP a
son dossier ici.

## Les TP

| Dossier | Problème | Résolu avec | Fourni |
|---|---|---|---|
| [MachineLearning/Lab1-performance-evaluation/](MachineLearning/Lab1-performance-evaluation/) | Six prédicteurs sur les données du cancer du sein, comparés par exactitude, précision, rappel, F1, ROC et AUC | métriques scikit-learn | sujet, correction officielle |
| [MachineLearning/Lab2-supervised-ml/](MachineLearning/Lab2-supervised-ml/) | Un SVM linéaire sur des blobs synthétiques, puis la prédiction d'avalanches à partir de données météo et neige | SVM, la marge souple `C` | sujet, correction officielle, `avalanche_data.csv`, deux figures |
| [MachineLearning/Lab3-unsupervised-learning/](MachineLearning/Lab3-unsupervised-learning/) | k-means sur les images de chiffres, puis ACP et t-SNE | clustering, AMI, silhouette | sujet, correction officielle |
| [MachineLearning/Lab4-regularization/](MachineLearning/Lab4-regularization/) | Prédire le statut MICI de 396 patients à partir de 1939 abondances microbiennes, p bien plus grand que n | régularisation | sujet, `gut_abundances.tsv`, `ibd_status.lst` |
| [MachineLearning/Lab5-deep-learning/](MachineLearning/Lab5-deep-learning/) | Les salaires Hitters par régression linéaire et Lasso, puis un réseau à deux couches en PyTorch | `nn.Module`, une boucle d'entraînement écrite à la main | sujet, `utilsDL.py`, `data/hitters.csv` |
| [MachineLearning/Lab6-fine-tuning/](MachineLearning/Lab6-fine-tuning/) | Affiner un ResNet18 pré-entraîné sur ImageNet pour la détection d'objets sur des images VOC | apprentissage par transfert | sujet seul |
| [MachineLearning/Lab7-recurrent-networks/](MachineLearning/Lab7-recurrent-networks/) | Prédire l'humidité à partir des données du bâtiment CUBEMS, fenêtres de pas passés en entrée, pas futurs en sortie | RNN, LSTM | sujet, `utils.py`, `data.csv` |
| [SymbolicAI/Lab1-datalog/](SymbolicAI/Lab1-datalog/) | Une base de connaissances de 45 règles sur les prêts, un arbre généalogique Game of Thrones, des correspondances de trains et plus courts trajets | pyDatalog | sujet, base de règles, `familyTree.py`, `test-pyDatalog.py`, `got.csv`, `trains.csv` |
| [SymbolicAI/Lab2-constraint-programming/](SymbolicAI/Lab2-constraint-programming/) | N reines, un solveur de Sudoku, un solveur de cryptarithmes, des requêtes familiales en modèle CP | Google OR-Tools | sujet, `got.csv` |

Trois choses à savoir avant d'en ouvrir un :

- **Le TP 5 lit `data/hitters.csv`**, en minuscules et dans un sous-dossier,
  alors que l'archive livre `Hitters.csv` à sa racine. La copie ici est placée
  là où la cellule 4 la cherche. Le même notebook télécharge FashionMNIST et
  CIFAR10 dans `data/`, d'où l'exclusion de ce dossier entier par `.gitignore`.
- **Le TP 6 ne peut pas s'exécuter tel que livré.** Son notebook importe
  `model.py` et `utils.py` et charge `data/*.pt`, dont aucun n'a jamais été
  distribué avec lui. Le dossier contient le sujet et rien d'autre tant qu'ils
  ne sont pas apparus.
- **`familyTree.py` est une amorce à laquelle on ajoute des prédicats**
  (questions 8 à 11). La copie intacte reste telle que fournie ; le travail va
  dans un module à part qui l'importe, pour ne jamais versionner le fichier de
  l'enseignant comme s'il était le mien.

## Mise en place

Un environnement conda pour tous les TP, déclaré une fois dans
[environment.yml](environment.yml) :

```bash
conda env create -f environment.yml
conda activate m1ai-intro-ai
```

On commence un TP en copiant son sujet hors de `handout/` et en ouvrant la copie :

```bash
cd MachineLearning/Lab2-supervised-ml
cp handout/Lab2-supervised-ml.ipynb .
jupyter lab Lab2-supervised-ml.ipynb
```

Cette copie est le fichier versionné. Celui de `handout/` ne change jamais.

## Structure du dossier

Chaque TP garde ce que l'équipe a distribué dans `handout/` (sujet, correction
officielle quand elle existe, et une extraction `.txt` de tout PDF pour qu'il
soit greppable). Les modules fournis et les jeux de données sont à la racine du
TP, là où le notebook les attend. `.gitignore` exclut tout cela, donc ce qu'un
dossier montre sur GitHub est le notebook complété et rien d'autre, et un TP
pas encore commencé ne montre rien.

```
IntroductionToAI/
|-- environment.yml              <- l'unique environnement conda
|-- MachineLearning/
|   |-- Lab1-performance-evaluation/
|   |   |-- handout/             <- sujet, correction officielle
|   |-- Lab2-supervised-ml/
|   |   |-- handout/
|   |   |-- avalanche_data.csv svm.png svm0.png   <- ce que lit le notebook
|   |   |-- as-downloaded.zip    <- l'archive, pour la provenance
|   |-- ... Lab7-recurrent-networks/
|-- SymbolicAI/
|   |-- Lab1-datalog/
|   |   |-- handout/             <- sujet, Datalog-Rules.pdf, les deux en .txt aussi
|   |   |-- familyTree.py test-pyDatalog.py got.csv trains.csv
|   |-- Lab2-constraint-programming/
```

## Où sont les explications

Pas ici. Les concepts dont chaque TP a besoin — métriques d'évaluation, SVM,
clustering, régularisation, descente de gradient et rétropropagation, réseaux
récurrents, logique propositionnelle et du premier ordre, Datalog, propagation
de contraintes — sont rédigés dans un coffre Obsidian séparé, une note par
concept, avec les diapositives de cours dont ils viennent, les annales et les
manuels. Chaque TP y associe ses questions aux concepts qu'elles demandent. Un
commentaire d'ici qui se met à enseigner la théorie a sa place dans cette note.

## Matériel source

Les sujets, les corrections officielles, les modules fournis et les jeux de
données ne sont **pas redistribués ici** : voir [NOTICE](../../../../NOTICE).
Ils restent sur le disque dans chaque dossier de TP et `.gitignore` les exclut
du dépôt. Ce qui est versionné est le travail écrit en réponse.
