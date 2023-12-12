import weasyprint


def generate_pdf(contract: str) -> str:
    """Gera um arquivo PDF a partir do layout HTML e CSS do documento.

    Args:
        contract: O contrato preenchido com os dados JSON.

    Returns:
        O arquivo PDF gerado.
    """

    # Renderizar o HTML

    html = Template(contract).render()

    # Gerar o PDF

    pdf = weasyprint.HTML(html).write_pdf()

    return pdf
