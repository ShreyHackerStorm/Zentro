from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CategoryBudget, Expense
from .forms import CategoryBudgetForm, ExpenseForm

@login_required
def set_budgets(request):
    if request.method == 'POST':
        form = CategoryBudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('set_budgets')
    
    budgets = CategoryBudget.objects.filter(user=request.user)
    form = CategoryBudgetForm()
    return render(request, 'set_budgets.html', {
        'form': form,
        'budgets': budgets
    })

@login_required
def add_expenses(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, user=request.user)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('add_expenses')
    
    expenses = Expense.objects.filter(user=request.user)
    form = ExpenseForm(user=request.user)
    return render(request, 'add_expenses.html', {
        'form': form,
        'expenses': expenses
    })

@login_required
def view_spending(request):
    categories = CategoryBudget.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    
    spending_data = []
    total_saved = 0
    
    for category in categories:
        cat_expenses = expenses.filter(category=category)
        total_spent = sum(e.amount for e in cat_expenses)
        difference = category.budget - total_spent
        total_saved += difference
        
        spending_data.append({
            'category': category.name,
            'budget': category.budget,
            'spent': total_spent,
            'difference': difference,
            'overspent': difference < 0
        })
    
    return render(request, 'view_spending.html', {
        'spending_data': spending_data,
        'total_saved': total_saved
    })