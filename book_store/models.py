from datetime import date, datetime
import logging

from django.db import models
from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=250)
    isbn = models.CharField('ISBN', max_length=13)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    published_date = models.DateField(default=None, null=True)

    def __str__(self):
        return '%s by %s, published at %s' % (
            self.title, self.author, self.published_date)


@receiver(post_save, sender=Book)
def log_created_or_updated(sender, instance, created, *args, **kwargs):
    logger = logging.getLogger(__name__)
    if not created:
        current_time = str(datetime.now())
        logger.debug('Book ' + instance.title + ' updated at: ' + current_time)
    else:
        create_time = str(datetime.now())
        logger.debug('Book ' + instance.title + ' created at: ' + create_time)


@receiver(post_delete, sender=Book)
def log_deleted(sender, instance, *args, **kwargs):
    logger = logging.getLogger(__name__)
    delete_time = str(datetime.now())
    logger.debug('Book ' + instance.title + ' deleted at: ' + delete_time)


class Request(models.Model):
    request_date = models.DateField(default=date.today)
    scheme = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    method = models.CharField(max_length=250)
    content_type = models.CharField(max_length=250)