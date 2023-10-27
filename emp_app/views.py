from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Memo
from emp_app.forms import MemoForm
from .models import Mail

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def all_emp(request):

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

@login_required
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id= dept, role_id=role, hire_date= datetime.now())
        new_emp.save()
        return render(request, 'add_emp.html', {'employee_added': True})
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An exception Occurred! Employee Has Not Been Added")

@login_required
def remove_emp(request, emp_id=0):
    employee_removed = False
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            employee_removed = True
        except Employee.DoesNotExist:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps,
        'employee_removed': employee_removed,
    }
    return render(request, 'remove_emp.html', context)
@login_required
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')

def memo_list(request):
    memos = Memo.objects.all()
    return render(request, 'memo/memo_list.html', {'memos': memos})


def memo_create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    else:
        form = MemoForm()
    return render(request, 'memo/memo_form.html', {'form': form})


def memo_update(request, pk):
    memo = Memo.objects.get(pk=pk)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memo/memo_form.html', {'form': form})


def memo_delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memo_list')


def Mails(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        content = request.POST['content']

        # Create a new Mail object and save it to the database
        mail = Mail(recipient=recipient, subject=subject, content=content)
        mail.save()

        return render(request, 'create_mail.html', {'mail_added': True})
    elif request.method == 'GET':
        return render(request, 'create_mail.html')
    else:
        return HttpResponse("An exception occurred! Mail was not created")


def index_mail(request):
    return render(request, 'index_mail.html')

def sent_mail(request):
    mails = Mail.objects.all()  # Query the database for all sent mails

    return render(request, 'sent_mail.html', {'mails': mails})