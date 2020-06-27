from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.
class Order(models.Model):
    STATUS_TYPES = (
        ('new', 'New'),
        ('complete', 'Complete'),
        ('in processing', 'In processing'),
        ('accepted', 'Accepted'),
    )
    SERVICE_TYPES = (
        ('Restoration & Renovation','Restoration & Renovation'),
        ('Tenant Turns','Tenant Turns'),
        ('Property Maintenance','Property Maintenance'),
        ('none', 'none'),

    )
    service = models.CharField(max_length=30,
                              choices=SERVICE_TYPES,
                              default='none')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    mob_number = models.CharField(max_length=250)
    message = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=30,
                              choices=STATUS_TYPES,
                              default='new')
    # def get_absolute_url(self):
    #     return reverse('product_url', kwargs={
    #         'slug_product': self.slugproduct, 'category':self.subcategory.category,
    #         'slug_subcategory': self.subcategory.slug_subcategory})

    # def __str__(self):
    #     return self.title
