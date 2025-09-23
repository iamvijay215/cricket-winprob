# src/config.py
from pathlib import Path

# Base project directory (one level up from src/)
PROJ = Path(__file__).resolve().parents[1]

# Data directories
RAW = PROJ / "data" / "raw" / "ipl"
PROC = PROJ / "data" / "processed"

# File paths
MATCHES_RAW = RAW / "matches.csv"
DELIV_RAW   = RAW / "deliveries.csv"

MATCHES_CLEAN = PROC / "matches_clean.csv"
DELIV_CLEAN   = PROC / "deliveries_clean.csv"

# Feature-engineered datasets (later)
FEATURES_TRAIN = PROC / "features_train.csv"
FEATURES_TEST  = PROC / "features_test.csv"