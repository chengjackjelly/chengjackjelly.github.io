import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Define the path to the 'markdown' and 'html' folders
markdown_folder_path = Path('./markdown')
html_folder_path = Path('./html')

# Ensure that the html folder exists
html_folder_path.mkdir(exist_ok=True)

# Function to convert a markdown file to HTML using pandoc
def convert_markdown_to_html(markdown_file):
    output_file = html_folder_path / (markdown_file.stem + '.html')
    command = f"pandoc -f markdown+lists_without_preceding_blankline -s {markdown_file} -o {output_file}"
    try:
        print(f"Converting {markdown_file} to {output_file}...")
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully converted {markdown_file} to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {markdown_file}: {e}")

# Get all markdown files from the markdown folder
markdown_files = list(markdown_folder_path.glob('*.md'))

# Use ThreadPoolExecutor to convert files in parallel
with ThreadPoolExecutor() as executor:
    executor.map(convert_markdown_to_html, markdown_files)
