# CNLL text & reports

See also: [CNLL News](https://cnll.fr/news/) and [CNLL Etudes et rapports](https://cnll.fr/publications/)


## Contents (in reverse chronological order)

- [Déclaration du CNLL sur le CRA (*Cyber Resilience Act*)](src/etude-cra-sept-2023.md)
- [La France doit protéger sa filière du logiciel libre des effets de bord du Cyber Resilience Act (CRA)](src/cp-cnll-cra-sept-2023.md)


## Install

This project is developped using [rye](https://rye-up.com/) and [typst](https://typst.app/) which much be installed independently.

To generate the PDFs from the Markdown sources, run:

```bash
make
```

Under the hood, this will call the `build.py` script which will transform the Markdown sources to Typst source files (`.typ`) then into PDFs using [typst](https://typst.app/).
