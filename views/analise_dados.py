import streamlit as st
import streamlit_antd_components as sac
from streamlit_pdf_viewer import pdf_viewer
from streamlit_extras.add_vertical_space import add_vertical_space




def page():
    st.header("Análise de Dados",  divider="rainbow")

    st.write("Nesta seção, apresento alguns cases de análise de dados que desenvolvi ao longo da minha carreira.")
    add_vertical_space(10)
            
    temas = st.selectbox(
        "**Selecione o _case_:**",
        ["Plataforma de Performance", "E-commerce", "RH"]
    )
    st.divider()

    if temas == "Plataforma de Performance":

        st.markdown(
        """
        <div style="text-align: justify;">
        <p style="font-size: 24px;">
        <strong>Plataforma de <i>Performance</i></strong>
        </p>
        <p style="font-size: 18px;">
        Um dos nossos principais produtos de uma HRTech é o módulo de <i>Performance</i>, focado no desempenho dos colaboradores, 
        cujo acompanhamento se dá por meio do alcance das metas individuais estabelecidas para cada um. 
        Ao longo dos anos, percebeu-se que as empresas têm envolvido os colaboradores cada vez mais na etapa 
        de planejamento das metas. No entanto, os administradores têm notado que o processo atual de criação de metas 
        tem se mostrado extenso e complexo para os usuários finais.
        Para entender melhor essas dores, o time de produto realizou uma pesquisa com os clientes 
        e obteve as informações a seguir.

        <p style="font-size: 18px;">
        <strong>Complexidade do processo:</strong> a criação de metas envolve múltiplas etapas e critérios, tornando o processo demorado e difícil de 
        ser executado pelos usuários finais das empresas clientes.
        </p>
        <p style="font-size: 18px;">
        <strong>Sobrecarga dos administradores:</strong> devido à complexidade, a responsabilidade de cadastrar as metas recai sobre os administradores, 
        sobrecarregando-os e reduzindo sua eficiência.
        </p>
        <p style="font-size: 18px;">
        <strong>Incoerência das metas:</strong> quando os usuários finais tentam criar suas próprias metas, muitas vezes elas não são alinhadas com a estratégia 
        da empresa ou com as metas dos líderes, resultando em objetivos descoordenados e ineficazes.
        </p>
        <p style="font-size: 18px;">
        Esses desafios prejudicam tanto a usabilidade da plataforma quanto a efetividade do acompanhamento de performance dos colaboradores.
        </p>
        </div>
        """,
        unsafe_allow_html=True
        )

        add_vertical_space(1)

        st.markdown(
        """
        <div style="text-align: justify;">
        <p style="font-size: 22px;">
        <strong>Proposta de Solução por Zana Malta</strong>
        </p>
        <p style="font-size: 18px;">
        Entendendo que o processo complexo de criação de tarefas resulta em sobrecarga dos administradores e na 
        criação de metas incoerentes, fatores que comprometem tanto a usabilidade da plataforma quanto a eficácia no 
        acompanhamento de performance dos colaboradores, decidi sugerir o desenvolvimento de novas funcionalidade.
        </p>
        <p style="font-size: 18px;">
        Essa funcionalidade visa simplificar as ações dos colaboradores, evitando a sobrecarga dos administradores e 
        garantindo a coerência das metas, interrompendo assim o ciclo de problemas. A proposta de solução é baseada em 
        um <strong>assistente inteligente</strong>, <strong>templates de metas</strong> e <strong>validação de metas</strong>.
        </p>
        <p style="font-size: 18px;">
        Para entender melhor essa proposta, acesse o documento com <i>storytelling</i> abaixo.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )

        pdf_viewer("data/pdfs/case_performance.pdf", height=580, pages_vertical_spacing=7)

        col1, col2 = st.columns([1,1.5])
        with col1:
            st.markdown(
            """
            <div style="text-align: justify;">
            <p style="font-size: 20px;">
            <p style="font-size: 18px;">
            A solução apresentada no documento de <i>storytelling</i> acima é descrita 
            em mais detalhes no documento ao lado.
            </p>
            </div>
            """,
            unsafe_allow_html=True
            )

        with col2:
            pdf_viewer("data/pdfs/case_performance_desenv.pdf", height=580)


        add_vertical_space(15)

        opcoes_1 = st.radio(
            "Selecione a opção desejada:", ["Contexto", "Desenvolvimento da Solução", "Storytelling"], horizontal=True)
        add_vertical_space(1)

        if opcoes_1 == "Contexto":
            col1, col2 = st.columns([1.4,1])
            with col1:
                st.markdown(
                    """
                    <div style="text-align: justify;">
                    <p style="font-size: 18px;">
                    Para entender melhor essas dores, o time de produto realizou uma pesquisa com os clientes e obteve as seguintes informações:
                    <p style="font-size: 18px;">
                    <strong>Complexidade do processo:</strong> a criação de metas envolve múltiplas etapas e critérios, tornando o processo demorado e difícil de 
                    ser executado pelos usuários finais das empresas clientes.
                    </p>
                    <p style="font-size: 18px;">
                    <strong>Sobrecarga dos administradores:</strong> devido à complexidade, a responsabilidade de cadastrar as metas recai sobre os administradores, 
                    sobrecarregando-os e reduzindo sua eficiência.
                    </p>
                    <p style="font-size: 18px;">
                    <strong>Incoerência das metas:</strong> quando os usuários finais tentam criar suas próprias metas, muitas vezes elas não são alinhadas com a estratégia 
                    da empresa ou com as metas dos líderes, resultando em objetivos descoordenados e ineficazes.
                    </p>
                    <p style="font-size: 18px;">
                    Esses desafios prejudicam tanto a usabilidade da plataforma quanto a efetividade do acompanhamento de performance dos colaboradores.
                    </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                st.image("img/performance.png")

        if opcoes_1 == "Desenvolvimento da Solução":
            col1, col2 = st.columns([1,1.5])
            with col1:
                st.markdown(
                    """
                    <div style="text-align: justify;">
                    <p style="font-size: 18px;">
                    Para resolver esses problemas, o time de produto decidiu desenvolver uma nova funcionalidade na plataforma de Performance: 
                    o módulo de Criação de Metas. O objetivo desse módulo é permitir que os usuários finais criem suas próprias metas de forma 
                    rápida e intuitiva, alinhadas com a estratégia da empresa e com as metas dos líderes.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                pdf_viewer("data/pdfs/case_performance_desenv.pdf", height=500, pages_vertical_spacing=7)


        if opcoes_1 == "Storytelling":
            col1, col2 = st.columns([1, 1.5])
            with col1:
                st.markdown(
                    """
                    <div style="text-align: justify;">
                    <p style="font-size: 18px;">
                    Teste de Storytelling [...]
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                pdf_viewer("data/pdfs/case_performance.pdf", height=500, pages_vertical_spacing=7)
