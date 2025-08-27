from django.shortcuts import render
from django.http import HttpResponse
import requests 
# what is requests here :
# It’s a popular third-party HTTP library in Python.
# Used to make outgoing HTTP requests (GET, POST, PUT, DELETE, etc.) from your Python code to other servers or APIs.


# what is response.json() here:
# this is a method of the response object returned by the requests library.
# It parses the JSON content of the response and returns it as a Python dictionary or list, depending on the structure of the JSON data.

# Questions


#Q7 - calculating 
def calculate(request,operation,value1,value2):
    if operation == 'add':
        result = value1 + value2
    elif operation == 'subtract':
        result = value1 - value2
    elif operation == 'multiply':
        result = value1 * value2
    elif operation == 'divide':
        if value2 == 0:
            return render(request, 'error.html', {'message': 'Division by zero is not allowed.'})
        result = value1 / value2
    return render(request, 'result.html', {'result': result})


#Q8 - getting api
def get_api_data(request,id):
    url = f'https://jsonplaceholder.typicode.com/posts/{id}' # f is for formatting strings
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render(request, 'api_data.html', {'data': data})
    else:
        return render(request, 'error.html', {'message': 'Failed to retrieve API data.'})


#Q9 - regex
def user_profile(request,uname):
    return HttpResponse(f"User Profile of: {uname}")

def item_id(request, item_id):
    return HttpResponse(f"Item ID: {item_id}")

def empname(request, name):
    return HttpResponse(f"Employee Name: {name}")

def gender(request, gender):
    return HttpResponse(f'Customer Gender: {gender}');


def password(request, password ):
    return HttpResponse(f'Password: {password}')


def trialbase(request):
    return render(request, 'trialbase.html')

def homepage(request):
    return render(request, 'homepage.html')

def aboutpage(request):
    return render(request, 'aboutpage.html')

def contactpage(request):
    return render(request, 'contactpage.html')

def productpage(request):
    return render(request, 'productpage.html')

