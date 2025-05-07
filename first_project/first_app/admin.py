from django.contrib import admin
from first_app.models import Webpage,AccessRecord,Topic,WebUsers

# Register your models here.

admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebUsers)