from django.contrib import admin
from .models import Status
from .form import StatusForm
# Register your models here.
class StatuSAmin(admin.ModelAdmin):
    list_display = ["user", "__str__", "image"]
    form = StatusForm
    # class Meta:
    #     model = StatusForm
admin.site.register(Status, StatuSAmin)