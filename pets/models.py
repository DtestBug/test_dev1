from django.db import models
from utils.base_model import BaseModels


class PetsModels(BaseModels):
    name = models.CharField(verbose_name='name', help_text='名字', max_length=10, unique=True)
    weight = models.TextField(verbose_name='weight', help_text='当前体重', max_length=3)

    # null=True该字段可以为空并且不报错
    birthday = models.DateField(verbose_name='birthday', help_text='什么时候出生的', null=True)
    varieties = models.TextField(verbose_name='varieties', help_text='什么样的品种', max_length=50)
    color = models.TextField(verbose_name='color', help_text='什么颜色', max_length=20)

    class Meta:
        db_table = 'pets_data'
        verbose_name = '宠物信息表'

    def __str__(self):
        return self.name
