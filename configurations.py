from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv('BASE_URL')
users_api_url = os.getenv('USERS_API_URL')
