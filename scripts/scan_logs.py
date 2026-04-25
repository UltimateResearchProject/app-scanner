import ast, pathlib, sys
p = pathlib.Path('app.py')
code = p.read_text()
root = ast.parse(code)
issues = 0
for node in ast.walk(root):
    if isinstance(node, ast.Call):
        fn = ast.unparse(node.func) if hasattr(ast,'unparse') else ''
        if fn == 'print':
            print('ISSUE: print() used instead of logger')
            issues += 1
        if fn.endswith('info') and node.args:
            txt = ast.unparse(node.args[0]) if hasattr(ast,'unparse') else ''
            if 'login success' in txt:
                print('ISSUE: unstructured auth log')
                issues += 1
            if 'password' in txt:
                print('ISSUE: password appears in log')
                issues += 1
print(f'Total issues: {issues}')
sys.exit(1 if issues else 0)
