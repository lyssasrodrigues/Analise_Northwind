import pandas as pd

# Função para carregar arquivos CSV com tratamento de erros e renomear colunas
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', encoding='utf-8', sep=';')
        df.columns = [col.strip().lower() for col in df.columns]
        print(f"Arquivo {file_path} carregado com sucesso. Colunas: {df.columns.tolist()}")
        return df
    except Exception as e:
        print(f"Erro ao carregar {file_path}: {e}")
        return None

# Caminhos dos arquivos descompactados
file_paths = {
    'categories': 'C:/Users/USER/Downloads/nortwind/categories.csv',
    'customer_customer_demo': 'C:/Users/USER/Downloads/nortwind/customer_customer_demo.csv',
    'customer_demographics': 'C:/Users/USER/Downloads/nortwind/customer_demographics.csv',
    'customers': 'C:/Users/USER/Downloads/nortwind/customers.csv',
    'employee_territories': 'C:/Users/USER/Downloads/nortwind/employee_territories.csv',
    'employees': 'C:/Users/USER/Downloads/nortwind/employees.csv',
    'order_details': 'C:/Users/USER/Downloads/nortwind/order_details.csv',
    'orders': 'C:/Users/USER/Downloads/nortwind/orders.csv',
    'products': 'C:/Users/USER/Downloads/nortwind/products.csv',
    'region': 'C:/Users/USER/Downloads/nortwind/region.csv',
    'shippers': 'C:/Users/USER/Downloads/nortwind/shippers.csv',
    'suppliers': 'C:/Users/USER/Downloads/nortwind/suppliers.csv',
    'territories': 'C:/Users/USER/Downloads/nortwind/territories.csv',
    'us_states': 'C:/Users/USER/Downloads/nortwind/us_states.csv'
}

# Carregar arquivos CSV em dataframes
def load_all_data(file_paths):
    dataframes = {}
    for key, path in file_paths.items():
        dataframes[key] = load_csv(path)
    return dataframes

if __name__ == "__main__":
    data = load_all_data(file_paths)
    for name, df in data.items():
        if df is not None:
            print(f"\n{name}:")
            print(df.head())
        else:
            print(f"\n{name}: Falha ao carregar o dataframe.")
