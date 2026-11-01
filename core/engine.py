import sys
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

        # Step 3: Map active variables to secure semantic dictionary tokens
        tokenizer = SemanticTokenizer(self.code, self.language)
        self.code = tokenizer.transform_identifiers(target_vars)

        return self.code

if __name__ == "__main__":
    # Sample integration test check for verification
    demo_cpp = """
int main() {
    int n = 20;
    for (int i = 0; i < n; i++) {
        cout << i;
    }
}
    """
    engine = ASTBreakerOrchestrator(demo_cpp, "cpp")
    transformed_output = engine.compile_stealth_output(["n", "i"])
    print("--- Transformed Output Example ---")
    print(transformed_output)
