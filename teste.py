
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.write(f"""
    # Arquivo: {uploaded_file.name}
    """)
    if uploaded_file.name[-3:] == 'csv':
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

    elif uploaded_file.name[-7:] == 'parquet':
        dataframe = pd.read_parquet(uploaded_file)
        st.write(dataframe)

    

# # URL do túnel Ngrok
# url = "https://f0df-2804-7f4-3d80-2b35-9606-146a-368b-7743.ngrok-free.app"

# # Adicionar o cabeçalho para ignorar o aviso do navegador
# headers = {
#     'ngrok-skip-browser-warning': '69421'
# }

# # Fazer a solicitação HTTP com o cabeçalho
# response = requests.get(url, headers=headers)


# st.write("""
# # Eureciclo etapa 3
# """)
    
# df = pd.read_parquet("/home/cassio/accountfy-storage/IM-13/DATABUILDER_439_c246fb70-343b-414a-b3c0-7689e2a74d99_3.parquet")
# df

# st.write("""
# # Eureciclo etapa 2
# """)
    
# df2 = pd.read_parquet("/home/cassio/accountfy-storage/IM-13/DATABUILDER_439_c246fb70-343b-414a-b3c0-7689e2a74d99_2.parquet")
# df2


# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)
# # df["accountId"] = pd.to_datetime(df["accountId"])
# df = df.sort_values("accountId")

# accountId = st.sidebar.selectbox("Conta contabil", df['accountId'].unique())

# df_filtered = df[df['accountId'] == accountId]
# df_filtered

# df

#df2 = pd.read_parquet("/home/cassio/accountfy-storage/IM-13/DATABUILDER_439_c246fb70-343b-414a-b3c0-7689e2a74d99_2.parquet")

#df2
# df3 = pd.read_parquet("/home/cassio/accountfy-storage/IM-13/DATABUILDER_439_c246fb70-343b-414a-b3c0-7689e2a74d99_2.parquet")

# df3
# st.line_chart(df['accountId'])