# Generated by Django 3.2.3 on 2021-06-22 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_like'),
        ('common', '0002_rename_text_comment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
