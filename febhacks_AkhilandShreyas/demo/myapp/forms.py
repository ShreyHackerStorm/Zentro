from django import forms
from .models import Category, WeeklyAllowance, DailyExpense

class AllowanceForm(forms.ModelForm):
    class Meta:
        model = WeeklyAllowance
        fields = ['amount', 'week_start_date']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = DailyExpense
        fields = ['day', 'category', 'amount', 'date']