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
        """Processes code through full obfuscation tracking pipeline sequentially"""
        # Step 1: Manage layout specifications for python properties
        if self.language == 'python':
            guard = PythonLayoutGuard(self.code)
            self.code = guard.inject_stealth_paths()

        # Step 2: Run loop configuration rewriter (Syntax Supplier)
        supplier = SyntaxSupplier(self.code, self.language)
        self.code = supplier.transform_loops()
        self.code = supplier.invert_conditionals()
        self.code = supplier.inject_icpc_path_breaker()

        # Step 3: Map active variables to secure semantic dictionary tokens
        tokenizer = SemanticTokenizer(self.code, self.language)
        self.code = tokenizer.transform_identifiers(target_vars)

        return self.code

    def save_transformation_to_file(self, target_vars: list, filename: str = "output_result") -> str:
        """Compiles the source code and logs the structure into a dedicated result file"""
        processed_code = self.compile_stealth_output(target_vars)
        
        # Mapping standard structural extensions
        ext = ".py" if self.language == "python" else f".{self.language}"
        full_path = f"{filename}{ext}"
        
        # Executing discrete local storage save operations
        try:
            with open(full_path, "w", encoding="utf-8") as file:
                file.write(processed_code)
            print(f"[SUCCESS] Transformed logic saved safely to localized structure: '{full_path}'")
        except Exception as e:
            print(f"[ERROR] Failed to save code block inside results file: {e}")
            
        return full_path

if __name__ == "__main__":
    # Standard runtime verification pipeline check
    demo_cpp = """
int main() {
    int n = 20;
    for (int i = 0; i < n; i++) {
        cout << i;
    }
}
    """
    engine = ASTBreakerOrchestrator(demo_cpp, "cpp")
    # Generates code matrix and stores it cleanly inside output_result.cpp file
    engine.save_transformation_to_file(["n", "i"], filename="output_result")
