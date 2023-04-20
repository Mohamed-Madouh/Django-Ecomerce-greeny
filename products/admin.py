from django.contrib import admin
from .models import product , Category, Brand, Productimages,ProdactReviews
# Register your models here.

class ProdactImagesInLine(admin.TabularInline):
    model = Productimages
    
    
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','flag']
    inlines = [ProdactImagesInLine]

admin.site.register(product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Productimages)
admin.site.register(ProdactReviews)
admin.site.register(Category)
