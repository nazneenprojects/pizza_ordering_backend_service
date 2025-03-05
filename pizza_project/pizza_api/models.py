# from django.db import models
#
# class Pizza(models.Model):
#     name = models.CharField(max_length=100)
#     size = models.CharField(max_length=50, default='Medium')
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     toppings = models.JSONField()
#
#     def __str__(self):
#         return self.name
#
# class Order(models.Model):
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()