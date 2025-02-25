from django.db import models
from django.contrib.auth.models import User

class contactForm(models.Model):
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    content = models.TextField()

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=50, blank= False, null= False)
    image = models.ImageField(upload_to='category', blank= True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['-created',]
        verbose_name_plural ='Categories'
    
    
class Product(models.Model):
    name = models.CharField(max_length=50, blank= False, null= False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_des = models.CharField(max_length=255, verbose_name ='Short Descriptions')
    description = models.TextField(max_length=1000, verbose_name ='Descriptions')
    image = models.ImageField(upload_to='products', blank= False, null=False)
    price = models.FloatField()
    old_price = models.FloatField(default=0.00, blank= True, null = True )
    is_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['-created']

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	fullname = models.CharField(max_length=255, null=True, blank=True)  
	phone = models.CharField(max_length=15, null=True, blank=True) 
	address = models.TextField(null=True, blank=True)  
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.user.username if self.user else "Khách hàng không xác định"


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	@property
	def get_cart_total(self):
		self.orderitem_set.filter(product__isnull=True).delete()  
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems if item.product])  # Chỉ tính nếu product != None
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	@property
	def get_total(self):
		if self.product:  
			return self.product.price * self.quantity
		return 0
	class Meta:
		unique_together = ('order', 'product')

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

