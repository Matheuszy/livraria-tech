from dotenv import load_dotenv
from passlib.context import CryptContext
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


