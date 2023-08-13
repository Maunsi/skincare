from app.models import Product
from django.core.management.base import BaseCommand
import pandas as pd

class Command(BaseCommand):
    help = 'Populate database with dummy data'

    def handle(self, *args, **options):
        df_products = pd.read_excel('../Skincare.xlsx', sheet_name='Products')
        for _, row in df_products.iterrows():
            product = Product(name=row['Product'], brand=row['Brand'])
            product.save()