import sys
from core.engine import ASTBreakerOrchestrator

def run_system_file_tests():
    print("=" * 60)
    print("      AST-BREAKER ENGINE CORE PIPELINE INTEGRATION TEST      ")
    print("=" * 60)

    # C++ Test Case Structure
    cpp_input = """#include <iostream>
using namespace std;

int main() {
    int n = 50;
    if (n == 50) {
        for (int i = 0; i < n; i++) {
            cout << i << " ";
        }
    }
    return 0;
}"""
    
    print("\n[TEST 1] Processing C++ Segment Loop Target...")
    cpp_engine = ASTBreakerOrchestrator(cpp_input, "cpp")
    # This automatically compiles code and creates 'cpp_result.cpp' in current directory
    cpp_engine.save_transformation_to_file(["n", "i"], filename="cpp_result")
    print("-" * 60)

    # Python Test Case Structure
    python_input = """def solve_problem():
    limit = 10
    for idx in range(limit):
        print(idx)
"""

    print("\n[TEST 2] Processing Python Dynamic Indentation Layout...")
    py_engine = ASTBreakerOrchestrator(python_input, "python")
    # This automatically compiles code and creates 'py_result.py' in current directory
    py_engine.save_transformation_to_file(["limit", "idx"], filename="py_result")
    print("=" * 60)
    print("Pipeline compilation verified successfully.")

if __name__ == "__main__":
    run_system_file_tests()
