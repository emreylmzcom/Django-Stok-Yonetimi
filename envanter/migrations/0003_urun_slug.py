from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('envanter', '0002_urun_fotoğraf'),  # Önceki migrasyonun doğru ismini buraya yazın
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
