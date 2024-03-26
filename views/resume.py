import streamlit as st
import streamlit_antd_components as sac


def page():

    col1, col2 = st.columns([4, 1])

    with col1:
        st.header("Resumo", divider="rainbow")
    with col2:
        with open("data/Curriculo_Rozana_Martins.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Confira meu currículo!",
                    data=PDFbyte,
                    file_name="test.pdf",
                    mime='application/octet-stream',
                    use_container_width=True,
                    #type="primary"
                    )
        st.link_button("LinkedIN", "https://www.linkedin.com/in/rozanamalta/", use_container_width=True)


    col1, col2 = st.columns([2.5, 1])
    
    st.markdown(
        """
        <div style="text-align: justify;">
        <p><strong>Olá!</strong> Seja bem-vindo(a) ao meu portfólio, que representa um pouco de tudo que eu 
        sei sobre ciência/análise de dados.</p>
        <p>Tenho <strong>quase 3 anos</strong> de experiência na área, e antes de ingressar no campo de dados, 
        construí uma carreira como química, acumulando <strong>cerca de 6 anos</strong> de experiência como técnica 
        em química e pesquisadora.</p>
        <p>Mesmo durante meu tempo na química, estava envolvida na análise de dados. 
        Com muita curiosidade e vontade de crescer, comecei a aprender sobre análise de dados com <strong>Python</strong>, 
        o que se revelou um ponto de virada na minha carreira.</p>
        <p>Posteriormente, tive a oportunidade de iniciar o time de dados na <strong>ABLA One</strong>, tornando-me a 
        primeira funcionária da empresa na área de dados. Como você pode imaginar, assumir esse papel 
        exigiu que eu aprendesse todos os processos envolvidos na área de dados, desde a <strong>extração, preparo, 
        análise e implementação de modelos</strong> até o compartilhamento e ação. Sou responsável por todas essas etapas.</p>
        <p>Atualmente, sou uma <strong>Cientista de Dados Pleno</strong>, pronta para enfrentar novos desafios e 
        continuar aprendendo!</p>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div style="text-align: justify">
        Abaixo, você pode conferir minhas habilidades técnicas, certificações, 
        hobbies e interesses e dados de diversidade.
        </div>
        """,
        unsafe_allow_html=True
        )



    st.divider()
    
    st.markdown("**Experiências**")
    col1, col2 = st.columns(2)
    with col2:
        st.markdown("*Experiência acadêmica*")
        sac.buttons([
        sac.ButtonsItem(label='Bacharel em Química', icon='mortarboard'),
        ], index=None, align='start', radius='lg', gap='md', color='cyan', key='academia')
    with col1:
        st.markdown("*Experiência profissional*")
        sac.buttons([
        sac.ButtonsItem(label='ABLA One'),
        sac.ButtonsItem(label='MGgrafeno'),
        sac.ButtonsItem(label='Dativa JR'),
        sac.ButtonsItem(label='LEC-UFMG'),
        ], index=None, align='start', radius='lg', gap='md', color='cyan', key='profissional')


    st.divider()

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Habilidades Técnicas**")
        sac.buttons([
            sac.ButtonsItem(label='Python', icon='code-slash'),
            sac.ButtonsItem(label='SQL', icon='table'),
            sac.ButtonsItem(label='ETL', icon='gear'),
            sac.ButtonsItem(label='DataViz', icon='bar-chart-line'),
            sac.ButtonsItem(label='Machine Learning', icon='robot'),
            ], index=None, align='start', radius='lg', gap='md', color='cyan', key='habilidades')
    
    with col2:
        st.markdown("**Cursos e Certificações**")
        st.text(
            """
            - Certificado Profissional Google Data Analytics
            - Artificial Neural Network for Regression
            - Artificial Intelligence A-Z: Learn How To Build An AI
            - Deep Learning A-Z: Hands-On Artificial Neural Networks
            - Python for Machine Learning & Data Science Masterclass
            - Python for Time Series Data Analysis
            - 100 Days of Code: The Complete Python Pro BootCamp for2022
            """)

    st.divider()

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Hobbies e Interesses**")
        sac.buttons([
            sac.ButtonsItem(label='Andar de Bicicleta', icon='bicycle'),
            sac.ButtonsItem(label='Fazer trilhas até cachoeiras', icon='signpost-2-fill'),
            sac.ButtonsItem(label='Tocar pandeiro', icon='music-note'),
            sac.ButtonsItem(label='Jogar jogos de tabuleiro', icon='dice-3'),
            ], index=None, align='start', radius='lg', gap='md', color='cyan', key='hobbies')

    with col2:
        st.markdown("**Diversidade**")
        sac.buttons([
            sac.ButtonsItem(label='Mulher Cis', icon='gender-female'),
            sac.ButtonsItem(label='Parda', icon='palette'),
            sac.ButtonsItem(label='Heterossexual', icon='suit-heart'),
            ], index=None, align='start', radius='lg', gap='md', color='cyan', key='diversidade')

    st.divider()
