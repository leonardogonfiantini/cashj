import json
import requests

import dotenv
import os
import sys
dotenv.load_dotenv()
API_URL = os.getenv('API_URL')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from backend.api.schema import Category, Supplier, Product, RawProduct, ProductRecipe

def read_static_data():
    with open('static_data.json') as f:
        data = json.load(f)
    return data    
            
def init_table(istance, data, api):
    for item in data[api]:
        try: 
            item = istance(
                **item
            )
            response = requests.post(f'{API_URL}/{api}/', json=item.model_dump())
            print(response.json())
        except Exception as e:
            print(e)
            
def init_all(data):
    init_table(Category, data, 'category')
    init_table(Supplier, data, 'supplier')
    init_table(Product, data, 'product')
    init_table(RawProduct, data, 'raw_product')
    init_table(ProductRecipe, data, 'product_recipe')
    
def main():
    data = read_static_data()
    init_all(data)
    
if __name__ == '__main__':
    main()