from django.http import HttpResponse
from django.shortcuts import render

# Simple implementation returning HTML directly
# def home(request):
#     return HttpResponse("""
#         <html>
#             <head>
#                 <title>Hello World</title>
#                 <style>
#                     body {
#                         display: flex;
#                         justify-content: center;
#                         align-items: center;
#                         height: 100vh;
#                         margin: 0;
#                     }
#                     h1 {
#                         font-size: 2rem;
#                         color: #333;
#                     }
#                 </style>
#             </head>
#             <body>
#                 <h1>Hello from Hello World App!</h1>
#             </body>
#         </html>
#     """)

# Alternative implementation using a template
def home(request):
    return render(request, 'land.html')


# Custom 404 error page
def custom_404(request, exception):
    return render(request, '404.html', status=404)

# Custom 500 error page
def custom_500(request):
    return render(request, '500.html', status=500)