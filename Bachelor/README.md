# Bachelor Degree Coursework

This directory contains all coursework and projects from my bachelor's degree studies. The work is organized by subject area and semester, covering core computer science concepts, programming languages, mathematics, and applied data analysis.

## Directory Structure

### Java Programming
- **[Complement_IA-main/](Java/Complement_IA-main/)** – A comprehensive Battleship AI project featuring multiple AI strategies (Uniform, Markov, Monte Carlo, Smart) and a graphical interface. Demonstrates advanced OOP design, algorithms, and statistical analysis.
- **[OOP/](Java/OOP/)** – Object-oriented programming coursework including:
  - `TD/` – Directed exercises covering classes, inheritance, interfaces, generics, exceptions, and file I/O
  - `TM/` – Mini-projects applying OOP principles to substantial problems

### L3 (Third Year)

#### Semester 5 (S5)
- **[ComplementMath1/](L3/S5/ComplementMath1/)** – Practical sessions on mathematical analysis using R and Quarto, covering Fourier analysis, signal processing, and differential equations
- **[Econometrie1/](L3/S5/Econometrie1/)** – Econometrics course with real-estate sales analysis project using data from Grenoble
- **[MathStat2/](L3/S5/MathStat2/)** – Statistical practicals on simulation, bootstrap, estimation, and hypothesis testing using R

#### Semester 6 (S6)
- **ComplementMath2/** – Machine Learning
- **Econometrie2/** – Advanced econometrics
- **MathStat3/** – Advanced statistics
- **WebDev/** – Web development coursework

### Programming Languages and Paradigms
- **[SecondSemestreLanguage/](SecondSemestreLanguage/)** – Second-semester language modules exposing multiple programming paradigms:
  - **[DrRacket/](SecondSemestreLanguage/DrRacket/)** – Functional programming in Racket (Scheme dialect), covering recursion, list processing, and higher-order functions
  - **[Prolog/](SecondSemestreLanguage/Prolog/)** – Logic programming with Prolog, exploring facts, rules, backtracking, and reasoning systems
  - **[SQL/](SecondSemestreLanguage/SQL/)** – Database practicals covering SQL queries, joins, aggregations, and database design

## Technology Stack

- **Languages**: Java, R, Racket, Prolog, SQL
- **Tools & Frameworks**: 
  - Java: JDK 11+, Maven/Gradle
  - R: Tidyverse, Quarto notebooks
  - Databases: PostgreSQL, MySQL, SQLite
  - IDE: VS Code with extensions, DrRacket, SWI-Prolog

## Getting Started

### Prerequisites
- **Java projects**: JDK 11 or newer
- **R projects**: R environment with tidyverse and Quarto
- **Prolog projects**: SWI-Prolog
- **SQL projects**: PostgreSQL, MySQL, or SQLite

### Running Projects

Each subdirectory includes its own README with specific instructions. General patterns:

**Java projects:**
```sh
javac -d bin $(find src -name '*.java')
java -cp bin package.ClassName
```

**R projects:**
```sh
quarto preview path/to/notebook.qmd
```

**Prolog projects:**
```sh
swipl -s filename.pl
```

**SQL projects:**
```sh
psql -d database_name -f tp01.sql
```

## Learning Journey

This coursework represents a comprehensive computer science education covering:
- **Core Programming**: Object-oriented design patterns, modular architecture
- **Algorithms & Heuristics**: AI strategies, search algorithms, optimization
- **Data Science**: Statistical analysis, econometric modeling, data visualization
- **Paradigm Diversity**: Procedural, functional, logic programming, SQL
- **Mathematical Foundations**: Fourier analysis, statistics, differential equations

## Project Highlights

- **Battleship AI**: Complex multi-agent system with performance benchmarking
- **OOP Exercises**: Progressive difficulty from basic encapsulation to complex design patterns
- **Econometrics Project**: Real-world data analysis with statistical modeling
- **Statistical Practicals**: Bootstrap methods, hypothesis testing, estimation theory
- **Polyglot Programming**: Experience with five different programming paradigms

## Tips for Navigation

- Start with **Java/Complement_IA-main/** for a complete application example
- Review **Java/OOP/** for foundational programming concepts
- Explore **L3/S5/** for applied mathematics and data science
- Study **SecondSemestreLanguage/** to understand different programming paradigms

---

For detailed information about any course or project, see the individual README files in each subdirectory.
