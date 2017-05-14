from django.core.urlresolvers import reverse
from django.views import generic

from .models import Request


class RequestsListView(generic.ListView):
    model = Request
    template_name = 'http_requests/requests.html'
    queryset = Request.objects.all()[:10]
