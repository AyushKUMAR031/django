from django.shortcuts import render
from django.http import HttpResponse
import requests 
# # what is requests here :
# # It’s a popular third-party HTTP library in Python.
# # Used to make outgoing HTTP requests (GET, POST, PUT, DELETE, etc.) from your Python code to other servers or APIs.


# # what is response.json() here:
# # this is a method of the response object returned by the requests library.
# # It parses the JSON content of the response and returns it as a Python dictionary or list, depending on the structure of the JSON data.

# # Questions

# #Q7 - calculating 
# def calculate(request,operation,value1,value2):
#     if operation == 'add':
#         result = value1 + value2
#     elif operation == 'subtract':
#         result = value1 - value2
#     elif operation == 'multiply':
#         result = value1 * value2
#     elif operation == 'divide':
#         if value2 == 0:
#             return render(request, 'error.html', {'message': 'Division by zero is not allowed.'})
#         result = value1 / value2
#     return render(request, 'result.html', {'result': result})


# #Q8 - getting api
# def get_api_data(request,id):
#     url = f'https://jsonplaceholder.typicode.com/posts/{id}' # f is for formatting strings
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return render(request, 'api_data.html', {'data': data})
#     else:
#         return render(request, 'error.html', {'message': 'Failed to retrieve API data.'})


# #Q9 - regex
# def user_profile(request,uname):
#     return HttpResponse(f"User Profile of: {uname}")

# def item_id(request, item_id):
#     return HttpResponse(f"Item ID: {item_id}")

# def empname(request, name):
#     return HttpResponse(f"Employee Name: {name}")

# def gender(request, gender):
#     return HttpResponse(f'Customer Gender: {gender}');

# def password(request, password ):
#     return HttpResponse(f'Password: {password}')


# practice signup 1
from .models import User
def signup(request) :
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # --- Simple Validation Rules ---
        if not username or len(username) < 3:
            errors.append("Username must be at least 3 characters long.")

        if not name:
            errors.append("Name is required.")

        if not email or "@" not in email:
            errors.append("Enter a valid email address.")

        if not password or len(password) < 8:
            errors.append("Password must be at least 8 characters long.")

        # --- If no errors, save user ---
        if not errors:
            user = User.objects.create(
                username=username,
                name=name,
                email=email,
                password=password
            )
            user.save()
            return HttpResponse("User created successfully!")

        return render(request, 'signup.html', {'errors': errors, 'username': username, 'name': name, 'email': email, 'password': password})
    else:
        return render(request, 'signup.html')
    

# signup 2
from .forms import SignupForm
def signup2(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created successfully with forms.py!")
        else:
            return render(request, 'signup2.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'signup2.html', {'form': form})