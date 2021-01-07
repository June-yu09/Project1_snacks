from django.db import models

class SnacksIntro(models.Model):
    title = models.CharField(max_length=35, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='fat_gui.png' , upload_to='intro/', null=True, blank=True)

    def __str__(self):
        return self.title
    