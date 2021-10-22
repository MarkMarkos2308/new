from django.contrib import admin
from .models import human


@admin.register(human)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('AdminCase',)


    def AdminCase(self, obj):
        age = 2021 - int(obj.year_of_birth)
        return obj.name + ' ' + obj.surname + ' ' +obj.gander + ' ' + str(age)

    AdminCase.short_description = 'USERS'
