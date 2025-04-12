from django import forms
from .models import CategoryBudget, Expense

class CategoryBudgetForm(forms.ModelForm):
    class Meta:
        model = CategoryBudget
        fields = ['name', 'budget']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category name'}),
            'budget': forms.NumberInput(attrs={'placeholder': '$'})
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['day', 'category', 'amount']