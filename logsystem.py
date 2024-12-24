import logging

class LoggingSystem:
    def __init__(self, log_file="game_log.log"):
        self.logger = logging.getLogger("GameLogger")
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)


# Example usage
if __name__ == "__main__":
    log_system = LoggingSystem()
    log_system.log_info("Game started successfully.")
    log_system.log_warning("Memory usage is high.")
    log_system.log_error("Failed to load resource.")
    log_system.log_critical("System crash occurred.")