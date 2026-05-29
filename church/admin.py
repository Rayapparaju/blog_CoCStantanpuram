from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import BlogPost, Sermon, Book, Song, GalleryImage, ContactMessage


admin.site.site_header = 'CoC Stantanpuram Administration'
admin.site.site_title = 'CoC Stantanpuram Admin'
admin.site.index_title = 'Welcome to Church Admin Panel'


class PublishableAdmin(admin.ModelAdmin):
    actions = ['publish_selected', 'unpublish_selected']

    @admin.action(description='Publish selected items')
    def publish_selected(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f'{updated} item(s) published.')

    @admin.action(description='Unpublish selected items')
    def unpublish_selected(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f'{updated} item(s) unpublished.')


@admin.register(BlogPost)
class BlogPostAdmin(PublishableAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'is_published')
    list_filter = ('category', 'is_published', 'created_at')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    list_per_page = 20
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'category', 'author')}),
        ('Content', {'fields': ('content', 'image', 'image_preview')}),
        ('Status', {'fields': ('is_published', 'created_at', 'updated_at')}),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:100px;max-width:150px;border-radius:4px;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Image Preview'


@admin.register(Sermon)
class SermonAdmin(PublishableAdmin):
    list_display = ('title', 'preacher_name', 'bible_reference', 'sermon_date', 'has_audio', 'is_published')
    list_filter = ('is_published', 'sermon_date', 'preacher_name')
    search_fields = ('title', 'preacher_name', 'bible_reference', 'description')
    list_editable = ('is_published',)
    date_hierarchy = 'sermon_date'
    readonly_fields = ('image_preview',)
    list_per_page = 20
    fieldsets = (
        (None, {'fields': ('title', 'preacher_name', 'bible_reference', 'sermon_date')}),
        ('Content', {'fields': ('description', 'image', 'image_preview', 'audio_file', 'video_url')}),
        ('Status', {'fields': ('is_published',)}),
    )

    def has_audio(self, obj):
        if obj.audio_file:
            return format_html('<span style="color:green;">&#10003;</span>')
        return format_html('<span style="color:#ccc;">&#10007;</span>')
    has_audio.short_description = 'Audio'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:100px;max-width:150px;border-radius:4px;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Image Preview'


@admin.register(Book)
class BookAdmin(PublishableAdmin):
    list_display = ('title', 'author', 'cover_preview', 'has_pdf', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'author', 'description')
    list_editable = ('is_published',)
    date_hierarchy = 'created_at'
    readonly_fields = ('cover_preview',)
    list_per_page = 20
    fieldsets = (
        (None, {'fields': ('title', 'author', 'description')}),
        ('Files', {'fields': ('cover_image', 'cover_preview', 'pdf_file')}),
        ('Status', {'fields': ('is_published', 'created_at')}),
    )

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="max-height:80px;max-width:80px;border-radius:4px;" />', obj.cover_image.url)
        return '-'
    cover_preview.short_description = 'Cover'

    def has_pdf(self, obj):
        if obj.pdf_file:
            return format_html('<span style="color:green;">&#10003;</span>')
        return format_html('<span style="color:#ccc;">&#10007;</span>')
    has_pdf.short_description = 'PDF'


@admin.register(Song)
class SongAdmin(PublishableAdmin):
    list_display = ('title', 'has_audio', 'lyrics_preview', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'lyrics')
    list_editable = ('is_published',)
    date_hierarchy = 'created_at'
    readonly_fields = ('lyrics_preview',)
    list_per_page = 20

    def has_audio(self, obj):
        if obj.audio_file:
            return format_html('<span style="color:green;">&#10003;</span>')
        return format_html('<span style="color:#ccc;">&#10007;</span>')
    has_audio.short_description = 'Audio'

    def lyrics_preview(self, obj):
        if obj.lyrics:
            return format_html('<pre style="max-height:100px;overflow-y:auto;background:#f5f5f5;padding:8px;border-radius:4px;">{}</pre>', obj.lyrics[:200])
        return '-'
    lyrics_preview.short_description = 'Lyrics Preview'


@admin.register(GalleryImage)
class GalleryImageAdmin(PublishableAdmin):
    list_display = ('title', 'image_thumb', 'uploaded_at', 'is_published')
    list_filter = ('is_published', 'uploaded_at')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    date_hierarchy = 'uploaded_at'
    readonly_fields = ('image_preview_full',)
    list_per_page = 20

    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px;max-width:80px;border-radius:4px;object-fit:cover;" />', obj.image.url)
        return '-'
    image_thumb.short_description = 'Thumbnail'

    def image_preview_full(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:250px;max-width:100%;border-radius:4px;" />', obj.image.url)
        return '-'
    image_preview_full.short_description = 'Image Preview'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at', 'message_preview')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message', 'phone')
    date_hierarchy = 'created_at'
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')
    list_per_page = 20
    actions = ['export_messages']
    fieldsets = (
        ('Sender Info', {'fields': ('name', 'email', 'phone')}),
        ('Message', {'fields': ('subject', 'message')}),
        ('Received', {'fields': ('created_at',)}),
    )

    @admin.action(description='Export selected messages as text')
    def export_messages(self, request, queryset):
        lines = []
        for msg in queryset:
            lines.append(f"From: {msg.name} ({msg.email})")
            lines.append(f"Phone: {msg.phone}")
            lines.append(f"Subject: {msg.subject}")
            lines.append(f"Date: {msg.created_at}")
            lines.append(f"Message:\n{msg.message}")
            lines.append("-" * 40)
        text = '\n'.join(lines)
        from django.http import HttpResponse
        response = HttpResponse(text, content_type='text/plain; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="contact_messages.txt"'
        return response
    export_messages.short_description = 'Export selected as text file'

    def message_preview(self, obj):
        return obj.message[:80] + '...' if len(obj.message) > 80 else obj.message
    message_preview.short_description = 'Message Preview'

    def has_add_permission(self, request):
        return False
