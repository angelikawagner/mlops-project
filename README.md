# Analyzing Market Sentiment
[Sentiment Analyzer](https://huggingface.co/spaces/awagner/tlsa-bot) - A proof of concept deployed as a Streamlit app on Hugging Face Spaces.


## Steps
- `conda env create -f environment.yml`
- `conda activate tsla_bot`
- `python -m pip install -e .`
- Create .env file in the root directory and store api credentials  
reddit_api_client_id=XXXXXX  
reddit_api_client_secret=XXXXXX  
stock_data_api_key=XXXXXX  
- Run Streamlit app: `streamlit run TSLA-Streamlit/app.py`

## Data
- Reddit
- [Twelve Data](https://twelvedata.com)
