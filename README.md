# J_LLM

This repository contains utilities related to running language model workflows.

## Summary AI Results

The `scripts/summarize_ai_results.py` script summarizes numerical data, images and clinical notes using OpenAI's GPT-4.1 API. Core functionality lives in the `j_llm.summarizer` module so it can be reused in other workflows.

### Prerequisites

- Python 3.8+
- Install the `openai` package: `pip install openai`
- Set the environment variable `OPENAI_API_KEY` with your API key.

### Usage

```bash
python scripts/summarize_ai_results.py \
    --images path/to/image1.png path/to/image2.jpg \
    --data path/to/values.csv \
    --text path/to/clinical.txt \
    --output summary.txt
```

The script prints the generated summary to the console or saves it to `--output` if provided.
