from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from django.shortcuts import redirect
from .models import Employee
# Create your views here.

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
        
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})


# list view
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})

# update view
def update_employee(request, pk):
    employee = Employee.objects.get(employee_id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form})
      
# delete view
def delete_employee(request, pk):
    employee = Employee.objects.get(employee_id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('list')
   