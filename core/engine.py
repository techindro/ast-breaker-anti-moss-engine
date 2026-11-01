import sys
import os
from core.tokenizer import SemanticTokenizer
from core.syntax_supplier import SyntaxSupplier
from languages.python_handler import PythonLayoutGuard

class ASTBreakerOrchestrator:
    def __init__(self, target_code: str, language: str):
        self.code = target_code
        self.language = language.lower()

    def compile_stealth_output(self, target_vars: list) -> str:
        """Routes source segments across structured modular transformation phases"""
        # Step 1: Manage specific layout blocks for python indentation stability
        if self.language == 'python':
            guard = PythonLayoutGuard(self.code)
            self.code = guard.inject_stealth_paths()

        # Step 2: Initialize Structural Syntax Supplier layers
        supplier = SyntaxSupplier(self.code, self.language)
        
        if self.language == 'sql':
            self.code = supplier.transform_sql_logic()
        else:
            self.code = supplier.transform_loops()
            self.code = supplier.invert_conditionals()

        # Step 3: Map user target identifiers to elite software glossary tokens
        if target_vars:
            tokenizer = SemanticTokenizer(self.code, self.language)
            self.code = tokenizer.transform_identifiers(target_vars)

        return self.code

    def save_transformation_to_file(self, target_vars: list, filename: str = "output_result") -> str:
        """Saves the completely obfuscated valid output to your localized file system"""
        processed_code = self.compile_stealth_output(target_vars)
        
        # Extensions mapping lookup configurations
        ext_map = {
            "python": ".py", "sql": ".sql", "cpp": ".cpp", 
            "c": ".c", "java": ".java", "javascript": ".js"
        }
        ext = ext_map.get(self.language, f".{self.language}")
        full_path = f"{filename}{ext}"
        
        try:
            with open(full_path, "w", encoding="utf-8") as file:
                file.write(processed_code)
            print(f"[SUCCESS] Transformed logic saved safely to root environment: '{full_path}'")
        except Exception as e:
            print(f"[ERROR] Failed to save code block inside results file: {e}")
            
        return full_path
