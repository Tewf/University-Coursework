# Prolog : Programmation logique

> [Read in English](README.md) · [Ouvrir sur le site ↗](https://tewf.github.io/University-Coursework/Bachelor/SecondSemestreLanguage/Prolog/)

**Cours :** Programmation logique, Licence MIASHS, Universite Grenoble Alpes

Une introduction a la programmation logique avec Prolog. Au lieu d'ecrire des instructions pas a pas, on declare des **faits** et des **regles**, puis on pose des questions, et le moteur Prolog trouve les reponses.

## Ce que vous apprendrez

- Definir des faits et des regles pour representer des connaissances
- Interroger des relations et effectuer du raisonnement logique
- Definitions recursives et mecanismes de backtracking
- Unification et pattern matching
- Recherche et resolution de problemes avec la logique declarative

## Fichiers

| Fichier | Theme |
|---------|-------|
| `TD5.pl`, `TD6.pl` | Exercices diriges : faits, regles, requetes |
| `TP.pl` | Predicats de base et relations |
| `TP2.pl` | Definitions recursives |
| `TP3.pl` | Traitement de listes en Prolog |
| `TP5.pl` | Backtracking avance |
| `TP6.pl` | Resolution de problemes par la logique |

## Executer le code

Installer [SWI-Prolog](https://www.swi-prolog.org/), puis :

```sh
swipl -s TP.pl
```

Utiliser des requetes a l'invite `?-` pour tester les predicats. Chaque fichier inclut des commentaires avec les predicats attendus et des exemples de requetes.

## Prerequis

- Aucune experience prealable en programmation logique requise
- Utile de comprendre la logique propositionnelle de base (ET, OU, implications)
