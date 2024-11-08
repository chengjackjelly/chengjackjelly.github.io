import time
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment and load templates from the current directory
env = Environment(loader=FileSystemLoader('.'))

# Load the template
template = env.get_template('template.html')

nav_links = [
    {"name": html_file.stem, "url": str(html_file), "last_update":time.ctime(html_file.stat().st_mtime)}
    for html_file in Path("./html").glob('*.html')
]
nav_links.sort(key=lambda link: link["last_update"], reverse=True)

# Render the template with the provided data
html_content = template.render(nav_links=nav_links)

# Save the rendered HTML to a file
with open('index.html', 'w') as f:
    f.write(html_content)

print("HTML file 'index.html' generated successfully.")
