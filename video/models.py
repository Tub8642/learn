from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/')
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects'
    )
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    class ContactMessage(models.Model):
        CONTACT_CHOISES = [
            ('email', 'Email'),
            ('phone', 'Телефон')
            ('vk', 'Вконтакте')
        ]
        name = models.CharField(max_length=100)
        contact_type = models.CharField(max_length=50, choices=[CONTACT_CHOISES])
        contact_value = models.CharField(max_length=200)
        massage = models.TextField()
        send_at = models.DateField(auto_now_add=True)