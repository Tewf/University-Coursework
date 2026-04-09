# utils.R -- Fonctions et configuration partagées
# Aligné sur Rapport_Projet_Parfums_V6.Rmd (rendu officiel du projet).

# Bibliothèques communes
suppressPackageStartupMessages({
  library(tidyverse)
  library(caret)
  library(knitr)
  library(pROC)
  library(corrplot)
  library(here)
  library(stringr)
  library(scales)
  library(gridExtra)
})

# ── Chemins du projet ─────────────────────────────────────────────────────────
DATA_DIR   <- here::here("data")
OUTPUT_DIR <- here::here("output")
if (!dir.exists(OUTPUT_DIR)) dir.create(OUTPUT_DIR, recursive = TRUE)

# ── Palette et thème graphique (identique à la V6) ─────────────────────────────
COL_PRIMARY  <- "#2E86AB"
COL_POSITIVE <- "#28A745"
COL_NEGATIVE <- "#DC3545"
COL_KNN      <- "#FF8C00"
COL_NB       <- "#9B59B6"
COL_TREE     <- "#795548"

FILL_SATISFACTION <- scale_fill_manual(
  values = c("Non" = COL_NEGATIVE, "Oui" = COL_POSITIVE)
)

THEME_REPORT <- theme_minimal(base_size = 10) +
  theme(
    plot.title = element_text(face = "bold", size = 11),
    axis.text  = element_text(size = 8),
    legend.position = "bottom"
  )

# ── Validation croisée 5-fold (métrique = AUC) ────────────────────────────────
CV_CONTROL <- trainControl(
  method = "cv",
  number = 5,
  classProbs = TRUE,
  summaryFunction = twoClassSummary,
  savePredictions = "final"
)

# ── Regrouper les catégories rares en "Other" ─────────────────────────────────
merge_rare_categories <- function(data, col, threshold_pct = 5) {
  freq <- data %>%
    filter(!is.na(.data[[col]])) %>%
    count(.data[[col]], sort = TRUE) %>%
    mutate(pct = n / sum(n) * 100)
  rare <- freq %>% filter(pct < threshold_pct) %>% pull(1)
  data[[col]][data[[col]] %in% rare] <- "Other"
  data
}

# ── Mapping accords textuels → 10 familles olfactives (V6) ────────────────────
map_accords_to_families <- function(data, accord_cols) {
  family_map <- list(
    fruity   = c("fruity", "citrus", "tropical"),
    floral   = c("floral", "rose", "white floral", "yellow floral"),
    herbal   = c("herbal", "aromatic", "green", "lavender"),
    leather  = c("leather", "animalic"),
    smoky    = c("smoky", "tobacco"),
    woody    = c("woody", "earthy", "mossy"),
    fresh    = c("fresh", "aquatic", "ozonic", "marine", "clean"),
    sweet    = c("sweet", "vanilla", "caramel", "powdery", "gourmand", "cacao"),
    oriental = c("oriental", "amber", "balsamic", "warm", "musky"),
    spicy    = c("spicy", "warm spicy", "cinnamon")
  )
  for (fam in names(family_map)) {
    kw <- family_map[[fam]]
    data[[paste0("fam_", fam)]] <- apply(data[accord_cols], 1, function(row) {
      as.integer(any(str_to_lower(str_trim(row)) %in% kw, na.rm = TRUE))
    })
  }
  data
}

OLFACTIVE_FAMILIES <- c("fruity", "floral", "herbal", "leather", "smoky",
                        "woody", "fresh", "sweet", "oriental", "spicy")

# ── Mapping notes textuelles → colonnes binaires (top 10 par phase) ───────────
map_notes_to_columns <- function(data, phase, note_col) {
  notes <- str_split(data[[note_col]], ",") %>%
    lapply(str_trim) %>%
    lapply(str_to_lower)
  all_notes <- unlist(notes)
  all_notes <- all_notes[!is.na(all_notes) & all_notes != ""]
  top_n <- names(sort(table(all_notes), decreasing = TRUE))[1:10]
  for (n in top_n) {
    data[[paste0(phase, "_", make.names(n))]] <-
      sapply(notes, function(x) as.integer(n %in% x))
  }
  data
}

# ── Helper d'extraction de fréquences de notes (pour exploration) ─────────────
parse_notes <- function(col) {
  n <- str_split(col, ",") %>%
    lapply(str_trim) %>%
    lapply(str_to_lower) %>%
    unlist()
  n[!is.na(n) & n != ""]
}

# ── Chargement train/test/feature_cols (factorisé pour les chapitres modèles) ─
load_train_test <- function() {
  list(
    train_data   = readRDS(here::here("output", "train_data.rds")),
    test_data    = readRDS(here::here("output", "test_data.rds")),
    feature_cols = readRDS(here::here("output", "feature_cols.rds"))
  )
}
