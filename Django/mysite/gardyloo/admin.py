from django.contrib import admin

from .models import Country, Language, CountryLanguage, Religion, CountryReligion

admin.site.register(Country)
admin.site.register(Language)
admin.site.register(CountryLanguage)
admin.site.register(Religion)
admin.site.register(CountryReligion)
admin.site.register(Question)


