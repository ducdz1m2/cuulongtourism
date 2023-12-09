from django.shortcuts import render, redirect
from . import models
from django.views import View
from django.contrib.auth import authenticate,  logout
from .forms import CustomerForm, LoginForm, CustomUserChangeForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

def home(request):
    

    products = models.Product.objects.all()
    blogs = models.Blog.objects.all()
    
    return render(request, 'home.html', {
        'blogs': blogs,
        'products': products,

    })


def new(request):
    posts = models.Post.objects.all()[:2]
    postall = models.Post.objects.all()[2:8]
    foods = models.Food.objects.all()
    return render(request, 'new.html', {'posts': posts, 'postall': postall, 'foods': foods})
def product(request):
    products = models.Product.objects.all()
    products_sale = models.Product.objects.filter(giachuasale__gt=0)
    return render(request, 'product.html', {'products': products, 'products_sale': products_sale})

@login_required
def cart(request):
   
    customer = request.user.customer.id
    orders = models.Order.objects.filter(customer=customer)

   

    if request.method == 'POST':
        orders.complete = True
        for order in orders:
            order.complete = True
            order.save()
            
    context = {
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'cart.html', context)




class newsdetails(View):
    def get(self, request, post_id):
        post = models.Post.objects.get(id = post_id)
        posts = models.Post.objects.all()[9:17]
        products = models.Product.objects.all()
        return render(request, 'newsdetails.html', {'post': post, 'products': products, 'posts': posts})
###
def register(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()  # Lưu thông tin User
            customer = models.Customer.objects.create(user=user)  # Tạo Customer và liên kết với User
            return redirect('login')
    context = {
        'form': form
    }

    return render(request, 'register.html', context)
def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username ,password=password)

            if user is not None:
                print(user)
                auth.login(request, user)

                return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def my_logout(request):
    logout(request)
    return redirect('home')


def create_order(request, product_id):
    if request.user.is_authenticated:
        order, created = models.Order.objects.get_or_create(customer=request.user.customer, complete=False)

        product = models.Product.objects.get(id = product_id)
        cart_item, created = models.OrderItem.objects.get_or_create(product=product, order=order)

        cart_item.quantity+=1
        cart_item.save()
        return redirect('cart')
@login_required
def delete_order(request, product_id):
    if request.user.is_authenticated:
        order, created = models.Order.objects.get_or_create(customer=request.user.customer, complete=False)
        product = models.Product.objects.get(id=product_id)

        # Sử dụng filter() để lấy QuerySet của OrderItem và sau đó gọi delete() trên nó
        models.OrderItem.objects.filter(product=product, order=order).delete()
        
        return redirect('cart')
    
@login_required
def profile(request):

    customer = request.user


    return render(request, 'profile.html', { 'customer':customer})

@login_required
def edit_info(request, ):
    customer = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Thay 'profile' bằng tên đường dẫn đến trang profile của bạn
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'edit.html', { 'customer':customer, 'form': form})


def map(request):
    return render(request, 'map.html')