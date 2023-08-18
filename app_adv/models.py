from django.db import models

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    auction = models.BooleanField("Торг", default=False, help_text="Выберите, будет ли торг уместен")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата изменения", auto_now=True)

    def __str__(self):
        return f"{self.id} | {self.title} | {self.price}"

    class Meta:
        db_table = "advertisements"