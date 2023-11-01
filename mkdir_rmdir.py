from pathlib import Path
cwd = Path('/Users') / 'Xadmin' / 'Desktop' / 'python' / 'python_teach-2' / 'Django'

if not cwd.exists():
        cwd.mkdir()

if cwd.exists():
    cwd.rmdir()
