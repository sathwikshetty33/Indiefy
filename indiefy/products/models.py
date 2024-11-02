from django.db import models
from django.contrib.auth.models import User

# Category based on Product Type (like Clothing, Jewelry, etc.)
class ProductType(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True, blank=False)
    description = models.TextField(default='description')


    def __str__(self):
        return self.name
class seller(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    mobileno = models.CharField(max_length=12)
    adharno = models.CharField(max_length=16)
    panno = models.CharField(max_length=20)
    products = models.ManyToManyField( 'Product', related_name="po")

    def __str__(self):
        return self.user.username

class StateCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True, blank=False)
    description = models.TextField(default='1')
    def __str__(self):
        return self.name
class substate(models.Model):
    state_category = models.ForeignKey(StateCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=255,default='not specified')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)  # Type-based categorization
    sub_type = models.ForeignKey(substate, on_delete=models.CASCADE,default=1)   # State-based categorization
    image = models.ImageField(upload_to='product_images/',default='aunty1.jpg', null=True, blank=True)  # Add image field
    seller = models.ForeignKey(seller, on_delete=models.CASCADE,default=1)
    stock = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user}-{self.created_at}"
class cartitem(models.Model):
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.cart}-{self.quantity}"
class address(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return f"{self.user}"
class order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(seller, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    total=models.IntegerField(default=100)
    address=models.ForeignKey(address,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f"{self.buyer}-{self.product}"
class feeback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=20,default=1)
    lname=models.CharField(max_length=20,default=1)
    email=models.EmailField
    phone=models.CharField(max_length=12,default=1)
    meesage=models.TextField(max_length=200,default="hello")
    def __str__(self):
        return f"{self.user}"