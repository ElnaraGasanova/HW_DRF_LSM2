import stripe
from config import settings
stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_product(product_name):
    '''Метод создания продукта в stripe'''
    product = stripe.Product.create(name=product_name)
    return product['id']

def create_stripe_price(amount, product_id):
    '''Метод создания продукта в stripe, используя заданное количество,
    идентификатор продукта и валюту. Валюта по умолчанию "rub"'''
    return stripe.Price.create(unit_amount_decimal=amount * 100, currency='rub', product=product_id)
    return price['id']

def create_stripe_sessions(price):
    '''Метод создания сессии на оплату в stripe.'''
    session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/user/payments/',
        line_items=[{'price': price.get('id'), 'quantity': 1}],
        mode='payment',
    )
    # возвращаем url сессии и ее id
    return session.get('url'), session.get('id')
