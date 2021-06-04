To setup this web service in your local machines, the following steps needs to be performed :

1. Create a virtual environment for the application:

	if using an anaconda environment, use the command : 

	conda create -n MathServiceEnvironment python==3.7

	if using a normal python (3.7) environment, use the command : 

	python -m venv MathServiceEnvironment

2. Activate the virtual environment by using the following command :

	activate MathServiceEnvironment 

3. Create a new directory for keeping the web service related scripts.

4. Unzip the contents of the folder MathWebApi.zip to this directory

5. Install all the python packages required to run the solution. Use the following command :

	pip install -r requirements.txt

6. The environment is now ready for the solution to run. Deploy the application to the local host by running the following command :

	python mathApi.py

7. Open the script named testApi.py and test the math services you need to call.Use the following command to call different math services :

	python testApi.py

Few sample api calls and their responses are illustrated below :

call : get('http://localhost:5000/').json()
response : {'Available Math web services': {'Fibonacci': 'returns the nth number in the Fibonacci series, where n is the input from the user', 'Ackermann': 'returns the Ackermann function(m,n) with values of m and n provided by the user', 'Factorial': 'returns the factorial of a non negative number n , provided by the user'}}

call : put('http://127.0.0.1:5000/fibonacci/',data={'count':"10"}).json()
response : {'Fibonacci number F(n)': 34, 'Turnaround time for the api call': '0.0050 seconds'}

call : put('http://127.0.0.1:5000/ackermann/',data={'m':"2",'n':"10"}).json()
response : {'Ackermann function A(m,n)': 23, 'Turnaround time for the api call': '0.0020 seconds'}

call : put('http://127.0.0.1:5000/factorial/',data={'n':"6"}).json()
response : {'Factorial n! ': 720, 'Turnaround time for the api call': '0.0009999275 seconds'}