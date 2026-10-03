from django.shortcuts import render

from .models import Student


def home(request):
    """Retrieve all student records and send them to the home template."""
    students = Student.objects.all()
    context = {
        "students": students,
        "student_count": students.count(),
    }
    return render(request, "main/home.html", context)
