from django.urls import path
from . import views
app_name = "store"
urlpatterns = [
    path('',views.store,name="home"),
    path('login/',views.LoginUser.as_view(),name="login"),
    path('register/',views.RegisterUser.as_view(),name="register"),
    path('cart/',views.cart,name="cart"),
    path('detail/<int:id>',views.detail,name="detail"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('logout/',views.logoutUser.as_view(), name='logout'),
    path('products/<int:id>', views.storeCategory, name = 'storeCategory')
]