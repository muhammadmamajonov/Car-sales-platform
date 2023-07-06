import logging

# Configure logging to write to a file
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Redirect prints to the logging system
class PrintLogger:
    def __init__(self, logger, level=logging.INFO):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message.strip() != "":
            self.logger.log(self.level, message.strip())

# Create an instance of the PrintLogger class
print_logger = PrintLogger(logging.getLogger(), logging.INFO)

# Redirect the print function to the PrintLogger instance
# This will capture print statements and log them to the file
print = print_logger.write

# Usage example
print("This is my log.")

# # Other logging statements
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
print("This is my second log.")