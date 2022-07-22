from django.core.mail import send_mail
from projectalpha.settings import API_KEY, EMAIL_HOST_USER
import requests

def get_asset_price(asset):

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={asset}.SA&apikey={API_KEY}'
    res = requests.get(url).json()
    price = float(res['Global Quote']['05. price'])
    price
    return price

def update_asset_price(*args):
    obj = args[0]
    price = get_asset_price(obj.asset.name)
    obj.price = price

    obj.save()

    notifier = AssetNotifier()

    if price > obj.maximun_price:
        title, message = notifier.sell_nodifier(obj)
        send_mail(subject=title, message=message, from_email=EMAIL_HOST_USER , recipient_list=[obj.investor.email])

    if price < obj.minimun_price:
        title, message = notifier.buy_notifier(obj)

        send_mail(subject=title, message=message, from_email=EMAIL_HOST_USER , recipient_list=[obj.investor.email])

class AssetNotifier():
    title = 'Sugestão de {} do(a): {}'
    message = 'Ativo {} chegou ao limite {}.\nValor atual do ativo: {}\nLimite :{}'

    def sell_nodifier(self, obj):
        return (
            self.title.format('venda', obj.asset.name),
            self.message.format(obj.asset.name, 'máximo', obj.price, obj.maximum_price)
        )

    def buy_notifier(self, obj):
        return (
            self.title.format('compra', obj.asset.name),
            self.message.format(obj.asset.name, 'mínimo', obj.price, obj.minimum_price)
        )