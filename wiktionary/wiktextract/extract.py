# Copyright Jiaqi Liu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from wiktionary.wiktextract.german import get_gender_modifier
from wiktionary.wiktextract.german import get_german_inflection


def extract_data(wiktextract_data_path: str):
    """
    Extract data from raw-wiktextract-data.jsonl useful for wilhelmlang.com.

    There will be 3 languages extracted, each of which in a dedicated .jsonl file:

    1. German
    2. Latin
    3. Ancient Greek

    Each line of the JSONL file has the following fields:

    - term: the word of the language
    - pos: the Part of Speech of this word
    - definitions: an array of definitions, each element of the array is a string

    :param wiktextract_data_path: the path of the wiktextract jsonl file. Can be downloaded from https://kaikki.org/dictionary/rawdata.html
    """
    import json
    from wiktionary.wiktextract.parse import get_audios
    from wiktionary.wiktextract.parse import get_definitions

    with (open(wiktextract_data_path) as data,
          open("german-wiktextract-data.jsonl", "w") as german,
          open("latin-wiktextract-data.jsonl", "w") as latin,
          open("ancient-greek-wiktextract-data.jsonl", "w") as ancient_greek,
          open("old-persian-wiktextract-data.jsonl", "w") as old_persian
    ):
        for line in data:
            vocabulary = json.loads(line)
            if "lang" in vocabulary:
                term = vocabulary["word"]
                pos = vocabulary["pos"] if "pos" in vocabulary else "Unknown"
                definitions = get_definitions(vocabulary)
                audios = get_audios(vocabulary)

                if vocabulary["lang"] == "German":
                    term = get_gender_modifier(vocabulary) + term
                    german.write(
                        json.dumps({
                            "term": term,
                            "part of speech": pos,
                            "definitions": definitions,
                            "audios": audios,
                            "inflection": get_german_inflection(vocabulary)
                        })
                    )
                    german.write("\n")
                if vocabulary["lang"] == "Latin":
                    latin.write(json.dumps({"term": term, "part of speech": pos, "definitions": definitions, "audios": audios}))
                    latin.write("\n")
                if vocabulary["lang"] == "Ancient Greek":
                    ancient_greek.write(json.dumps({"term": term, "part of speech": pos, "definitions": definitions, "audios": audios}))
                    ancient_greek.write("\n")
                if vocabulary["lang"] == "Old Persian":
                    old_persian.write(json.dumps({"term": term, "part of speech": pos, "definitions": definitions, "audios": audios}))
                    ancient_greek.write("\n")

def extract_graph(wiktextract_data_path: str):
    import json
    from wiktionary.wiktextract.parse import get_definitions

    with (open(wiktextract_data_path) as data, open("word-definition-graph-data.jsonl", "w") as graph):
        for line in data:
            vocabulary = json.loads(line)
            if "lang" in vocabulary:
                term = vocabulary["word"]
                if vocabulary["lang"] == "German":
                    term = get_gender_modifier(vocabulary) + term

                source_node = {"term": term, "language": vocabulary["lang"]}

                definitions = get_definitions(vocabulary)
                for definition in definitions:
                    graph.write(json.dumps({"source": source_node, "target": definition, "label": "definition"}))
                    graph.write("\n")