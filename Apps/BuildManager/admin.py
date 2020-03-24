from django.contrib import admin
from .models import BuildData, SearchQuery
# NOTE: Register your models here, this will make them accessible from the Django Admin.

admin.site.register(BuildData)

admin.site.register(SearchQuery)
