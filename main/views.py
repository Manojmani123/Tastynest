from django.shortcuts import render, redirect
from .models import CustomUser, Item  # Make sure you have an Item model
from django.contrib import messages
import json
from .models import Order
from django.utils.dateparse import parse_date

# Example menu items (in real app, use models)
CURRIES = [
    {'id': 1, 'name': 'Paneer Butter Masala', 'price': 180, 'img': 'paneer.jpg'},
    {'id': 2, 'name': 'Chicken Curry', 'price': 220, 'img': 'chickencurry.jpg'},
    {'id': 3, 'name': 'Dal Tadka', 'price': 140, 'img': 'daltadka.jpg'},
]
BURGERS = [
    {'id': 101, 'name': 'Cheese Burger', 'price': 120, 'img': 'cheeseburger.jpg'},
    {'id': 102, 'name': 'Veggie Burger', 'price': 100, 'img': 'veggieburger.jpg'},
    {'id': 103, 'name': 'Chicken Burger', 'price': 140, 'img': 'chickenburger.jpg'},
]
BIRYANIS = [
    {'id': 11, 'name': 'Hyderabadi Biryani', 'price': 200, 'img': 'hyderabadi.jpg'},
    {'id': 12, 'name': 'Veg Biryani', 'price': 160, 'img': 'vegbiryani.jpg'},
    {'id': 13, 'name': 'Chicken Dum Biryani', 'price': 220, 'img': 'chickenbiryani.jpg'},
]
TIFFINS = [
    {'id': 21, 'name': 'Idli', 'price': 40, 'img': 'idli.jpg'},
    {'id': 22, 'name': 'Dosa', 'price': 50, 'img': 'dosa.jpg'},
    {'id': 23, 'name': 'Puri', 'price': 45, 'img': 'puri.jpg'},
]
SOFTDRINKS = [
    {'id': 31, 'name': 'Coke', 'price': 40, 'img': 'coke.jpg'},
    {'id': 32, 'name': 'Sprite', 'price': 40, 'img': 'sprite.jpg'},
    {'id': 33, 'name': 'Fresh Lime Soda', 'price': 50, 'img': 'limesoda.jpg'},
]
ALL_ITEMS = CURRIES + BURGERS + BIRYANIS + TIFFINS + SOFTDRINKS

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def main(request):
    return render(request, 'main.html')

def signin(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = CustomUser.objects.filter(name=name, password=password).first()
        if user:
            request.session['user_id'] = user.id
            request.session['role'] = user.role
            if user.role == 'admin':
                return redirect('admin_home')  # Create an admin home view/page
            else:
                return redirect('menu')  # User home page
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')
        if CustomUser.objects.filter(name=name).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'signup.html')
        CustomUser.objects.create(name=name, email=email, password=password)
        messages.success(request, "Account created successfully. Please sign in.")
        return redirect('signin')
    return render(request, 'signup.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def menu(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        item_id = str(request.POST.get('item_id'))
        if item_id in cart:
            cart[item_id] += 1
        else:
            cart[item_id] = 1
        request.session['cart'] = cart
        return redirect('menu')
    items = Item.objects.all()
    return render(request, 'menu.html', {'items': items})

def burgers(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        item_id = str(request.POST.get('item_id'))
        if item_id in cart:
            cart[item_id] += 1
        else:
            cart[item_id] = 1
        request.session['cart'] = cart
        return redirect('cart')
    return render(request, 'burgers.html', {'burgers': BURGERS})

def biryanis(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if isinstance(cart, list):
            cart = {}
        item_id = str(request.POST.get('item_id'))
        if item_id in cart:
            cart[item_id] += 1
        else:
            cart[item_id] = 1
        request.session['cart'] = cart
        return redirect('cart')
    return render(request, 'biryanis.html', {'biryanis': BIRYANIS})

def curries(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        # If cart is a list (old format), reset to empty dict
        if isinstance(cart, list):
            cart = {}
        item_id = str(request.POST.get('item_id'))
        if item_id in cart:
            cart[item_id] += 1
        else:
            cart[item_id] = 1
        request.session['cart'] = cart
        return redirect('cart')
    return render(request, 'curries.html', {'curries': CURRIES})

def tiffins(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if isinstance(cart, list):
            cart = {}
        item_id = str(request.POST.get('item_id'))
        if item_id in cart:
            cart[item_id] += 1
        else:
            cart[item_id] = 1
        request.session['cart'] = cart
        return redirect('cart')
    return render(request, 'tiffins.html', {'tiffins': TIFFINS})

def softdrinks(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if isinstance(cart, list):
            cart = {}
        item_id = str(request.POST.get('item_id'))
        if item_id in cart:
            cart[item_id] += 1
        else:
            cart[item_id] = 1
        request.session['cart'] = cart
        return redirect('cart')
    return render(request, 'softdrinks.html', {'softdrinks': SOFTDRINKS})

def cart(request):
    cart = request.session.get('cart', {})
    items = []
    grand_total = 0
    for item_id, quantity in cart.items():
        try:
            item = Item.objects.get(id=item_id)
            item_dict = {
                'id': item.id,
                'name': item.name,
                'price': item.price,
                'category': item.category,
                'quantity': quantity,
                'total': item.price * quantity,
            }
            items.append(item_dict)
            grand_total += item.price * quantity
        except Item.DoesNotExist:
            continue
    return render(request, 'cart.html', {'items': items, 'grand_total': grand_total})

def pay(request):
    if request.method == 'POST':
        payment_type = request.POST.get('payment_type')
        address = request.POST.get('address')
        cart = request.session.get('cart', {})
        items = []
        grand_total = 0
        for item_id, quantity in cart.items():
            try:
                item = Item.objects.get(id=item_id)
                item_dict = {
                    'id': item.id,
                    'name': item.name,
                    'price': item.price,
                    'category': item.category,
                    'quantity': quantity,
                    'total': item.price * quantity,
                }
                items.append(item_dict)
                grand_total += item.price * quantity
            except Item.DoesNotExist:
                continue
        # Save order
        user_id = request.session.get('user_id', 0)
        Order.objects.create(
            user_id=user_id,
            address=address,
            payment_type=payment_type,
            items=json.dumps(items),
            total=grand_total
        )
        # Clear cart after payment
        request.session['cart'] = {}
        return render(request, 'pay.html', {
            'payment_done': True,
            'payment_type': payment_type,
            'address': address,
            'items': items,
            'grand_total': grand_total
        })
    return render(request, 'pay.html', {'payment_done': False})

def myorders(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('signin')  # Redirect to sign in if not logged in
    orders = Order.objects.filter(user_id=user_id).order_by('-created_at')
    filter_date = request.GET.get('date')
    if filter_date:
        # Filter orders by date (date only, not time)
        orders = orders.filter(created_at__date=parse_date(filter_date))
    for order in orders:
        order.items_list = json.loads(order.items)
    return render(request, 'myorders.html', {'orders': orders, 'filter_date': filter_date})

def logout_view(request):
    request.session.flush()
    return redirect('signin')

def admin_home(request):
    # Add your admin dashboard logic here
    return render(request, 'admin_home.html')

def admin_manage_items(request):
    if request.session.get('role') != 'admin':
        return redirect('menu')
    # Remove item
    if request.method == 'POST':
        if 'remove_id' in request.POST:
            Item.objects.filter(id=request.POST['remove_id']).delete()
        elif 'add_item' in request.POST:
            name = request.POST['name']
            price = request.POST['price']
            category = request.POST.get('category', '')
            Item.objects.create(name=name, price=price, category=category)
        return redirect('admin_manage_items')
    items = Item.objects.all()
    return render(request, 'admin_manage_items.html', {'items': items})