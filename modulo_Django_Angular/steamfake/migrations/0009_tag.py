# Generated by Django 5.1.2 on 2024-10-16 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamfake', '0008_delete_aluno_remove_turma_curso_delete_curso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=23, unique=True)),
                ('descricao', models.CharField(max_length=350, unique=True)),
            ],
        ),
    ]