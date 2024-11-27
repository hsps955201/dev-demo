from config import ssm_retriever

API_URL = ssm_retriever.get_parameter("/api/url")
DB_HOST = "STAGING_HOST"
