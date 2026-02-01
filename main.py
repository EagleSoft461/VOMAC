from core.core import Core
import time

def main():
    core = Core()
    core.start()

    input("System running. Press ENTER to shutdown...")
    input()
    
    core.shutdown()

if __name__ == "__main__":
    main()