from django.contrib import admin
from .models import FarmerRegister
from .models import *


# Register your models here.
admin.site.register(FarmerRegister)
admin.site.register(CropRegister)
admin.site.register(Contact_us)
admin.site.register(AgentInfo)
admin.site.register(ConsumerInfo)
admin.site.register(Feedback)
admin.site.register(Add_Items)
admin.site.register(checkout)
admin.site.register(CartUser)
admin.site.register(Seconddata)