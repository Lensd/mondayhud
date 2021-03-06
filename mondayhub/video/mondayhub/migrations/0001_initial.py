# Generated by Django 3.2.7 on 2022-04-03 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='filesInput/')),
                ('csv', models.FileField(upload_to='filesInput/')),
                ('csvTimeL', models.CharField(default='00:00:02.02', max_length=50)),
                ('csvTimeR', models.CharField(default='00:00:02.4', max_length=50)),
                ('urlTimeL', models.CharField(default=3, max_length=50)),
                ('urlTimeR', models.CharField(default=8, max_length=50)),
                ('siteUrl', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resVideo', models.FileField(upload_to='')),
                ('inputData', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mondayhub.post')),
            ],
        ),
    ]
