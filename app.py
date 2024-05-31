import streamlit as st
import streamlit_antd_components as sac

from views import home
from views import resume
from views import projects
from views import forecast
from views import machine_learning
from views import deep_learning
from views import ia
from views import analise_dados

st.set_page_config(
    page_title = "Portfólio | Zana Malta",
    page_icon = "🍊",
    layout = "wide",
)

with st.sidebar:
    pagina_selecionada = sac.menu(
        [
            sac.MenuItem("Início", icon="house"),
            sac.MenuItem("Resumo", icon="body-text"),
            sac.MenuItem(
                "Projetos",
                icon="bar-chart",
                children=[
                    sac.MenuItem("Análises de Dados", icon="chevron-right"),
                    #sac.MenuItem("Previsões", icon="chevron-right"),
                    #sac.MenuItem("Machine Learning", icon="chevron-right"),
                    #sac.MenuItem("Deep Learning", icon="chevron-right"),
                    #sac.MenuItem("IA", icon="chevron-right"),
                ],
            ),
        ],
    )

page_mapping = {
        "Início": home.page,
        "Resumo": resume.page,
        "Projetos": projects.page,
        "Análises de Dados": analise_dados.page,
        #"Previsões": forecast.page,
        #"Machine Learning": machine_learning.page,
        #"Deep Learning": deep_learning.page,
        #"IA": ia.page,
    }

page_mapping[pagina_selecionada]()



