from pathlib import Path
from pydantic import (
    BaseSettings
)

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = Path(BASE_DIR, "results")
APP_DIR = Path(BASE_DIR, "TSLA-Streamlit")

# Create dirs
DATA_DIR.mkdir(parents=True, exist_ok=True)
APP_DIR.mkdir(parents=True, exist_ok=True)
 
# Load creds
class Settings(BaseSettings):

    reddit_api_client_id: str
    reddit_api_client_secret: str
    stock_data_api_key: str
    reddit_api_user_agent: str = "USERAGENT"
    model_path: str = "fourthbrain-demo/model_trained_by_me2"
    class Config:
        env_file = ".env"

settings = Settings()
