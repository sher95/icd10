###Anorbank icd10 automation
On windows should be installed Python 3.9

1. Clone repository to your IDE

2. Create vertual environment and activate it

3. pip install -r requirements.txt

4. To run seperate browsers:
pytest -v -s .\main.py  --browser edge
pytest -v -s .\main.py  --browser chrome

5. Install allure-comandline in: https://docs.qameta.io/allure/
    Save it in some directory and add the path in environment variable

6. To run test and save it to reports directoy run command below:
   ***pytest -v -s --alluredir="path_to_project\reports" .\main.py.py***
   
7. After that open cmd and run this command:
***allure serve path_to_dir\reports***
