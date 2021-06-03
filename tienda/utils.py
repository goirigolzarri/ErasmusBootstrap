import json
from .models import *
from members.models import User


def cookieCart(request):

    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = (product.precio * cart[i]["quantity"])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]
            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'precio': product.precio,
                    'fotoURL': product.fotoURL,
                },
                'quantity': cart[i]["quantity"],
                'get_total': total,
            }
            items.append(item)
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):

    if request.user.is_authenticated:
        logged_in_user = request.user
        customer, created = Customer.objects.get_or_create(user=logged_in_user)
        order, created = Order.objects.get_or_create(pedido_de=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}




def guestOrder(request, data):

    print('User is not logged')
    print('Cookies:', request.COOKIES)

    name = data['form']['name']
    email = data['form']['email']
    
    print(name)
    print(email)
    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(email=email)
    customer.name = name
    customer.save()
    print('crea customer loggout')
    
    order = Order.objects.create(
    pedido_de = customer,
    complete = False
    )
    print('crea order loggout')

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )



    return customer, order