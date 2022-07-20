from core.views import CreateRegisteredAssetView, CreateUserView, DeleteRegisteredAssetView, DetailsRegisteredAssetView, GetRegisteredAssetView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GetRegisteredAssetView.as_view(), name='home'),
    path('<pk>/details/', DetailsRegisteredAssetView.as_view(), name='details'),
    path('<pk>/delete/', DeleteRegisteredAssetView.as_view(), name='delete'),
    path('stock/', CreateRegisteredAssetView.as_view(), name='create_stock'),
    path('sign_up/', CreateUserView.as_view(), name="sign_up"),
    path('accounts/', include('django.contrib.auth.urls'))
    
]
