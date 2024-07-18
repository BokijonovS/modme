from django.contrib import admin

from leads.models import Lead, Expectation, Set

# Register your models here.

admin.site.register(Lead)
admin.site.register(Expectation)
admin.site.register(Set)

