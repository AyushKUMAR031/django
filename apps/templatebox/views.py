from django.shortcuts import render

def demo_view(request):
    student = "Ayush"
    marks = 92
    items = ['Django', 'Templates', 'Python']
    is_topper = True
    context = {
        'student': student,
        'marks': marks,
        'items': items,
        'is_topper': is_topper,
    }
    return render(request, 'demo.html', context)
