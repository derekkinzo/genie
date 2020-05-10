#!/bin/bash
cd "$(dirname "$0")"
python3 fetch.py
python3 write_binary.py
make
./ranker
python3 load_pubmed_ranks.py
cd ..
