from django.contrib import admin
from myapp.models import Modelos_nexu
# Register your models here.
@admin.register(Modelos_nexu)
class Modelos_nexu_admin(admin.ModelAdmin):
    list_display = ['id','name']
