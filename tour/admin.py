from django.contrib import admin

# Register your models here.
from .models import MyUser,Region,Tour,Compra,CompraTour

admin.site.register(MyUser)
admin.site.register(Region)
admin.site.register(Tour)
admin.site.register(Compra)
admin.site.register(CompraTour)

