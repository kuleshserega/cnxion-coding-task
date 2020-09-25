import json

from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import OfferForm
from offers.models import Offer


class OfferFormView(FormView):
    template_name = 'offers/offer_form.html'
    form_class = OfferForm
    success_url = reverse_lazy('offers:add')

    def form_valid(self, form):
        """If the form is valid, save to the json data field."""
        form.save()

        if self.kwargs.get('pk'):
            messages.success(self.request, 'Offer updated.')
        else:
            messages.success(self.request, 'Offer added.')

        return super().form_valid(form)

    def get_initial(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            offer = Offer.objects.get(pk=pk)
            offer.data['offer_id'] = pk
            return offer.data

        return super().get_initial(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        pk = self.kwargs.get('pk')
        if pk:
            ctx['action'] = 'Update'
            ctx['action_url'] = reverse_lazy('offers:update', args=(pk,))
        else:
            ctx['action_url'] = reverse_lazy('offers:add')

        return ctx


class OfferListView(ListView):
    template_name = 'offers/offer_list.html'
    model = Offer
