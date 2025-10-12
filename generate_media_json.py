import os
import json

# 🔧 CONFIGURE THIS
username = "GYFTDCHYLD"
repo = "Yingyu-Laoshi-Files"
branch = "main"

# Base folders
folders = ["audio"]

# Add flashcard and story folders for starter, junior, senior (1–10)
levels = ["starter", "junior", "senior"]
for level in levels:
    folders += [f"scene/{level}/flashcards/{i}" for i in range(1, 11)]
    folders += [f"scene/{level}/story/{i}" for i in range(1, 11)]

def build_raw_url(path):
    return f"https://github.com/{username}/{repo}/raw/{branch}/{path}"

media_map = {}

for folder in folders:
    for root, _, files in os.walk(folder):
        for file in files:
            rel_path = os.path.join(root, file).replace("\\", "/")
            media_map[rel_path] = build_raw_url(rel_path)

with open("media.json", "w") as f:
    json.dump(media_map, f, indent=2)

print("✅ media.json generated with", len(media_map), "entries.")
