import load_data
import analyze_data
import visualize_data

def main():
    data = load_data.load_all_data(load_data.file_paths)
    faturamento_mensal, ticket_medio = analyze_data.analyze_data(data)
    visualize_data.plot_faturamento_mensal(faturamento_mensal)
    print(f"Ticket Médio: {ticket_medio:.2f}")

if __name__ == "__main__":
    main()
