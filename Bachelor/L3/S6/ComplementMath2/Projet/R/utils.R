# R/utils.R -- Fonctions et configuration partagées

# Bibliothèques communes
library(tidyverse)
library(caret)
library(knitr)
library(pROC)
library(corrplot)
library(here)
library(stringi)

# Chemins du projet
DATA_DIR   <- here("data")
OUTPUT_DIR <- here("output")

# ── Palette UGA (Université Grenoble Alpes) ───────────────────────────────────
COL_PRIMARY   <- "#1D2B44"   # bleu foncé UGA
COL_SECONDARY <- "#E8601C"   # orange UGA
COL_POSITIVE  <- "#2ECC71"
COL_NEGATIVE  <- "#E74C3C"
COL_ACCENT    <- "#E8601C"   # orange UGA

FILL_SATISFACTION <- scale_fill_manual(
  values = c("Non" = COL_NEGATIVE, "Oui" = COL_POSITIVE)
)

THEME_REPORT <- theme_minimal(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", size = 12),
    legend.position = "bottom"
  )

# Configuration commune pour la validation croisée
CV_CONTROL <- trainControl(
  method = "cv",
  number = 5,
  classProbs = TRUE,
  summaryFunction = twoClassSummary,
  savePredictions = "final"
)

# ── Mapping des accords Fragrantica → familles olfactives ──────────────────────
# Basé sur une roue des parfums détaillée (16 familles → 10 groupes)
ACCORD_FAMILY_MAP <- c(
  # Citrus
  "citrus"       = "citrus",
  # Green
  "green"        = "green",
  "herbal"       = "green",
  "conifer"      = "green",
  # Aquatic / Ozone
  "aquatic"      = "aquatic",
  "marine"       = "aquatic",
  "ozonic"       = "aquatic",
  "fresh"        = "aquatic",
  # Floral
  "floral"       = "floral",
  "white floral" = "floral",
  "yellow floral" = "floral",
  "rose"         = "floral",
  "iris"         = "floral",
  "tuberose"     = "floral",
  "violet"       = "floral",
  "lavender"     = "floral",
  # Fruity
  "fruity"       = "fruity",
  "tropical"     = "fruity",
  "cherry"       = "fruity",
  "coconut"      = "fruity",
  # Spicy
  "warm spicy"   = "spicy",
  "fresh spicy"  = "spicy",
  "soft spicy"   = "spicy",
  "spicy"        = "spicy",
  "cinnamon"     = "spicy",
  "saffron"      = "spicy",
  # Woody
  "woody"        = "woody",
  "aromatic"     = "woody",
  "oud"          = "woody",
  "patchouli"    = "woody",
  "mossy"        = "woody",
  "earthy"       = "woody",
  "mineral"      = "woody",
  "camphor"      = "woody",
  # Gourmand
  "sweet"        = "gourmand",
  "vanilla"      = "gourmand",
  "caramel"      = "gourmand",
  "chocolate"    = "gourmand",
  "cacao"        = "gourmand",
  "coffee"       = "gourmand",
  "honey"        = "gourmand",
  "almond"       = "gourmand",
  "lactonic"     = "gourmand",
  "nutty"        = "gourmand",
  "coconut"      = "gourmand",
  "rum"          = "gourmand",
  "anis"         = "gourmand",
  # Leather / Smoky
  "leather"      = "leather_smoky",
  "animalic"     = "leather_smoky",
  "smoky"        = "leather_smoky",
  "tobacco"      = "leather_smoky",
  # Powdery / Musky / Amber
  "powdery"      = "powdery_amber",
  "musky"        = "powdery_amber",
  "amber"        = "powdery_amber",
  "balsamic"     = "powdery_amber",
  "aldehydic"    = "powdery_amber",
  "soapy"        = "powdery_amber"
)

OLFACTIVE_FAMILIES <- c("citrus", "green", "aquatic", "floral", "fruity",
                         "spicy", "woody", "gourmand", "leather_smoky",
                         "powdery_amber")

# ── Mapping des notes individuelles → familles olfactives ──────────────────────
# Patterns regex pour classer les notes par famille
NOTE_FAMILY_PATTERNS <- list(
  citrus = c("bergamot", "lemon", "lime", "orange", "grapefruit", "mandarin",
             "tangerine", "yuzu", "citrus", "citruses", "pomelo", "kumquat",
             "lemongrass", "verbena", "petit grain", "petitgrain", "neroli",
             "blood orange", "clementine", "cedrat"),
  green = c("green", "galbanum", "bamboo", "basil", "mint", "spearmint",
            "peppermint", "tea", "green tea", "fig leaf", "fig", "grass",
            "ivy", "fern", "artemisia", "hemp", "cannabis", "tarragon",
            "thyme", "rosemary", "sage", "clary sage", "eucalyptus",
            "juniper", "pine", "cypress", "spruce", "fir"),
  aquatic = c("aquatic", "marine", "ozonic", "ozone", "sea", "water",
              "rain", "ocean", "calone", "algae", "seaweed", "salt",
              "ambroxan", "ambrox"),
  floral = c("rose", "jasmine", "jasmin", "lily", "muguet", "gardenia",
             "magnolia", "peony", "orchid", "violet", "iris", "orris",
             "tuberose", "ylang", "neroli", "orange blossom", "geranium",
             "freesia", "carnation", "heliotrope", "honeysuckle", "lilac",
             "hyacinth", "plumeria", "frangipani", "mimosa", "chamomile",
             "chrysanthemum", "lotus", "davana", "osmanthus", "linden",
             "cherry blossom", "tiare", "peach blossom", "magnolia",
             "narcissus", "marigold", "flowers", "floral"),
  fruity = c("apple", "peach", "pear", "plum", "apricot", "berry",
             "raspberry", "strawberry", "blackberry", "blueberry", "cherry",
             "blackcurrant", "currant", "cassis", "mango", "papaya",
             "passion fruit", "pineapple", "coconut", "banana", "melon",
             "watermelon", "guava", "lychee", "litchi", "pomegranate",
             "fruity", "tropical", "quince", "fig", "dates", "grape",
             "kiwi", "cranberry"),
  spicy = c("pepper", "cinnamon", "clove", "cardamom", "ginger",
            "nutmeg", "saffron", "cumin", "coriander", "anise", "star anise",
            "fennel", "elemi", "pink pepper", "black pepper", "white pepper",
            "szechuan", "chili", "spicy", "spices"),
  woody = c("sandalwood", "cedar", "cedarwood", "vetiver", "oud",
            "agarwood", "patchouli", "guaiac", "guaiacwood",
            "birch", "oak", "ebony", "teak", "mahogany",
            "driftwood", "wood", "woody", "woods",
            "cashmeran", "hinoki", "cypress", "bamboo",
            "moss", "oakmoss", "treemoss"),
  gourmand = c("vanilla", "vanillin", "caramel", "chocolate", "cocoa",
               "cacao", "coffee", "praline", "toffee", "honey", "maple",
               "sugar", "candy", "almond", "hazelnut", "pistachio",
               "walnut", "rum", "cognac", "whiskey", "bourbon",
               "tonka", "coumarin", "milk"),
  leather_smoky = c("leather", "suede", "tobacco", "smoke", "smoky",
                     "incense", "frankincense", "olibanum", "myrrh",
                     "labdanum", "opoponax", "birch tar", "castoreum",
                     "civet", "styrax", "benzoin"),
  powdery_amber = c("musk", "amber", "ambergris", "powder", "powdery",
                     "benzoin", "copal", "resin", "balsam", "tolu",
                     "peru balsam", "aldehydes", "aldehyde",
                     "white musk", "muscs", "iso e super")
)

# ── Fonction : mapper les accords vers les familles olfactives ────────────────
map_accords_to_families <- function(data, accord_cols) {
  for (fam in OLFACTIVE_FAMILIES) {
    col_name <- paste0("fam_", fam)
    data[[col_name]] <- 0L
  }
  col_other <- "fam_autre"
  data[[col_other]] <- 0L

  for (col in accord_cols) {
    vals <- str_trim(tolower(data[[col]]))
    for (i in seq_along(vals)) {
      if (!is.na(vals[i]) && vals[i] != "") {
        mapped_fam <- ACCORD_FAMILY_MAP[vals[i]]
        if (!is.na(mapped_fam)) {
          data[[paste0("fam_", mapped_fam)]][i] <- 1L
        } else {
          data[[col_other]][i] <- 1L
        }
      }
    }
  }
  return(data)
}

# ── Fonction : mapper les notes vers les familles olfactives ──────────────────
map_notes_to_families <- function(data, col, prefix) {
  for (fam in OLFACTIVE_FAMILIES) {
    data[[paste0(prefix, fam)]] <- 0L
  }

  raw <- data[[col]]
  raw[!is.na(raw)] <- stri_enc_toutf8(raw[!is.na(raw)])

  for (i in seq_along(raw)) {
    if (is.na(raw[i]) || raw[i] == "") next
    notes <- str_trim(unlist(str_split(raw[i], ",\\s*")))
    notes <- tolower(notes[notes != ""])

    for (note in notes) {
      matched <- FALSE
      for (fam in names(NOTE_FAMILY_PATTERNS)) {
        patterns <- NOTE_FAMILY_PATTERNS[[fam]]
        if (any(sapply(patterns, function(p) grepl(p, note, fixed = TRUE)))) {
          data[[paste0(prefix, fam)]][i] <- 1L
          matched <- TRUE
          break
        }
      }
    }
  }
  return(data)
}

# ── Fonction : regrouper les catégories rares (<seuil%) en "Autre" ────────────
merge_rare_categories <- function(data, col, threshold_pct = 5) {
  freq <- table(data[[col]], useNA = "no")
  pct <- prop.table(freq) * 100
  rare <- names(pct[pct < threshold_pct])
  data[[col]] <- ifelse(data[[col]] %in% rare, "Autre", data[[col]])
  return(data)
}

# ── Fonction : fréquence des notes par phase (pour exploration) ────────────────
extract_notes_freq <- function(data, col, label) {
  raw <- data[[col]]
  raw <- raw[!is.na(raw) & raw != ""]
  all_notes <- unlist(str_split(raw, ",\\s*"))
  all_notes <- str_trim(all_notes)
  all_notes <- all_notes[all_notes != ""]
  freq <- as.data.frame(table(all_notes), stringsAsFactors = FALSE)
  colnames(freq) <- c("Note", "Freq")
  freq %>%
    mutate(Pct = round(Freq / nrow(data) * 100, 1), Type = label) %>%
    arrange(desc(Freq))
}

# ── Fonction legacy : extraction top features (conservée pour compatibilité) ──
extract_top_features <- function(data, col, top_n = 10, prefix = "") {
  raw <- data[[col]]
  raw[!is.na(raw)] <- stri_enc_toutf8(raw[!is.na(raw)])
  data[[col]] <- raw
  all_items <- raw %>%
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

# ── Fonction legacy : extraction top accords ──────────────────────────────────
extract_top_accords <- function(data, accord_cols, top_n = 10, prefix = "accord_") {
  all_accords <- data %>%
    select(all_of(accord_cols)) %>%
    unlist() %>%
    str_trim()
  all_accords <- all_accords[!is.na(all_accords) & all_accords != ""]

  top_items <- names(sort(table(all_accords), decreasing = TRUE))[1:top_n]

  for (item in top_items) {
    col_name <- paste0(prefix, make.names(item))
    data[[col_name]] <- as.integer(
      rowSums(data[accord_cols] == item, na.rm = TRUE) > 0
    )
  }
  return(list(data = data, items = top_items))
}
