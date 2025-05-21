import base64
import os
from pathlib import Path
from typing import Iterable, List, Optional

import openai


def read_text(path_or_text: str) -> str:
    """Return text from a path or the string itself."""
    if os.path.isfile(path_or_text):
        with open(path_or_text, "r", encoding="utf-8") as f:
            return f.read()
    return path_or_text


def encode_images(image_paths: Iterable[str]) -> List[str]:
    """Encode each image to a base64 data URL."""
    encoded_images = []
    for img_path in image_paths:
        with open(img_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        encoded_images.append(
            f"Image {Path(img_path).name}: data:image/png;base64,{b64}"
        )
    return encoded_images


def read_data_files(data_paths: Iterable[str]) -> List[str]:
    """Return the contents of numeric data files."""
    contents = []
    for data_path in data_paths:
        with open(data_path, "r", encoding="utf-8") as f:
            contents.append(f"{Path(data_path).name}:\n{f.read()}")
    return contents


def build_prompt(
    images: Optional[Iterable[str]] = None,
    data_files: Optional[Iterable[str]] = None,
    clinical_text: Optional[str] = None,
) -> str:
    """Construct the prompt to send to the language model."""
    parts: List[str] = []

    if images:
        parts.append("Images:\n" + "\n".join(encode_images(images)))

    if data_files:
        parts.append("Numeric data:\n" + "\n".join(read_data_files(data_files)))

    if clinical_text:
        parts.append("Clinical text:\n" + read_text(clinical_text))

    return "\n\n".join(parts) + "\n\nSummarize the above information."


def generate_summary(prompt: str, api_key: str, *, model: str = "gpt-4-1106-preview") -> str:
    """Call the OpenAI API and return the summary."""
    openai.api_key = api_key
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes medical data."},
        {"role": "user", "content": prompt},
    ]
    response = openai.ChatCompletion.create(model=model, messages=messages)
    return response["choices"][0]["message"]["content"].strip()
