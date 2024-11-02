from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
   path('', views.home, name='home'),
   path('category/<str:product_type_id>/', views.product_type_products, name='category_products'),
   path('state/',views.state,name='state'),
   path('state_products/<int:state_id>/', views.subcategories_by_state, name='state_products'),
   path('subcategory/<int:subcategory_id>/', views.products_by_subcategory, name='products_by_subcategory'),
   path('details/<int:product_id>/', views.details, name='details'), 
   path('details/<int:product_id>/', views.details, name='details'), 
   path('userreg/', views.userreg, name='userreg'), 
   path('sellercredentials/', views.cred, name='cred'),
   path('slogin/', views.slogin, name='slogin'),
   path('sellerlogin/', views.slogin2, name='slogin2'),
   path('login/', views.loginview, name='login'),
   path('sellerdetails/', views.sellerdetails, name='sellerdetails'),
   path('logout/', views.logoutview, name='logout'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('products/', views.products, name='products'),
   path('iteminc-<int:pid>/', views.iteminc, name='iteminc'),
   path('itemdec-<int:pid>/', views.itemdec, name='itemdec'),
   path('iteminc1-<int:pid>/', views.iteminc1, name='iteminc1'),
   path('itemdec1-<int:pid>/', views.itemdec1, name='itemdec1'),
   path('addcart-<int:pid>/', views.addcart, name='addcart'),
   path('cartdetails/', views.cartdetails, name='cartdetails'),
   path('address/', views.addresss, name='address'),
   path('deletecart-<int:pid>/', views.deletecart, name='delcart'),
   path('deletecart1-<int:pid>/', views.deletecart1, name='delcart1'),
   path('addproducts/', views.addproducts, name='addproducts'),
   path('payment/', views.payment, name='payment'),
   path('aboutus/', views.aboutus, name='aboutus'),
   path('blog/', views.blog, name='blog'),
   path('sorders/', views.sorders, name='sorders'),
   path('contact/', views.contact, name='contact'),
   path('stocks-<int:eid>/', views.stocks, name='stocks'),



] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
