from django.contrib import admin

from .models import MemberOfProject, Project, User, Member, Task, Tag

# Register your models here.


@admin.register(Tag)
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


class ProjectMembersInline(admin.TabularInline):
    model = MemberOfProject
    extra = 1


class TaskMembersInline(admin.TabularInline):
    model = Task.members.through
    extra = 1


class TagsInline(admin.TabularInline):
    model = Task.tags.through
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = (TaskMembersInline,)
    exclude = ["members",]
    filter_horizontal = ("tags",)
    list_display = [
        "title",
        "assigner",
        "short_description",
        "finished",
        "date_created",
        "deadline"
    ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectMembersInline,)
    list_display = [
        'title',
        'leader',
        'short_description',
        'start_date',
    ]
