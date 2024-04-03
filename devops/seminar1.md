### Django
##### jiach613

#### Django summary
- Django: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. 

#### What language is used in project
- Django: Python(97.2%) and HTML/CSS/JavaScript

#### What version control tools are used
- Django: Git

####  What build tools are used
- Django: Django use *setuptools* to manage dependencies, establish project metadata, and build distributable packages. We can find the setup.py and pyproject.toml files defined in the project repo for the detail of project execution and dependencies.
  
#### What type of testing and CI mechanism are used
- Django: in .github/workflow/tests.yml it installs all the dependencies needed for the test and runs tests/runtest.py for the unit testing using python unit testing framework *unittest*. Django use both Jenkins and Github Actions for CI. The Jenkins continuous integration environment at ​https://djangoci.com builds pull requests using the [​GitHub Integration Plugin](https://plugins.jenkins.io/github-pullrequest/).
  
####  Who is the owner of the project
- Django: The owner of the project is the Django organization, which are comprised of some
core maintainers and contributes.

#### How many active contributors
- Django: In total there are over 2500 contributers to Neovim with around 35 being active with 67 Merged pull requests in 
the last months.

#### Are the contributors a homogenius group

- Django: No, everyone with the right knowledge can contribute and they’re not from the same company
#### What are the currently working on
- Django: the recent issues are related to 
        - clarify the document
        - fix bug in database layer(ORM)
        - fix bug in Template system
        - improve CSRF origin checking messaging
#### Any official communication channels
- Django: Developer use both Django forum and Discord to communicate in the community.They also held official conference *djangocon* in both EU and US each year.

#### Any unofficial communication channels
- Django: Reddit.

####  What is the recommended way of contributing to the project
- Django: In their documents for contributors, they suggest to start with unreviewed ticket and try to reproduce the bug and writing a patch that add a test for the bug's behavior. In order for the new comer to build familiarity with the codebase, they suggest to look for tickets that are accpeted and review patches related to them. There are very detailed and useful advice for the contributing process in their [document](https://docs.djangoproject.com/en/dev/internals/contributing/new-contributors/#guidelines)

####  Would you like to contribute to this project
- Django: Yes I would like to. I will write more personal projects and use more funtionality with Django before I start to contribute. As they suggest, start with ask/answering question in their forum can be a good way to start as well.