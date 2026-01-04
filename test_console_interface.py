"""
Simple test to verify ConsoleInterface can be instantiated.
"""
from src.interfaces.console_interface import ConsoleInterface


def test_console_interface():
    print("Testing ConsoleInterface instantiation...")
    
    # Create an instance of ConsoleInterface
    console_interface = ConsoleInterface()
    
    # Verify that it has the required attributes
    assert hasattr(console_interface, 'repository')
    assert hasattr(console_interface, 'service')
    assert hasattr(console_interface, 'running')
    
    print("OK ConsoleInterface instantiation successful")
    print("OK ConsoleInterface has required attributes")

    # Verify that the service is properly connected to the repository
    assert console_interface.service.repository == console_interface.repository
    print("OK Service is properly connected to repository")
    
    print("\nConsoleInterface test passed!")


if __name__ == "__main__":
    test_console_interface()