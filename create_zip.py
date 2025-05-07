#!/usr/bin/env python3

import os
import zipfile
from go_home import go_home

go_home()

dirs: list[str] = [i for i in os.listdir() if os.path.isdir(i) and i.startswith("CypoPack")]

for name in dirs:
    with zipfile.ZipFile(f"zip/{name}.zip", 'w') as zfile:
        for root, _, files in os.walk(name):
            for file in files:
                file_path = os.path.join(root, file)
                zfile.write(file_path, arcname=file_path)
