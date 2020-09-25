from django.conf.urls import url

from . import views


app_name = "offers"
urlpatterns = [
	url(regex=r"^$", view=views.OfferListView.as_view(), name="list"),
	url(regex=r"^add/$", view=views.AddOfferFormView.as_view(), name="add"),
    url(regex=r"^update/(?P<pk>\d+)/$", view=views.UpdateOfferFormView.as_view(), name="update"),
]
