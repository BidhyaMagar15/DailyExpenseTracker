from django.db import models
from users.models import UserProfile
from categories.models import Category



class Expense(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Unnamed Expense"
