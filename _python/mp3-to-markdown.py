import config
import os
import subprocess
import sys
from markitdown import MarkItDown

path = config.PATH
FOLDER = f"{path}/converts/"

def run_convert():
    for filename in os.listdir(FOLDER):
        if filename.endswith('.mp3'):
            input_file = os.path.join(FOLDER, filename)
            output_file = os.path.join(FOLDER, f"{os.path.splitext(filename)[0]}.md")

            md = MarkItDown()
            result = md.convert(input_file)
            outcome = result.markdown_content

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(outcome)
                print(f"Markdown content written to {output_file}")


if __name__ == '__main__':
    run_convert()