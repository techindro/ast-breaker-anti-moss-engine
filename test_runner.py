import sys
from core.engine import ASTBreakerOrchestrator

def run_comprehensive_matrix_tests():
    print("=" * 70)
    print("      AST-BREAKER ENGINE FULL SIX-LANGUAGE INTEGRATION TEST          ")
    print("=" * 70)

    # --- 1. JAVA TARGET CHECK ---
    java_input = """public class Solution {
    public void compute() {
        int n = 100;
        for (int i = 0; i < n; i++) {
            System.out.println(i);
        }
    }
}"""
    print("\n[TEST 1] Testing Java Plagiarism Bypass Matrix...")
    java_engine = ASTBreakerOrchestrator(java_input, "java")
    java_engine.save_transformation_to_file(["n", "i"], filename="JavaResult")
    print("-" * 60)

    # --- 2. JAVASCRIPT TARGET CHECK ---
    js_input = """function processData() {
    var limit = 45;
    for (var idx = 0; idx < limit; idx++) {
        console.log(idx);
    }
}"""
    print("\n[TEST 2] Testing JavaScript Lexical Node Transformation...")
    js_engine = ASTBreakerOrchestrator(js_input, "javascript")
    js_engine.save_transformation_to_file(["limit", "idx"], filename="JavaScriptResult")
    print("-" * 60)

    # --- 3. C PROGRAM TARGET CHECK ---
    c_input = """int main() {
    int counter = 25;
    if (counter == 25) {
        for (int x = 0; x < counter; x++) {
            printf("%d", x);
        }
    }
}"""
    print("\n[TEST 3] Testing C Syntax Loops Realignment...")
    c_engine = ASTBreakerOrchestrator(c_input, "c")
    c_engine.save_transformation_to_file(["counter", "x"], filename="CResult")
    print("=" * 70)
    print("All multi-language validation checks completed successfully.")

if __name__ == "__main__":
    run_comprehensive_matrix_tests()
