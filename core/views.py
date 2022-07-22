from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from core.forms import RegisteredAssetsForm, UserCreation
from core.models import Assets, RegisteredAssets
from core.utils import get_asset_price
from core.scheduler import create

class CreateRegisteredAssetView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = RegisteredAssetsForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.investor = self.request.user
        self.object.price = get_asset_price(self.object.asset)

        self.object.save()

        create(self.object)
        return HttpResponseRedirect(self.get_success_url())

class GetRegisteredAssetView(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = RegisteredAssets
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(investor=self.request.user)

class DetailsRegisteredAssetView(LoginRequiredMixin, UpdateView):
    template_name = 'details.html'
    form_class = RegisteredAssetsForm
    model = RegisteredAssets
    success_url = '/'
    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, pk=self.kwargs['pk'], **kwargs)

class DeleteRegisteredAssetView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = RegisteredAssets
    success_url = '/'

class CreateUserView(CreateView):
    template_name = 'sign_up.html'
    form_class = UserCreation
    success_url = '/accounts/login/'

