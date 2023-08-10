from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # МНОГОЕ К ОДНОМУ
    tags = models.ManyToManyField(Tag, blank=True) # МНОГОЕ КО МНОГИМ
    name = models.CharField("Название", max_length=100)

    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name}"