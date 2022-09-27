import sys
import os

os.system('git add .')
message = " ".join(sys.argv[1:])
os.system(f'git commit -m "{message}"')
os.system('git push')
