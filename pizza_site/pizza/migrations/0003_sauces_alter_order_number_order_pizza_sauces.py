# Generated by Django 4.1.3 on 2022-12-06 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_alter_order_number_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sauces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='У пиццы нет соуса', max_length=20, verbose_name='Название соуса к пицце')),
            ],
            options={
                'verbose_name': 'Соус',
                'verbose_name_plural': 'Соусы',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='number_order',
            field=models.IntegerField(default='6_3_28', error_messages='Проблема при создании индивидуального номера заказа', unique=True, verbose_name='Индивидуальный номер заказа'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='sauces',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.sauces'),
            preserve_default=False,
        ),
    ]
