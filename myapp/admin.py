from django.contrib import admin
from .models import Category, WeeklyAllowance, DailyExpense

admin.site.register(Category)
admin.site.register(WeeklyAllowance)
admin.site.register(DailyExpense)