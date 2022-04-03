from django.contrib import admin

from petstagram.pets.models import Pet


# Show data as columns in admin panel
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'age', 'likes_count')
    list_filter = ('name',)
    sortable_by = ('name',)

    # Adding likes to the admin panel
    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Pet, PetAdmin)
