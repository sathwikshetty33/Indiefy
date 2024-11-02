from django.contrib import admin
from .models import Product, ProductType, StateCategory, substate, seller, cartitem, cart, order, address, feeback

# Register the models to make them available in the admin interface
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(StateCategory)
admin.site.register(substate)
admin.site.register(seller)
admin.site.register(cart)
admin.site.register(cartitem)
admin.site.register(order)
admin.site.register(feeback)
admin.site.register(address)
