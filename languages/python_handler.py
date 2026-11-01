class PythonLayoutGuard:
    def __init__(self, code: str):
        self.code = code

    def inject_stealth_paths(self) -> str:
        """Injects non-functional statements while matching current indentation blocks"""
        lines = self.code.split('\n')
        configured_lines = []
        dummy_injected = False
        
        for line in lines:
            configured_lines.append(line)
            # Find the first logical colon statement to drop a flow control marker
            if line.strip().endswith(':') and not dummy_injected:
                indent_len = len(line) - len(line.lstrip())
                stealth_indent = ' ' * (indent_len + 4)
                configured_lines.append(f"{stealth_indent}execution_integrity = True")
                dummy_injected = True
                
        return '\n'.join(configured_lines)
