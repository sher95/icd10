###Anorbank icd10 automation
On windows should be installed Python 3.9

Clone repository to your IDE

1. Create vertual environment and activate it

2. pip install -r requirements.txt

3. To run seperate browsers:
pytest -v -s .\main.py  --browser edge
pytest -v -s .\main.py  --browser chrome

4. Install allure-comandline in: https://docs.qameta.io/allure/
    Save it and add in environment variable to the path

5. To run test and save it to reports directoy run command below:
   ***pytest -v -s --alluredir="path_to_project\reports" .\main.py.py***
   
6. After that open cmd and run this command:
***allure serve path_to_dir\reports***

If want to remove files from repository and not to push to repo then do this:
Add file in .gitignore

Then:
 git rm -r --cached path/to/folder