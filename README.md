# Scifi_Library_Viewer
website/s for da scifi library viewer. 

Planned Features for the website
- [] Public side viewer 
- [] Admin side viewer  

Public:
- [] Allows you to browse the full collection
- [] Tells you if an item is loaned out or not 

Admin:
- [] Manually set if an item is loaned out or returned 
- [] Way to track current loaned items as well as past loans 
  - [] Used to be an excel sheet that ONLY tracks current loans, much better system pleaaase
  - [] Current plan is to track 
    - [] Name & Email of loanee 
    - [] Day item was loaned   
- [] Show info such as shelf code to the admins 
- [] Method to add & remove entries to the library 

## Python HTML Explanation
Haiiii im setting up the webpage setup with Python's flask framework.

In order to run this, you're going to want to create a venv in the folder containing the library viewer
you then acticate the venv with venvLocation/Scripts/Activate (might be diff on another OS)

when you've created and activated your venv, you should run  pip install -r Scifi_Library_Viewer\requirements.txt, this will download all the libraries the application needs to run.

If you run Python Scifi_Library_Viewer\app.py you'll see it hosts a blank html page locally
