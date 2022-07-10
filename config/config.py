from pathlib import Path

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = Path(BASE_DIR, "results")
APP_DIR = Path(BASE_DIR, "TSLA-Streamlit")

# Create dirs
DATA_DIR.mkdir(parents=True, exist_ok=True)
APP_DIR.mkdir(parents=True, exist_ok=True)
