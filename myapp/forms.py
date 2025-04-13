from django import forms
from .models import Category, WeeklyAllowance, DailyExpense

class AllowanceForm(forms.ModelForm):
    class Meta:
        model = WeeklyAllowance
        fields = ['amount']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = DailyExpense
        fields = ['day', 'category', 'amount']