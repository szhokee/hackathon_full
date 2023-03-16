
from django.contrib import admin
from ticket.models import Ticket, Category


admin.site.register(Ticket)
admin.site.register(Category)