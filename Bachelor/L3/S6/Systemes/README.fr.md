# Systemes d'exploitation

> [Read in English](README.md)

**Cours :** Systemes — Licence 3 MIASHS, Semestre 6, Universite Grenoble Alpes

Travaux pratiques sur les concepts des systemes d'exploitation avec un accent sur la **synchronisation et coordination de threads** en Java.

## Ce que vous apprendrez

- Gestion de threads Java avec `Runnable` et ressources partagees
- Mecanismes de blocage et detection de bordures
- Coordination par signaux : `wakeOne()` et `wakeAll()`
- Patterns d'attente/notification conditionnelle
- Programmation d'interface graphique avec Swing (`JComponent`)

## TP note : Simulation de robots dans une piece

Une simulation graphique ou plusieurs robots se deplacent dans une piece. Le TP se concentre sur la synchronisation de threads :

| Exercice | Points | Description |
|----------|--------|-------------|
| Blocage aux bords | 3 pts | Faire s'arreter les robots aux limites de la piece |
| `wakeOne()` / `wakeAll()` | 4 pts | Implementer le reveil selectif et broadcast des threads |
| Deblocage automatique | 5 pts | Reveiller automatiquement les robots quand le nombre de bloques > 10 |

### Fichiers principaux

```
Systemes/2025/tpnote2025-v3/
|-- src/main/java/
|   |-- Robot.java     <- Robot Runnable avec logique de deplacement
|   |-- Room.java      <- Interface graphique + synchronisation
|-- pom.xml            <- Configuration Maven
```

### Execution

```sh
cd 2025/tpnote2025-v3
mvn compile exec:java
```

## Prerequis

- Programmation Java (fondamentaux POO)
- Comprehension de base des concepts de programmation concurrente

## Outils

- **Java** (JDK 11+)
- **Maven** pour la gestion du build
- **Swing** pour l'interface graphique
