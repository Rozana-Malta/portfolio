import streamlit as st
import streamlit_antd_components as sac
from streamlit_pdf_viewer import pdf_viewer



def page():
    st.header("Portfólio da Zana Malta")
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(
            """
            <div style="text-align: justify;">
            <p style="font-size: 18px;"><strong>Olá!</strong> Seja bem-vindo(a) ao meu portfólio, que representa um pouco de tudo que eu 
            sei sobre <strong>Ciências e Análises de Dados</strong>.</p>
            <p style="font-size: 18px;">Nessa página, apresento resumidamente os projetos que compõem o meu <strong>portfólio</strong>. Em cada um deles segui
            uma linha de raciocínio que me permitiu explorar diferentes aspectos da análise de dados, desde a
            coleta e limpeza dos dados até painéis e relatórios e alguns também a implementação de modelos. Etapas
            que geralmente vivenciamos no mercado de trabalho.</p>
            <p style="font-size: 18px;">Dúvidas ou sugestões? Fique à vontade para entrar em contato.</p>
            <p style="font-size: 18px;">Se você é da área de dados eu espero esses trabalhos desenvolvidos contribua para o seus conhecimentos.</p>
            <p style="font-size: 18px;">Se você é de outra área, espero que esses trabalhos possam te inspirar a aprender mais sobre ciências e análise de dados.</p>
            <p style="font-size: 18px;">Se você é um recrutador, espero que esses trabalhos possam te ajudar a entender um pouco mais sobre o meu trabalho.</p>
        
            <p style="font-size: 18px;"><strong>Aproveite a visita!</strong></p>
        
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image("img/home.svg", use_column_width=True)

    st.divider()
    
    tabs = sac.tabs([
        sac.TabsItem(label='Análises de Dados'),
        sac.TabsItem(label='Previsões'),
        sac.TabsItem(label='Machine Learning'),
        sac.TabsItem(label='Deep Learning'),
        ], align='center', size='lg', variant='outline', use_container_width=True)

    if tabs == 'Análises de Dados':
        st.write("Análises de Dados")
        pdf_viewer("data/pdfs/case_ecommerce.pdf", height=700, width=1300, pages_vertical_spacing=7)
