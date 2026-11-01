import sys
from core.tokenizer import SemanticTokenizer
from core.syntax_supplier import SyntaxSupplier
from languages.python_handler import PythonLayoutGuard

class ASTBreakerOrchestrator:
    def __init__(self, target_code: str, language: str):
        self.code = target_code
        self.language = language.lower()

    def compile_stealth_output(self, target_vars: list) -> str:
        """Processes code through the multi-layered ICPC protection pipeline"""
        # Step 1: Manage Indentation for Python scripts
        if self.language == 'python':
            guard = PythonLayoutGuard(self.code)
            self.code = guard.inject_stealth_paths()

        # Step 2: Initialize Syntax Supplier layer
        supplier = SyntaxSupplier(self.code, self.language)
        
        # Run advanced structural transformations
        self.code = supplier.transform_loops()
        self.code = supplier.invert_conditionals()
        self.code = supplier.inject_icpc_path_breaker()

        # Step 3: Replace user variables with software architecture words
        tokenizer = SemanticTokenizer(self.code, self.language)
        self.code = tokenizer.transform_identifiers(target_vars)

        return self.code

if __name__ == "__main__":
    # Test file validation simulating an ICPC competitive block
    icpc_demo_cpp = """
int main() {
    int n = 50;
    if (n == 50) {
        for (int i = 0; i < n; i++) {
            cout << i;
        }
    }
}
    """
    engine = ASTBreakerOrchestrator(icpc_demo_cpp, "cpp")
    print("--- Transformed ICPC Grade Output ---")
    print(engine.compile_stealth_output(["n", "i"]))
