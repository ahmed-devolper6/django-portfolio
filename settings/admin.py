from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import porflie
# Apply summernote to all TextField in model.
class ProfileModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
# Register your models here.
admin.site.register(porflie , ProfileModelAdmin)