import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import glob as glob
pd.options.display.max_columns = None


####################  RECOLLIDA DE DADES  #####################################


estructura = pd.read_csv('EURECAT_ACPC\Estructura de dades.txt', sep=";")
columnes = list(estructura['Museu'])
columnes.insert(0, 'Museu')
#data = pd.read_csv("Eurecat_2021/eurecat_mnactec_2021.txt",
 #                  sep='|', names=columnes, low_memory=False)
data = pd.concat([pd.read_csv(f, sep='|', names=columnes, low_memory=False)
                  for f in glob.glob("Eurecat_2021/*.txt")], ignore_index=True)
data2 = pd.concat([pd.read_csv(f, sep='|', names=columnes, low_memory=False)
                  for f in glob.glob("Eurecat_2022/*.txt")], ignore_index=True)
data = pd.concat([data, data2], ignore_index=True)
data['Data venda'] = pd.to_datetime(data['Data venda'], format='%Y-%m-%d %H:%M:%S.%f')
data['dia'] = data['Data venda'].dt.date
del data['Hora inici de la sessió']
del data['Hora final de la sessió']


catalunya = ["Barri Vell", "Barcelonès", "Gironès", "Garrotxa", "Selva",
             "Baix Empordà", "Alt Empordà", "Maresme", "Berguedà",
             "Alta Ribagorça", "Baix Llobregat", "Vila Roja", "Bages",
             "Sant Narcís", "Baix Ebre", "Tarragona ciutat", "Santa Eugència",
             "Baix Penedès", "Noguera", "Solsonès", "Osona", "Devesa - Güell",
             "Lleida ciutat", "Pla d’Estany", "Vallès Oriental", "Tarragonès",
             "Ripollès", "Alt Camp", "Anoia", "Cerdanya", "Baix Camp",
             "Montsià", "Eixample", "Fontajau", "Mas Catofa", "Segrià",
             "Garraf", "Montjuïc", "Garrigues", "Domeny - Taialà",
             "Vallès Occidental", "Alt Penedès", "Terra Alta",
             "Montilivi - La Creueta", "Priorat", "Sant Daniel", "Alt Urgell",
             "Pla d’Urgell", "Conca de Barberà", "Segarra", "Val d’Aran",
             "Pallars Sobirà", "Mercadal", "Can Gibert del Pla", "Urgell",
             "Pont Major", "Les Corts", "Sant Andreu", "Sarrià-Sant Gervasi",
             "Sant Martí", "Santa Coloma de Gramanet", "Ciutat Vella",
             "Gràcia", "Horta-Guinardo", "L'Hospitalet de Llobregat",
             "Badalona", "Sants-Montjuïc", "Nou Barris", "Sant Adrià de Besos",
             "Girona ciutat", "Ribera d’Ebre", "Pallars Jussà",
             "Resta Catalunya", "Resta Comarca", "Municipi", "Lleida Ciutat",
             "BCN Ciutat", "Grup Sant Daniel", "Olèrdola", "Ribera d'Ebre",
             "Pla d'Urgell", "Pla de l'Estany", "Moianès",
             "Tarragona Província", "Tarragona Ciutat", "Barcelona Província",
             "Girona Província", "Constantí", "Lleida província",
             "Girona Ciutat", "Altafulla", "Lleida Ciutat", "LLeida Provincia",
             "Sant Sebastià", "Girona provincia", "Tarragona provincia",
             "Barcelona ciutat", "Barcelona provincia", "Tarragona ciutat",
             "Barcelona Ciutat", "Girona Provincia", "PORTES OBERTES",
             "Tarragona Provincia", "Barcelona Provincia", "Lleida provincia",
             "LLeida Ciutat", "Tarragona ciutat ", "Terrassa", "Sabadell",
             "Rubí", "Sant Cugat del Vallès", "Badia del Vallès",
             "Cerdanyola del Vallès", "Barberà del Vallès", "Ripollet",
             "Carme - Vista Alegre", "Pla de Palau - Sant Pau", "Matadepera",
             "Sant Quirze del Vallès", "Sant Llorenç Savall", "Sentmenat",
             "Montcada i Reixac", "Castellar del Vallès", "Castellbisbal",
             "Palau-solità i Plegamans", "Santa Perpètua de Mogoda",
             "Rellinars", "Polinyà", "Sant Ponç","Palau Sa Costa - Avellaneda",
             "Gallifa", "Pedreres", "Campdorà - Les Gavarres", "Can Boada",
             "Sant Pere Nord", "Germans Sàbat", "Figuerola - Bonastruc",
             "Pedret", "Mas Ramada", "Pujada de la Torrassa",
             "Font de la Pólvora"]

comunitat = ['Madrid', 'Comunitat Valenciana', 'Castella - La Manxa',
             'Cantàbria ', 'Cantàbria', 'Múrcia', 'Andalusia', 'Aragó',
             'Astúries', 'País Basc', 'Extremadura', 'Canàries', 'Galícia',
             'Castella i Lleó', 'Navarra', 'Ceuta i Melilla', 'Illes Balears',
             'Resta Espanya', 'País Valencià', 'Comunitat de Madrid',
             'Castella-la Manxa', 'Regió de Múrcia']

ciutatsSpain = ['La Rioja', 'Albacete', 'Murcia', 'Alava', 'Lugo', 'Alicante',
                'Valencia', 'Zaragoza', 'Asturias', 'Castellón', 'Vizcaya',
                'Córdoba', 'Toledo', 'Ciudad Real', 'A Coruña', 'Huesca',
                'León', 'Zamora', 'Pontevedra', 'Sevilla', 'Guipuzcoa',
                'Guadalajara', 'Soria', 'Cantabria', 'Cuenca', 'Burgos',
                'Segovia', 'Baleares', 'Almeria', 'Teruel', 'Salamanca',
                'Cadiz', 'Sant Sebastià', 'Las Palmas', 'Palencia', 'Granada',
                'Avila', 'Valladolid', 'Málaga', 'Huelva', 'Cáceres', 'Ceuta',
                'Guipúzcoa', 'Lugo ', 'Melilla', 'Orense', 'Palència ',
                'Ciudad Real ', 'Badajoz', 'Jaen', 'Malaga', 'A.Coruña',
                'Santa Cruz de Tenerife', 'Ceuta ', 'Palencia ']

andalusia = ['Córdoba', 'Sevilla', 'Cadiz', 'Huelva', 'Málaga', 'Malaga',
             'Almeria', 'Granada', 'Almería', 'Jaen', 'Jaén', 'Cádiz',
             'Andalusia']
extremadura = ['Cáceres', 'Caceres', 'Badajoz', 'Mérida', 'Merida',
               'Extremadura']
castellaManxa = ['Castella - La Manxa', 'Castella-la Manxa', 'Albacete',
                 'Toledo', 'Guadalajara', 'Cuenca', 'Ciudad Real',
                 'Castella - la Manxa']
castellaLleo = ['León', 'Burgos', 'Segovia', 'Valladolid', 'Salamanca',
                'Zamora', 'Soria', 'Avila', 'Palencia', 'Palència', 'Àvila',
                'Ávila', 'Leon', 'Lleó', 'Castella i Lleó']
arago = ['Zaragoza', 'Saragossa', 'Teruel', 'Huesca', 'Terol', 'Òsca', 'Aragó']
galicia = ['Lugo', 'A Coruña', 'Pontevedra', 'Orense', 'A.Coruña', 'La Coruña',
           'Santiago de Compostela', 'Compostela', 'Santiago', 'Ourense',
           'Galícia', 'Galicia']
asturias = ['Asturias', 'Oviedo', 'Gijón', 'Astúries']
cantabria = ['Cantabria', 'Santander', 'Cantàbria']
paisBasc = ['Bilbao', 'Bilbo', 'Guipúzcoa', 'San Sebastian', 'San Sebastián',
            'Sant Sebastià', 'Alava', 'Álava', 'Vizcaya', 'Guipuzcoa',
            'Donostia', 'Vitoria', 'Vitoria-Gasteiz', 'Gasteiz', 'País Basc']
rioja = ['Logroño', 'La Rioja']
navarra = ['Pamplona', 'navarra', 'Navarra']
comunitatValenciana = ['País Valencià', 'Valencia', 'València', 'Alicante',
                       'Alacant', 'Castellon', 'Castellón', 'Castelló',
                       'Comunitat Valenciana']
murcia = ['Murcia', 'Múrcia', 'Cartagena', 'Regió de Múrcia']
balears = ['Ibiza', 'Palma', 'Menorca', 'Mallorca', 'Eivissa', 'Illes Balears']
canaries = ['Santa Cruz de Tenerife', 'La Palma', 'Lanzarote', 'Gran Canaria',
            'Illes Canàries', 'Canàries']
ceutaMelilla = ['Ceuta', 'Melilla', 'Ceura i Melilla']
madrid = ['Madrid', 'Comunitat de Madrid']

paisos = catalunya + comunitat + ciutatsSpain

francia = ['Pirynées-Oriental', 'Bouches du Rhone', 'Aude', 'Ariege',
           'Haute-Garonne', 'Hèrault', '*Resta de França']


###############################################################################


st.set_page_config(layout="wide")
st.write("""

# MOTOR DE RESERVES

""")

#####################  PREPARACIÓ FILTRES  ####################################


st.sidebar.header('FILTRES')
first_date = pd.to_datetime(datetime.date(2021, 1, 1))
last_date = pd.to_datetime(datetime.date(2021, 12, 31))
data_inici = st.sidebar.date_input("DATA D'INICI", first_date)
data_fi = st.sidebar.date_input("DATA DE FI", last_date)
llista_museus = data['Museu'].unique().tolist()
llista_museus.insert(0, 'TOTS')
museus = st.sidebar.selectbox("ESCULL MUSEU", llista_museus)

data_inici = pd.to_datetime(data_inici)
data_fi = pd.to_datetime(data_fi)
data = data[((data['Data venda'] >= data_inici) &
                 (data['Data venda'] <= data_fi))]
if museus != 'TOTS':
    data = data[data['Museu'] == museus]


###############################################################################

fig_title = "VENDES DIÀRIES"
temp = data.groupby(['dia'], sort=False, as_index=False). \
    agg({'Unitats': 'sum'})
temp = temp.sort_values('dia')
temp.columns = ['data', 'total']
fig = go.Figure([go.Scatter(x=temp['data'], y=temp.total)])
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)
fig.update_xaxes(rangeslider_visible=True)
st.write(fig)

###############################################################################

if museus != 'TOTS':
    fig_title = "VENDES PER VISITA"
    temp = data.groupby(["Descripció de l'activitat o article"], sort=False,
                        as_index=False).agg({'Unitats': 'sum'})
    temp.columns = ['activitat', 'total']
    temp.sort_values(by=['total'], inplace=True, ascending=False)
    fig = px.bar(temp[0:15], x='activitat', y='total')
    fig.update_layout(
        title=dict(text=fig_title, font=dict(family='Arial', size=30,
                                             color='#000000')),
        yaxis_zeroline=False, xaxis_zeroline=False)
    fig.update_layout(
        autosize=False,
        width=1350,
        height=700)
    fig.update_traces(marker_color='darksalmon')
    st.write(fig)

###############################################################################


fig_title = "VENDES PER FRANJA HORÀRIA"
data['hour'] = data['Data venda'].dt.hour
temp = data.groupby(['hour'], sort=False, as_index=False). \
    agg({'Unitats': 'sum'})
temp.columns = ['hora', 'total']
temp.sort_values(by=['hora'], inplace=True)
fig = go.Figure(go.Scatter(x=temp['hora'], y=temp['total'],
                           mode='lines+markers'))
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)
st.write(fig)


###############################################################################


def in_spain(s):
    if s in paisos:
        return 'Espanya'
    else:
        return s


def in_france(s):
    if s in francia:
        return 'França'
    else:
        return s


fig_title = "VENDES PER NACIONALITAT"
data['Descripció zona estadística'] = data['Descripció zona estadística'].\
                                        apply(in_france)
data['nacionalitat'] = data['Descripció zona estadística'].apply(in_spain)
temp = data[~data['nacionalitat'].isnull()]
temp = temp.groupby(['nacionalitat'], sort=False, as_index=False).\
    agg({'Unitats': 'sum'})
temp.columns = ['zona', 'total']
temp = temp.sort_values(['total'], ascending=False)
top15_paisos = temp['zona'][0:16].to_list()
fig = px.bar(temp[1:16], x='zona', y='total')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)
fig.update_traces(marker_color='darksalmon')
fig.add_annotation(x=10, y=10,
            text='Dada de referència total espanya: '
                 +str(temp[0:1]['total'].values),
            showarrow=False,
            yshift=400, font=dict(size=20))

st.write(fig)


###############################################################################
if mixed_dtypes:=  {c: dtype for c in data.columns if (dtype:= pd.api.types.
        infer_dtype(data[c])).startswith("mixed")}:
    raise TypeError(f"Dataframe has one more mixed dtypes: {mixed_dtypes}")

def distribucioComunitats(s):
    if s in catalunya:
        return 'Catalunya'
    elif s in arago:
        return 'Aragó'
    elif s in madrid:
        return 'Comunitat de Madrid'
    elif s in cantabria:
        return 'Cantàbria'
    elif s in asturias:
        return 'Astúries'
    elif s in castellaLleo:
        return 'Castella i Lleó'
    elif s in castellaManxa:
        return 'Castella - la Manxa'
    elif s in paisBasc:
        return 'País Basc'
    elif s in navarra:
        return 'Navarra'
    elif s in rioja:
        return 'La Rioja'
    elif s in murcia:
        return 'Regió de Múrcia'
    elif s in extremadura:
        return 'Extremadura'
    elif s in andalusia:
        return 'Andalusia'
    elif s in ceutaMelilla:
        return 'Ceuta i Melilla'
    elif s in balears:
        return 'Illes Balears'
    elif s in canaries:
        return 'Illes Canàries'
    else:
        return 'NO'


fig_title = "VENDES PER COMUNITAT AUTÒNOMA"
data['comunitat'] = data['Descripció zona estadística'].\
                        apply(distribucioComunitats)
temp = data[data['comunitat'] != 'NO']
temp = temp.groupby(['comunitat'], sort=False, as_index=False). \
    agg({'Unitats': 'sum'})
temp.columns = ['comunitat', 'total']
temp = temp.sort_values(['total'], ascending=False)
fig = px.bar(temp[1:], x='comunitat', y='total')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)
fig.update_traces(marker_color='olive')
fig.add_annotation(x=10, y=10,
            text='Dada de referència total Catalunya: '
                 +str(temp[0:1]['total'].values),
            showarrow=False,
            yshift=400, font=dict(size=20))


st.write(fig)


###############################################################################

general = ['Adults', 'General', 'Sencera', 'Normal', 'Adults ',
           'General_Segarrulls',"Ti-web Gi-Ep General"]
acpc = ["ACPC Girona Epis. Bescanvi Ind", "ACPC I.Sencera",
        "ACPC I.Majors 65 anys", "ACPC I.Usuaris", "ACPC I. Estudiants",
        "ACPC Girona Epis. General", "ACPC I. Menors 16 anys",
        "ACPC I.Professorat reglat", "ACPC Girona Epis. Reduïda",
        "ACPC I.Amics del museu d'Art", "ACPC I.Pensionistes",
        "ACPC I.Discapacitat certificat", "ACPC Activitat Agenda 10 €",
        "ACPC I.Rec. Museu Arqueologia", "ACPC I.Gratuïta (varis)",
        "ACPC I. Red. Carnet Jove", "ACPC I.Activitats Agenda Grat",
        "ACPC Família nom/monop Especia", "ACPC I.Rec. Museu Història",
        "ACPC I.Rec. Museu Jueus", "ACPC I.Discapacitat Acompanyan",
        "ACPC Activitat Agenda 6 €", "ACPC I.Aturats", "ACPC I.ICOM i ICOMOS",
        "ACPC Girona Epis. Reduïda Esp.", "ACPC I. promoció 2X1 MuseuArt",
        "ACPC Sta Caterina Sencera", "ACPC I.Activitat Agenda Sencer",
        "ACPC I. Acompanyant Menor", "ACPC Sta Caterina I.Reduïda",
        "ACPC Girona Epis.Bescanvi Grup", "ACPC Grup Acompanyant",
        "ACPC I.Rec. Museu Cinema", "ACPC I. Conveni Salut/ICS",
        "ACPC Girona Epis.Menors 8 anys", "ACPC I.Carnet Cult Girona",
        "ACPC I.Dia portes obertes", "ACPC I.Activitat Agenda Reduïd",
        "ACPC Grup estud.7 altres", "ACPC I.Rec. Casa Masó", "ACPC I.Protocol",
        "ACPC I.Guies turístics", "ACPC Activitats agenda 4€",
        "ACPC Grup Activ Educ Sencera", "ACPC Sta Caterina + Museu Sen",
        "ACPC Grup Amics MDA", "ACPC I.Associació museòlegs",
        "ACPC Grup No turístic", "ACPC Grup estud.1 infantil",
        "ACPC Grup mdA Guiat", "Carnet ACdPC" "ACPC Gi-Ep Bescanvi Ind",
        "ACPC INDIKA(activitat educati)", "ACPC Gi-Ep General",
        "ACPC. Grup Act. Escoles Desfav", "ACPC Gi-Ep Reduïda",
        "ACPC Grup estud.6 universitat", "ACPC Grup estud.2 primària",
        "ACPC Grup No Turístic 4 €", "ACPC Grup Gratuïta (varis)",
        "ACPC Sta Caterina Grup NT", "ACPC Familiar acompanyant",
        "ACPC Gi-Ep Reduïda Especial", "ACPC Gi-Ep Menors 8 anys",
        "ACPC Grup estudiants", "ACPC I.Família Acollid/Ado Esp",
        "ACPC Grup estud.4 batxillerat", "ACPC Grup estud.5 cic.formatiu",
        "ACPC I.Rec. Oficina Turisme", "ACPC Gi-Ep Bescanvi Ind",
        "Carnet ACdPC", "ACPC Grup estud.3 eso", "ACPC Activitat Per molts anys",
        "ACPC I.Congressos"]
reduida_grups = ["Professors", "Certificat de discapacitat", "Docents",
           "Carnet F. Nombr./Monop.", "Carnet Biblioteques", "Discapacitats",
           "Biblioteques 20%", "Fam. nombrosa/monoparental",
           "Certificat discapacitat", "Tarifa conjunta centres MNAT",
           "Familia Nombrosa/Monoparental", "Tarifa nocturna estiu",
           "1r. diumenge de mes. 25-65", "Grups ", "Grups estudiants",
           "Familia nombrosa", "Reduïda Fam nomb i monop",
           "Membres ICOM o ICOMOS", "ICOM", "Membres ICOM i ICOMOS",
           "Reduïda pensionista", "CARNET CULTURAL",
           "1r. diumenge de mes 17-25 anys", "1r. diumenge de mes. +65",
           "1r. diumenge de menor 16 anys", "Famlies monoparentals", "TR3SC",
           "Tr3sC", "Grups", "Escoles Alta Complexitat", "Reduïda_Segarrulls",
           "25% dte SOM Museu Historia Cat", "Reduïda grup+10p TEMPORAL",
           "Diari ARA 2x1", "Famílies Acollida", "RED GRUP NO TURÍSTIC",
           "FAMILIES D'ACOLLIDA", "Grup CONCERTAT Tarf Reduc",
           "Grups turístics", "Grup no turístic 10 o més",
           "Reduïda grup no turístic =+10p", "Grups Escolars",
           "Reduïda families adults + nens", "Reduïda 65 anys o més",
           "Reduïda Grups escolars >16", "Grup Escolar Preu antic",
           "Reduïda joves de 16 a 24 anys", "Reduïda Esp. Família nombrosa",
           "Reduïda Grup no Turístic", "Reduïda Grup+10 o més persones",
           "Reduïda PRO Cinema a la fresca", "Reduïda Esp. Família monoparen",
           "Grup Turístic amb conveni AjT", "Reduïda grup +10",
           "Reduïda Grup Aj. Terrassa", "Promo XATIC 2x1/pers",
           "Reduïda Grup reduït >65 anys ", "de 5 a 18 anys",
           "Promo TR3SC 2x1/pers", "Reduïda estudiant carnet inter",
           "Passi Gaudeix del Patrimoni", "Famílies acollida acreditades",
           "Bat a Bat IND Reduïda", "BCN Card Express 20%",
           "Bat a Bat MULTI Reduïda", "Bat a Bat MULTI FAM NOMBROSA",
           "Entrada reduïda MNACTEC COL SEDÓ", "Bat a Bat MULTI Normal",
           "Bat a Bat IND Normal", "Athlètic Hoquei+mNACTEC", 
           "Grups Promo Menja't Montjuïc", "Visita guiada Caius i Faustina",
           "Ti-web Gi-Ep Reduïda", "Grups estud. amb professor"]
menors_students_carnetJove = ['Reduïda Carnets estudiant Int.', 'Carnet Jove',
                               'Persones menors de 16 anys',
                              'Red. carnet estudiant', 'Reduïda Carnet Jove',
                              'UNIVERSITARIS INDIVIDUALS', 'ESTUDIANT',
                              'Carnet estudiant internacional',
                              'Carnet jove 2x1', 'Nens ( de 5 a 16 anys)',
                              'Red.Carnet Estudiant Internaci',
                              'Estudiants Carnet Internaciona', 'Grup Escolar',
                              'CARNET JOVE', 'Menor de 8 anys',
                              'Carnet Jove 2x1', 'Menors de 5 anys',
                              "Infants de 4 a 12 anys", 'Menors de 16 anys',
                              "Pack Jove (estalvi 4,5€)", "CARNET JOVE 2x1",
                              "5 a 16 anys", "Redu Estudiant carnet internac",
                              "Gratuïta Carnet Jove 2x1", "Menors de 3 anys",
                              "Club super3", "PROMO Espai EXPLORA 0-6", 
                              "Menors de 6 anys"]
jubilats_aturats = ['65 anys o més', 'Majors de 65 anys', 'Reduïda +65',
                    'Reduïda Pensionistes', 'Reduides majors 65 anys',
                    'Aturats', 'Pensionistes', 'Red. Pensionistes',
                    'Reduïda 65 o +', "Reduïda pensionistes", 
                    "Grup 65 anys o més"]
altres = ["Altre Museu ", "Altre Museu", "Webs turistiques", "GironaMuseus",
          "BCN CARD 20%", "Guies Turístics", "MACTiquet", "Guíes Turístics",
          "Itinerari", "GIRONA MONÀSTICA", "PUNT DE BENVINGUDA",
          "Tarifa conjunta MNAT", "Agències", "BCN Card",
          "Professionals de premsa", "Recepció Macticket", "Port Aventura",
          "PROMOCIÓ MACTIKET", "Targeta Rosa", "Carnet Cultural l'Escala",
          "VISITA TEATRALITZADA", "Activitat familiar",
          "Tarifa Conjunta centres MNAT", "Recepció MAC Ticket",
          "Associació museòlegs", "Membres AMC", "De Bat a Bat IND Normal",
          "Tarifa Conjunta MNAT", "CARNET CULTURAL VG",
          "Guiatge entre setmana", "PREMSA", "ARTICLE",
          "De Bat a Bat IND Reduïda", "OMNIUM CULTURAL",
          "De Bat a Bat MULTI Reduïda", "Passi Patrimoni", "Museus Agraïts ",
          "INDIKA", "Arqueoticket", "Ruta urbana", "PASSI PATRIMONI",
          "De Bat a Bat MULTI Fam Nombros", "USUARIS BIBLIOTECA ",
          "AQVA INDIVIDUAL", "Activ + Degustació", "Premsa",
          "JORNADES EUROPEES ARQUEOLOGIA", "Casal d'estiu", "Quadern Cultura",
          "Anul.lació visita/taller", "GEIEG", "De Bat a Bat MULTI Normal",
          "FIRA MODERNISTA", "Activitats Cap de setmana","LA NIT DELS MUSEUS",
          "Jornades Europees Patrimoni", "Dia Internacional Museus",
          "Trobada Catbrick LEGO®", "Trobada HISPABRICK LEGO®",
          "Cinema a la fresca", "DIA INTERNACIONAL DELS MUSEUS",
          "JORNADES EUROPEES PATRIMONI", "Guiatge Caps de setmana",
          "Promo La Vanguardia 2x1 ", "Promo Diari ARA 2X1 fins 31.12",
          "SIMBOLS COMPARTITS", "VISITA HERÀLDICA", "ITINERARI SEPULTURES",
          "ACTV CAP SETMANA IBÈRIC", "LLUMS CROMÀTIQUES",
          "VISITA GENERAL ESCOLARS", "FGC Tiquet combinat ",
          "TALLERS DE NADAL A 3 €", "Parelles Linguístiques",
          "Desplaçament MNACTEC-ESCOLES", "AMICS DEL MUSEU D'ART",
          "SOCIETAT CATALANA ARQUEOLOGIA", "RSAT", "TALLERS DE NADAL A 2 €",
          "Serradora d'Àreu", "FIRATOCS", "Visita Exprés Promoció", 
          "Itinerari diumenges", "Temporal 2x1", "Anul.lació visites romanes",
          "Seminari Arqueol. Experimental", "Red. Carnet familiar",
          "Ti-web Gi-Ep Especial"]
acompanyants = ['Acompanyants', 'Acompanyants Grups', 'Acomp. Grups',
                'Acompanyant Discapacitat', 'Gratuïta Acompanyant Discapaci',
                'Gratuïta Acompanyant', 'ACOMPANYANTS',
                'Acomp. certificat discapacitat',
                "Gratuït Acomp Grups/NO escolar"]
gratuita = ['Gratuïta -16', 'Jornada Portes Obertes', 'Gratuïta professors',
            'Gratuïta Activitat', 'Gratuïta Activitats', 'Gratuïta aturat',
            'Gratuïta discapacitat', 'Diumenge gratuït', 'Gratuitat Protocol',
            'Gratuita persones Aturades', 'Entra gratuït paga activitat ',
            'Grups estudiants gratuïta', 'Gratuïta grup estudiant',
            'Gratuïta Professors', 'De Bat a Bat GRATUÏTA Visitant',
            'Gratuïta ', 'Gratuïta Invitacions', 'Gratuïta Discapacitats',
            'Gratuïta Aturats', 'Gratuïtat protocol', 'Director gratuitat',
            'Gratuïta guies turístics', 'Gratuïta ICOM/ICOMOS', 'Gratuïta SCA',
            'Gratuita Activitat', 'Gratuïta PREMSA', 'Premsa acreditat',
            'Gratuïta Associació Museòlegs', 'VISITA GUIADA GRATUÏTA',
            'Gratuïta -3 anys', 'Gratuïta_Segarrulls', 'Gratuïta online',
            'Gratuïta ICOM i ICOMOS', 'Gratuïta Guies Turístics',
            'Gratuïta SOM MuseuHistoriaCata', "Gratuita grup Universitat",
            "Gratuïta Membres AMC", "Gratuïta Quadern de Cultura",
            "Activitat gratuïta ", "Invitació Romans al S. XXI",
            "GRATUITA CONCERTS ESPECT", "Grups escolars entrada gratuït",
            "Gratis Primer diumenge de mes", "Gratis Acompanyants Grups Esc.",
            "Gratis Jornada Portes Obertes", "Gratuïta menors de 16 anys",
            "Gratuïta Activitat - Adult", "Gratuïta Activitat/Individual",
            "Gratuïta grup/no escolar", "Gratuïta Patge Xiu-Xiu",
            "Gratuïta Covid DIUMENGE", "Gratuïta Portes Obertes",
            "Gratuïta personal docent Cat.", "Gratis Certificat discapacitat",
            "Gratuïta COVID Dissabte Desemb", "Portes obertes Festa Major Ter",
            "Gratuïta aturats/des", "Gratis Actes Interns Cessió es",
            "Gratis Actes Externs Lloguer e", "Gratis Grup Certi Discapacitat",
            "Gratuïta Nit dels Museus", "Gratuïta protocol",
            "Activitat GRATUÏTA Cap Setmana", "Portes Obertes",
            "Gratuïta Premsa", "Bat a Bat VISITANT gratuïta",
            "PRO Gratis Escoles Prog Social", "Gratuïta C.N.L",
            "PRO Gratis Adul Program Social", "Gratis Club Ferroviari Terrass",
            "Gratuït Guia Turístic", "Gratuïta Cinema a la fresca",
            "Gratis Associació Museu AMCTAI", "Gratuïta Família d'acollida",
            "Gratuïta Assoc. Museòlegs Cat", "Gratis Covid Dv a Dg Estudiant",
            "Tiquet-web museu gratuïta ", "Gratuïta Passi Sistema",
            "Serradora d'Àreu GRATUÏT", "Gratuïta Families Acollida",
            "Gratuit Promo Menja't Montjuïc"]


def agruparTarifes(s):
    if s in general:
        return 'GENERAL'
    elif s in acpc:
        return 'ACPC'
    elif s in reduida_grups:
        return 'REDUÏDA O GRUPAL'
    elif s in menors_students_carnetJove:
        return 'MENORS, ESTUDIANTS O CARNET JOVE'
    elif s in jubilats_aturats:
        return 'JUBILATS O ATURATS'
    elif s in acompanyants:
        return 'ACOMPANYANTS'
    elif s in gratuita:
        return 'GRATUITA'
    elif s in altres:
        return 'ALTRES'
    else:
        return s


fig_title = "VENDES PER TARIFA"
data['tarifes'] = data['Descripció de la tarifa'].apply(agruparTarifes)
temp = data[~data['Descripció de la tarifa'].isnull()]
temp = temp.groupby(['tarifes'], sort=False, as_index=False). \
    agg({'Unitats': 'sum'})
temp.columns = ['tarifa', 'total']
temp = temp.sort_values(['total'], ascending=False)
fig = px.bar(temp, x='tarifa', y='total')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)
fig.update_traces(marker_color='orange')
st.write(fig)


###############################################################################

def dia_setmana(s):
    if s == 'Monday':
        return "Dilluns"
    elif s == "Tuesday":
        return "Dimarts"
    elif s == "Wednesday":
        return "Dimecres"
    elif s == "Thursday":
        return "Dijous"
    elif s == "Friday":
        return "Divendres"
    elif s == "Saturday":
        return "Dissabte"
    elif s == "Sunday":
        return "Diumenge"
    else:
        return s

fig_title = "VENDES PER DIA DE LA SETMANA"
data['day'] = data['Data venda'].dt.day_name()
data['numberDay'] = data['Data venda'].dt.weekday
temp = data.groupby(['day', 'numberDay'], sort=False, as_index=False).\
    agg({'Unitats': 'sum'})
temp.columns = ['day', 'numero', 'total']
temp['dia'] = temp['day'].apply(dia_setmana)
temp.sort_values(by=['numero'], inplace=True)
fig = px.bar(temp, x='dia', y='total')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)
fig.update_traces(marker_color='cadetblue')
st.write(fig)


###############################################################################


fig_title = "VENDES INTERNACIONALS PER DIA DE LA SETMANA"

temp = data[data['nacionalitat'] != 'Espanya']
temp = temp.groupby(['day', 'numberDay'], sort=False,
                    as_index=False).agg({'Unitats': 'sum'})
temp.columns = ['day', 'numberDay', 'total']
temp['dia'] = temp['day'].apply(dia_setmana)
temp = temp.sort_values(['numberDay'])
fig = px.bar(temp, x='dia', y='total')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################

fig_title = "VENDES NACIONALS PER DIA DE LA SETMANA"

temp = data[data['nacionalitat'] == 'Espanya']
temp = temp.groupby(['day', 'numberDay'], sort=False,
                    as_index=False).agg({'Unitats': 'sum'})
temp.columns = ['day', 'numberDay', 'total']
temp['dia'] = temp['day'].apply(dia_setmana)
temp = temp.sort_values(['numberDay'])
fig = px.bar(temp, x='dia', y='total')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################

fig_title = "TOP 15 DE NACIONALITAT PER DIA DE LA SETMANA (NO INCLOU ESPANYA)"
top15 = data[data['nacionalitat'].isin(top15_paisos)]
resta = data[~data['nacionalitat'].isin(top15_paisos)]
resta['nacionalitat'] = 'resta'
no_espanyols = top15[top15['nacionalitat'] != 'Espanya']
temp = pd.concat([no_espanyols, resta], ignore_index=True)
temp = temp.groupby(['nacionalitat', 'day', 'numberDay'], sort=False,
                    as_index=False).agg({'Unitats': 'sum'})
temp.columns = ['nacionalitat', 'day', 'numberDay', 'total']
temp['dia'] = temp['day'].apply(dia_setmana)
temp = temp.sort_values(['numberDay'])
fig = px.bar(temp, x='dia', y='total', color='nacionalitat')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################


fig_title = \
    "VENDES PER COMUNITAT AUTÒNOMA I DIA DE LA SETMANA (NO INCLOU CATALUNYA)"
temp = data.groupby(['comunitat', 'day', 'numberDay'], sort=False,
                    as_index=False).agg({'Unitats': 'sum'})
temp = temp[temp['comunitat'] != 'NO']
temp.columns = ['comunitat', 'day', 'numberDay', 'total']
temp['dia de la setmana'] = temp['day'].apply(dia_setmana)
temp = temp.sort_values(['numberDay'])
no_catalans = temp[temp['comunitat'] != 'Catalunya']
fig = px.bar(no_catalans, x='dia de la setmana', y='total', color='comunitat')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################


fig_title = "VENDES PER CATALANS I DIA DE LA SETMANA"
temp = data[data['comunitat'] == 'Catalunya']
temp = temp.groupby(['day', 'numberDay'], sort=False, as_index=False). \
    agg({'Unitats': 'sum'})
temp.columns = ['day', 'numberDay', 'total']
temp['dia de la setmana'] = temp['day'].apply(dia_setmana)
temp = temp.sort_values(['numberDay'])
fig = px.bar(temp, x='dia de la setmana', y='total')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################

def convertir_mes(mes_ingles):
    if mes_ingles == "January":
        return "Gener"
    elif mes_ingles == "February":
        return "Febrer"
    elif mes_ingles == "March":
        return "Març"
    elif mes_ingles == "April":
        return "Abril"
    elif mes_ingles == "May":
        return "Maig"
    elif mes_ingles == "June":
        return "Juny"
    elif mes_ingles == "July":
        return "Juliol"
    elif mes_ingles == "August":
        return "Agost"
    elif mes_ingles == "September":
        return "Setembre"
    elif mes_ingles == "October":
        return "Octubre"
    elif mes_ingles == "November":
        return "Novembre"
    elif mes_ingles == "December":
        return "Desembre"
    else:
        return mes_ingles

fig_title = "VENDES PER MES"
data['month'] = data['Data venda'].dt.month_name()
data['numberMonth'] = data['Data venda'].dt.month
temp = data.groupby(['month', 'numberMonth'], sort=False, as_index=False).\
    agg({'Unitats': 'sum'})
temp.columns = ['month', 'numero', 'total']
temp['mes'] = temp['month'].apply(convertir_mes)
temp.sort_values(by=['numero'], inplace=True)
countMonths = len(temp['mes'].unique())
if countMonths > 6:
    fig = px.bar(temp, x='mes', y='total')
    fig.update_traces(marker_color='bisque')
else:
    fig = px.pie(temp, names='mes', values='total')
    fig.update_traces(textposition='inside', textinfo='percent+label',
                      textfont_size=20, marker=dict(line=dict(color='#000000',
                                                              width=2)))
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################


fig_title = "VENDES NACIONALS PER MENSUALITAT"
temp = data[data['nacionalitat'] == 'Espanya']
temp = temp.groupby(['month', 'numberMonth'], sort=False, as_index=False).\
    agg({'Unitats': 'sum'})
temp.columns = ['month', 'numberMonth', 'total']
temp['mes'] = temp['month'].apply(convertir_mes)
temp = temp.sort_values(['numberMonth'])
countMonths = len(temp['mes'].unique())

if countMonths > 6:
    fig = px.bar(temp, x='mes', y='total')
else:
    fig = px.pie(temp, names='mes', values='total')
    fig.update_traces(textposition='inside', textinfo='percent+label',
                      textfont_size=20, marker=dict(line=dict(color='#000000',
                                                              width=2)))
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################


fig_title = \
    "VENDES PER NACIONALITAT (TOP 15) I MENSUALITAT (NO INCLOU ESPANYA)"
temp = data[data['nacionalitat'].isin(top15_paisos)]
resta = data[~data['nacionalitat'].isin(top15_paisos)]
resta['nacionalitat'] = 'resta'
temp = pd.concat([temp, resta], ignore_index=True)
temp = temp.groupby(['nacionalitat', 'month', 'numberMonth'], sort=False,
                    as_index=False).agg({'Unitats': 'sum'})
temp.columns = ['nacionalitat', 'month', 'numberMonth', 'total']
temp['mes'] = temp['month'].apply(convertir_mes)
temp = temp.sort_values(['numberMonth'])
temp = temp[temp['nacionalitat'] != 'Espanya']
fig = px.bar(temp, x='mes', y='total', color='nacionalitat')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################


fig_title = "VENDES PER COMUNITAT AUTÒNOMA I MENSUALITAT (NO INCLOU CATALUNYA)"
temp = data.groupby(['comunitat', 'month', 'numberMonth'], sort=False,
                    as_index=False).agg({'Unitats': 'sum'})
temp = temp[temp['comunitat'] != 'NO']
temp.columns = ['comunitat', 'month', 'numberMonth', 'total']
temp['mes'] = temp['month'].apply(convertir_mes)
temp = temp.sort_values(['numberMonth'])
temp = temp[temp['comunitat']!='Catalunya']
fig = px.bar(temp, x='mes', y='total', color='comunitat')
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################


fig_title = "VENDES PER CATALANS I MENSUALITAT"
temp = data[data['comunitat'] == 'Catalunya']
temp = temp.groupby(['month', 'numberMonth'], sort=False, as_index=False). \
    agg({'Unitats': 'sum'})
temp.columns = ['month', 'numberMonth', 'total']
temp['mes'] = temp['month'].apply(convertir_mes)
temp = temp.sort_values(['numberMonth'])
countMonths = len(temp['mes'].unique())
if countMonths > 6:
    fig = px.bar(temp, x='mes', y='total')
else:
    fig = px.pie(temp, names='mes', values='total')
    fig.update_traces(textposition='inside', textinfo='percent+label',
                      textfont_size=20, marker=dict(line=dict(color='#000000',
                                                              width=2)))
fig.update_layout(title=dict(text=fig_title, font=dict(family='Arial', size=30,
                             color='#000000')),
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_layout(
    autosize=False,
    width=1350,
    height=700)

st.write(fig)


###############################################################################
