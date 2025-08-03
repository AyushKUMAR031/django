from django.http import HttpResponse, Http404
from .models import Student

# 1. Home View
def home(request):
    return HttpResponse("Welcome to College Portal!")

# 2. View student by ID (path param)
def student_detail(request, id):
    try: 
        student = Student.objects.get(pk=id)
        return HttpResponse(f"Student #{id}: {student.name}, from Batch: {student.batch}")
    except Student.DoesNotExist:
        raise Http404("Student not found")
    
# 3. Search students by query param
def search_student(request):
    name = request.GET.get('name') # default to 'Guest' if no name provided if we add , 'Guest'
    if name:
        students = Student.objects.filter(name__icontains=name)
        if students.exists():
            result = ", ".join([s.name for s in students])
            return HttpResponse(f"Search Results for student: {result}")
        return HttpResponse("No student found with that name.")
    return HttpResponse("Please provide a name query.")

# 4. Regex route view
def batch_year(request, year):
    students = Student.objects.filter(batch=year)
    if students.exists():
        return HttpResponse(f"Students from batch {year}: " + ", ".join(s.name for s in students))
    return HttpResponse(f"No students in batch {year}.")

# 5. Custom 404 error handler
def custom_404(request, exception):
    return HttpResponse("Oops! Page not found (custom 404)", status=404)
