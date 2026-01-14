"""
Skill-4: ReportSkill
Generate final summary report including total files scanned, warnings found, 
and fixes applied in human-readable format.
"""
from typing import List, Dict, Any


class ReportSkill:
    """Skill to generate a human-readable report of the import case fixing process."""
    
    def execute(self, 
                total_files_scanned: int, 
                warnings: List[Dict[str, Any]], 
                changes_summary: Dict[str, Any]) -> str:
        """
        Execute the report generation.
        
        Args:
            total_files_scanned: Total number of files that were scanned
            warnings: List of warnings found during import checking
            changes_summary: Summary of changes made during auto-fixing
            
        Returns:
            Human-readable report string
        """
        report_lines = []
        
        # Header
        report_lines.append("=" * 60)
        report_lines.append("IMPORT CASE SENSITIVITY FIXER - SUMMARY REPORT")
        report_lines.append("=" * 60)
        report_lines.append("")
        
        # Summary statistics
        report_lines.append("SUMMARY:")
        report_lines.append(f"  - Total files scanned: {total_files_scanned}")
        report_lines.append(f"  - Total warnings found: {len(warnings)}")
        report_lines.append(f"  - Files with issues: {len(set(w['file'] for w in warnings)) if warnings else 0}")
        report_lines.append(f"  - Fixes applied: {changes_summary.get('fixes_applied', 0)}")
        report_lines.append(f"  - Files modified: {len(changes_summary.get('files_modified', []))}")
        report_lines.append("")
        
        # Detailed warnings
        if warnings:
            report_lines.append("WARNINGS FOUND:")
            report_lines.append("-" * 40)
            for i, warning in enumerate(warnings, 1):
                report_lines.append(f"{i}. File: {warning['file']}")
                report_lines.append(f"   Import Path: {warning['importPath']}")
                report_lines.append(f"   Issue: {warning['issue']}")
                if warning.get('expected'):
                    report_lines.append(f"   Expected: {warning['expected']}")
                if warning.get('actual'):
                    report_lines.append(f"   Actual: {warning['actual']}")
                if warning.get('suggestion'):
                    report_lines.append(f"   Suggestion: {warning['suggestion']}")
                report_lines.append("")
        else:
            report_lines.append("NO WARNINGS FOUND:")
            report_lines.append("-" * 40)
            report_lines.append("All import statements appear to have correct case sensitivity.")
            report_lines.append("")
        
        # Applied fixes
        if changes_summary.get('details'):
            report_lines.append("FIXES APPLIED:")
            report_lines.append("-" * 40)
            for i, change in enumerate(changes_summary['details'], 1):
                report_lines.append(f"{i}. File: {change['file']}")
                report_lines.append(f"   Changed: '{change['old_path']}' -> '{change['new_path']}'")
                report_lines.append(f"   Replacements made: {change['replacements']}")
                report_lines.append("")
        else:
            report_lines.append("NO FIXES APPLIED:")
            report_lines.append("-" * 40)
            report_lines.append("No automatic fixes were applied.")
            report_lines.append("")
        
        # Files modified
        if changes_summary.get('files_modified'):
            report_lines.append("FILES MODIFIED:")
            report_lines.append("-" * 40)
            for file_path in changes_summary['files_modified']:
                report_lines.append(f"  - {file_path}")
            report_lines.append("")
        
        # Footer
        report_lines.append("=" * 60)
        report_lines.append("END OF REPORT")
        report_lines.append("=" * 60)
        
        return "\n".join(report_lines)