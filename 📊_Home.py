# bibliotecas necessárias
import pandas as pd
import numpy   as np 
import folium
import streamlit as st
from PIL import Image

# libraries
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

st.set_page_config(
    page_title="Main Home",
    page_icon="📊",
    layout="wide",
)
# -----------------------------------------------------
# Funções
#======================================================

def clean_code(df1):
    """ Está função tem a responsábilidade de limpar o dataframe
        
        Tipos de limpeza:
        1. Remoçao dos dados Nam.
        2. Removendo linhas duplicadas.
        3. Criando a coluna Index
        4. Convertendo objet/string e removendo da coluna "cuisines" os demais tipos de culinária
        5. Descartando coluna com 1 valor único em todas as linhas.
        6. Criando os nomes dos países 
        7. Criando a coluna do Tipo de Categoria de Comida 'Type of Food Category'
        8. Criando a coluna nomes das cores 'Name color'
        
        Imput: Dataframe
        Output: dataframe 
 
    """
    # 1. Remoçao dos dados Nan.
    df1 = df1[df1['Cuisines'].notnull()]
    
    linhas_selecionadas = df1['Restaurant ID'] != 18516213
    df1 = df1.loc[linhas_selecionadas, :]

    linhas_selecionadas = df1['Restaurant ID'] != 16547518
    df1 = df1.loc[linhas_selecionadas, :]    
    
    # 1.1 Apaga todos os Nan do dataframe
    #df1 = sort.drop()

    # 2. Removendo linhas duplicadas
    df1 = df1.drop_duplicates( keep ='first')

    # 3. Criando a coluna Index 
    df1 = df1.reset_index()
    df1 = df1.rename(columns={'index': 'ID'})

    # 4. Convertendo objet/string e removendo da coluna "cuisines" os demais tipos de culinária
    df1["Cuisines"] = df1.loc[:, "Cuisines"].astype(str).apply(lambda x: x.split(',')[0])
    
    # 6. Criando os nomes dos países    
    df1["Name country"] = df1["Country Code"].apply(lambda x:country_name(x))

    # 5. Descartando coluna com 1 valor único em todas as linhas-
    df1 = df1.drop(columns=['Switch to order menu'])

    # 7. Criando a coluna do Tipo de Categoria de Comida 'Type of Food Category'
    df1["Type of Food Category"] = df1["Price range"].apply(lambda x:create_price_tye(x))

    # 8. Criando a coluna nomes das cores 'Name color'
    df1["Name color"] = df1["Rating color"].apply(lambda x:color_name(x))
    return df1

# 6. Criando os nomes dos países
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
    """ Está função tem a responsábilidade contém todos os nomes dos países. """
    return COUNTRIES[country_id]

# 7. Criando a coluna do Tipo de Categoria de Comida 'Type of Food Category'
def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

# 8. Criando a coluna nomes das cores 'Name color'
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
    """ Está função tem a responsábilidade contém todos os nomes das cores. """
    return COLORS[color_code]


# 9. Função para renomear colunas'
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

def country_maps(df1):
    df_aux = df1.loc[:,['Name country','Restaurant ID','City','Restaurant Name','Average Cost for two','Currency','Name color','Cuisines','Locality','Aggregate rating','Latitude','Longitude']
                    ].reset_index()

    lat = list(df_aux["Latitude"])
    lon = list(df_aux["Longitude"])
    restaurante = list(df_aux["Restaurant Name"])
    price = list(df_aux["Average Cost for two"])
    cozinha = list(df_aux["Cuisines"])
    avaliac = list(df_aux["Aggregate rating"])
    moeda = list(df_aux["Currency"])
    namecolor = list(df_aux["Name color"])

    map = folium.Map( )
    marker_cluster = MarkerCluster(name="clustered name").add_to(map)
    for lt,ln,rt,prec,coz,avl,md,nc in zip(lat, lon, restaurante, price, cozinha, avaliac,moeda, namecolor):
        html = f'''
            <p>   {rt}<p/>
            <p>Price: {prec},00 {md} para dois<p/>
            <p> Type: {coz}<p/>
            <p> Aggregate Rating: {avl}/5.0<p/>
            '''    
        iframe = folium.IFrame(html=html, width=300, height=200)
        popup = folium.Popup(iframe, max_width=300)
        folium.Marker(location=[lt,ln],
        icon=folium.Icon(color=nc, icon='glyphicon-cutlery'),  
        popup=popup,zoom_start=1).add_to(marker_cluster)              
    folium_static( map, width=1024 , height=600)
    
#======================================================
# Início da Estrutura Lógica do código
# -----------------------------------------------------

# lendo o arquivo importado
#======================================================
# lendo o arquivo importado
df = pd.read_csv( 'dataset/zomato.csv' ) 
# -----------------------------------------------------

# Fazendo uma copia do Dataframe
#======================================================
df1 = df.copy()

# -----------------------------------------------------
# Limpando dados
#======================================================
df1 = clean_code(df)
df2 = df1.copy()
#======================================================
#barrra Lateral
#======================================================
#st.set_page_config(
#    page_title="Main Home",page_icon="📊",layout="wide",
#)
    
with st.sidebar.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        image_path = 'logo.png'
        image = Image.open( image_path )
        st.image( image, width= 40)
    with col2:
        st.markdown('## Fome Zero')
    with col3:
        st.header('')
        
st.sidebar.markdown('# Filtros')

country_options = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ['India','Australia','Brazil','Canada','Indonesia',
     'New Zeland','Philippines','Qatar','Singapure','South Africa',
     'Sri Lanka','Turkey','United Arab Emirates','England','United States of America',],
    
    default=['Brazil', 'England', 'Qatar', 'South Africa','Canada','Australia',
            ] )

st.sidebar.markdown('# Dados Tratados')

df2 = df1.copy()
def convert_df_to_csv(df2):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  return df2.to_csv().encode('utf-8')

st.sidebar.download_button(
  label="Download",
  data=convert_df_to_csv(df2),
  file_name='data.csv',
  mime='text/csv',
)

# Filtro de paises
linhas_selecionadas = df1['Name country'].isin(country_options)
df1 = df1.loc[linhas_selecionadas,:]

#======================================================
# Layout no Streamlit
#======================================================
st.header('🎯 Fome Zero!')

st.markdown('### O Melhor lugar para encontrar seu mais novo restaurante favorito!')

with st.container():    
    st.markdown('#### Temos as seguintes marcas dentro da nossa plataforma:')
    col1, col2, col3, col4, col5 = st.columns(5, gap='small')
    with col1:
        # Total únicos de restaurantes cadastrados.
        df_total_rest = len(df2['Restaurant ID'].unique())
        col1.metric('Restaurante cadatrado.', df_total_rest)

    with col2:
        # Total de Paises cadastrados.
        df_total_pais = len(df2['Country Code'].unique())
        col2.metric('Países Cadatrado.', df_total_pais)
            
    with col3:
        # Total de Cidades cadastradas.
        df_total_cid = len(df2['City'].unique())
        col3.metric('Total Cidades.', df_total_cid)
            
    with col4:
        # Total de avaliações Feitas na Plataforma.
        df_total_aval =df2['Votes'].sum()
        df_total_aval = f'{df_total_aval:_}'
        df_total_aval=df_total_aval.replace("_",".") 
        col4.metric('Avaliações na plataforma.', df_total_aval)

    with col5:
        # Tipos de cúlinarias oferecidos.
        df_tipo_cul = len(df2.loc[:,'Cuisines'].unique())
        col5.metric('Tipos de Culinárias.',df_tipo_cul)
            
 # Country Maps
st.markdown("#### Mapas Países e Restaurantes.")
fig = country_maps(df1)
