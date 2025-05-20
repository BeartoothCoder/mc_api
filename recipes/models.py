from django.db import models as m

# Create your models here.
class Recipe(m.Model):
    """Model to represent a Minecraft crafting recipe."""
    name = m.CharField(max_length=100, null=True)
    data = m.JSONField()
    img_link = m.CharField(max_length=150, blank=True, null=True)