### Introduction
- a simple blog which we write markdown and the html will be served
- host blog in github.io
### Preinstallation
- linux
- pandoc
- python 
    - Jinja2

### Usage
write markdown
run ./run.sh
### TODO


- use github actions to further automate everything(because currently the post-commit hook is not visible for version control)
- move the scripts to a separate repo and make it a python package or something easy to install. only keep the blog content here
- add test to check typo
- ~~only regenerate the html when the corresponding markdown is changed since last generation~~
- ~~generating git commit message automatically from modified content(update/add/deleted...~~
- ~~add timestamp/author to each blog and update them during git commit~~
- ~~add recent update time to the index page and sorted the article by them~~