import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_faturamento_mensal(faturamento_mensal):
    # Verificar os tipos de dados
    print(faturamento_mensal.dtypes)
    
    sns.lineplot(data=faturamento_mensal, x='month', y='total')
    plt.xticks(rotation=45)
    plt.title('Faturamento Mensal')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import analyze_data
    import load_data
    data = load_data.load_all_data(load_data.file_paths)
    faturamento_mensal, ticket_medio = analyze_data.analyze_data(data)
    plot_faturamento_mensal(faturamento_mensal)
