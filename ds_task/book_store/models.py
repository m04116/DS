from datetime import date, datetime
import logging

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Author(models.Model):
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    def __str__(self):
        return '%s ' % self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    isbn = models.CharField('ISBN', max_length=13)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    # published_date = models.DateField(default=date.today, null=True)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s by %s, published at %s' % (
            self.title, self.author, self.published_date)


logger = logging.getLogger(__name__)

@receiver(post_save, sender=Book)
def log_created_or_updated(sender, instance, created, *args, **kwargs):
    actual_time = str(datetime.now())
    if not created:
        logger.debug('Book ' + instance.title + ' updated at: ' + actual_time)
    else:
        logger.debug('Book ' + instance.title + ' created at: ' + actual_time)


@receiver(post_delete, sender=Book)
def log_deleted(sender, instance, *args, **kwargs):
    actual_time = str(datetime.now())
    logger.debug('Book ' + instance.title + ' deleted at: ' + actual_time)
