# AUTO_CONTRACT

## Automação de geração de contratos

Este projeto implementa um sistema automatizado para geração de contratos. O sistema funciona da seguinte forma:

    1. O usuário preenche um formulário HTML com as informações do contrato. (Sandro)
    2. Os dados do formulário são válidados e salvos no formato JSON em um banco de dados. (Daniel)
    3. O modelo do contrato é preenchido com as informações já validadas do banco de dados. (Daniel)
    4. O layout de impressão do contrato é exibido para o usuário. (Sandro ou Daniel)
    5. O usuário pode clicar em um botão para gerar um PDF do contrato. (Sandro ou Daniel)

/automacao-contrato
├── code
│   ├── contracts
│   │   ├── associado
│   │   │   └── associado.html
│   │   │   └── associado.css
│   │   ├── venda_carro
│   │   │   └── venda_carro.html
│   │   │   └── venda_carro.css
│   │   ├── venda_casa
│   │   │   └── venda_casa.html
│   │   │   └── venda_casa.css
│   │   └── venda_terreno
│   │       └── venda_terreno.html
│   │       └── venda_terreno.css
│   ├── forms
│   │   └── contract_form.py
│   └── services
│       ├── form_validation
│       │   └── convert_form_input_to_json.py
│       ├── fill_contract_template_with_json.py
│       ├── generate_pdf.py
│       └── show_contract.py
├── docs
│   ├── README.md
│   └── code_of_conduct.md
├── tests
│   ├── test_contract_form.py
│   └── test_contract_generation.py
└── assets
    ├── images
    │   ├── associado.jpg
    │   ├── venda_carro.png
    │   └── venda_casa.pdf
    
