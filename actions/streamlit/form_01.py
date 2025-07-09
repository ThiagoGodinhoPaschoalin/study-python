import json
import streamlit as st

# Função para salvar os dados do formulário em um arquivo JSON
def save_to_json(form_data):
    with open('form_data.json', 'w') as json_file:
        json.dump(form_data, json_file, indent=4)
    st.success("Data saved to form_data.json")

# Função principal para criar a interface do formulário
def main():
    st.title("Formulário Dinâmico")

    # Campos principais
    name = st.text_input("Name")
    width = st.number_input("Question Width", min_value=0)
    height = st.number_input("Question Height", min_value=0)
    empty = st.number_input("Count Nonzero Empty", min_value=0)
    checked = st.number_input("Count Nonzero Checked", min_value=0)
    length = st.number_input("Coordinates Length", min_value=0)

    # Campos dinâmicos para options
    options = []
    num_options = st.number_input("Number of Options", min_value=1, step=1)
    for i in range(num_options):
        option_label = chr(65 + i)  # A, B, C, ...
        x = st.number_input(f"Option {option_label} X", key=f"{option_label}_x")
        y = st.number_input(f"Option {option_label} Y", key=f"{option_label}_y")
        options.append({option_label: {'x': x, 'y': y}})

    # Campos dinâmicos para columns
    columns = {}
    num_columns = st.number_input("Number of Columns", min_value=1, step=1)
    for i in range(1, num_columns + 1):
        questions = st.number_input(f"Column {i} Questions", key=f"col{i}_questions")
        x = st.number_input(f"Column {i} X", key=f"col{i}_x")
        y = st.number_input(f"Column {i} Y", key=f"col{i}_y")
        columns[str(i)] = {'questions': questions, 'x': x, 'y': y}

    # Botão para submeter o formulário
    if st.button("Submeter"):
        form_data = {
            'name': name,
            'question': {
                'width': width,
                'height': height,
                'count_nonzero': {
                    'empty': empty,
                    'checked': checked
                },
                'coordinates': {
                    'length': length,
                    'options': options
                }
            },
            'columns': columns
        }
        save_to_json(form_data)

if __name__ == "__main__":
    main()
