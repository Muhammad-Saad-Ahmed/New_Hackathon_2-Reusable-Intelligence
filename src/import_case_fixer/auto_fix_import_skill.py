"""
Skill-3: AutoFixImportSkill
Take warnings from CheckImportCaseSkill and automatically fix import paths to match 
correct file names on disk. Only apply fixes where a correct match can be found. 
Return summary of changes.
"""
import re
from pathlib import Path
from typing import List, Dict, Any


class AutoFixImportSkill:
    """Skill to automatically fix import paths based on warnings."""
    
    def __init__(self):
        # Pattern to match import statements that need fixing
        self.import_from_pattern = re.compile(r'(from\s+["\'])[^"\']+(["\'])')
        self.import_require_pattern = re.compile(r'(require\s*\(\s*["\'])[^"\']+(["\']\s*\))')
        self.import_simple_pattern = re.compile(r'(import\s+["\'])[^"\']+(["\'])')
        self.import_complex_pattern = re.compile(r'(import\s+[^"\']*\s+["\'])[^"\']+(["\'])')
    
    def execute(self, warnings: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Execute the auto-fix operation.
        
        Args:
            warnings: List of warnings from CheckImportCaseSkill
            
        Returns:
            Summary of changes made including files modified and fixes applied
        """
        changes_summary = {
            "files_modified": [],
            "fixes_applied": 0,
            "details": []
        }
        
        # Group warnings by file to process each file once
        file_warnings = {}
        for warning in warnings:
            file_path = warning["file"]
            if file_path not in file_warnings:
                file_warnings[file_path] = []
            file_warnings[file_path].append(warning)
        
        for file_path, file_warnings_list in file_warnings.items():
            file_changes = self._fix_file_imports(file_path, file_warnings_list)
            if file_changes:
                changes_summary["files_modified"].append(file_path)
                changes_summary["fixes_applied"] += len(file_changes)
                changes_summary["details"].extend(file_changes)
        
        return changes_summary
    
    def _fix_file_imports(self, file_path: str, warnings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Fix import statements in a single file based on warnings."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except Exception:
            return []  # Skip files that can't be read
        
        modified_content = original_content
        changes = []
        
        for warning in warnings:
            if warning.get("issue") == "case_mismatch":
                old_import_path = warning["importPath"]
                new_import_path = self._get_relative_path(file_path, warning["actual"])
                
                # Replace the import path in the content
                updated_content, replacements = self._replace_import_path(
                    modified_content, old_import_path, new_import_path
                )
                
                if replacements > 0:
                    changes.append({
                        "file": file_path,
                        "old_path": old_import_path,
                        "new_path": new_import_path,
                        "replacements": replacements
                    })
                    modified_content = updated_content
        
        # If content was modified, write it back to the file
        if modified_content != original_content:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
            except Exception:
                # If we can't write the file, remove the changes from the summary
                changes = []
        
        return changes
    
    def _replace_import_path(self, content: str, old_path: str, new_path: str) -> tuple:
        """Replace import paths in content, returning updated content and count of replacements."""
        # Calculate relative path from the file's directory
        old_path_normalized = self._normalize_path(old_path)
        new_path_normalized = self._normalize_path(new_path)
        
        # Count occurrences of the old path in import statements
        import_from_pattern = re.compile(r'(from\s+["\'])' + re.escape(old_path_normalized) + r'(["\'])')
        import_simple_pattern = re.compile(r'(import\s+["\'])' + re.escape(old_path_normalized) + r'(["\'])')
        import_complex_pattern = re.compile(r'(import\s+[^"\']*\s+["\'])' + re.escape(old_path_normalized) + r'(["\'])')
        import_require_pattern = re.compile(r'(require\s*\(\s*["\'])' + re.escape(old_path_normalized) + r'(["\']\s*\))')
        
        # Replace in 'from' imports
        updated_content, from_replacements = import_from_pattern.subn(
            r'\1' + new_path_normalized + r'\2', content
        )
        
        # Replace in simple imports
        updated_content, simple_replacements = import_simple_pattern.subn(
            r'\1' + new_path_normalized + r'\2', updated_content
        )
        
        # Replace in complex imports
        updated_content, complex_replacements = import_complex_pattern.subn(
            r'\1' + new_path_normalized + r'\2', updated_content
        )
        
        # Replace in require statements
        updated_content, require_replacements = import_require_pattern.subn(
            r'\1' + new_path_normalized + r'\2', updated_content
        )
        
        total_replacements = from_replacements + simple_replacements + complex_replacements + require_replacements
        return updated_content, total_replacements
    
    def _normalize_path(self, path: str) -> str:
        """Normalize a path string for comparison."""
        # Convert backslashes to forward slashes
        normalized = path.replace('\\', '/')
        # Remove extra slashes
        while '//' in normalized:
            normalized = normalized.replace('//', '/')
        return normalized
    
    def _get_relative_path(self, base_file: str, target_file: str) -> str:
        """Get the relative path from base_file to target_file."""
        base_dir = Path(base_file).parent
        target_path = Path(target_file)
        
        try:
            relative_path = target_path.relative_to(base_dir)
            # Convert to string and ensure it starts with ./ for relative imports
            relative_str = str(relative_path).replace('\\', '/')
            
            # If it's in a subdirectory, it will already be correct
            # If it's in the same directory, add ./
            if not relative_str.startswith('.') and not relative_str.startswith('/'):
                relative_str = './' + relative_str
            
            return relative_str
        except ValueError:
            # If target is not within base directory, return a relative path using ../
            base_parts = base_dir.parts
            target_parts = target_path.parts
            
            # Find common prefix
            common_len = 0
            for bp, tp in zip(base_parts, target_parts):
                if bp == tp:
                    common_len += 1
                else:
                    break
            
            # Calculate how many ../ to go up
            up_levels = len(base_parts) - common_len
            # Calculate the remaining path
            down_path = '/'.join(target_parts[common_len:])
            
            # Combine them
            if up_levels == 0:
                relative_str = './' + down_path
            else:
                relative_str = '../' * up_levels + down_path
            
            return relative_str