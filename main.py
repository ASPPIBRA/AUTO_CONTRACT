import json
import datetime
import weasyprint
from jinja2 import Template


def convert_form_input_to_json(form_input):
    # Cria um dicionário para armazenar as informações do formulário
    data = {}

    # Percorre os campos do formulário
    for field in form_input:
        # Obtém o valor do campo
        value = form_input[field]

        # Valida o valor do campo
        if field == "start_date":
            try:
                datetime.datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"A data de início deve estar no formato YYYY-MM-DD.")
        elif field == "end_date":
            try:
                datetime.datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"A data de término deve estar no formato YYYY-MM-DD.")

        # Adiciona o campo e o valor ao dicionário
        data[field] = value

    # Converte o dicionário para um objeto JSON
    json_data = json.dumps(data)

    # Retorna o objeto JSON
    return json_data


# Função principal
def main():
    # Carregamento das informações do arquivo .json
    with open("dados/contrato.json", "r") as f:
        data = json.load(f)

    # Validação das informações do contrato
    validate_contract_data(data)

    # Geração do documento PDF
    document = generate_pdf(data)

    # Salvamento do documento PDF
    with open("documento.pdf", "wb") as f:
        f.write(document)


if __name__ == "__main__":
    main()


# Função de validação das informações do contrato
def validate_contract_data(data):
    # Verifica se a data de início é anterior à data de término
    if data["start_date"] > data["end_date"]:
        raise ValueError("A data de início deve ser anterior à data de término.")


# Função de geração do documento PDF
def generate_pdf(data):
    # Lê o conteúdo do arquivo HTML
    with open("templates/index.html", "r") as f:
        template = Template(f.read())

    # Renderiza o conteúdo do arquivo HTML usando a biblioteca Jinja2, substituindo os valores com as informações do contrato
    html = template.render(data=data)

    # Cria um documento WeasyPrint com o HTML renderizado e o arquivo CSS
    document = weasyprint.fromString(html, css="styles.css")

    # Preenche os campos do documento PDF com as informações do contrato
    document.fill_pdf("number", data["number"])
    document.fill_pdf("start_date", data["start_date"])
    document.fill_pdf("end_date", data["end_dates"])
    document.fill_pdf("member_obligations", data["member_obligations"])
    document.fill_pdf("association_obligations", data["association_obligations"])
    document.fill_pdf("termination_clause", data["termination_clause"])

    # Retorna o documento PDF renderizado
    return document.render()
