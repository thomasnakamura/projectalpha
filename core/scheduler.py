from apscheduler.schedulers.background import BackgroundScheduler
from core.models import RegisteredAssets
from core.utils import update_asset_price


def start():
    scheduler = BackgroundScheduler()

    for asset in RegisteredAssets.objects.all():

        scheduler.add_job(update_asset_price, 'interval', days=asset.frequency, args=[asset])

    scheduler.start()

def create(asset):
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_asset_price, 'interval', days=asset.frequency, args=[asset])
    scheduler.start()