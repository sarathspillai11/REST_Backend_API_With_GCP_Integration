from flask import Flask
from flask_restful import Resource, Api,reqparse
import time
from functools import reduce

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
api = Api(app)

mathFunctions ={'Available Math web services': {'Fibonacci':'returns the nth number in the Fibonacci series, where n is the input from the user',
                'Ackermann':'returns the Ackermann function(m,n) with values of m and n provided by the user',
                'Factorial':'returns the factorial of a non negative number n , provided by the user'}}

parser = reqparse.RequestParser()


class mathFunctionsHome(Resource):
    def get(self):
        return mathFunctions

class fibonacciFunction(Resource):

    def generateFibonacciSeries(self,n):
        """
        :param n: the number of elements in the fibonacci series
        :return: a list of numbers in the fibonacci series
        """
        seq = [0,1]
        for i in range(2,n):
            seq.append(reduce(lambda a,b:a+b,seq[-2:]))
        return seq

    def get(self):
        return {mathFunctions['Fibonacci']}

    def put(self):
        # finding the time when an api call was made. Used to determine the complete turnaround time of the web service
        start_time = time.time()
        validationMsg = r"This is the count of elements in the series. Try a valid positive number"
        # adding the count argument with a validation for the Integer data type and validation error message
        parser.add_argument('count', type=int, help=validationMsg+r' :  {error_msg}')
        args = parser.parse_args()
        count = args['count']
        # additional validation to check for negative integers and return a validation error message in return
        if(count<1):
            return {'message': {'count': validationMsg}}
        return {'Fibonacci number F(n)': (self.generateFibonacciSeries(count)[-1]),
                'Turnaround time for the api call': "%.4f" %(time.time()-start_time)+" seconds"}

class ackermannFunction(Resource):

    def generateAckermannSeries(self,m,n):
        """
        :param m: any non negative integer
        :param n: any non negative integer
        :return: the output of ackermann function calculated for m and n
        """
        if(m==0):
            return n+1
        elif(n==0):
            return self.generateAckermannSeries(m-1,1)
        else:
            return self.generateAckermannSeries(m-1,self.generateAckermannSeries(m,n-1))

    def get(self):
        return {mathFunctions['Ackermann']}

    def put(self):
        # finding the time when an api call was made. Used to determine the complete turnaround time of the web service
        start_time = time.time()
        validationMsg = r"This should be a valid integer with a value greater than or equal to 0 !!"
        # adding the arguments m and n with a validation for the Integer data type and validation error messages
        parser.add_argument('m', type=int, help=validationMsg+r' :  {error_msg}')
        parser.add_argument('n', type=int, help=validationMsg + r' :  {error_msg}')
        args = parser.parse_args()
        m = args['m']
        n = args['n']
        # additional validation to check for negative integers
        validationCheck = any([i<0 for i in [m,n]])
        # return a validation error message when a negative number is found
        if(validationCheck):
            return {'message':'Please enter a valid value for m and n i.e greater or than equal to 0'}
        print("passed all validations in put")
        return {'Ackermann function A(m,n)': self.generateAckermannSeries(m,n),
                'Turnaround time for the api call': "%.4f" %(time.time()-start_time)+" seconds"}

class factorialFunction(Resource):

    def generateFactorial(self,n):
        """
        :param n: any non negative integer
        :return: the factorial of the number n given by n!
        """
        if(n==0):
            factorial = 1
        else:
            factorial = reduce(lambda x,y : x*y,[i for i in range(1,n+1)])
        return factorial

    def get(self):
        return {mathFunctions['Factorial']}

    def put(self):
        # finding the time when an api call was made. Used to determine the complete turnaround time of the web service
        start_time = time.time()
        validationMsg = r"This should be a valid integer with a value greater than or equal to 0 !!"
        parser.add_argument('n', type=int, help=validationMsg + r' :  {error_msg}')
        args = parser.parse_args()
        n = args['n']
        # additional validation to check for negative integers and return a validation error message in return
        if(n<0):
            return {'message':'Please enter a valid value for m and n i.e greater or than equal to 0'}
        return {'Factorial n! ': self.generateFactorial(n),
                'Turnaround time for the api call': "%.10f" %(time.time()-start_time)+" seconds"}


api.add_resource(mathFunctionsHome, '/')
api.add_resource(fibonacciFunction, '/fibonacci/')
api.add_resource(ackermannFunction, '/ackermann/')
api.add_resource(factorialFunction, '/factorial/')

if __name__ == '__main__':
    app.run(debug=True)