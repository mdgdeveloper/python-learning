import sys
import os

os.system('git add .')
os.system(f'git commit -m "{sys.argv[1:]}"')
os.system('git push')
