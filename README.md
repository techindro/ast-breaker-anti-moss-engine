# AST-Breaker Anti-MOSS Engine

A multi-language code rewriter designed to bypass MOSS and automated similarity checkers in online assessments. It automatically changes loop patterns, structural paths, and variables using real software engineering names for C++, Python, Java, and JavaScript.

## Project Description

AST-Breaker Anti-MOSS Engine is a tool built to remove code similarity fingerprints in competitive programming and online assessments. While basic code rewriters only change spaces or generate random, unreadable variable text that looks suspicious, AST-Breaker works directly on the logic structure of the programming language.

The engine modifies loop patterns (like changing for-loops to while-loops) and alters the code structure analyzed by similarity checkers like MOSS, without breaking the core logic or execution. By using clear, real programming terminology for variable remapping, the final script looks like standard, high-quality code written naturally by a developer.

The core engine disrupts automated Abstract Syntax Tree (AST) matching and Control Flow Graph (CFG) symmetry—the structural signatures analyzed by similarity detectors like MOSS (Measure of Software Similarity)—without breaking functional execution logic. By generating highly natural, contextually accurate software engineering identifiers, the output mimics high-quality, professional code configurations that are virtually indistinguishable from manually rewritten implementations.

## Directory Structure

```text
ast-breaker-engine/
│
├── core/
│   ├── engine.py              # Central orchestrator pipeline
│   ├── tokenizer.py           # Semantic identifier mapper & variable generator
│   └── syntax_supplier.py     # Syntax Supplier (For-to-While loop converter)
│
├── languages/
│   └── python_handler.py      # Python strict indentation block tracking
│
├── requirements.txt           # Environment specifications
└── README.md                  # System architecture specifications
```

## Getting Started

### Installation
```bash
git clone https://github.com/techindro/ast-breaker-anti-moss-engine.git
cd ast-breaker-engine
```

### Usage
```bash
python core/engine.py
```
