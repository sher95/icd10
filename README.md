###Anorbank icd10 automation

1. Create vertual env

2. pip install -r requirements.txt

3. Install allure-comandline in: https://docs.qameta.io/allure/
    Save it and add in environment variable to the path
4. To  run and execute test run command below:
***pytest -v -s testCases\test_icd10.py***

5. To run seperate browsers:
pytest -v -s .\testCases\test_icd10.py --browser edge
pytest -v -s .\testCases\test_icd10.py --browser chrome

6. To run test and save it to reports directoy run command below:
   ***pytest -v -s --alluredir="path_to_project\reports" testCases\test_icd10.py***
   
7. After that open cmd and run this command:
***allure serve path_to_dir\reports***

If want to remove files from repository and not to push to repo then do this:
Add file in .gitignore

Then:
 git rm -r --cached path/to/folder