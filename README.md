Setting up a new Repository
===============================
This is a template reporitory for setting up a new github repository.

1. Clone this repository into your desired directory

    ```git clone https://github.com/edmundsj/template.git```

2. Change the git hooks location:

    ```git config core.hooksPath .hooks```

3. Create a new repository on github
4. Change this repository's name with 

   ```git remote set-url origin <NEW_REPO_URL>```

5. Push to the new repository 

    ``git push -u origin main```

6. Confirm the build works on the remote server - the action should pass
7. Set github pages to use the ``docs/`` folder for github pages at the bottom
   of the "Settings" page
8. Make your first HTML build from the ``docs/`` directory:

    ```make html```

9. Commit the generated documentation and push to github.

Done! Your repository should be viewable on github pages: 
https://edmundsj.github.io/REPO_NAME/

Getting Started
-------------------


Writing the Documentation
------------------------------

Writing Tests and Adding them to the Test Runner
---------------------------------------------------


Contributing
----------------
