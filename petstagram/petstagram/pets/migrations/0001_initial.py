from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('parrot', 'Parrot')], max_length=6)),
                ('name', models.CharField(max_length=6)),
                ('age', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]
