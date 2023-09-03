from django.db import models

# Resim modeli
class Image(models.Model):
    # Resim adı
    title = models.CharField(max_length=100)
    # Resim dosyası
    image = models.ImageField(upload_to='images/')
    # Açıklama
    description = models.TextField(blank=True)

    # Resmi tanımlayan bir metin
    def __str__(self):
        return self.title
