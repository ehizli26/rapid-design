from django.db import models

# Resim modeli
class Image(models.Model):
    # Resim adı
    title = models.CharField(max_length=100)
    # Resim dosyası
    image = models.ImageField(upload_to='images/')
    # Açıklama
    description = models.TextField(blank=True)

    # Resmin silindiğinde dosyanın da silinmesi
    delete_on_delete = models.CASCADE

    # Resmi tanımlayan bir metin
    def __str__(self):
        return self.title

    # Resmi silerken resmin dosyasını da siler
    def delete(self, **kwargs):
        # Resmin dosyasını sil
        self.image.delete()

        # Resmi veritabanından sil
        super().delete(**kwargs)
