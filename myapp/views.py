from django.shortcuts import render, redirect
from .models import WeeklyAllowance, DailyExpense, Category
from .forms import AllowanceForm, ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required
def set_allowance(request):
    if request.method == 'POST':
        form = AllowanceForm(request.POST)
        if form.is_valid():
            allowance = form.save(commit=False)
            allowance.user = request.user
            allowance.save()
            return redirect('add_expenses')
    else:
        form = AllowanceForm()
    return render(request, 'set_allowance.html', {'form': form})

@login_required
def add_expenses(request):
    allowance = WeeklyAllowance.objects.filter(user=request.user).latest('id')
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.allowance = allowance
            expense.save()
            return redirect('view_spending')
    else:
        form = ExpenseForm()
    return render(request, 'add_expenses.html', {'form': form, 'allowance': allowance})

@login_required
def view_spending(request):
    # Get the most recent allowance (no longer filtering by week_start_date)
    allowance = WeeklyAllowance.objects.filter(user=request.user).latest('id')
    expenses = DailyExpense.objects.filter(allowance=allowance)
    total_spent = sum(expense.amount for expense in expenses)
    savings = allowance.amount - total_spent
    
    context = {
        'allowance': allowance,
        'expenses': expenses,
        'total_spent': total_spent,
        'savings': savings,
    }
    return render(request, 'view_spending.html', context)

def home(request):
    return render(request, 'home.html')