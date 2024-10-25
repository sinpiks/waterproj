from django.db import models

# Create your models here.


#Нужен для реализации выпадающего списка в панели администрации
TYPE_OF_BOTTLE = [
    ("largeBottleOfWater", "Вода питьевая 5 л - 19 л"),
    ("bottleOfWater", "Вода питьевая 1,5 л"),
    ("middleBottleOfWater", "Вода питьевая 0,5 л"),
    ("sweetBottleOfWater", "Напитки")
]


#Нужен для сопоставления категории соотвествующих  стилей
# [0] - style for <div class="catalog-description>
# [1] - style for <div class="things-container>
DEV_TYPE_OF_BOOTLE = [
    ("largeBottleOfWater", "large-water", "Вода питьевая 5 л - 19 л"),
    ("bottleOfWater", "mini-water", "Вода питьевая 1,5 л"),
    ("middleBottleOfWater", "middle-water", "Вода питьевая 0,5 л"),
    ("sweetBottleOfWater", "sweety-water", "Напитки")
]


#Класс, описывающий вакансии, появляющиеся на странице "Вакансии" и их редактирования в панели администрации
class Vacancies(models.Model):
    tittle = models.CharField('Вакансия', max_length = 50)
    image = models.ImageField(upload_to = "images/vacancies")
    working_conditions = models.TextField('Условия работы', default = 'Уточняйте информацию у администратора')
    requirements = models.TextField('Требования', default = 'Уточняйте информацию у администратора')
    duties = models.TextField('Обязанности', default = 'Уточняйте информацию у администратора')

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


#Класс, описывающий вакансии, появляющиеся на странице "О воде" и их редактирования в панели администрации
class Products(models.Model):
    tittle = models.CharField('Продукт', max_length = 50)
    image = models.ImageField(upload_to = "images/products/")
    type_bottle = models.CharField('Класс продукта', max_length = 30, choices = TYPE_OF_BOTTLE, default = 'Other')

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'