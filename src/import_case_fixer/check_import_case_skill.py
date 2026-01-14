"""
Skill-2: CheckImportCaseSkill
Read each file from ScanFilesSkill, parse all import statements, and detect case-sensitive 
mismatches or missing files. Output warnings with {file, importPath}.
"""
import re
from pathlib import Path
from typing import List, Dict, Any
import os


class CheckImportCaseSkill:
    """Skill to check import statements for case sensitivity issues."""
    
    def __init__(self):
        # Regular expression to match import statements
        self.import_pattern = re.compile(
            r'(?:^|\s)from\s+["\']([^"\']+)["\']|'
            r'(?:^|\s)import\s+["\']([^"\']+)["\']|'
            r'(?:^|\s)import\s+[^"\']*["\']([^"\']+)["\']'
        )
        
    def execute(self, file_paths: List[str]) -> List[Dict[str, Any]]:
        """
        Execute the import case checking operation.
        
        Args:
            file_paths: List of file paths to check for import case issues
            
        Returns:
            List of warnings with file path and import path that have case issues
        """
        warnings = []
        
        for file_path in file_paths:
            file_warnings = self._check_file_imports(file_path)
            warnings.extend(file_warnings)
        
        return warnings
    
    def _check_file_imports(self, file_path: str) -> List[Dict[str, Any]]:
        """Check a single file for import case issues."""
        warnings = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            # Skip files that can't be read
            return warnings
        
        # Find all import statements
        matches = self._find_imports(content)
        
        for import_path in matches:
            # Skip relative imports starting with ./ or ../
            if import_path.startswith('.') or import_path.startswith('/'):
                # For relative paths, check if the referenced file exists with correct case
                resolved_path = self._resolve_relative_path(file_path, import_path)
                if resolved_path and not os.path.exists(resolved_path):
                    # Check if there's a case-insensitive match
                    case_warning = self._check_case_sensitivity(file_path, import_path)
                    if case_warning:
                        warnings.append(case_warning)
        
        return warnings
    
    def _find_imports(self, content: str) -> List[str]:
        """Find all import paths in the content."""
        imports = []
        
        # Match ES6 imports: import ... from "path" or require("path")
        es6_pattern = r'from\s+["\']([^"\']+)["\']|import\s+["\']([^"\']+)["\']|import\s+[^"\']*["\']([^"\']+)["\']'
        matches = re.findall(es6_pattern, content)
        
        for match in matches:
            # Each match is a tuple, find the non-empty element
            for part in match:
                if part:
                    imports.append(part)
                    break
        
        # Match CommonJS requires: require("path")
        require_pattern = r'require\s*\(\s*["\']([^"\']+)["\']\s*\)'
        require_matches = re.findall(require_pattern, content)
        imports.extend(require_matches)
        
        # Remove duplicates
        return list(set(imports))
    
    def _resolve_relative_path(self, base_file: str, import_path: str) -> str:
        """Resolve a relative import path based on the base file location."""
        base_dir = os.path.dirname(base_file)
        
        # Handle relative paths
        if import_path.startswith('./'):
            resolved = os.path.join(base_dir, import_path[2:])
        elif import_path.startswith('../'):
            resolved = os.path.join(base_dir, import_path)
        else:
            resolved = os.path.join(base_dir, import_path)
        
        # Add .js extension if no extension is provided
        if not os.path.splitext(resolved)[1]:
            for ext in ['.js', '.ts', '.tsx', '.jsx']:
                if os.path.exists(resolved + ext):
                    return resolved + ext
        
        return resolved
    
    def _check_case_sensitivity(self, file_path: str, import_path: str) -> Dict[str, Any]:
        """Check if there's a case sensitivity issue with the import path."""
        base_dir = os.path.dirname(file_path)
        resolved_path = os.path.join(base_dir, import_path)
        
        # If the path has an extension, check for case mismatches
        if '.' in os.path.basename(resolved_path):
            expected_file = resolved_path
            actual_file = self._find_case_insensitive_match(expected_file)
            if actual_file and actual_file != expected_file:
                return {
                    "file": file_path,
                    "importPath": import_path,
                    "issue": "case_mismatch",
                    "expected": expected_file,
                    "actual": actual_file
                }
        else:
            # For paths without extensions, check with common extensions
            for ext in ['.js', '.ts', '.tsx', '.jsx']:
                expected_file = resolved_path + ext
                actual_file = self._find_case_insensitive_match(expected_file)
                if actual_file and actual_file != expected_file:
                    return {
                        "file": file_path,
                        "importPath": import_path,
                        "issue": "case_mismatch",
                        "expected": expected_file,
                        "actual": actual_file
                    }
        
        # Check if the file doesn't exist at all
        if not os.path.exists(resolved_path):
            # Try with extensions
            for ext in ['.js', '.ts', '.tsx', '.jsx']:
                if os.path.exists(resolved_path + ext):
                    return {
                        "file": file_path,
                        "importPath": import_path,
                        "issue": "missing_file",
                        "expected": resolved_path,
                        "suggestion": resolved_path + ext
                    }
        
        return None
    
    def _find_case_insensitive_match(self, path: str) -> str:
        """Find a file with case-insensitive matching."""
        path_obj = Path(path)
        parent_dir = path_obj.parent
        target_name = path_obj.name
        
        if not parent_dir.exists():
            return None
        
        for item in parent_dir.iterdir():
            if item.name.lower() == target_name.lower():
                return str(item)
        
        return None