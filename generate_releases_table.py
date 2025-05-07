#!/usr/bin/env python3

import os
import hashlib
from go_home import go_home

go_home()

FILES = os.listdir("zip")

def generate_checksums(file: str) -> tuple[str, str]:
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        for chunk in iter(lambda: f.read(8019), b''):
            sha1.update(chunk)
            sha256.update(chunk)

    return sha1.hexdigest(), sha256.hexdigest()


sums = [generate_checksums(f"zip/{i}") for i in FILES]


with open("releases_table.md", "w") as file:
    file.write("| File name | SHA-1 Checksum | SHA-256 Checksum |\n")
    file.write("| --- | --- | --- |\n")

    for i in range(len(FILES)):
        file.write(f"| {FILES[i]} | `{sums[i][0]}` | `{sums[i][1]}` |\n")
