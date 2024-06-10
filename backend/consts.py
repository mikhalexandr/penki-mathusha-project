from dotenv import load_dotenv
import os


load_dotenv()

# private variables
SECRET_KEY = os.getenv("SECRET_KEY")

YANDEX_GPT_DIRECTORY_ID = os.getenv("YANDEX_GPT_DIRECTORY_ID")
YANDEX_GPT_API_KEY = os.getenv("YANDEX_GPT_API_KEY")

KEYCLOAK_SERVER_URL = os.getenv("KEYCLOAK_SERVER_URL")
KEYCLOAK_USER_REALM_NAME = os.getenv("KEYCLOAK_USER_REALM_NAME")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET_KEY = os.getenv("KEYCLOAK_CLIENT_SECRET_KEY")


# configurations
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


# achievement triggers
solved_tasks_amount = [1000, 500, 100]
rating_amount = [200, 1000, 5000]
