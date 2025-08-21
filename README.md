## AI Meme Generator (Offline, Console)

Simple, offline meme caption generator in Python. No external APIs or image libraries.
Takes an image path, derives a description from the filename, and returns a random caption.

## Features
- Offline and dependency-free (standard library only)
- Works even if the file doesn’t exist (uses the filename)
- Built-in demo test cases

## How It Works
1. Extract base name from the provided path.
2. Remove extension, replace underscores/hyphens with spaces.
3. Pick a random caption template using that description.

## Requirements
- Python 3.8+ (tested on Python 3.13)

## Usage
```bash
python3 AiMemeGenerator.py
python3 AiMemeGenerator.py /absolute/path/to/funny_cat.png
python3 AiMemeGenerator.py "My Pictures/vacation_photo.jpeg"
```
