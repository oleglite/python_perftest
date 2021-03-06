# Generated by Django 2.1 on 2018-08-14 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('project', models.CharField(max_length=16)),
                ('region', models.CharField(db_index=True, max_length=8)),
                ('total_budget', models.FloatField(null=True)),
                ('info', models.CharField(max_length=128)),
                ('purpose', models.CharField(max_length=256)),
                ('department', models.CharField(max_length=256)),
                ('business', models.TextField()),
                ('is_budget', models.BooleanField()),
                ('customer', models.CharField(max_length=128)),
                ('owner', models.CharField(max_length=128)),
                ('approved_by', models.CharField(max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expires_at', models.DateTimeField(null=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
    ]
