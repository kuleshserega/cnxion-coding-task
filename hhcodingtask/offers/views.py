import json

from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import OfferForm
from offers.models import Offer


class AddOfferFormView(CreateView):
    template_name = 'offers/offer_form.html'
    form_class = OfferForm
    model = Offer

    def form_valid(self, form):
        """If the form is valid, save to the json data field."""
        # form.save()
        messages.success(self.request, 'Offer added.')
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['action_url'] = reverse_lazy('offers:add')
        return ctx

    def get_success_url(self):
        return reverse_lazy('offers:add')


class UpdateOfferFormView(UpdateView):
    template_name = 'offers/offer_form.html'
    form_class = OfferForm
    model = Offer

    def form_valid(self, form):
        """If the form is valid, save to the json data field."""
        # form.save()
        messages.success(self.request, 'Offer updated.')
        return super().form_valid(form)

    def get_initial(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            offer = Offer.objects.get(pk=pk)
            offer.data['object_id'] = pk
            return offer.data

        return super().get_initial(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['action'] = 'Update'
        ctx['action_url'] = reverse_lazy(
            'offers:update', args=(self.kwargs.get('pk'),)
        )
        return ctx

    def get_success_url(self):
        return reverse_lazy('offers:add')


class OfferListView(ListView):
    template_name = 'offers/offer_list.html'
    model = Offer
