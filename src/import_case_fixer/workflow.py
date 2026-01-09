"""
Main workflow for checking and fixing import case sensitivity issues in frontend code.
This workflow combines all four skills to create a complete solution.
"""
from pathlib import Path
from typing import List, Dict, Any
from src.import_case_fixer.scan_files_skill import ScanFilesSkill
from src.import_case_fixer.check_import_case_skill import CheckImportCaseSkill
from src.import_case_fixer.auto_fix_import_skill import AutoFixImportSkill
from src.import_case_fixer.report_skill import ReportSkill


class ImportCaseFixerWorkflow:
    """Complete workflow for checking and fixing import case sensitivity issues."""
    
    def __init__(self, base_path: str = "frontend/src"):
        self.scan_skill = ScanFilesSkill(base_path)
        self.check_skill = CheckImportCaseSkill()
        self.fix_skill = AutoFixImportSkill()
        self.report_skill = ReportSkill()
    
    def run(self, extensions: List[str] = None) -> str:
        """
        Run the complete workflow.
        
        Args:
            extensions: List of file extensions to scan for (default: ['.ts', '.tsx', '.js', '.jsx'])
            
        Returns:
            Human-readable report of the process
        """
        print("Starting import case sensitivity check and fix workflow...")
        
        # Skill-1: Scan files
        print("Step 1: Scanning files...")
        file_paths = self.scan_skill.execute(extensions)
        print(f"  Found {len(file_paths)} files to check")
        
        # Skill-2: Check import case sensitivity
        print("Step 2: Checking import statements for case sensitivity issues...")
        warnings = self.check_skill.execute(file_paths)
        print(f"  Found {len(warnings)} warnings")
        
        # Skill-3: Auto-fix import paths
        print("Step 3: Applying automatic fixes...")
        changes_summary = self.fix_skill.execute(warnings)
        print(f"  Applied fixes to {changes_summary['fixes_applied']} import statements")
        
        # Skill-4: Generate report
        print("Step 4: Generating report...")
        report = self.report_skill.execute(len(file_paths), warnings, changes_summary)
        
        print("Workflow completed successfully!")
        return report


def main():
    """Main function to run the import case fixer workflow."""
    import sys
    
    # Get base path from command line argument, default to frontend/src
    base_path = sys.argv[1] if len(sys.argv) > 1 else "frontend/src"
    
    # Create workflow instance
    workflow = ImportCaseFixerWorkflow(base_path)
    
    # Run the workflow
    report = workflow.run()
    
    # Print the report
    print(report)


if __name__ == "__main__":
    main()