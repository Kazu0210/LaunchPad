import os
import json

with open("config.json") as f:
    config = json.load(f)

xampp_path = config["xampp_path"]
vscode_path = config["vscode_path"]

os.startfile(xampp_path, "runas")
os.startfile(vscode_path)