# Generated by Django 4.1 on 2022-10-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_application', '0011_custominline_custominlineitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Test Custom Widget',
            },
        ),
    ]
