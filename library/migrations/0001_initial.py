# Generated by Django 5.2.1 on 2025-07-01 11:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('shelf_code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('shelf_count', models.PositiveIntegerField(default=0, editable=False)),
                ('max_borrow_per_student', models.PositiveIntegerField(default=1, help_text='Maximum books a student can borrow from this shelf.')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(max_length=20)),
                ('stream', models.CharField(max_length=20)),
                ('class_teacher', models.CharField(blank=True, max_length=100, null=True)),
                ('total_students', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'unique_together': {('form', 'stream')},
            },
        ),
        migrations.CreateModel(
            name='RevisionPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='revision_papers/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.room')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('publishers', models.CharField(blank=True, max_length=255, null=True)),
                ('first_publication', models.PositiveIntegerField(blank=True, null=True)),
                ('ISBN', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('book_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('category', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('book_picture', models.ImageField(blank=True, null=True, upload_to='book_pictures/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('shelf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.shelf')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('admission_number', models.PositiveIntegerField(unique=True)),
                ('student_picture', models.ImageField(blank=True, null=True, upload_to='student_pictures/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students', to='library.room')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('returned', models.BooleanField(default=False)),
                ('returned_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('processed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('shelf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.shelf')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.student')),
            ],
        ),
    ]
