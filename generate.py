import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path

# Define the path to the 'markdown' and 'html' folders
markdown_folder_path = Path('./markdown')
html_folder_path = Path('./html')

# Ensure that the html folder exists
html_folder_path.mkdir(exist_ok=True)

class GitCommitEnum(Enum):
    ADD="A"
    DELETED="D"
    MODIFIED="M"

@dataclass
class Blog:
    """
    Class for keeping track of markdown file and it's current git status
    """
    markdown_file: Path
    commit_status: GitCommitEnum
        
def insert_updatetime_to_markdown(markdown: Path):
    # Ensure the file is a markdown file
    if not markdown.suffix == '.md':
        raise ValueError(f"{insert_updatetime_to_markdown.__name__}: Expected a markdown file, got {markdown.suffix}")

    # Read the current content of the file
    content = markdown.read_text()
    create_date = None
    date_section_match = None

    # Use regex to find the "date" section
    date_section_match = re.search( r"## Write in\n- Created: ([\d-]+ [\d:]+)\n- Updated: ([\d-]+ [\d:]+)\n", content)
    if date_section_match:
        date_section_end = date_section_match.end()
        content = content[date_section_end:].strip()
        create_date = date_section_match.group(1)
    else:
        create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Set current date as Created if not found
    
    
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_block_template = f"\n## Write in\n- Created: {create_date}\n- Updated: {current_date}\n\n"

    markdown.write_text(date_block_template+content)

# Function to convert a markdown file to HTML using pandoc
def convert_markdown_to_html(markdown_file: Path):

    output_file = html_folder_path / (markdown_file.stem + '.html')
    command = f"pandoc -f markdown+lists_without_preceding_blankline -s {markdown_file} -o {output_file}"
    try:
        print(f"Converting {markdown_file} to {output_file}...")
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully converted {markdown_file} to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {markdown_file}: {e}")
def remove_deleted_blog(blog:Blog):
    blog_html=html_folder_path / Path(blog.markdown_file.stem + '.html')
    blog_html.unlink(missing_ok=True)
def process_blog(blog:Blog):
    match blog.commit_status:
        case GitCommitEnum.ADD | GitCommitEnum.MODIFIED:
            print("hi")
            insert_updatetime_to_markdown(blog.markdown_file)
            print("hi")
            convert_markdown_to_html(blog.markdown_file)
            return
        case GitCommitEnum.DELETED:
            remove_deleted_blog(blog)
            return


# Get all markdown files from the markdown folder


modified_files = sys.argv[1].split(',') if sys.argv[1] else []
added_files = sys.argv[2].split(',') if sys.argv[2] else []
deleted_files = sys.argv[3].split(',') if sys.argv[3] else []

markdown_files = []
for file in modified_files:
    markdown_files.append(Blog(Path(file),GitCommitEnum.MODIFIED))

for file in added_files:
    markdown_files.append(Blog(Path(file),GitCommitEnum.ADD))

for file in deleted_files:
    markdown_files.append(Blog(Path(file),GitCommitEnum.DELETED))

print(markdown_files)

# Use ThreadPoolExecutor to convert files in parallel
with ThreadPoolExecutor() as executor:
    executor.map(process_blog, markdown_files)
