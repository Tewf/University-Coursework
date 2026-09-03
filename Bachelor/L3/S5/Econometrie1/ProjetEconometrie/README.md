# Projet d'Économétrie : Prix hédoniques de l'immobilier grenoblois

**Auteurs :** HAMLIL Mohamed Ali Tewfik · ANZID Keltoum · EL KORAICHI Mohamed Yassine
*Projet de groupe, Économétrie 1, L3 MIASHS, Université Grenoble Alpes.*

Modélisation hédonique du marché immobilier grenoblois à partir des données
ouvertes DVF. La chaîne va du fichier national brut au nettoyage et à la
construction des variables, puis à une régression MCO avec diagnostics, et enfin
à une extension par forêt aléatoire.

## La méthode

La méthode des prix hédoniques (Rosen, 1974) traite un logement comme un panier
de caractéristiques et décompose son prix observé en leurs prix implicites :

```
P_i = f(X_i) + ε_i
```

où `X_i` est le vecteur des caractéristiques (surface, pièces, type de bien,
localisation) et `f` la fonction de prix hédonique, estimée ici d'abord en
spécifications linéaire et log-linéaire, puis de façon non paramétrique.

## Résultats

Le RMSE est en euros, sauf lorsque la variable dépendante est `log_price` : il
est alors en unités logarithmiques et n'est pas comparable d'une ligne à l'autre.

| Modèle | Variable dépendante | R² | R² ajusté | RMSE |
|---|---|---|---|---|
| MCO, spécification de base | `price` | 0,096 | 0,082 | 275 007 € |
| MCO, spécification étendue | `price` | 0,157 | 0,136 | 265 214 € |
| MCO, log-linéaire | `log_price` | **0,275** | 0,264 | 0,665 (log) |
| MCO, autre spéc. log | `log_price` | 0,167 | 0,157 | 0,776 (log) |
| **Forêt aléatoire** | `price` | — | — | **58 750 €** |

Deux lectures :

- **C'est la transformation logarithmique qui fait fonctionner le modèle
  linéaire.** Le R² passe de 0,096 à 0,275 ; les prix immobiliers sont
  asymétriques à droite et multiplicatifs en leurs caractéristiques, ce que
  postule précisément la spécification hédonique log-linéaire.
- **La forêt aléatoire divise le RMSE par environ 4,5** face au meilleur MCO en
  euros (58 750 € contre 265 214 €), ce qui indique des non-linéarités et des
  interactions (vraisemblablement localisation × surface) qu'une spécification
  additive ne peut pas représenter. Elle gagne cette précision en abandonnant les
  prix implicites interprétables qui étaient l'objet même de la démarche
  hédonique : les deux modèles répondent à des questions différentes.

Les diagnostics d'hétéroscédasticité et de multicolinéarité et le traitement des
valeurs aberrantes sont dans [`ModelTraining/`](ModelTraining/README.md).

## Structure

```
DataPreprocessing/     # DVF brut -> coupe transversale et panel grenoblois
ModelTraining/         # MCO hédonique + diagnostics
  Extension/           # extension par forêt aléatoire
RevueDeLitterature/    # revue critique de la littérature hédonique
```

Chaque répertoire a son propre README.

## Données

**Demandes de Valeurs Foncières (DVF)**, Direction générale des Finances
publiques (DGFiP), premier semestre 2025 : données ouvertes sous
[Licence Ouverte](https://www.etalab.gouv.fr/licence-ouverte-open-licence).
Source : https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres/

## Littérature

Laferrère, A. (2005). *Hedonic housing price indexes: the French experience.*
BIS Papers No 21, Banque des règlements internationaux.
https://www.bis.org/publ/bppdf/bispap21.htm

Rosen, S. (1974). *Hedonic Prices and Implicit Markets: Product Differentiation
in Pure Competition.* Journal of Political Economy, 82(1), 34–55.

## Source material

Les documents officiels DGFiP (notice, FAQ, conditions d'utilisation) et
l'article BIS sont cités et liés, non redistribués ici ; voir le
[NOTICE](../../../../../NOTICE) pour les crédits complets.
