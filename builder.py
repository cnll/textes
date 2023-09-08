#!/usr/bin/env python3

import subprocess
import re
from os import makedirs
from pathlib import Path

import cleez
from cleez import CLI
from cleez.colors import green


DOCS = [
    "cp-cnll-cra-sept-2023",
]


def sh(cmd: list):
    print(green(" ".join([str(x) for x in cmd])))
    subprocess.run(cmd, check=True)


class Make(cleez.Command):
    """Make the text"""

    name = "make"

    def run(self):
        for doc in DOCS:
            self.make(doc)

    def make(self, DOC):
        makedirs("dist", exist_ok=True)
        self.md_to_pdf(Path(f"src/{DOC}.md"), Path(f"dist/{DOC}.typ"))

    def md_to_pdf(self, md_file: Path, typ_file: Path):
        text = md_file.read_text()
        m = re.match("(?s)<!--(.*?)-->(.*)", text)
        if m:
            preamble = m.group(1).strip()
            text = m.expand(r"TOTOTITI\n\2")
            # text = text.replace(inserted_text, "TOTOTITI").strip()
        else:
            preamble = ""

        tmp_file = md_file.with_suffix(".tmp.md")
        Path(tmp_file).write_text(text)
        sh(["pandoc", "--wrap=none", "-o", str(typ_file), str(tmp_file)])

        text = typ_file.read_text()
        text = text.replace("TOTOTITI", preamble)
        typ_file.write_text(text)

        sh(["typst", "compile", "--root=.", str(typ_file)])


if __name__ == "__main__":
    cli = CLI()
    cli.add_command(Make)
    cli.run()
