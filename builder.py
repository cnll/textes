#!/usr/bin/env python3

import subprocess
import re
from os import makedirs
from pathlib import Path

import cleez
from cleez import CLI
from cleez.colors import green
from devtools import debug


DOC = "cnll-bullet-points"


def sh(cmd: list):
    print(green(" ".join([str(x) for x in cmd])))
    subprocess.run(cmd, check=True)


class Make(cleez.Command):
    """Make the text"""

    name = "make"

    def run(self):
        makedirs("dist", exist_ok=True)
        self.md_to_typ(Path(f"{DOC}.md"), Path(f"dist/{DOC}.typ"))

    def md_to_typ(self, md_file: Path, typ_file: Path):
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

    # def gen_file(self, md_file: Path):
    #     typ_file = md_file.with_suffix(".typ")
    #     if typ_file.exists() and typ_file.stat().st_mtime > md_file.stat().st_mtime:
    #         return
    #
    #     print(f"Converting {md_file} to {typ_file}")
    #     sh(["pandoc", "--wrap=none", "-o", typ_file, md_file])
    #
    #     txt = typ_file.read_text()
    #     txt = self.fix_typst(txt, md_file)
    #     typ_file.write_text(txt)
    #
    # def fix_typst(self, txt, md_file: Path):
    #     txt = txt.replace("#horizontalrule", "")
    #     depth = str(md_file).count("/") - 1
    #     txt = f'#import "{"../" * depth}templates/my-book.typ": *\n\n' + txt
    #     lines = txt.splitlines()
    #     for i in range(0, len(lines)):
    #         if lines[i].startswith("= "):
    #             lines[i] = f'#chapter("{lines[i][2:]}")'
    #     txt = "\n".join(lines)
    #     return txt


# class CleanBook(cleez.Command):
#     """Clean the book"""
#
#     name = "clean"
#
#     def run(self):
#         for md_file in Path("src").glob("**/*.md"):
#             typ_file = md_file.with_suffix(".typ")
#             if typ_file.exists():
#                 typ_file.unlink()


if __name__ == "__main__":
    cli = CLI()
    cli.add_command(Make)
    # cli.add_command(CleanBook)
    cli.run()
