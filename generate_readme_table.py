import csv
import json

from go_home import go_home

def main():
    go_home()

    descriptions: list[list[str]] = []

    tag_version: str = ""
    repo_link: str = ""

    with open("variables.json", "r") as file:
        loaded = json.load(file)
        tag_version = loaded["tag_version"]
        repo_link = loaded["repo_link"]

    with open("descriptions.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            descriptions.append(row)

    with open("readme_table.md", "w") as file:
        file.write("| Name | Description | Preview | Download |\n")
        file.write("| --- | --- | --- | --- |\n")

        for i in descriptions:
            file.write(f"| {i[0]} |"
                f" {i[1]} |"
                f" {'-' if i[0] == 'All' else f'![](preview/{i[0].lower()}.png)'} |"
                f" [Download {i[0]}]({repo_link}/releases/download/{tag_version}/CypoPack-{i[0]}.zip) |"
                f"\n"
            )

if __name__ == '__main__':
    main()