import pandas as pd
import argparse

class SkincareSearcher():
   def __init__(self, filepath):
      self.df_sheets = pd.read_excel(filepath, sheet_name=None)

#Refactor, since they seem to be doing the same thing
# Ideas: search by purpose
# Filter by good, medium or bad reviews, choosing the reviewer
   def ingredient_search(self, ingredient):
       df_ingredient = self.df_sheets['Ingredients'].loc[self.df_sheets['Ingredients']['Ingredient']==ingredient]
       if df_ingredient.empty:
           print("No such ingredient found, would you like to add an entry?")
       return df_ingredient

   def product_search(self, product):
       df_product = self.df_sheets['Products'].loc[self.df_sheets['Products']['Product'] == product]
       if df_product.empty:
           print("No such product found, would you like to add an entry?")
       return df_product

   def brand_search(self, brand):
       df_brand = self.df_sheets['Products'].loc[self.df_sheets['Products']['Brand'] == brand]
       if df_brand.empty:
           print("No such brand found, would you like to add an entry?")
       return df_brand

if __name__ == "__main__":
    searcher = SkincareSearcher('./Skincare.xlsx')
    parser = argparse.ArgumentParser(description='Get skincare recommendations')
    parser.add_argument('-i', '--ingredient', dest='ingredient', metavar='ingredient', help='Ingredient to search for')
    parser.add_argument('-p', '--product', dest='product', metavar='product', help='Product to search for')
    parser.add_argument('-b', '--brand', dest='brand', metavar='brand',
                        help='Brand to search for')
    args = parser.parse_args()
    if args.ingredient:
        res= searcher.ingredient_search(args.ingredient)
    elif args.product:
        res =searcher.product_search(args.product)
    elif args.brand:
        res= searcher.brand_search(args.brand)
    print(res)