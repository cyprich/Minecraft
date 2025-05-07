#!/usr/bin/env python3

import os
import hashlib
import json
from go_home import go_home

def main():
    go_home()

    files: list[str] = os.listdir("zip")
    remove_letters: int = len("CypoPack-")

    tag_version: str = ""
    repo_link: str = ""

    with open("variables.json", "r") as file:
        loaded = json.load(file)
        tag_version = loaded["tag_version"]
        repo_link = loaded["repo_link"]

    def generate_checksums(file: str) -> tuple[str, str]:
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        with open(file, 'rb') as f:
            for chunk in iter(lambda: f.read(8019), b''):
                sha1.update(chunk)
                sha256.update(chunk)

        return sha1.hexdigest(), sha256.hexdigest()

    sums = [generate_checksums(f"zip/{i}") for i in files]

    with open("releases_table.md", "w") as file:
        file.write("| Resource Pack | Download link | SHA-1 Checksum | SHA-256 Checksum |\n")
        file.write("| --- | --- | --- | --- |\n")

        for i in range(len(files)):
            name = files[i][remove_letters:-4]
            file.write(f"| {name} | "
                f"[Download {name}]({repo_link}/releases/download/{tag_version}/{files[i]}) | "
                f"`{sums[i][0]}` | "
                f"`{sums[i][1]}` |"
                f"\n"
            )

if __name__ == '__main__':
    main()