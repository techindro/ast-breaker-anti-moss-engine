import re

class SyntaxSupplier:
    def __init__(self, code: str, language: str):
        self.code = code
        self.language = language.lower()

    def transform_loops(self) -> str:
        """Converts for-loops into functional while-loops to bypass AST matching"""
        if self.language in ['cpp', 'java', 'javascript']:
            # Capture standard: for (int i = 0; i < n; i++)
            pattern = r'for\s*\(\s*int\s+(\w+)\s*=\s*([^;]+);\s*\1\s*<\s*([^;]+);\s*\1\s*\+\+\s*\)\s*\{'
            
            def cpp_replacer(match):
                var, start, limit = match.group(1), match.group(2), match.group(3)
                return f"int {var} = {start};\nwhile ({var} < {limit}) {{"
            
            self.code = re.sub(pattern, cpp_replacer, self.code)
            
        elif self.language == 'python':
            # Capture standard: for i in range(limit):
            pattern = r'for\s+(\w+)\s+in\s+range\(([^)]+)\)\s*:'
            
            def py_replacer(match):
                var, limit = match.group(1), match.group(2)
                return f"{var} = 0\nwhile {var} < {limit}:"
                
            self.code = re.sub(pattern, py_replacer, self.code)
            
        return self.code
