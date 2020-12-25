from django.contrib import admin

from .models import MemberOfProject, Project, User, Member

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "first_name",
        "last_name",
    ]


class MembersInline(admin.TabularInline):
    model = MemberOfProject
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (MembersInline,)
    list_display = [
        'title',
        'owner',
        'shrot_description',
        'start_date',
    ]
