"""
Test script to verify the import case sensitivity fixer workflow
"""
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from src.import_case_fixer.workflow import ImportCaseFixerWorkflow

def test_workflow():
    """Test the import case fixer workflow with test files."""
    print("Testing Import Case Fixer Workflow...")
    
    # Create workflow instance with test directory
    workflow = ImportCaseFixerWorkflow("test_import_case")
    
    # Run the workflow
    report = workflow.run()
    
    # Print the report
    print(report)
    
    # Show the content of the test file after fixing
    print("\nContent of TestComponent.tsx after fixing:")
    with open("test_import_case/TestComponent.tsx", "r") as f:
        print(f.read())

if __name__ == "__main__":
    test_workflow()