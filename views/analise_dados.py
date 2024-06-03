import streamlit as st
import streamlit_antd_components as sac
from streamlit_pdf_viewer import pdf_viewer
from streamlit_extras.add_vertical_space import add_vertical_space


def page():
    st.header("Análise de Dados",  divider="rainbow")

    col1, col2 = st.columns([1.5, 1])
    col1.markdown(
        """
        <div style="text-align: justify;">
        <p>
        Nesta seção, apresento alguns <i>cases</i> de análise de dados que desenvolvi ao longo da minha carreira. 
        Esses projetos envolvem diversas etapas essenciais para a análise eficiente e precisa dos dados:

        **- Tratamento e Normalização de Dados:** Abordo a limpeza e preparação dos dados para garantir sua qualidade e consistência, eliminando valores discrepantes e corrigindo inconsistências.
        
        **- Análise Exploratória de Dados (EDA):** Utilizo técnicas de análise exploratória para entender melhor a estrutura e as características dos dados, identificando padrões, tendências e relações significativas.
        
        **- Criação de Visualizações:** Desenvolvo visualizações impactantes e informativas utilizando ferramentas como Tableau, Power BI e matplotlib, para comunicar insights de forma clara e eficiente.
        
        **- Interpretação dos Resultados:** Analiso os resultados obtidos para extrair conclusões acionáveis, fornecendo recomendações baseadas em dados para orientar a tomada de decisões estratégicas.
        
        Cada <i>case</i>/projeto inclui uma descrição detalhada do problema abordado, a metodologia aplicada, as ferramentas utilizadas e os resultados alcançados. Esses exemplos demonstram minha capacidade de transformar dados brutos em insights valiosos que podem impulsionar o sucesso organizacional.
        </p>
        </div>
        """, 
        unsafe_allow_html=True
        )
    
    col2.image("img/Data extraction-pana.svg", use_column_width=True)
            
    temas = st.selectbox(
        "**Selecione o _case_:**",
        [ 
         "Applying SQL to Solve Issues in E-commerce Databases [EN]",
         "The best solution to your digital product [EN]",
         "Plataforma de Performance [PT]"
        ]
    )
    st.divider()

    if temas == "Plataforma de Performance [PT]":

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
        <strong>Desenvolvimento da Solução</strong>
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
        </div>
        """,
        unsafe_allow_html=True
        )

        add_vertical_space(1)

        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.write("👇🏽 Storytelling")
            pdf_viewer("data/pdfs/case_performance.pdf", height=370, width=700)
        with col2:
            st.write("👇🏽 Desenvolvimento do case")
            pdf_viewer("data/pdfs/case_performance_desenv.pdf", height=400, width=700)

    elif temas == "Applying SQL to Solve Issues in E-commerce Databases [EN]":
            
            st.markdown(
            """
            <div style="text-align: justify;">
            <p style="font-size: 20px;">
            <strong>Applying SQL to Solve Issues in E-commerce Databases</strong>
            </p>
            </div>
            """,
            unsafe_allow_html=True
            )

            col1, col2 = st.columns([1.8,0.9], gap="small")
            with col1:
                st.markdown(
                """
                <div style="text-align: justify;">
                <p>
                Sales recovery refers to the strategy or tools that help complete sales for those who, for some reason, did not complete them. 
                It is a resource that should be applied to any online business. 
                
                This is because it allows you to rescue people who did not complete the purchase for different reasons: lack of limit on the card, balance in the account, objections to the purchase, among others.
                
                One of platform tools recovers sales when the customer does not have a sufﬁcient limit on their credit card.
                
                When an attempt to purchase in installments is denied due to insufﬁcient balance on the part of the Buyer, the tool transforms the transaction into a recurring one to prevent the sale from being lost.
                
                Thus, the buyer will receive monthly charges from the platform Payment System until the total purchase amount is paid.
                </p>
                </div>
                """,
                unsafe_allow_html=True
                )

            with col2:
                container = st.container(border=True)
                container.markdown(
                """
                <div style="text-align: justify;">
                <p>
                <strong>✨ Skills to demonstrate</strong>
                </p>
                <p>
                - SQL programming;
                </p>
                <p>
                - Scenarios' breakdown for problem solving;
                </p>
                <p>
                - Logical thinking for directive questions.
                </div>
                """,
                unsafe_allow_html=True
                )

            add_vertical_space(2)

            col1, col2 = st.columns(2, gap="medium")
            with col1:
                with st.expander("**🗃️ Database Schema**", expanded=True):
                    st.markdown(
                        """
                        <div style="text-align: justify;">
                        <p><strong>
                        The database is fictional and was created to simulate an e-commerce scenario, consisting of three tables. 
                        </strong></p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.image("img/db_platform_ecomm.png")

                with st.expander("**📝 Straight forward questions**", expanded=True):
                     st.markdown(
                        """
                        <div style="text-align: justify;">
                        <p>
                        1. The top 10 products that sold the most in each niche with deactivated membership area and activated recovery.
                        </p>
                        <p>
                        2. The top 10 producers who joined platform from 2020 onwards and achieved the highest sales using recovery.
                        </p>
                        <p>
                        3. How much more a producer with the recovery feature activated is likely to sell in each niche? Consider only producers who registered from 2020 onwards.
                        </p>
                        <p>
                        4. The product niche(s) with the highest number of cancellations and refunds.
                        </p>
                        <p>
                        5. Calculate the total money lost by producer due to cancellations and refunds. Is there any difference for producers considering products with the recovery tool activated?
                        </p>
                        <p>
                        6. If you need to create a ranking of the top creators of 2023, which variables you consider crucial for ranking them? You can also create variables from the data. You must explain your reasoning and your choice of variables and show how this reflect in your SQL code.
                        </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                        )

            with col2:
                st.markdown(
                """
                <div style="text-align: justify;">
                <p style="font-size: 20px;">
                <strong>🧐 Development of the technical case</strong>
                </p>
                </div>
                """,    
                unsafe_allow_html=True
                )
                pdf_viewer("data/pdfs/straight_forward_questions.pdf", height=800, width=700)

    elif temas == "The best solution to your digital product [EN]":
        st.markdown(
            """
            <div style="text-align: justify;">
            <p style="font-size: 20px;">
            <strong>The best solution to your digital product</strong>
            </p>
            </div>
            """,
            unsafe_allow_html=True
            )
        
        st.markdown(
            """
            <div style="text-align: justify;">
            <p>
            Not every platform has the scalability and reliability of some market leaders. To be one of the leaders in the commercialization of digital products, it is important to focus on embracing each buyer persona to help creators live their passions.

            The Creator economy has different agents ranging from the content producer or co-producer to the affiliate, the latter can be an important sales channel for the creator. Basically:
            - Producers are people who create digital products in
            platforms, such as language courses, cooking recipe e-books,
            audiobooks, software, among many other examples.
            - Co-producers can be seen in cases where there is
            interaction of those who create digital products with the help of
            specialists, agencies or other collaborators.
            - Affiliates are people who promote products from
            producers in exchange for a commission on the sale, which
            varies from product to product and from affiliate to
            affiliate.

            When there is a purchase made through an affiliate or the product has a co-producer, the producer shares part of this revenue (GMV) with these agents, paying them a commission for this.
            The digital product can have a different format (ebook, video,
            etc), niche (music, history, etc) or type (subscription - recurring - or one-time purchase). The same applies to payment method, which deals with how and when the customer pays.            
            </p>
            </div>
            """,
            unsafe_allow_html=True
            )
        
        st.markdown(
            """
            <div style="text-align: justify;">
            <p>
            In “Purchases.csv” you will find some fictitious data referring to the platform’s purchasing database. 
            There are more than 1.0 million purchase records. 
            Based on the available data, you are open to exploring what you believe is relevant. Below are some “guiding questions” that will be important for your assessment:
            </p>
            <p>
            1. What inconsistencies did you identify in the database? Like you
            overcome these interferences?
            </p>
            <p>
            2. What indicators do you believe are important to measure when we need to
            Do you understand the health of plataform's business?
            </p>
            <p>
            3. What were these indicators historically like?
            </p>
            <p>
            4. Where do you see opportunities to increase and improve?
            </p>
            <p>
            5. Which areas do you believe would be interested in this information and
            perceptions?
            </p>
            <p>
            6. What actions can these areas take based on this information and insights?
            </p>
            <p>
            7. How will you identify the success of these actions?
            </p>
            </div>
            """,
            unsafe_allow_html=True
            )
        
        st.markdown(
                """
                <div style="text-align: justify;">
                <p style="font-size: 20px;">
                <strong>Development of the business case</strong>
                </p>
                </div>
                """,    
                unsafe_allow_html=True
                )
        

        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.write("👇🏽 Storytelling")
            pdf_viewer("data/pdfs/case_ecommerce.pdf", height=370, width=700)
        with col2:
            st.write("👇🏽 Business Case")
            pdf_viewer("data/pdfs/business_case_en.pdf", height=400, width=700)
        

        

        





    