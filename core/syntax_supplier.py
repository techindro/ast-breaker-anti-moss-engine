import re
import random

class SyntaxSupplier:
    def __init__(self, code: str, language: str):
        self.code = code
        self.language = language.lower()

    def transform_loops(self) -> str:
        """Transforms structural loops across all major programming languages"""
        # Group 1: Brace-based languages (C, C++, Java, JavaScript)
        if self.language in ['c', 'cpp', 'java', 'javascript']:
            # Capture standard: for (int i = 0; i < n; i++) or for (var i = 0; i < n; i++)
            pattern = r'for\s*\(\s*(int|var|let)?\s*(\w+)\s*=\s*([^;]+);\s*\2\s*<\s*([^;]+);\s*\2\s*\+\+\s*\)\s*\{'
            
            def brace_replacer(match):
                data_type = match.group(1) if match.group(1) else "int"
                var, start, limit = match.group(2), match.group(3), match.group(4)
                return f"{data_type} {var} = {start};\nwhile ({var} < {limit}) {{"
            
            self.code = re.sub(pattern, brace_replacer, self.code)
            
        elif self.language == 'python':
            # Capture standard: for i in range(limit):
            pattern = r'for\s+(\w+)\s+in\s+range\(([^)]+)\)\s*:'
            
            def py_replacer(match):
                var, limit = match.group(1), match.group(2)
                return f"{var} = 0\nwhile {var} < {limit}:"
                
            self.code = re.sub(pattern, py_replacer, self.code)
            
        return self.code

    def invert_conditionals(self) -> str:
        """Inverts decision blocks to disrupt Control Flow Graph (CFG) symmetry"""
        if self.language in ['c', 'cpp', 'java', 'javascript']:
            # Targets basic equality checkpoints: if (state == 0) -> if (! (state != 0))
            pattern = r'if\s*\(\s*(\w+)\s*==\s*([^)]+)\s*\)'
            
            def cond_replacer(match):
                var, val = match.group(1), match.group(2)
                return f"if (!({var} != {val}))"
                
            self.code = re.sub(pattern, cond_replacer, self.code)
        return self.code

    def transform_sql_logic(self) -> str:
        """Applies logical inversion and keyword casing updates to declarative SQL"""
        if self.language == 'sql':
            # Invert standard comparison symbols: threshold > 100 -> NOT (threshold <= 100)
            pattern_gt = r'\b(\w+)\s*>\s*([^\s;]+)'
            self.code = re.sub(pattern_gt, r'NOT (\1 <= \2)', self.code)
            
            # Randomize character capitalization matrix for SQL statements
            keywords = ['SELECT', 'FROM', 'WHERE', 'JOIN', 'ON', 'GROUP BY', 'ORDER BY', 'HAVING']
            for kw in keywords:
                pattern_kw = r'\b' + re.escape(kw) + r'\b'
                variant = "".join(random.choice([c.upper(), c.lower()]) for c in kw)
                self.code = re.sub(pattern_kw, variant, self.code, flags=re.IGNORECASE)
                
        return self.code
