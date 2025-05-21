import argparse
import os

from j_llm.summarizer import build_prompt, generate_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize AI results")
    parser.add_argument("--images", nargs="*", help="Paths to image files")
    parser.add_argument("--data", nargs="*", help="Paths to numeric data files")
    parser.add_argument("--text", help="Clinical text or path to a text file")
    parser.add_argument("--output", help="Optional path to save the summary")
    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        parser.error("OPENAI_API_KEY environment variable not set")

    prompt = build_prompt(images=args.images, data_files=args.data, clinical_text=args.text)
    summary = generate_summary(prompt, api_key)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(summary)
    else:
        print(summary)


if __name__ == "__main__":
    main()
