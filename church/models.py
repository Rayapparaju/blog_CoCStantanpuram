from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('sermon', 'Sermon'),
        ('devotional', 'Devotional'),
        ('teaching', 'Teaching'),
        ('news', 'Church News'),
        ('testimony', 'Testimony'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='sermon')
    author = models.CharField(max_length=100, default='CoC Stantanpuram')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Sermon(models.Model):
    title = models.CharField(max_length=255)
    preacher_name = models.CharField(max_length=100)
    bible_reference = models.CharField(max_length=200, blank=True)
    sermon_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='sermons/', blank=True, null=True)
    video_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='sermons/', blank=True, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sermon_date']

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='books/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='books/', blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)
    lyrics = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
