from datetime import datetime

class Logger:
    def log(self, level, source, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] [{source}] {message}")

    def info(self, source, message):
        self.log("INFO", source, message)

    def error(self, source, message):
        self.log("ERROR", source, message)