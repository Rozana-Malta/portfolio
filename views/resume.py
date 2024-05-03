import streamlit as st
import streamlit_antd_components as sac
import io
from importlib import resources

from PIL import Image

buffer = io.BytesIO()

def page():

    col1, col2 = st.columns([4, 1])

    with col1:
        st.header("Resumo", divider="rainbow")

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

    with col2:
        st.image("img/resume.svg", use_column_width=True)

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

    st.divider()
    
    st.markdown("**Experiências**")
    col1, col2 = st.columns(2)
    with col2:
        st.markdown("*Experiências acadêmicas*")
        sac.buttons([
        sac.ButtonsItem(label='Bacharel em Química - UFMG', icon='mortarboard'),
        sac.ButtonsItem(label='Técnico em Química - CEFET/MG', icon='mortarboard'),
        ], index=None, align='start', radius='lg', gap='md', color='cyan', key='academia')
    with col1:
        st.markdown("*Experiências profissionais*")
        b_experiencias = sac.buttons([
        sac.ButtonsItem(label='ABLA One'),
        sac.ButtonsItem(label='MGgrafeno'),
        sac.ButtonsItem(label='Dativa JR'),
        sac.ButtonsItem(label='LEC-UFMG'),
        ], align='start', radius='lg', gap='md', color='cyan', key='profissional')

        if b_experiencias == 'ABLA One':
            sac.tags([
                sac.Tag(label='Cientista de Dados Pleno', bordered=False),
            ], size='md', color='magenta')
            
            st.markdown(
                """
                <div style="text-align: justify">
                <p>Na <strong>ABLA One</strong>, sou responsável por todas as etapas do ciclo de vida dos dados, 
                desde a extração até a implementação de modelos. Também sou responsável 
                por garantir a qualidade dos dados e a confiabilidade dos modelos.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.caption("2 anos e 7 meses | Belo Horizonte e Região, Brasil")

        
        if b_experiencias == 'MGgrafeno':
            sac.tags([
                sac.Tag(label='Pesquisadora e Técnica em Química', bordered=False),
            ], size='md', color='magenta')

            st.markdown(
                """
                <div style="text-align: justify">
                <p>Na <strong>MGgrafeno</strong>, fui responsável por realizar análises químicas e físicas 
                de materiais de grafeno, bem como por desenvolver e otimizar métodos de análise.
                Foi aqui que desenvolvi um método de calibração multivariada
                utilizando as bibliotecas pandas, numpy e scikit-learn para tratamento e análise dos dados. 
                Como resultado, obtive um método capaz de quantificar dois compostos presentes na dispersão de grafeno simultaneamente a partir do espectro UV-vis.</p>
                </div>
                """,
                unsafe_allow_html=True
            )  
            st.caption("fev de 2017 - set de 2021 · 4 anos 8 meses | Belo Horizonte e Região, Brasil")
        
        if b_experiencias == 'Dativa JR':
            sac.tags([
                sac.Tag(label='Assessora da Gestão', bordered=False),
            ], size='md', color='magenta')
            
            st.markdown(
                """
                <div style="text-align: justify">
                <p>Na <strong>Dativa JR</strong>, como assessora da Gestão, 
                foquei em criar modelos de gestão mais eficientes para a equipe 
                de assessores da Dativa Jr. Além disso, trabalhei em estreita 
                colaboração com as Diretorias de Projetos, Recursos Humanos e 
                Jurídico-Financeiro para garantir o cumprimento dos OKRs 
                (Objectives and Key Results) estabelecidos pelos diretores de cada equipe.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption("jun de 2019 - dez de 2020 · 1 ano 7 meses | Belo Horizonte e Região, Brasil")

        if b_experiencias == 'LEC-UFMG':
            sac.tags([
                sac.Tag(label='Estágio - Técnico Química', bordered=False),
            ], size='md', color='magenta')

            st.markdown(
                """
                <div style="text-align: justify">
                <p>Na <strong>LEC-UFMG</strong>, fui responsável por realizar análises químicas e físicas 
                de combustíveis e biocombustíveis. 
                </div>
                """,
                unsafe_allow_html=True
            )  
            st.caption("jan de 2014 - nov de 2015 · 1 ano 11 meses | Belo Horizonte e Região, Brasil")

    st.divider()

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Habilidades Técnicas**")
        sac.buttons([
            sac.ButtonsItem(label='GIT', icon='git'),
            sac.ButtonsItem(label='Python', icon='code-slash'),
            sac.ButtonsItem(label='SQL', icon='table'),
            sac.ButtonsItem(label='Banco de Dados', icon='database'),
            sac.ButtonsItem(label='ETL', icon='gear'),
            sac.ButtonsItem(label='Estatística', icon='calculator'),
            sac.ButtonsItem(label='DataViz', icon='bar-chart-line'),
            sac.ButtonsItem(label='Microsoft Power BI', icon='earmark-bar-graph'),
            sac.ButtonsItem(label='Machine Learning', icon='robot'),
            sac.ButtonsItem(label='Deep Learning', icon='rocket-takeoff'),
            sac.ButtonsItem(label='Gestão', icon= 'person-lines-fill'),
            sac.ButtonsItem(label='Metologia Ágil', icon='kanban'),
            sac.ButtonsItem(label='Ingles Intermediário', icon='chat-dots'),
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
            sac.ButtonsItem(label='Fazer Trilhas / Ir em Cachoeiras', icon='signpost-2-fill'),
            sac.ButtonsItem(label='Tocar Pandeiro', icon='music-note'),
            sac.ButtonsItem(label='Dançar', icon='boombox'),
            sac.ButtonsItem(label='Jogos de Tabuleiro', icon='dice-3'),
            ], index=None, align='start', radius='lg', gap='md', color='cyan', key='hobbies')

    with col2:
        st.markdown("**Diversidade**")
        sac.buttons([
            sac.ButtonsItem(label='Mulher Cis', icon='gender-female'),
            sac.ButtonsItem(label='Parda', icon='palette'),
            sac.ButtonsItem(label='Heterossexual', icon='suit-heart'),
            ], index=None, align='start', radius='lg', gap='md', color='cyan', key='diversidade')

    st.divider()

    st.markdown("**O que posso dizer dos meu projetos?**")
    
    projetos = sac.buttons([
    sac.ButtonsItem(label='Projetos que me orgulho'),
    sac.ButtonsItem(label='Projetos que posso melhorar'),
    ], align='start', radius='lg', gap='md', color='cyan', key='projetos')

    if projetos == 'Projetos que me orgulho':     
        st.markdown(
            """
            <div style="text-align: justify">
            🚧 em desenvolvimento ...
            """,
            unsafe_allow_html=True
        )
    
    else:
        st.markdown(
            """
            <div style="text-align: justify">
            🚧 em desenvolvimento ...
            """,
            unsafe_allow_html=True
        ) 

    st.divider()

    st.markdown("**Características pessoais**")
        
    caracteristicas = sac.buttons([
    sac.ButtonsItem(label='Características que me considero boa'),
    sac.ButtonsItem(label='Características que preciso melhorar'),
    ], align='start', radius='lg', gap='md', color='cyan', key='caracteristicas')

    if caracteristicas == 'Características que me considero boa':     
        st.markdown(
            """
            <div style="text-align: justify">
            🚧 em desenvolvimento ...
            """,
            unsafe_allow_html=True
        )
    
    else:
        st.markdown(
            """
            <div style="text-align: justify">
            🚧 em desenvolvimento ...
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.markdown("**Feedbacks**")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="text-align: justify">
            <p><strong>Jéssica Del'Boccio</strong></p>
            <p>Eu e a Rozana trabalhamos juntas no LEC-UFMG e no MGgrafeno e, com base em vários anos de convívio, 
            digo com propriedade que a Rozana é uma profissional completa! Ela se destaca pelo comprometimento e 
            aprendizado rápido nas atividades que desempenha, sempre buscando conhecimento e melhorias nos processos. 
            A Rozana também é muito criativa, organizada, empática, dinâmica, proativa, preza pela comunicação clara, 
            tanto verbal como escrita, tem facilidade de trabalhar em equipe e discutir ideias. Foi um prazer trabalhar 
            ao lado dessa excelente profissional com quem aprendi tanto!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="text-align: justify">
            <p><strong>Isabela Cruz</strong></p>
            <p>Durante todo esse tempo você foi uma supervisora incrível, dedicada, compreensiva, 
            sensível e que soube me guiar em todos os momentos mas sempre me dando autonomia para aprender
            e tomar decisões sozinha também. Acho que caminhamos juntas em todo o processo e isso funcionou bastante. 
            Além disso, uma das coisas que mais admiro em você é que você faz acontecer, mesmo quando não domina todos 
            os aspectos da tarefa e isso me motivou de uma forma que você não tem ideia!</p>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.divider()
