# app_logger.py
import logging
import os

LOG_FILE = os.path.join("logs", "file_manager.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s - %(asctime)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def log_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error: {str(e)}")
    return wrapper
