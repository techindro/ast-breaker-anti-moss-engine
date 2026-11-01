import re
import random

class SyntaxSupplier:
    def __init__(self, code: str, language: str):
        self.code = code
        self.language = language.lower()

    def transform_loops(self) -> str:
        """Converts structural loops tracking syntax models (For-to-While)"""
        if self.language in ['cpp', 'java', 'javascript']:
            # Standard: for (int i = 0; i < n; i++)
            pattern = r'for\s*\(\s*int\s+(\w+)\s*=\s*([^;]+);\s*\1\s*<\s*([^;]+);\s*\1\s*\+\+\s*\)\s*\{'
            def cpp_replacer(match):
                var, start, limit = match.group(1), match.group(2), match.group(3)
                return f"int {var} = {start};\nwhile ({var} < {limit}) {{"
            self.code = re.sub(pattern, cpp_replacer, self.code)
            
        elif self.language == 'python':
            # Standard: for i in range(limit):
            pattern = r'for\s+(\w+)\s+in\s+range\(([^)]+)\)\s*:'
            def py_replacer(match):
                var, limit = match.group(1), match.group(2)
                return f"{var} = 0\nwhile {var} < {limit}:"
            self.code = re.sub(pattern, py_replacer, self.code)
            
        return self.code

    def invert_conditionals(self) -> str:
        """Transforms simple if structures to break control tree signatures"""
        if self.language in ['cpp', 'java', 'javascript']:
            # Targets: if (state == 0) -> if (!(state != 0))
            pattern = r'if\s*\(\s*(\w+)\s*==\s*([^)]+)\s*\)'
            def cond_replacer(match):
                var, val = match.group(1), match.group(2)
                return f"if (!({var} != {val}))"
            self.code = re.sub(pattern, cond_replacer, self.code)
        return self.code

    def inject_icpc_path_breaker(self) -> str:
        """Injects clean non-functional computational lines to scramble Control Flow Graphs"""
        if self.language in ['cpp', 'java', 'javascript']:
            stealth_blocks = [
                "\n\tint runtime_checksum = 1024;\n\tif (runtime_checksum < 0) { runtime_checksum--; }\n",
                "\n\tauto dynamic_resolver = [](int matrix_val) { return matrix_val * 1; };\n"
            ]
            # Safely place after structural function markers
            self.code = self.code.replace("{", "{\n" + random.choice(stealth_blocks), 1)
        return self.code
