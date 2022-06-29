# Generated by Django 4.0.5 on 2022-06-29 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='students.studentgroup', verbose_name='Группа'),
        ),
    ]