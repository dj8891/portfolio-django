from django.contrib import admin

# Register your models here.
from .models import Jobs, Projects, Tools, Usages

admin.site.register([Jobs, Projects, Tools, Usages])