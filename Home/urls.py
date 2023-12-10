from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('new/newsdetails/<int:post_id>/', views.newsdetails.as_view(), name="newsdetails"),
    path('product/', views.product, name="product"),
    path('product/<int:card_id>/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('cart/<int:customer_id>/', views.cart, name="cart"),
    path('register/', views.register, name="register"),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name="logout"),
    path('create_order/<int:product_id>/', views.create_order, name='create_order'),
    path('delete_order/<int:product_id>/', views.delete_order, name="delete_order"),
    path('profile/', views.profile, name= 'profile'),
    path('edit_info', views.edit_info, name='edit'),
    path('map/', views.map, name="map"),
    path('introduction/', views.introduction, name="introduction"),
    path('policy/', views.policy, name='policy'),
    path('blog/', views.blog, name="blog"),
    path('tourdetails/<int:product_id>/', views.tourdetails, name = "tourdetails"),
    path('accommodation/', views.accommodation, name="accommodation"),
    path('feedback/', views.feedback, name='feedback'),
    # Định nghĩa các URL khác nếu cần thiết
]
