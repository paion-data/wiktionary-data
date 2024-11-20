---
license: apache-2.0
pretty_name: English Wiktionary Data in JSONL
language:
  - en
  - de
  - grc
  - la
configs:
  - config_name: Languages
    data_files:
    - split: German
      path: german-wiktextract-data.jsonl
    - split: Latin
      path: latin-wiktextract-data.jsonl
    - split: AncientGreek
      path: ancient-greek-wiktextract-data.jsonl
    - split: GraphData
      path: word-definition-graph-data.jsonl
tags:
  - Wiktionary
  - German
  - Ancient Greek
  - Latin
  - Vocabulary
size_categories:
  - 1M<n<10M
---

Wiktionary Data on Hugging Face Datasets
========================================

![Python Version Badge]
[![GitHub workflow status badge][GitHub workflow status badge]][GitHub workflow status URL]
[![Hugging Face sync status badge]][Hugging Face sync status URL]
[![Hugging Face dataset badge]][Hugging Face dataset URL]
[![Apache License Badge]][Apache License, Version 2.0]

[wiktionary-data]() is a sub-data extraction of the [English Wiktionary](https://en.wiktionary.org) that currently
supports the following languages:

- German
- Latin
- Ancient Greek
- Old Persian

[wiktionary-data]() was originally a sub-module of [wilhelm-graphdb](https://github.com/QubitPi/wilhelm-graphdb). While
the dataset it's getting bigger, I noticed a wave of more exciting potentials this dataset can bring about that
stretches beyond the scope of the containing project. Therefore I decided to promote it to a dedicated module; and here
comes this repo.

The Wiktionary language data is available on 🤗 [Hugging Face Datasets][Hugging Face dataset URL].

```python
from datasets import load_dataset
dataset = load_dataset("QubitPi/wiktionary-data", split="German")
```

The available splits are

- `German`
- `Latin`
- `AncientGreek`
- `OldPersian`

In addition, a separate split for graph data is offered:

- `GraphData`

This split contains all the languages and puts everything in a giant graph

Development
-----------

Although [the original Wiktionary dump](https://dumps.wikimedia.org/) is available, parsing it from scratch involves
rather complicated process. We would probably do it in the future. At present, however, we would simply take the awesome
works by [tatuylonen](https://github.com/tatuylonen/wiktextract) which has already processed it and presented it in
[in JSON format](https://kaikki.org/dictionary/rawdata.html). wiktionary-data takes the
__raw Wiktextract data (JSONL, one object per line)__ option.

License
-------

The use and distribution terms for [wiktionary-data]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0

[Docker login command]: https://docker.qubitpi.org//reference/cli/docker/login/#options

[GitHub workflow status badge]: https://img.shields.io/github/actions/workflow/status/QubitPi/wiktionary-data/ci-cd.yaml?branch=master&style=for-the-badge&logo=github&logoColor=white&label=CI/CD
[GitHub workflow status URL]: https://github.com/QubitPi/wiktionary-data/actions/workflows/ci-cd.yaml

[Hugging Face dataset badge]: https://img.shields.io/badge/Hugging%20Face%20Dataset-wilhelm--graphdb-FFD21E?style=for-the-badge&logo=huggingface&logoColor=white
[Hugging Face dataset URL]: https://huggingface.co/datasets/QubitPi/wiktionary-data

[Hugging Face sync status badge]: https://img.shields.io/github/actions/workflow/status/QubitPi/wiktionary-data/ci-cd.yaml?branch=master&style=for-the-badge&logo=github&logoColor=white&label=Hugging%20Face%20Sync%20Up
[Hugging Face sync status URL]: https://github.com/QubitPi/wiktionary-data/actions/workflows/ci-cd.yaml

[Python Version Badge]: https://img.shields.io/badge/Python-3.10-FFD845?labelColor=498ABC&style=for-the-badge&logo=python&logoColor=white
