Setting up a new Repository
===============================
[![Build](https://github.com/edmundsj/template/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/edmundsj/template/actions/workflows/python-package-conda.yml)

This is a template reporitory for setting up a new github repository for
sphinx-based documentation integrated with github pages, also integrated with
github actions for running unit tests, and (in the future) deploying to pyPi.

Getting Started
------------------
1. Clone this repository into your desired directory

    ```git clone https://github.com/edmundsj/template.git <DESIRED_DIRECTORY>```

2. Change the git hooks location:

    ```git config core.hooksPath .hooks```

3. Create a new repository on github
4. Change this repository's name with 

   ```git remote set-url origin <NEW_REPO_URL>```

5. Push to the new repository 

    ```git push -u origin main```

6. Confirm the build works on the remote server - the action should pass
7. Set github pages to use the ``docs/`` folder for github pages at the bottom
   of the "Settings" page
8. After your actions pass, create a status badge from the "Actions" section on
   github and paste it up top.

Done! Your repository should be viewable on github pages: 
https://edmundsj.github.io/REPO_NAME/, unit tests and a new docs build will run
on every commit, 

Adding Additional Unit Tests
-------------------------------
- Any time you want to add additional unit tests (and you should write these
BEFORE you have fully working code) make sure to add them to the fullRunner.py
test runner to ensure they are run on commit and on the remote server.


Writing the Documentation
------------------------------
- The documentation source is located in 

Building the Documentation
----------------------------
Simply run ``make html`` from the ``docs/`` directory. This will compile the
files in the ``source/`` directory, and place them in the main ``docs/``
directory where github pages can find them.

Writing Tests and Adding them to the Test Runner
---------------------------------------------------
The tests are run from github hooks prior to each commit and on the remote
server with the file located in ``test/fullRunner.py``. This is meant to be a
comprehensive set of unit tests, and any additional test files should be added
to that file.


Contributing
----------------
