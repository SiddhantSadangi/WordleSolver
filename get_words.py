#!/usr/bin/env python
# coding: utf-8

import json
import sys

import requests

# Loading words
word_site = (
    "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
)
response = requests.get(word_site)

if response.status_code == 200:
    words = response.text.split()
    print(f"Loaded {len(words)} words")
else:
    print(response)
    sys.exit(f"ERROR: {response.status_code}\nWord source not reachable")

# Saving words
with open("words.txt", "w") as f:
    json.dump(words, f)
