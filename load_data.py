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
    'categories': 'categories.csv',
    'customer_customer_demo': 'customer_customer_demo.csv',
    'customer_demographics': 'customer_demographics.csv',
    'customers': 'customers.csv',
    'employee_territories': 'employee_territories.csv',
    'employees': 'employees.csv',
    'order_details': 'order_details.csv',
    'orders': 'orders.csv',
    'products': 'products.csv',
    'region': 'region.csv',
    'shippers': 'shippers.csv',
    'suppliers': 'suppliers.csv',
    'territories': 'territories.csv',
    'us_states': 'us_states.csv'
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
