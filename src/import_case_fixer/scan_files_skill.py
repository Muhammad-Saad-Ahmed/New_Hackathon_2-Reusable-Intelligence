"""
Skill-1: ScanFilesSkill
Recursively scan the folder (default: frontend/src) and list all .ts, .tsx, .js, and .jsx files.
Return the full file paths.
"""
import os
from pathlib import Path
from typing import List


class ScanFilesSkill:
    """Skill to scan files in a directory for specific file extensions."""
    
    def __init__(self, base_path: str = "frontend/src"):
        self.base_path = Path(base_path)
        
    def execute(self, extensions: List[str] = None) -> List[str]:
        """
        Execute the file scanning operation.
        
        Args:
            extensions: List of file extensions to scan for (default: ['.ts', '.tsx', '.js', '.jsx'])
            
        Returns:
            List of full file paths matching the extensions
        """
        if extensions is None:
            extensions = ['.ts', '.tsx', '.js', '.jsx']
        
        file_paths = []
        
        # Convert extensions to lowercase for comparison
        extensions = [ext.lower() for ext in extensions]
        
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                # Check if file extension matches any of the target extensions
                _, ext = os.path.splitext(file)
                if ext.lower() in extensions:
                    full_path = os.path.join(root, file)
                    file_paths.append(full_path)
        
        return file_paths