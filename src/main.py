"""
Main entry point for the Todo Application.
"""
from src.interfaces.console_interface import ConsoleInterface


def main():
    """
    Main function to start the Todo Application.
    """
    print("Welcome to the Todo Application!")
    console_interface = ConsoleInterface()
    console_interface.run()


if __name__ == "__main__":
    main()