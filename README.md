# mlops-project
An MLOps end-to-end pipeline.

## Steps
- conda env create -f environment.yml
- conda activate tsla_bot
- python -m pip install -e .
- Create .env file in the root directory and store api credentials  
reddit_api_client_id=""  
reddit_api_client_secret=""  
stock_data_api_key=""  
- Run Streamlit app: `streamlit run TSLA-Streamlit/app.py`
