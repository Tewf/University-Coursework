# Tournoi de stratégies : des agents Prolog dans un jeu répété

> [Read in English](README.md) · [Ouvrir sur le site ↗](https://tewf.github.io/University-Coursework/Bachelor/SecondSemestreLanguage/Prolog/StrategyTournament/)

**Cours :** Programmation logique, Licence MIASHS, Université Grenoble Alpes

Deux stratégies déterminées sur le papier, écrites comme agents Prolog, puis
engagées dans un tournoi à 16 agents face au reste de la promotion. L'intéressant
n'est pas leur classement, mais ce que ce classement mesure réellement.

## Résultats

![Seize agents classés par score cumulé, échelle logarithmique](results/leaderboard.png)

`stage_test` finit **7e sur 16** avec 6 163 877 points et `nash_equilibrium`
**8e** avec 1 490 429. Ce classement se trouvait page 1 d'un journal de 636 pages.

En relisant le même journal match par match, l'ordre s'inverse :

| | agent | score cumulé | matchs gagnés |
|---|---|---:|---:|
| 1 | best_duo | 2,02 × 10⁶² | 6 sur 15 |
| 2 | naenae | 2,58 × 10⁵⁷ | 9 sur 15 |
| 6 | syntax_terror | 6,34 × 10²⁹ | **2 sur 15** |
| **7** | **stage_test** | **6 163 877** | **7 sur 15** |
| **8** | **nash_equilibrium** | **1 490 429** | 5 sur 15 |
| 13 | un_pain_pita | 9 566 | 12 sur 15 |
| 14 | ghost | 9 350 | **13 sur 15** |

Le vainqueur a gagné 6 de ses 15 matchs. L'agent qui en a gagné 13 sur 15 finit
14e. Sur les seize, finir plus bas est corrélé au fait de gagner **plus** de
matchs (Spearman +0,62 contre le rang final, p = 0,011). Les deux agents engagés
battent le vainqueur dans leur match direct, 782 à 435 et 490 335 à 4 772.

Le tournoi ne classait donc pas les agents selon leur nombre de victoires, mais
selon leur score, et ce sont deux objectifs distincts.

## Pourquoi les scores atteignent 10⁶²

Le tournoi employait une version modifiée du jeu où **répéter un nombre multiplie
son gain par ce nombre**, vérifié sur 5 050 des 5 216 répétitions consécutives du
journal. Une série de `best_duo` jouant 5 quarante fois de suite rapporte 5⁴⁰,
soit 9 × 10²⁷ sur un seul tour.

Les deux agents engagés ont été dérivés pour la version simple du jeu, et tous
deux sont sans mémoire : ils tirent dans une distribution fixe sans jamais lire
l'historique.

| agent | joue | plus longue série | répétitions |
|---|---|---:|---:|
| `stage_test` | `[0.03, 0.444, 0.203, 0.323, 0.0]` | 10 | 32,9 % |
| `nash_equilibrium` | `[0, 0, 4/9, 2/9, 1/3]` | 9 | 35,4 % |

Ces taux sont exactement ceux que produit un tirage indépendant, 34,4 % et
35,8 %. Tous les agents classés devant eux atteignent des séries de 37 à 100. Une
stratégie mixte fixe ne peut pas exploiter une règle qui récompense la répétition
délibérée, et c'est là tout l'écart entre la 7e et la 1re place.

## Le jeu

Les deux joueurs choisissent simultanément un entier de 1 à 5. Si les choix
diffèrent d'exactement un, celui qui a choisi le **plus petit** nombre prend la
somme et l'autre rien ; sinon chacun marque ce qu'il a choisi. Sous-coter d'une
unité est récompensé, donc chaque nombre invite à être sous-coté.
[`Algorithme_Explication.pdf`](Algorithme_Explication.pdf) en dérive la matrice de
gain 5 × 5 et pose la stratégie.

`stage_test` sort de [`Equilibrium_Analysis.ipynb`](Equilibrium_Analysis.ipynb),
et les constantes correspondent à l'arrondi près : `Fraction(27, 896)` → `0.03`,
`Fraction(440, 991)` → `0.444`, `Fraction(101, 497)` → `0.203`,
`Fraction(292, 905)` → `0.323`. L'analyse et l'agent soumis sont le même objet.

`stage_test` bat aussi `nash_equilibrium` en tête-à-tête, 1 414 à 661, ce qui est
l'ordre que l'analyse prévoyait.

## Fichiers

| Fichier | Contenu |
|---------|---------|
| `Code.pl` | Quatre agents derrière `joue/3` : `stage_test` et `nash_equilibrium` (sans mémoire), `khawa_khawa` (adaptatif, meilleure réponse aux fréquences estimées de l'adversaire), `khawa_khawa_prime` |
| `Algorithme_Explication.pdf` | Le jeu, ses matrices de gain et la stratégie proposée |
| `Stage_test.pdf` | Construction de l'équilibre `stage_test` |
| `Equilibrium_Analysis.ipynb` | Le notebook dont viennent les constantes |
| `data2.pdf` | Le journal du tournoi, 636 pages |
| `results/` | Le journal converti en CSV, et le graphique ci-dessus |

`khawa_khawa` est l'agent le plus abouti, et il **n'apparaît pas du tout dans le
journal** : zéro tour, contre 1 805 pour `stage_test` et 1 813 pour
`nash_equilibrium`. Il a été construit à côté des agents engagés, sans être
engagé lui-même.

## Exécuter le code

```sh
swipl -s Code.pl          # puis interroger, par exemple : joue(stage_test, [], Coup).
cd results && python3 analyse_log.py && python3 plot_leaderboard.py
```

`analyse_log.py` compare les scores de match de chaque agent à son total au
classement et s'arrête s'ils divergent, ce qui a permis de repérer un bug
d'analyse du journal.

## Prérequis

SWI-Prolog pour les agents. Python 3 avec matplotlib, et poppler-utils pour
`pdftotext`, pour régénérer les résultats.

## Supports de cours

L'énoncé du projet appartient au cours et n'est pas redistribué ici ; voir
[NOTICE](../../../../NOTICE).
