import re
import random

class SemanticTokenizer:
    def __init__(self, code: str, language: str):
        self.code = code
        self.language = language.lower()
        self.mapping = {}
        
        # Professional standard dictionary for generating meaningful names
        self.prefixes = ['engine', 'stream', 'buffer', 'metric', 'payload', 'task', 'pipeline', 'state', 'node', 'cluster']
        self.suffixes = ['handler', 'manager', 'tracker', 'adapter', 'resolver', 'validator', 'schema', 'factory', 'context']

    def generate_semantic_identifier(self) -> str:
        """Generates clean variable tokens using standard coding terminology"""
        while True:
            p = random.choice(self.prefixes)
            s = random.choice(self.suffixes)
            candidate = f"{p}_{s}"
            if candidate not in self.mapping.values():
                return candidate

    def transform_identifiers(self, active_variables: list) -> str:
        """Maps user variables to new semantic words using strict word boundaries"""
        for var in sorted(active_variables, key=len, reverse=True):
            if var not in self.mapping:
                self.mapping[var] = self.generate_semantic_identifier()
            
            self.code = re.sub(r'\b' + re.escape(var) + r'\b', self.mapping[var], self.code)
        return self.code
