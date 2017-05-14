from datetime import date, datetime

from django.db import models


class Request(models.Model):
    request_date = models.DateField(default=date.today)
    scheme = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    method = models.CharField(max_length=250)
    content_type = models.CharField(max_length=250)
