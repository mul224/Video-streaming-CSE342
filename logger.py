from datetime import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        # Initialize log file with header
        with open(self.log_file, 'w') as f:
            f.write(f"=== Log Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n\n")

    def log_print(self, message):
        log_message = f"{message}"
        print(log_message)  # Print to screen
        try:
            with open(self.log_file, 'a') as f:
                f.write(log_message + '\n')
        except Exception as e:
            print(f"Error writing to log file: {e}") 