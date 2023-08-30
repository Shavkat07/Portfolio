from django.contrib import admin
from django import forms
from .models import Comment, Blogs, Portfolio, Skills, Services, Messages

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blogs
        fields = '__all__'


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", 'publish', 'id',)
    form = BlogAdminForm
    readonly_fields = ('id', 'date_created', 'author',)
    list_filter = ['date_created', 'publish', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['publish']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("blog", 'email', 'text')
    readonly_fields = ('id', 'data_created',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'id',)
    readonly_fields = ('id',)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id',)
    readonly_fields = ('id',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    readonly_fields = ('id',)


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id',)
    readonly_fields = ('id',)

# class BLogsGroup(admin.AdminSite):
#     site_header = "Blogs"
#     site_title = "Blogs Group Admin Site"
#     index_title = "Welcome to Blogs Group Admin"
#
# class AboutMeGroup(admin.AdminSite):
#     site_header = "About Me"
#     site_title = "Model1 Group Admin Site"
#     index_title = "Welcome to Model1 Group Admin"

# about_admin_group = AboutMeGroup(name='about_group')
# about_admin_group.register(Portfolio, PortfolioAdmin)
# about_admin_group.register(Services, ServicesAdmin)
# about_admin_group.register(Skills, SkillsAdmin)
#
# blogs_admin_site = BLogsGroup(name="blog_group")
# blogs_admin_site.register(Blogs, BlogsAdmin)
# blogs_admin_site.register(Comment, CommentsAdmin)
