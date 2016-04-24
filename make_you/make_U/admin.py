from django.contrib import admin
from make_U import models as make_U_models
# Register your models here.

admin.site.register(make_U_models.Contents)
admin.site.register(make_U_models.Templates)
