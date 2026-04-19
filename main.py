from dotenv import load_dotenv

load_dotenv()

from app.logger import setup_logger
from app import create_app

logger = setup_logger(__name__)


logger.info("=" * 60)
logger.info("STARTING Simple AI Agent")
logger.info("=" * 60)

app = create_app()

logger.info("Application ready to serve requests")
