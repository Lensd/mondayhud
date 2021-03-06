# Generated by Django 3.2.7 on 2022-04-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mondayhub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
                ('file', models.FileField(upload_to='video/')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='inputData',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
