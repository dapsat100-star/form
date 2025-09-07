# -*- coding: utf-8 -*-
import io, json, datetime as dt
from typing import List
from pathlib import Path

import streamlit as st
from pydantic import BaseModel, Field

class Autor(BaseModel):
    nome: str = ""
    cargo: str = ""
    email: str = ""

class Relatorio(BaseModel):
    titulo: str = "Relatório Técnico"
    cliente: str = ""
    projeto: str = ""
    codigo: str = ""
    data: str = dt.date.today().strftime("%Y-%m-%d")
    versao: str = "1.0"
    autores: List[Autor] = Field(default_factory=lambda: [Autor()])
    resumo_exec: str = ""
    escopo: str = ""
    metodologia: str = ""
    resultados: str = ""
    conclusoes: str = ""

def to_markdown(r: Relatorio) -> str:
    return f"""# {r.titulo}
**Cliente:** {r.cliente}  
**Projeto:** {r.projeto}  
**Código:** {r.codigo}  
**Data:** {r.data}  
**Versão:** {r.versao}

## Resumo Executivo
{r.resumo_exec}

## Escopo
{r.escopo}

## Metodologia
{r.metodologia}

## Resultados
{r.resultados}

## Conclusões
{r.conclusoes}
"""

st.set_page_config(page_title="Relatório Técnico", page_icon="📝", layout="wide")
st.title("📝 Formulário de Relatório Técnico")

if "rel" not in st.session_state:
    st.session_state.rel = Relatorio()

rel: Relatorio = st.session_state.rel

with st.form("form-relatorio"):
    rel.titulo = st.text_input("Título", value=rel.titulo)
    rel.cliente = st.text_input("Cliente", value=rel.cliente)
    rel.projeto = st.text_input("Projeto", value=rel.projeto)
    rel.codigo = st.text_input("Código", value=rel.codigo)
    rel.data = st.date_input("Data", value=dt.date.fromisoformat(rel.data)).isoformat()
    rel.versao = st.text_input("Versão", value=rel.versao)

    rel.resumo_exec = st.text_area("Resumo Executivo", value=rel.resumo_exec)
    rel.escopo = st.text_area("Escopo", value=rel.escopo)
    rel.metodologia = st.text_area("Metodologia", value=rel.metodologia)
    rel.resultados = st.text_area("Resultados", value=rel.resultados)
    rel.conclusoes = st.text_area("Conclusões", value=rel.conclusoes)

    submitted = st.form_submit_button("Atualizar prévia")
    if submitted:
        st.session_state.rel = rel

st.subheader("Prévia (Markdown)")
st.code(to_markdown(rel), language="markdown")
