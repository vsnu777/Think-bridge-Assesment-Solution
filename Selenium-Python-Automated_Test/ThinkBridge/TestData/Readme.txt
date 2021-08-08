1. Install or make sure Chrome version Version 92.0.4515.131 is installed on your system

2. Locate and open 'Thinkbridge' project in Pycharm.

3).Make sure python is installed in your system.

4).Python is configured in the system
	Set environment variable %PYTHONPATH%
		pythonPath;pythonPath\DLLs;pythonPath\Lib;pythonPath\Scripts;pythonPath\Tools;pythonPath\libs;

4).Use below command from command prompt to install selenium(if already not installed)
 	pip install selenium 

5).Open Project in Pycharm

6).Setting webdriver executable path"
 i)Copy Chrome driver location from chrome driver folder
 ii)open conftest.py and update current chrome webdriver location in executable path.

7). Open command prompt navigate to project directory. 
	e.g cd C:\Users\Vishnu\PycharmProjects\ThinkBridge

8). Enter below command to run test_dropdown.py
   	pytest -s -v Tests\test_dropdown.py --browser chrome

9). Enter below command to run test_dropdown.py
   	pytest -s -v Tests\test_signup.py --browser chrome

