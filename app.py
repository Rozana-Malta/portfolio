import streamlit as st
import streamlit_antd_components as sac



st.set_page_config(
    page_title = "Portfólio | Zana Malta",
    page_icon = "📊",
    layout = "wide",
)

from views import resume
from views import projects


with st.sidebar:
    pagina_selecionada = sac.menu(
        [
            sac.MenuItem("Resumo", icon="body-text"),
            sac.MenuItem(
                "Projetos",
                icon="bar-chart",
                #children=[
                #    sac.MenuItem("Emplacamentos Setor", icon="chevron-right"),
                #    sac.MenuItem("Emplacamentos Região", icon="chevron-right"),
                #    sac.MenuItem("Investimentos", icon="chevron-right"),
                #],
            ),
        ],
    )

page_mapping = {
        "Resumo": resume.page,
        "Projetos": projects.page,
    }

page_mapping[pagina_selecionada]()



