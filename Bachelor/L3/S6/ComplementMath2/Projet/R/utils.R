# R/utils.R -- Fonctions et configuration partagées

# Bibliothèques communes
library(tidyverse)
library(caret)
library(knitr)
library(pROC)
library(corrplot)
library(here)

# Chemins du projet
DATA_DIR   <- here("data")
OUTPUT_DIR <- here("output")

# Extraction des top N éléments d'une colonne texte en indicatrices binaires
extract_top_features <- function(data, col, top_n = 10, prefix = "") {
  all_items <- data[[col]] %>%
    str_split(",\\s*") %>%
    unlist() %>%
    str_trim()
  all_items <- all_items[!is.na(all_items) & all_items != ""]

  top_items <- names(sort(table(all_items), decreasing = TRUE))[1:top_n]

  for (item in top_items) {
    col_name <- paste0(prefix, make.names(item))
    data[[col_name]] <- as.integer(grepl(item, data[[col]], fixed = TRUE))
  }
  return(list(data = data, items = top_items))
}
