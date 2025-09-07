# Relatório Técnico – Streamlit

App de formulário para gerar relatório técnico com exportação em **PDF**, **DOCX** e **Markdown**, e suporte a **LOGO**.

## Rodando localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy no Streamlit Community Cloud
1. Crie um repositório no GitHub com estes arquivos.
2. Acesse o Streamlit Community Cloud e clique em **New app**.
3. Selecione o repositório, branch e o caminho `app.py`.
4. (Opcional) Configure **secrets** se necessário (não é obrigatório neste app).

## Estrutura
```
.
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
    └── logo_sample.png
```

## Uso
- Faça upload do LOGO (PNG/JPG) na barra lateral e ajuste a largura (cm).
- Preencha o formulário e use os botões de **download** para exportar.
- Você pode salvar/recuperar rascunhos via **JSON**.

## Licença
MIT
