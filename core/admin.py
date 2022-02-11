from django.contrib import admin
from core.models import Photo
from .models.user import User
from .models.profile import Article, Career


class UserAdmin(admin.ModelAdmin):
    def get_full_name(user):
        return "%s %s" % (user.first_name, user.last_name)
    get_full_name.short_description = "Name"

    list_display = (get_full_name, "email")


class CareerAdmin(admin.ModelAdmin):
    def get_full_name(career):
        return "%s %s" % (career.user.first_name, career.user.last_name)
    get_full_name.short_description = "Name"

    def get_career_name(career):
        return career.career_name

    get_career_name.short_description = "Career Name"

    def get_career_type(career):
        return career.get_career_type()

    get_career_type.short_description = "Career Type"

    def get_start_date(career):
        return career.start_date

    get_start_date.short_description = "Start Date"

    def get_end_date(career):
        return career.end_date

    get_end_date.short_description = "End Date"

    list_display = (get_full_name, get_career_name, get_career_type, get_start_date, get_end_date)


class ArticleAdmin(admin.ModelAdmin):
    def get_full_name(article):
        return "%s %s" % (article.user.first_name, article.user.last_name)
    get_full_name.short_description = "Name"

    list_display = (get_full_name, "title")


admin.site.register(User, UserAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Photo)
admin.site.register(Article, ArticleAdmin)
