from core.core import Core

def main():
    core = Core()
    core.start()

    input("System running. Press ENTER to shutdown...")

    core.shutdown()

if __name__ == "__main__":
    main()