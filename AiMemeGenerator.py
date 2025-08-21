#!/usr/bin/env python3
import os
import random
import sys
from typing import List


def generate_image_caption(image_path: str) -> str:
    """Generate a mock image caption from the file name.

    Uses the file's base name without extension. Replaces underscores and hyphens
    with spaces. Falls back to a generic label if the name is empty.
    """
    base_name = os.path.basename(image_path.rstrip(os.sep))
    if not base_name:
        return "mysterious image"

    name_without_ext, _ = os.path.splitext(base_name)
    cleaned = name_without_ext.replace("_", " ").replace("-", " ").strip()
    return cleaned or "mysterious image"


def generate_meme_caption(description: str) -> str:
    """Create a random meme caption from a set of templates."""
    templates: List[str] = [
        f"When you see {description} and can't even",
        f"That moment with {description} be like 😎",
        f"POV: {description} is happening right now",
        f"Me reacting to {description} 😂",
        f"Can't handle {description} right now!",
        f"Plot twist: it was {description} all along",
        f"If {description} had a theme song, it'd slap",
        f"Tell me you're {description} without telling me you're {description}",
    ]
    return random.choice(templates)


def main() -> None:
    # Use default sample image path if none is provided
    if len(sys.argv) < 2:
        print("No image path provided. Using default sample image path.")
        img_path = "sample_image.jpg"  # default test image path
    else:
        img_path = sys.argv[1]

    # Check if path exists (mock check, no actual image processing)
    if not os.path.exists(img_path):
        print(f"Image path '{img_path}' not found. Using mock description instead.")

    description = generate_image_caption(img_path)
    print(f"Generated description: {description}")

    meme_caption = generate_meme_caption(description)
    print(f"Generated meme caption: {meme_caption}")

    # ------------------------
    # TEST CASES
    # ------------------------
    test_img_paths = ["sample_image.jpg", "funny_cat.png", "vacation_photo.jpeg", "meme-idea.PNG", ""]
    for test_path in test_img_paths:
        test_description = generate_image_caption(test_path)
        test_caption = generate_meme_caption(test_description)
        print(f"Test Path: {test_path if test_path else '[empty path]'}")
        print(f"Description: {test_description}")
        print(f"Meme Caption: {test_caption}")
        print("---")


if __name__ == "__main__":
    main()
