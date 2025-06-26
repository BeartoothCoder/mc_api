from django.db import models as m

# Create your models here.
class Recipe(m.Model):
    """Model to represent a Minecraft crafting recipe."""
    name = m.CharField(max_length=100, null=True)
    data = m.JSONField()
    img_link = m.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        right = str(self.data).split("'description': {'identifier': 'minecraft:")[-1]
        name = right.split("'", 1)[0]
        name = name.replace('_', ' ').title()
        return name