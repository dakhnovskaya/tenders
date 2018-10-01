from django.contrib import admin
from .models import Customer, Category, Stage, TypePurchase, Tender

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Stage)
admin.site.register(TypePurchase)
admin.site.register(Tender)
