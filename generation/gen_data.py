import json, requests, os, sys, random, datetime, faker, holidays, dotenv
dotenv.load_dotenv()
API_URL = os.getenv('API_URL')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
fake = faker.Faker()

from backend.api.schema import Category, Supplier, Product, RawProduct, ProductRecipe, Transaction

def read_static_data():
    with open('static_data.json') as f:
        data = json.load(f)
    return data    

def delete_table(table: str):
    response = requests.delete(f'{API_URL}/deletetable/{table}')
    print(response.json())
    
def delete_all_tables():
    delete_table('productrecipe')
    delete_table('product')
    delete_table('category')
    
    delete_table('rawproduct')
    delete_table('supplier')

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
            
def init_all_table(data):
    init_table(Category, data, 'category')
    init_table(Supplier, data, 'supplier')
    init_table(Product, data, 'product')
    init_table(RawProduct, data, 'rawproduct')
    init_table(ProductRecipe, data, 'productrecipe')
    
    
def generate_data():
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    luck = [0.7, 0.2, 0.3, 0.6, 0.5, 0.7]
    
    for year, luck_year in zip(years, luck):
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
        clients = random.randint(800, 1000) * luck
    elif luck > 0.6:
        clients = random.randint(500, 800) * luck
    elif luck > 0.4:
        clients = random.randint(300, 500) * luck
    elif luck > 0.2:
        clients = random.randint(200, 300) * luck
    else:
        clients = random.randint(0, 200) * luck
    
    return int(clients)

def generate_transaction():
    # Vedere product recipe per ordinare uno stack di 300/400 prodotti a botta
    
    pass

def generate_client():
    # A seconda del rate il cliente acquista determiante cose
    
    pass
    
def generate_day(date, luck_year):
    
    luck = luck_day(date, luck_year)
    
    n_clients = clients_day(luck)
    
    print(f'Generating data for {date} with luck {luck} and {n_clients} clients')

    
    
    # Controlla la quantita del magazzino e se sotto acquista
    # Aggiorna il magazzino
    # Genera i clienti e i loro acquisit
    pass



def main():
    data = read_static_data()
    
    delete_all_tables()
    init_all_table(data)
    
    generate_data()
    
if __name__ == '__main__':
    main()