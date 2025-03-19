"""from django.db import models


class Image(models.Model):
   caption=models.CharField(max_length=100)
   image=models.ImageField(upload_to="img/%y")
   
   def __str__(self):
     return self.caption"""

from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    modif_image = models.ImageField(upload_to='modif_images/', blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True, null=True)  # Nom de l'image
    text = models.CharField(max_length=200, blank=True, null=True)     # Texte personnalisé

    def __str__(self):
        return self.caption if self.caption else "Image sans caption"