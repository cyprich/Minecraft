import os

def go_home():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
