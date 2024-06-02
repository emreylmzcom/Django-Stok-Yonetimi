from django.db import migrations, models
import django.utils.text
import itertools

def generate_unique_slug(apps, schema_editor):
    Urun = apps.get_model('envanter', 'Urun')
    for urun in Urun.objects.all():
        if not urun.slug:
            slug = django.utils.text.slugify(urun.isim)
            for i in itertools.count(1):
                if not Urun.objects.filter(slug=slug).exists():
                    break
                slug = f'{slug}-{i}'
            urun.slug = slug
            urun.save()

class Migration(migrations.Migration):

    dependencies = [
        ('envanter', '0003_urun_slug'),
    ]

    operations = [
        migrations.RunPython(generate_unique_slug),
    ]
