# Generated by Django 3.1 on 2020-09-29 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200919_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Kategori İsmi')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='Kategori Bağlantı')),
                ('description', models.CharField(max_length=100, verbose_name='Kategori Açıklaması')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')),
                ('is_category', models.BooleanField(default=False, verbose_name='Is Category')),
                ('is_label', models.BooleanField(default=False, verbose_name='Is Label')),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='PostTermStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='post.post', verbose_name='Post of Term')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.postterm', verbose_name='Term of Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postlabel',
            name='label',
        ),
        migrations.RemoveField(
            model_name='postlabel',
            name='post',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Label',
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
        migrations.DeleteModel(
            name='PostLabel',
        ),
    ]
