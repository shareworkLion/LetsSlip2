

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('m_no', models.AutoField(primary_key=True, serialize=False)),
                ('m_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('pwd', models.CharField(max_length=255)),
                ('nick_nm', models.CharField(max_length=255)),
                ('galary_nm', models.CharField(blank=True, max_length=255, null=True)),
                ('motto', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_img', models.CharField(blank=True, max_length=255, null=True)),
                ('mbti', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('lock_yn', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'member',
                'managed': False,
            },
        ),
    ]
