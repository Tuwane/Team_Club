from django.contrib import admin
from .models import Player


# Register your models here.



class PlayerAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
admin.site.register(Player, PlayerAdmin)

admin.site.site_header = "Vall ecos Football Club Admin"
admin.site.site_title = "Vall ecos Football Club Portal"
admin.site.index_title = "Wellcome to Vall Ecoes FC Management Panel"

