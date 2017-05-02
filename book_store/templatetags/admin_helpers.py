from django import template
from django.urls import reverse
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def admin_edit(book):
    admin_url = 'admin:%s_%s_change' % (
        book._meta.app_label, book._meta.model_name)

    return format_html(
        '<a href="{}">Edit in admin</a>',
        reverse(admin_url, args=[book.id]))
