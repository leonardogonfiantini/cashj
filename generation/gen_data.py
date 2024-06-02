import json, requests, os, sys, random, datetime, faker, holidays, dotenv

dotenv.load_dotenv()
API_URL = os.getenv('API_URL')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
fake = faker.Faker()

from backend.api.schema import Category, Supplier, Product, RawProduct, ProductRecipe, Transaction, Order

def read_static_data():
    with open('static_data.json') as f:
        data = json.load(f)
    return data    
data = read_static_data()

def get_data(api: str, params: dict = None):
    try:
        response = requests.get(f'{API_URL}/{api}', params=params)
        return response.json()
    except Exception as e:
        print(e)
        return None
    
def delete_table(table: str):
    try:
        response = requests.delete(f'{API_URL}/deletetable/{table}')
        return response.json()
    except Exception as e:
        print(e)
        return None
            
def delete_all_tables():
    delete_table('productrecipe')
    delete_table('product')
    delete_table('category')
    delete_table('order')
    delete_table('transaction')    
    delete_table('rawproduct')
    delete_table('supplier')
    

def init_table(istance, api):
    for item in data[api]:
        try: 
            item = istance(
                **item
            )
            response = requests.post(f'{API_URL}/{api}/', json=item.model_dump())
        except Exception as e:
            print(e)
            
def init_all_table():
    init_table(Category, 'category')
    init_table(Supplier, 'supplier')
    init_table(Product, 'product')
    init_table(RawProduct, 'rawproduct')
    init_table(ProductRecipe, 'productrecipe')
    
    
def generate_data():
    global inflation
    inflation = 0
    years = [2020, 2021, 2022, 2023]
    luck = [0.3, 0.5, 0.7, 0.6]
    
    for year, luck_year in zip(years, luck):
        print(f'Generating data for year {year}')
        inflation += 0.1
        generate_year(year, luck_year)
        
def generate_year(year, luck_year):

    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    delta = end_date - start_date
    
    for i in range(delta.days + 1):
        date = start_date + datetime.timedelta(days=i)
        generate_day(date, luck_year)

def luck_day(date, luck_year):
    if date in holidays.Italy(years=date.year):
        return round((random.uniform(0.8, 1.4) + luck_year) / 2, 2)
    
    month_luck = [0.1, 0.1, 0.3, 0.4, 0.6, 0.7, 0.9, 1.2, 0.8, 0.4, 0.1, 0.4]
    week_luck = [0.2, 0.1, 0.2, 0.4, 0.8, 1, 0.5]
    
    return round((luck_year + week_luck[date.weekday()] + month_luck[date.month - 1]) / 3, 2)

def clients_day(luck):
    clients = 0
    if luck > 0.8:
        clients = random.randint(700, 900) * luck
    elif luck > 0.6:
        clients = random.randint(400, 700) * luck
    elif luck > 0.4:
        clients = random.randint(200, 400) * luck
    elif luck > 0.2:
        clients = random.randint(100, 200) * luck
    else:
        clients = random.randint(0, 100) * luck
    
    return int(clients)

def find_products_by_raw(raw_id):
    products = []
    for recipe in data['productrecipe']:
        if recipe['id_raw'] == raw_id:
            products.append(recipe['id_prod'])
    return products

def get_rate_product(product_id):
    for product in data['product_rate']:
        if product['id_prod'] == product_id:
            return product['rate']

def find_supplier_by_raw(raw_id):
    for supplier in data['supplier_product']:
        for raw in supplier['sell']:
            if raw_id == raw[0]:
                return supplier['id_supplier']

def find_price_by_raw(raw_id):
    for supplier in data['supplier_product']:
        for raw in supplier['sell']:
            if raw_id == raw[0]:
                return raw[1]  
            
def get_raw_needed(product_id, raw_id):
    for recipe in data['productrecipe']:
        if recipe['id_prod'] == product_id and recipe['id_raw'] == raw_id:
            return recipe['amount']
        
def find_category_by_product(product_id):
    for product in data['product']:
        if product['id_prod'] == product_id:
            return product['category_name']

def isSummer(date):
    return date.month in [6, 7, 8]

def isWinter(date):
    return not isSummer(date)

def generate_transaction(date):    
    STACK = 160
    warehouse = get_data('rawproducts', params={'limit': 100})
    
    for raw in warehouse:
        id_raw = raw['id_raw']
        products_id = find_products_by_raw(id_raw)
        
        abs_quantity = 0
        for id in products_id:
            product_rate = get_rate_product(id)
            raw_needed = get_raw_needed(id, id_raw)
            if isWinter(date):
                abs_quantity += STACK * raw_needed * product_rate[0]
            else:
                abs_quantity += STACK * raw_needed * product_rate[1]
        
        get_raw_amount = raw['amount']    
        
        if get_raw_amount < abs_quantity:
            supplier = find_supplier_by_raw(id_raw)
            
            needed_raw = round((abs_quantity - get_raw_amount) * random.uniform(0.8, 1.2) + 1, 2) + 1
            price = round(find_price_by_raw(id_raw) * (inflation + random.uniform(0.8, 1.2) * needed_raw), 2)
            
            transaction = Transaction(
                date=date.strftime('%Y-%m-%d'),
                id_supplier=supplier,
                id_raw=id_raw,
                amount=needed_raw,
                price=price
            )
        
            try:
                response = requests.post(f'{API_URL}/transaction/', json=transaction.model_dump())
                response.raise_for_status()
            except Exception as e:
                print(e)

def create_group(max):
    n = random.choices(  
            range(1, 11),
                    # 1,   2,  3,  4, 5, 6, 7, 8,  9,  10
            weights= [10, 30, 26, 16, 8, 4, 3, 2, 0.5, 0.5], 
            k=1
        )[0]

    return n if n < max else max

def is_product_available(product_id, warehouse):
    for recipe in data['productrecipe']:
        if recipe['id_prod'] == product_id:
            raw_id = recipe['id_raw']
            raw_needed = recipe['amount']
            for raw in warehouse:
                if raw['id_raw'] == raw_id and raw['amount'] < raw_needed:
                    return False
    return True

def update_warehouse(prod_id, amount, warehouse):
    for recipe in data['productrecipe']:
        if recipe['id_prod'] == prod_id:
            raw_id = recipe['id_raw']
            raw_needed = recipe['amount']
            for raw in warehouse:
                if raw['id_raw'] == raw_id:
                    raw['amount'] -= raw_needed * amount
                    break
        
def get_random_product_by_rate_and_category(date, category):
    products_tmp = data['product_rate']
    products = []
    
    for product in products_tmp:
        if find_category_by_product(product['id_prod']) == category:
            products.append(product)
    
    if isSummer(date):
        weights = [product['rate'][1] for product in products]
    else: 
        weights = [product['rate'][0] for product in products]
        
    products = [product['id_prod'] for product in products]
    
    # choose a product with a rate
    return random.choices(products, weights=weights, k=1)[0]

def get_random_product_by_rate(date):
    products = data['product_rate']
    
    if isSummer(date):
        weights = [product['rate'][1] for product in products]
    else: 
        weights = [product['rate'][0] for product in products]
        
    products = [product['id_prod'] for product in products]
    
    # choose a product with a rate
    return random.choices(products, weights=weights, k=1)[0]

def get_product_price(product_id, type):
    for product in data['product']:
        if product['id_prod'] == product_id:
            return product[type]

def generate_table():
    table = random.choices(  
            range(1, 11),
            weights= [8, 8, 8, 8, 8, 8, 8, 8, 8, 28], 
            k=1
        )[0]
    if table==10:
        return 'banco'
    else:
        return 'tavolo - ' + str(table)
    
def generate_discount(price):
    
    if random.random() > 0.1:
        return 0
    
    cut_price = 0
    if price > 60:
        cut_price = price % 10
    elif price > 30:
        cut_price = price % 8
    elif price > 10:
        cut_price = price % 3
        
    return cut_price

def generate_price(table, list_products):

    overall_price = 0
    for product_id, quantity in list_products.items():
        if table == 'banco':
            price_u = get_product_price(product_id, 'price_u_retail')
        else:
            price_u = get_product_price(product_id, 'price_u_table')

        overall_price += price_u * quantity
        
    discount = generate_discount(overall_price)
    
    overall_price -= discount
    
    return discount, overall_price
    
def generate_orders(n_clients, date):
    # A seconda del rate il cliente acquista determiante cose
    warehouse = get_data('rawproducts', params={'limit': 100})
    
    while n_clients > 0:
        group = create_group(n_clients)
        n_clients -= group
                
        list_products = {}
        starting_category = random.choice(data['category'])['name']
        for _ in range(group):
            for _ in range(random.randint(1, 3)):
                
                if random.random() < 0.15:
                    product_id = get_random_product_by_rate(date)
                else:
                    product_id = get_random_product_by_rate_and_category(date, starting_category)
                    
                if is_product_available(product_id, warehouse):
                    if product_id in list_products:
                        list_products[product_id] += 1
                    else:
                        list_products[product_id] = 1
                    update_warehouse(product_id, 1, warehouse)
        
        if list_products == {}:
            continue
                
        table = generate_table()
        discount, price = generate_price(table, list_products)
        
        order = Order(
            date=date.strftime('%Y-%m-%d'),
            billNo=fake.ean(length=8),
            table=table,
            discount=discount,
            price=price,
            n_client=group,
            order_details=list_products
        )
        
        try:
            response = requests.post(f'{API_URL}/order/', json=order.model_dump())
            response.raise_for_status()
        except Exception as e:
            print(order.model_dump())
            print(e)
    
def generate_day(date, luck_year):
    
    luck = luck_day(date, luck_year)    
    n_clients = clients_day(luck)
    
    generate_transaction(date)
    
    print(f"Date: {date} - Luck: {luck} - Clients: {n_clients} - Inflation: {inflation}")
    generate_orders(n_clients, date)


def main():    
    delete_all_tables()
    init_all_table()
    generate_data()
    
if __name__ == '__main__':
    main()