from django.contrib import admin
from .models import ticket
from .models import question
from .models import optq

admin.site.register(ticket)
admin.site.register(question)
admin.site.register(optq)

