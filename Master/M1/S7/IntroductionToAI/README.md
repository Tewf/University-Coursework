# Introduction to AI

> [Lire en français](README.fr.md)

**Course:** Introduction to AI, M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes
**Teaching staff:** Nguyen Kim Thang (machine learning), Sylvain Bouveret (symbolic AI)

Two halves and nine labs. The machine-learning half runs from model evaluation
to recurrent networks in seven notebooks; the symbolic half writes logic
programs in Datalog and constraint models in OR-Tools. Every lab is a
notebook or a script to complete, so every lab has a folder here.

## The labs

| Folder | Problem | Solved with | Provided |
|---|---|---|---|
| [MachineLearning/Lab1-performance-evaluation/](MachineLearning/Lab1-performance-evaluation/) | Six predictors on the breast-cancer data, compared by accuracy, precision, recall, F1, ROC and AUC | scikit-learn metrics | subject, official correction |
| [MachineLearning/Lab2-supervised-ml/](MachineLearning/Lab2-supervised-ml/) | A linear SVM on synthetic blobs, then avalanche prediction from weather and snow data | SVM, the soft margin `C` | subject, official correction, `avalanche_data.csv`, two figures |
| [MachineLearning/Lab3-unsupervised-learning/](MachineLearning/Lab3-unsupervised-learning/) | k-means on the digits images, then PCA and t-SNE | clustering, AMI, silhouette | subject, official correction |
| [MachineLearning/Lab4-regularization/](MachineLearning/Lab4-regularization/) | Predict the IBD status of 396 patients from 1939 gut-microbe abundances, p far above n | regularisation | subject, `gut_abundances.tsv`, `ibd_status.lst` |
| [MachineLearning/Lab5-deep-learning/](MachineLearning/Lab5-deep-learning/) | Hitters salaries by linear regression and Lasso, then a two-layer network in PyTorch | `nn.Module`, a hand-written training loop | subject, `utilsDL.py`, `data/hitters.csv` |
| [MachineLearning/Lab6-fine-tuning/](MachineLearning/Lab6-fine-tuning/) | Fine-tune a ResNet18 pretrained on ImageNet for object detection on VOC images | transfer learning | subject only |
| [MachineLearning/Lab7-recurrent-networks/](MachineLearning/Lab7-recurrent-networks/) | Predict humidity from the CUBEMS building data, windows of past steps in, future steps out | RNN, LSTM | subject, `utils.py`, `data.csv` |
| [SymbolicAI/Lab1-datalog/](SymbolicAI/Lab1-datalog/) | A 45-rule loan knowledge base, a Game of Thrones family tree, train connections and shortest journeys | pyDatalog | subject, rule base, `familyTree.py`, `test-pyDatalog.py`, `got.csv`, `trains.csv` |
| [SymbolicAI/Lab2-constraint-programming/](SymbolicAI/Lab2-constraint-programming/) | N-queens, a Sudoku solver, a cryptarithmetic solver, family queries as a CP model | Google OR-Tools | subject, `got.csv` |

Three things to know before opening one:

- **Lab 5 reads `data/hitters.csv`**, lowercase and in a subfolder, while the
  archive ships `Hitters.csv` at its root. The copy here is placed where cell 4
  looks for it. The same notebook downloads FashionMNIST and CIFAR10 into
  `data/`, which is why that directory is gitignored whole.
- **Lab 6 cannot run as shipped.** Its notebook imports `model.py` and
  `utils.py` and loads `data/*.pt`, none of which were ever distributed with
  it. The folder holds the subject and nothing else until they turn up.
- **`familyTree.py` is a starter you add predicates to** (questions 8 to 11).
  The pristine copy stays as provided; the work goes in a module of its own
  that imports it, so the staff's file is never committed as if it were mine.

## Setting up

One conda environment for every lab, declared once in
[environment.yml](environment.yml):

```bash
conda env create -f environment.yml
conda activate m1ai-intro-ai
```

Start a lab by copying its subject out of `handout/` and opening the copy:

```bash
cd MachineLearning/Lab2-supervised-ml
cp handout/Lab2-supervised-ml.ipynb .
jupyter lab Lab2-supervised-ml.ipynb
```

That copy is the file that gets committed. The one in `handout/` never changes.

## Folder Structure

Each lab keeps what the staff handed out in `handout/` (subject, official
correction when one exists, and a `.txt` extraction of any PDF so it greps).
Provided modules and datasets sit at the lab root, where the notebook expects
them. `.publishignore` withholds all of it, so what a folder shows on GitHub is my
work and nothing else: a README saying what it asks, in my words, and the
completed notebook once there is one.

```
IntroductionToAI/
|-- environment.yml              <- the one conda environment
|-- MachineLearning/
|   |-- Lab1-performance-evaluation/
|   |   |-- handout/             <- subject, official correction
|   |   |-- README.md            <- the ask in my words
|   |-- Lab2-supervised-ml/
|   |   |-- handout/
|   |   |-- avalanche_data.csv svm.png svm0.png   <- what the notebook reads
|   |   |-- as-downloaded.zip    <- the archive, for provenance
|   |-- ... Lab7-recurrent-networks/
|-- SymbolicAI/
|   |-- Lab1-datalog/
|   |   |-- handout/             <- subject, Datalog-Rules.pdf, both as .txt too
|   |   |-- familyTree.py test-pyDatalog.py got.csv trains.csv
|   |-- Lab2-constraint-programming/
```

## Where the explanations live

Not here. The concepts each lab needs — evaluation metrics, SVMs, clustering,
regularisation, gradient descent and backpropagation, recurrent networks,
propositional and first-order logic, Datalog, constraint propagation — are
written up in a separate Obsidian vault, one note per concept, alongside the
lecture slides they come from, the exam papers and the textbooks. Each lab
there maps its questions to the concepts they need. A comment here that starts
teaching theory belongs in that note instead.

## Source material

The subjects, the official corrections, the helper modules and the datasets
are **not redistributed here**: see [NOTICE](../../../../NOTICE). They stay on
disk in each lab folder and `.publishignore` keeps them out of the public repository. What
is committed is the work written against them.
