# Operating Systems

> [Lire en francais](README.fr.md)

**Course:** Systemes — Licence 3 MIASHS, Semester 6, Universite Grenoble Alpes

Practical work on operating system concepts with a focus on **thread synchronization and coordination** in Java.

## What You'll Learn

- Java threading with `Runnable` and shared resources
- Thread blocking and border detection mechanisms
- Signal-based coordination: `wakeOne()` and `wakeAll()`
- Conditional wait/notify patterns
- GUI programming with Swing (`JComponent`)

## Graded Assignment: Robot Room Simulation

A graphical simulation where multiple robots move within a room. The assignment focuses on thread synchronization:

| Task | Points | Description |
|------|--------|-------------|
| Border blocking | 3 pts | Make robots stop when reaching room boundaries |
| `wakeOne()` / `wakeAll()` | 4 pts | Implement selective and broadcast thread signaling |
| Auto-unlock | 5 pts | Automatically wake robots when blocked count > 10 |

### Key Files

```
Systemes/2025/tpnote2025-v3/
|-- src/main/java/
|   |-- Robot.java     <- Runnable robot with movement logic
|   |-- Room.java      <- GUI + thread synchronization
|-- pom.xml            <- Maven build configuration
```

### Running

```sh
cd 2025/tpnote2025-v3
mvn compile exec:java
```

## Prerequisites

- Java programming (OOP fundamentals)
- Basic understanding of concurrent programming concepts

## Tools

- **Java** (JDK 11+)
- **Maven** for build management
- **Swing** for GUI
