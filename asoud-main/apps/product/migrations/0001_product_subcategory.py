from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Define dependencies if initial migrations exist
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, blank=True, null=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.market', verbose_name='Market')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory', verbose_name='Sub Category')),
            ],
            options={
                'db_table': 'product_sub_category',
                'verbose_name': 'Product sub category',
                'verbose_name_plural': 'Product sub categories',
                'unique_together': {('market', 'sub_category')},
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='product',
            name='product_sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productsubcategory', verbose_name='Product sub category', null=True),
        ),
    ]
