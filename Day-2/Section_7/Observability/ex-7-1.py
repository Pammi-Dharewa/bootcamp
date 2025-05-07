import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_with_context(user_id, func_name):
    logging.info(f"User ID: {user_id}, Function: {func_name} - Log Message")
