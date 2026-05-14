import os
from dotenv import load_dotenv

load_dotenv()

# Detect Railway environment or local
DATA_DIR = os.getenv("RAILWAY_VOLUME_MOUNT_PATH", os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(DATA_DIR):
    try:
        os.makedirs(DATA_DIR)
    except Exception:
        DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data_path(filename):
    """Returns the full path for a data file, ensuring it's in the persistent DATA_DIR."""
    return os.path.join(DATA_DIR, filename)

CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID", "common").strip() or "common"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
GRAPH_SCOPES = [
    "https://graph.microsoft.com/Mail.ReadWrite",
    "https://graph.microsoft.com/Mail.Send",
    "https://graph.microsoft.com/Files.ReadWrite"
]

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", 30))
MARKETING_FOLDER_PATH = os.getenv("MARKETING_FOLDER_PATH", "Marketing")
LINKEDIN_PROFILE_URL = os.getenv(
    "LINKEDIN_PROFILE_URL",
    "https://www.linkedin.com/in/muhammad-haris-2a805b24b/"
)

# Persistent file paths
TOKEN_CACHE_PATH = get_data_path("outlook_token_cache.bin")
LINKEDIN_STATE_PATH = get_data_path("linkedin_state.json")
PROCESSED_EMAILS_PATH = get_data_path("processed_email_ids.json")
PROCESSED_MARKETING_PATH = get_data_path("processed_marketing_onedrive_files.json")
ANALYTICS_DB_PATH = get_data_path("analytics.db")
MARKETING_PROMPT_CONFIG_PATH = get_data_path("marketing_campaign_system_prompt.json")
