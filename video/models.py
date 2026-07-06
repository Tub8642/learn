from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug_candidate = base_slug
            counter = 1
            while Category.objects.filter(slug=slug_candidate).exists():
                slug_candidate = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug_candidate
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Project(models.Model):
    slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class ContactMessage(models.Model):
    CONTACT_CHOISES = [
        ('email', 'Email'),
        ('phone', 'Телефон'),
        ('vk', 'Вконтакте'),
    ]
    name = models.CharField(max_length=100)
    contact_type = models.CharField(max_length=50, choices=CONTACT_CHOISES)
    contact_value = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateField(auto_now_add=True)  

    def __str__(self):
        return f'Сообщение от {self.name}'
    
    class Meta:
        ordering = ['sent_at']
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'