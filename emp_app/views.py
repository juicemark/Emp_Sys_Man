from django.shortcuts import render, HttpResponse

from .models import Employee, Role,Department
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        salary = int(request.POST['First_name'])
        bonus = int(request.POST['First_name'])
        Phone = int(request.POST['First_name'])
        dept = int(request.POST['First_name'])
        role = int(request.POST['First_name'])
        new_emp = Employee(First_name=First_name, Last_name=Last_name, salary=salary, bonus=bonus, Phone=Phone, dept_id= dept, role_id=role, hire_date= datetime.now())
        new_emp.save()
        return  HttpResponse('Employee added Successfully')

    elif request.method=='GET':

       return render(request, 'add_emp.html')
    else:
       return HttpResponse("An exception Occured! Employee Has Not Been Added")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Sucessfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context )

def filter_emp(request):

    return render(request, 'filter_emp.html')