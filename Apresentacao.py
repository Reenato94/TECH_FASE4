import streamlit as st
import pandas as pd
from PIL import Image
import joblib
from prophet.plot import plot_plotly
import plotly.graph_objects as go

# Configurações iniciais
st.set_page_config(page_title="Petróleo Brent", page_icon=":book:", layout="wide")

# Função para mostrar o Propósito
def show_propósito():
    # Título principal
    st.markdown('<h1 style="text-align: center;">Análise e Previsão de Preços - Petróleo Brent</h1>', unsafe_allow_html=True)
    



    # Carregar e exibir a imagem centralizada
    imagem = "Home.jpg"
    try:
        img = Image.open(imagem)
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <img src="data:image/png;base64,{get_base64_string(imagem)}" style="max-width: 100%; height: auto;" alt="Home">
            </div>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

# Função auxiliar para converter imagem em Base64
import base64

def get_base64_string(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Chamar a função para exibir o conteúdo
show_propósito()

# Seções do conteúdo
st.header("📊 Introdução")

st.markdown("""
O petróleo, especialmente o Brent, é uma das commodities mais influentes no cenário econômico global. Sua cotação não reflete apenas o mercado de energia, mas também impacta setores como transporte e indústria, além de influenciar políticas econômicas de países ao redor do mundo. 

A sensibilidade do preço do petróleo às flutuações de oferta e demanda o torna um termômetro das dinâmicas geopolíticas e econômicas globais. Sua volatilidade é frequentemente impulsionada por eventos imprevistos, como crises financeiras, conflitos internacionais e pandemias, além de decisões políticas de grandes produtores e consumidores.

Dessa forma, a presente análise busca aprofundar a compreensão das oscilações no preço do petróleo Brent ao longo do tempo, destacando os eventos e fatores determinantes que explicam essas variações, e fornecendo uma base robusta para decisões que possam beneficiar tanto os setores envolvidos diretamente na comercialização de petróleo quanto os mercados financeiros que o acompanham.
""")

st.header("🧑‍💻Extração dos Dados")

st.markdown("""
A extração dos dados partiu do site do Instituto de Pesquisa Econômica Aplicada (IPEA).
""")

st.header("🔍Análise dos Dados")

st.markdown("""

Aqui estão alguns dos destaques:

•	**Máximo e Mínimo Preço:** O  maior preço já registrado, mas também o menor preço, destacando os momentos de extremos no mercado e proporcionando uma visão de como o preço do petróleo se comportou nos momentos mais voláteis.

•	**Preço Médio:** O preço médio oferece um panorama geral de como os preços evoluíram, revelando padrões, tendências e flutuações que podem passar despercebidos em uma análise mais superficial.

•	**Períodos de Maior e Menor Preço:** destaca as épocas de grande instabilidade e aquelas mais equilibradas. Isso trás uma compreensão mais dinâmica do mercado e dos fatores que influenciam esses preços.

Além dessas métricas de preço, o comportamento do mercado de petróleo, mostra **quatro momentos chave** que impactaram no preço do petróleo ao longo do período analisado, como entender as forças econômicas, geopolíticas e ambientais que moldaram o preço do petróleo. Confira: 
""")


st.write("") 

st.header("💡Insights")

st.subheader("✔︎ Guerra Israel-Hamas e seus Efeitos no Petróleo")

st.markdown("""
A eclosão da guerra entre Israel e Hamas, em 7 de outubro de 2023, teve um impacto imediato e significativo nos mercados globais de energia, refletido principalmente no preço do petróleo Brent. Este evento aumentou as tensões geopolíticas em uma região extremamente estratégica para o fornecimento de energia global: o Oriente Médio. Esta região não só abriga alguns dos maiores produtores de petróleo do mundo, como a Arábia Saudita, Irã e Iraque, mas também é responsável por rotas comerciais essenciais, como o Estreito de Ormuz, que conecta o Golfo Pérsico ao restante do mercado internacional de energia.

O Oriente Médio é um ponto nevrálgico para a produção e transporte de petróleo, sendo responsável por cerca de 30% da oferta global de petróleo e possuindo infraestrutura crítica, como oleodutos e portos. O Estreito de Ormuz, por exemplo, é responsável por aproximadamente 20% do petróleo transportado por via marítima no mundo. Qualquer sinal de instabilidade ou bloqueio nesta região pode gerar temores sobre uma interrupção no fornecimento de petróleo, o que imediatamente pressiona os preços para cima.

A guerra intensificou as incertezas sobre a produção e exportação de petróleo, uma vez que tanto Israel quanto países da região têm papéis estratégicos, direta ou indiretamente, no fornecimento energético mundial. Além disso, o aumento das tensões militares pode resultar em uma escalada de conflitos em outras áreas sensíveis, exacerbando a volatilidade dos preços do petróleo. Este cenário de incerteza gerou reações nos mercados financeiros, com investidores buscando segurança em ativos como o ouro e o dólar, e também afetou a confiança no preço do petróleo, levando a aumentos abruptos no valor do barril, conforme os mercados antecipavam possíveis rupturas no fornecimento.
""")

st.subheader("✔︎ Impactos do COVID-19 no Preço do Petróleo")

st.markdown("""
A **pandemia de COVID-19**, que se iniciou no final de 2019, teve um **impacto devastador** em todos os setores da economia global, com efeitos particularmente graves sobre o mercado de petróleo. À medida que os países adotaram **medidas rigorosas de contenção**, como **lockdowns** e restrições a viagens internacionais, a **demanda global por petróleo despencou**. A paralisação de atividades econômicas em grande escala, o fechamento de fábricas, a redução do transporte aéreo e a diminuição do consumo de combustíveis impulsionaram uma **queda histórica nos preços do petróleo Brent**.

Durante o primeiro semestre de 2020, o **excesso de oferta aliado à queda acentuada na demanda** resultou em uma pressão sem precedentes sobre os preços. Os estoques de petróleo se acumularam, enquanto a indústria enfrentava a difícil tarefa de ajustar a produção para conter o excesso. Em abril de 2020, o preço do petróleo Brent chegou a cair **abaixo de 20 dólares por barril**, um nível não visto em décadas. A situação foi ainda mais dramática quando os **preços dos contratos futuros de petróleo nos Estados Unidos**, no mercado WTI, chegaram a se tornar negativos.

Este período refletiu não apenas uma **crise de oferta e demanda**, mas também destacou a **vulnerabilidade do mercado de petróleo frente a choques globais**. A **recuperação dos preços**, embora gradual, só começou a ocorrer à medida que as **vacinas começaram a ser distribuídas** e as economias começaram a se reabrir, reanimando a demanda por energia e restabelecendo um equilíbrio mais sustentável no mercado de petróleo. O impacto da pandemia, portanto, não foi apenas uma crise temporária, mas também um **ponto de inflexão** que moldou os rumos futuros do mercado de energia.
""")


st.subheader("✔︎ Crise do Petróleo de 2014: O Colapso dos Preços")

st.markdown("""
Em **2014**, o preço do petróleo Brent passou por uma **queda acentuada** devido a uma combinação de fatores de oferta e demanda. O principal fator foi o **aumento da produção de petróleo de xisto nos Estados Unidos**, que expandiu significativamente a oferta global. Esse aumento de produção pressionou os preços para baixo, especialmente quando a **demanda global não acompanhou esse crescimento**. A **desaceleração econômica na Europa e na Ásia**, com menor consumo de energia, agravou ainda mais a situação, resultando em um **desequilíbrio entre oferta e demanda**.

Adicionalmente, a **Organização dos Países Exportadores de Petróleo (OPEP)** manteve sua produção em níveis elevados, ao invés de reduzir, o que **intensificou a queda nos preços**. A decisão da OPEP de não cortar a produção foi motivada por uma **estratégia de manter sua participação no mercado**, acreditando que os preços baixos eliminariam produtores mais caros, como os de petróleo de xisto, e fortaleceriam a posição do cartel a longo prazo.

O impacto dessa crise foi profundo, com os **preços do petróleo atingindo níveis historicamente baixos**. Para os países produtores, isso significou uma queda nas receitas e sérias dificuldades econômicas, enquanto para o mercado global, o episódio reforçou a **vulnerabilidade dos preços do petróleo a choques externos e à dinâmica de produção global**.
""")

st.subheader("✔︎ Crise Financeira de 2008 e a Queda do Preço do Petróleo")

st.markdown("""
Em **2008**, o mercado de petróleo experimentou uma das oscilações mais dramáticas de sua história recente. Durante o primeiro semestre daquele ano, os preços do petróleo Brent dispararam, atingindo um **pico histórico de 147,50 dólares por barril** em julho. Esse aumento foi impulsionado por uma **combinação de fatores**, como **tensões geopolíticas**, especialmente no Oriente Médio, e uma **forte demanda das economias emergentes**, particularmente da China e da Índia. Além disso, a **especulação no mercado financeiro** contribuiu para a elevação dos preços, alimentando uma bolha que logo se mostraria insustentável.

No entanto, a partir de **setembro de 2008**, o cenário mudou drasticamente. A **crise financeira global**, desencadeada pelo colapso de grandes instituições financeiras nos Estados Unidos e a falência do **Lehman Brothers**, um dos maiores bancos de investimento dos Estados Unidos, teve um efeito devastador sobre a economia mundial. A **instabilidade financeira** reduziu significativamente a confiança dos investidores e, mais importante ainda, diminuiu drasticamente a **demanda por petróleo**, à medida que a desaceleração econômica se espalhava globalmente. As economias desenvolvidas, que eram grandes consumidores de energia, entraram em recessão, e o consumo de petróleo caiu vertiginosamente.

Essa mudança abrupta na demanda foi refletida de forma drástica nos preços do petróleo. De julho a **dezembro de 2008**, o preço do barril de petróleo Brent caiu mais de **70%**, chegando a ser negociado a cerca de **39,35 dólares por barril**. Essa queda acentuada não apenas ilustrou a **vulnerabilidade do mercado de petróleo às crises econômicas globais**, mas também ressaltou a **sensibilidade do preço da commodity** às flutuações na demanda mundial. O episódio de 2008 se tornou um marco que demonstrou como a **instabilidade econômica pode desencadear uma rápida reversão no mercado de petróleo**, afetando a estabilidade dos preços e expondo as **interdependências entre o setor energético e a saúde econômica global**.
""")


st.header("Modelo de Previsão de Preço do Petróleo")

st.markdown("""
Séries temporais que apresentam padrões sazonais, tendências de crescimento e eventos de feriados ou datas especiais, o que o torna ideal para prever preços de commodities como o petróleo, que possuem variações sazonais e são fortemente impactados por fatores externos, como eventos econômicos, geopolíticos e climáticos.

Digite abaixo a quantidade de dias que deseja prever e veja o modelo em funcionamento, gerando as previsões para os períodos selecionados:
""")

model = joblib.load('prophet_model_final.pkl')

days = st.number_input("", min_value=1, max_value=365, value=7)

future_dates = model.make_future_dataframe(periods=days)

# Gerar previsão
forecast = model.predict(future_dates)

forecast['ds'] = forecast['ds'].dt.strftime('%Y-%m-%d')  # Formato: 'YYYY-MM-DD'
forecast['yhat'] = forecast['yhat'].round(2)  # Arredondar os valores de yhat para 2 casas decimais

st.write("Previsão do preço em US$ para os próximos {} dias:".format(days))
st.markdown("""
    <div style="display: flex; justify-content: center;">
        {}</div>
""".format(forecast[['ds', 'yhat']].tail(days).to_html(index=False)), unsafe_allow_html=True)


plot = plot_plotly(model, forecast)
st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
st.plotly_chart(plot)
st.markdown("</div>", unsafe_allow_html=True)

st.header("📝Conclusão")
st.markdown("""
A análise do preço do petróleo Brent ao longo das últimas décadas revela a **complexidade e a interdependência dos fatores** que influenciam o mercado global de energia. A **volatilidade do preço do petróleo**, como evidenciado pelos eventos chave examinados — a **crise financeira de 2008**, a **crise do petróleo de 2014**, os impactos da **pandemia de COVID-19** e a recente **guerra Israel-Hamas** — destaca a sensibilidade da commodity às mudanças geopolíticas, econômicas e de demanda. Cada um desses eventos teve um impacto profundo nas dinâmicas do mercado, moldando o comportamento do preço do petróleo de maneiras inesperadas e, muitas vezes, disruptivas.

A **extração e o tratamento dos dados históricos**, seguidos da criação de um **dashboard interativo no Power BI**, proporcionaram uma maneira eficaz de visualizar e entender essas flutuações de preços. Através de métricas como **preço máximo, mínimo, médio** e a identificação dos **períodos de maior volatilidade**, foi possível mapear as oscilações de preço ao longo do tempo, oferecendo uma base sólida para tomar decisões informadas, seja para investidores, analistas ou formuladores de políticas econômicas.

Além disso, a aplicação do modelo **Prophet para prever os preços futuros do petróleo** representa uma importante ferramenta para a análise de séries temporais, considerando a **complexidade dos padrões sazonais** e os eventos inesperados que influenciam esse mercado. Embora o modelo não elimine as incertezas, ele fornece uma visão útil das **tendências futuras**, oferecendo uma ajuda valiosa na formulação de estratégias no setor energético.

Em suma, a **dinâmica do mercado de petróleo é intrinsecamente volátil**, e a análise contínua de seus preços é crucial para entender e antecipar os efeitos de fatores econômicos e geopolíticos globais. A **combinação de dados históricos, análise interativa e modelos preditivos** abre novas possibilidades para quem busca acompanhar de perto este mercado, ajudando a mitigar riscos e a identificar oportunidades no complexo cenário econômico global.
""")


st.header("📚Referências Bibliográficas")

st.markdown("""

- CNN Brasil. (2024). *Petróleo Brent tem queda de quase 6% após ataque limitado de Israel contra o Irã*. CNN Brasil. Disponível em: [https://www.cnnbrasil.com.br/economia/macroeconomia/petroleo-brent-tem-queda-de-quase-6-apos-ataque-limitado-de-israel-contra-o-ira/](https://www.cnnbrasil.com.br/economia/macroeconomia/petroleo-brent-tem-queda-de-quase-6-apos-ataque-limitado-de-israel-contra-o-ira/)

- Poder360. (2024). *Preço do petróleo sobe 2% com tensões no Oriente Médio*. Disponível em: [https://www.poder360.com.br/economia/preco-do-petroleo-sobe-2-com-tensoes-no-oriente-medio/](https://www.poder360.com.br/economia/preco-do-petroleo-sobe-2-com-tensoes-no-oriente-medio/)

- Veja. (2024). *Petróleo dispara após ataque de Irã a Israel; Dólar e Ibovespa sobem*. Disponível em: [https://veja.abril.com.br/economia/petroleo-dispara-apos-ataque-de-ira-a-israel-dolar-e-ibovespa-sobem](https://veja.abril.com.br/economia/petroleo-dispara-apos-ataque-de-ira-a-israel-dolar-e-ibovespa-sobem)

- Poder360. (2024). *Possível guerra entre Irã e Israel deve fazer petróleo subir*. Disponível em: [https://www.poder360.com.br/economia/possivel-guerra-entre-ira-e-israel-deve-fazer-petroleo-subir/](https://www.poder360.com.br/economia/possivel-guerra-entre-ira-e-israel-deve-fazer-petroleo-subir/)

- CNN Brasil. (2024). *Como o mercado dos EUA e o petróleo devem reagir à guerra entre Israel e Hamas*. Disponível em: [https://www.cnnbrasil.com.br/internacional/como-o-mercado-dos-eua-e-o-petroleo-devem-reagir-a-guerra-entre-israel-e-hamas/](https://www.cnnbrasil.com.br/internacional/como-o-mercado-dos-eua-e-o-petroleo-devem-reagir-a-guerra-entre-israel-e-hamas/)

- CNN Brasil. (2020). *Preços do petróleo caem e Brent toca US$40 por estoques recorde por Covid-19*. Disponível em: [https://www.cnnbrasil.com.br/economia/macroeconomia/precos-do-petroleo-caem-e-brent-toca-us40-por-estoques-recorde-por-covid-19/](https://www.cnnbrasil.com.br/economia/macroeconomia/precos-do-petroleo-caem-e-brent-toca-us40-por-estoques-recorde-por-covid-19/)

- Brasil de Fato. (2020). *Pandemia da Covid-19 gera maior crise do mercado mundial de petróleo em 30 anos*. Disponível em: [https://www.brasildefato.com.br/2020/04/08/pandemia-da-covid-19-gera-maior-crise-do-mercado-mundial-de-petroleo-em-30-anos](https://www.brasildefato.com.br/2020/04/08/pandemia-da-covid-19-gera-maior-crise-do-mercado-mundial-de-petroleo-em-30-anos)

- Agência Brasil. (2020). *Coronavírus afeta variação nos preços do barril de petróleo no mundo*. Disponível em: [https://agenciabrasil.ebc.com.br/geral/noticia/2020-03/coronavirus-afeta-variacao-nos-precos-do-barril-de-petroleo-no-mundo](https://agenciabrasil.ebc.com.br/geral/noticia/2020-03/coronavirus-afeta-variacao-nos-precos-do-barril-de-petroleo-no-mundo)

- FPA Bramão. (2020). *As perspectivas para os mercados de commodities e os efeitos do coronavírus em seis gráficos*. Disponível em: [https://fpabramo.org.br/observabr/2020/05/14/as-perspectivas-para-os-mercados-de-commodities-e-os-efeitos-do-coronavirus-em-seis-graficos/](https://fpabramo.org.br/observabr/2020/05/14/as-perspectivas-para-os-mercados-de-commodities-e-os-efeitos-do-coronavirus-em-seis-graficos/)

- IELA. (2020). *Indústria do Petróleo: Fim da crise e emergência da Rússia*. Disponível em: [http://iela.ufsc.br/industria-do-petroleo-fim-da-crise-e-emergencia-da-russia/](http://iela.ufsc.br/industria-do-petroleo-fim-da-crise-e-emergencia-da-russia/)

- Exame. (2020). *Preços do petróleo se aproximam do fundo do poço de 2008*. Disponível em: [https://exame.com/economia/precos-do-petroleo-se-aproximam-do-fundo-do-poco-de-2008/](https://exame.com/economia/precos-do-petroleo-se-aproximam-do-fundo-do-poco-de-2008/)

- Streamlit. (2024). *Streamlit Docs*. Disponível em: [https://docs.streamlit.io/](https://docs.streamlit.io/)
            
- [Instituto de Pesquisa Econômica Aplicada (IPEA).](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view) - Dados Econômicos.
""")
