import pandas as pd

def analyze_data(dataframes):
    # Exemplo de análise de faturamento mensal e ticket médio
    order_details = dataframes['order_details']
    orders = dataframes['orders']
    products = dataframes['products']

    # Unir as tabelas de pedidos e detalhes dos pedidos
    orders_details_merged = pd.merge(order_details, orders, on='order_id')
    orders_details_merged = pd.merge(orders_details_merged, products, on='product_id')

    # Verificar as colunas após a junção
    print("Colunas após a junção:", orders_details_merged.columns)

    # Converter a coluna de data para datetime
    orders_details_merged['order_date'] = pd.to_datetime(orders_details_merged['order_date'])

    # Faturamento mensal
    orders_details_merged['month'] = orders_details_merged['order_date'].dt.to_period('M')
    orders_details_merged['total'] = orders_details_merged['quantity'] * orders_details_merged['unit_price_x']
    faturamento_mensal = orders_details_merged.groupby('month')['total'].sum().reset_index()

    # Converter 'month' para string
    faturamento_mensal['month'] = faturamento_mensal['month'].astype(str)

    # Ticket médio
    ticket_medio = orders_details_merged.groupby('order_id')['total'].sum().mean()

    return faturamento_mensal, ticket_medio

if __name__ == "__main__":
    import load_data
    data = load_data.load_all_data(load_data.file_paths)
    faturamento_mensal, ticket_medio = analyze_data(data)
    print(faturamento_mensal)
    print(f"Ticket Médio: {ticket_medio:.2f}")
