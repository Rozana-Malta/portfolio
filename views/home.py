import streamlit as st
import streamlit_antd_components as sac
from streamlit_pdf_viewer import pdf_viewer



def page():
    st.header("Portfólio da Zana Malta", divider="rainbow")
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(
            """
            <div style="text-align: justify;">
            <p style="font-size: 18px;"><strong>Olá!</strong> Seja bem-vindo(a) ao meu portfólio, onde compartilho um pouco de tudo que eu 
            sei sobre <strong>Ciências e Análises de Dados</strong>.</p>
            <p style="font-size: 18px;">
            Com quase 3 anos de experiência na área, 
            tenho o prazer de apresentar meus projetos e cases desenvolvidos. 
            Cada projeto segue uma linha de raciocínio que me permitiu explorar
            diversos aspectos da análise de dados, desde a coleta e limpeza de 
            dados até a criação de painéis, relatórios e a implementação de 
            modelos. Essas são etapas comuns no mercado de trabalho, 
            e cada uma delas está refletida aqui.
            </p>
            <p style="font-size: 18px;"><strong>📧💬 Dúvidas ou sugestões?</strong> Fique à vontade para entrar em contato.</p>
            <p style="font-size: 18px;"><strong>📊📚 Se você é da área de dados</strong> eu espero esses trabalhos desenvolvidos contribua para o seus conhecimentos.</p>
            <p style="font-size: 18px;"><strong>🔍📈 Se você é de outra área</strong>, espero que esses trabalhos possam te inspirar a aprender mais sobre ciências e análise de dados.</p>
            <p style="font-size: 18px;"><strong>🤝💼 Se você é um recrutador</strong>, espero que esses trabalhos possam te ajudar a entender um pouco mais sobre o meu trabalho.</p>
        
            <p style="font-size: 18px;"><strong>Aproveite a visita!</strong></p>
        
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image("img/home.svg", use_column_width=True)

    st.divider()
    