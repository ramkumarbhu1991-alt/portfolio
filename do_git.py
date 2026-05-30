import subprocess
import os

commands = [
    ['git', 'config', 'user.name', 'Sahumayank2006'],
    ['git', 'config', 'user.email', 'mayank.sahu1@s.amity.edu'],
    ['git', 'add', '.'],
    ['git', 'commit', '-m', 'Initial commit with portfolio website']
]

for cmd in commands:
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=r'c:\Users\licsa\Downloads\ramcv', capture_output=True, text=True)
    if result.stdout:
        print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

