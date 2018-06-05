import os
import sys

abspath = os.path.abspath(__file__)
path = os.path.join(os.path.split(abspath)[0],'..')

for p,ds,fs in os.walk(path):
    if ('__pycache__' not in p and
                '__init__.py' in fs and
                'venv' not in p):
        sys.path.insert(0, p)

from lib.config_run import app

if __name__ == '__main__':
     app.run(debug=True, port=9990)