from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class WeeklyAllowance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    week_start_date = models.DateField()
    
    def __str__(self):
        return f"{self.user.username}'s allowance for {self.week_start_date}"

class DailyExpense(models.Model):
    allowance = models.ForeignKey(WeeklyAllowance, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)  # e.g., "Monday"
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.day} - {self.category}: ${self.amount}"