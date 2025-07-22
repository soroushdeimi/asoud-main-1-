from django.db import migrations, models
import uuid
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryGroup',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, blank=True, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory', verbose_name='Sub Category')),
            ],
            options={
                'db_table': 'product_category_group',
                'verbose_name': 'Product category group',
                'verbose_name_plural': 'Product category groups',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, blank=True, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategorygroup', verbose_name='Group')),
            ],
            options={
                'db_table': 'product_category',
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, blank=True, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategory', verbose_name='Category')),
            ],
            options={
                'db_table': 'product_sub_category',
                'verbose_name': 'Product sub category',
                'verbose_name_plural': 'Product sub categories',
            },
        ),
    ]
