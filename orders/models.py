from django.db import models
from authentication.models import User
from django.utils.translation import gettext_lazy as _
from products.models import Product
from model_utils import Choices

PAYMENT_MODES = Choices(
    (1, "cod", _("code")),
    (2, "card", _("card")),
    (3, "upi", _("upi")), 
    (4, "netbanking", _("netbanking"))        
)

PAYMENT_STATUS = Choices(
    (1, "pending", _("pending")),
    (2, "completed", _("completed"))    
)

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_amount = models.IntegerField(default=0)
    payment_mode = models.IntegerField(choices=PAYMENT_MODES, default=PAYMENT_MODES.cod)
    payment_status = models.IntegerField(choices=PAYMENT_STATUS, default=PAYMENT_STATUS.pending)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # price and quantity at the time of order
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
