import os
import sys
import logging
from datetime import datetime

# Define a detailed logging format to include more context
logging_str = (
    "[%(asctime)s: %(levelname)s: %(name)s: %(funcName)s: Line %(lineno)d]: %(message)s"
)

# Create a timestamp for log file versioning (optional)
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, f"running_logs_{current_time}.log")

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format=logging_str,  # Use the detailed logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout),  # Log to the console
    ],
)

# Create a logger instance
logger = logging.getLogger("cnnClassifierLogger")

# Example usage of the logger
if __name__ == "__main__":
    logger.info("Logging setup is complete.")
    logger.debug("This is a DEBUG level message.")
    logger.warning("This is a WARNING level message.")
    logger.error("This is an ERROR level message.")
    logger.critical("This is a CRITICAL level message.")

