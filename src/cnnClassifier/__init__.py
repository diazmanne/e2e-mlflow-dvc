import os
import sys
import logging


# Example log output:
# [2025-01-21 10:15:30,123: INFO: my_module: This is an example log message]
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where logs will be stored
log_dir = "logs"

# Define the full path to the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the logs directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Use the custom logging format defined above
    handlers=[
        logging.FileHandler(log_filepath),  # Save logs to the specified file
        logging.StreamHandler(sys.stdout)  # Output logs to the console (stdout)
    ]
)

# Create a logger instance with a custom name
logger = logging.getLogger("cnnClassifierLogger")
