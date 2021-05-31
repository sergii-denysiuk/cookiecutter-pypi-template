# cookiecutter-python-package-template

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), this is a template for python package.


## Usage

Let's pretend you want to create a python package called "the_great_package".

First, get Cookiecutter:
```bash
pip install cookiecutter
```

Now run it against this repo:
```bash
cookiecutter git@github.com:sergii-denysiuk/cookiecutter-python-package-template.git
```
or 
```bash
cookiecutter https://github.com/sergii-denysiuk/cookiecutter-python-package-template.git
```
or, if you cloned the repo to your local machine
```bash
cookiecutter cookiecutter-python-package-template
```

You'll be prompted for some values. Provide them, then a Python package template will be created for you.


## How to update project

Change branch to cookiecutter
```bash
git checkout cookiecutter
```
    
Go to outside on your project
```bash
cd ..
```
    
Generate project in cookiecutter branch
```bash
cookiecutter --overwrite-if-exists --config-file=the_great_package/.cookiecutterrc cookiecutter git@github.com:sergii-denysiuk/cookiecutter-python-package-template.git
```
or
```bash
cookiecutter --overwrite-if-exists --config-file=the_great_package/.cookiecutterrc cookiecutter https://github.com/sergii-denysiuk/cookiecutter-python-package-template.git
```
or, if you cloned the repo to your local machine
```bash
cookiecutter --overwrite-if-exists --config-file=the_great_package/.cookiecutterrc cookiecutter cookiecutter-python-package-template
```
    
Now you must add changes and new file, eg. `git add FILE_NAME`
```bash
git add -u
```

Check changes and commit
```bash
git status
git commit -m "update project template"
```

Then change branch to master
```bash
git checkout master
```
    
And merge from cookiecutter branch with updated of new template
```bash
git merge cookiecutter
```

The last but not least is you must solving all conflict by hand and update remote repository.
```bash
git push -u origin cookiecutter
git push -u origin master
```
