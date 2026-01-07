# AutoStart

## Description
AutoStart is a Python-based application launcher that automatically starts essential development tools with a single command.

## Purpose
This utility streamlines your development workflow by launching multiple applications simultaneously. It eliminates the need to manually open each tool every time you start your work session, saving time and improving productivity.

## Features
- Configurable application paths via JSON configuration
- Launches XAMPP (web server stack) with elevated privileges
- Opens VS Code editor
- Simple and lightweight Python script
- Easy to extend for additional applications

## Configuration
Edit `config.json` to modify application paths:

```json
{
  "xampp_path": "C:\\xampp\\xampp-control.exe",
  "vscode_path": "C:\\Users\\Clifford\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}
```

## Usage
Run the script:
```bash
python index.py
```

This will automatically launch all configured applications.

## Files
- `index.py` - Main launcher script
- `config.json` - Application configuration
