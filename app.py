import streamlit as st
import pandas as pd

# ======================
# Carregar base de dados
# ======================
@st.cache_data
def load_data():
    return pd.read_csv("membros.csv")

df = load_data()

# Pegamos o usuário desejado (exemplo: o primeiro do CSV)
usuario = df.iloc[0]

# ======================
# Sidebar
# ======================
st.sidebar.title("📌 Navegação")
menu = st.sidebar.radio(
    "Escolha a seção:",
    ["Visão Geral", "Informações Pessoais", "Formação", "Projetos", "Premiações", "Links Externos"]
)

# ======================
# Estilos customizados
# ======================
st.markdown(
    """
    <style>
    /* Estilos gerais */
    .profile-card {
        border-radius: 15px;
        border: 2px solid #4CAF50;
        padding: 25px;
        background: linear-gradient(135deg, #f0fdf4, #e6ffe6);
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        transition: transform 0.3s ease-in-out;
    }
    .profile-card:hover {
        transform: scale(1.03);
    }
    .profile-card h2 {
        color: #2e7d32;
        margin-bottom: 5px;
    }
    .profile-card h4 {
        color: #555;
        margin-top: 0px;
    }
    .section {
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #ffffff;
        box-shadow: 0px 3px 6px rgba(0,0,0,0.08);
        transition: box-shadow 0.3s ease;
    }
    .section:hover {
        box-shadow: 0px 6px 12px rgba(0,0,0,0.12);
    }
    .section h3 {
        color: #1b5e20;
        margin-bottom: 10px;
        font-size: 1.5em;
    }
    .stExpander > div > label {
        font-size: 1.1em;
        color: #4CAF50;
        font-weight: 600;
    }
    /* Texto e estilo de links */
    a {
        color: #4CAF50;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }
    a:hover {
        text-decoration: underline;
        color: #388e3c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# Card de apresentação
# ======================
st.markdown(
    f"""
    <div class="profile-card">
        <h2>{usuario['nome']}</h2>
        <h4>{usuario['curso']} - {usuario['instituicao']}</h4>
        <p>{usuario['descricao']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ======================
# Conteúdo por menu
# ======================
if menu == "Visão Geral":
    st.markdown('<div><h3>📌 Visão Geral</h3></div>', unsafe_allow_html=True)
    st.write(f"Olá! Meu nome é **{usuario['nome']}** e sou estudante de **{usuario['curso']}** na **{usuario['instituicao']}**. Estou sempre em busca de novos desafios e oportunidades para aprender e crescer. Aqui estão algumas informações sobre mim!")
    
    st.write(f"**Email:** {usuario['email']}")
    st.write(f"**Período atual:** {usuario['periodo']}")
    st.write(f"**Formação acadêmica:** {usuario['formacao']}")
    st.markdown("### Projetos 🛠")
    projetos = str(usuario["projetos"]).split(";")
    for proj in projetos:
        with st.expander(f"🔹 {proj.strip()}"):
            st.write(f"**Descrição do projeto:** {usuario.get('descricao_projeto', 'Ainda estamos definindo os detalhes!')}")
            st.write(f"**Ferramentas utilizadas:** {usuario.get('ferramentas', 'Ferramentas não especificadas.')}")
            st.write(f"**Data de início:** {usuario.get('inicio_projeto', 'Data não especificada.')}")
            st.write(f"**Status:** {usuario.get('status_projeto', 'Em andamento...')} ⚙️")
    st.markdown("### Premiaçoes 🛠")
    premiacoes = str(usuario["premiacoes"]).split(";")
    for prem in premiacoes:
        with st.expander(f"🥇 {prem.strip()}"):
            st.write(f"**Detalhes da premiação:** {usuario.get('detalhes_premiacao', 'Mais informações em breve!')}")
            st.write(f"**Ano da premiação:** {usuario.get('ano_premiacao', 'Ano não especificado.')}")
    st.markdown(f"[🌐 GitHub]({usuario['github']})", unsafe_allow_html=True)
    st.markdown(f"[💼 LinkedIn]({usuario['linkedin']})", unsafe_allow_html=True)
    st.markdown(f"[📧 Email]({usuario['email']})", unsafe_allow_html=True)

elif menu == "Informações Pessoais":
    st.markdown('<div class="section"><h3>👤 Informações Pessoais</h3></div>', unsafe_allow_html=True)
    st.write(f"**Email:** {usuario['email']}")
    st.write(f"**Período atual:** {usuario['periodo']}")
    
    st.markdown("### Detalhes adicionais 📝")
    st.write(f"**Idade:** {usuario.get('idade', 'Idade não especificada')} 🎂")

elif menu == "Formação":
    st.markdown('<div class="section"><h3>🎓 Formação e Certificações</h3></div>', unsafe_allow_html=True)
    st.write(f"**Formação Acadêmica:** {usuario['formacao']}")
    
    st.markdown("### Certificados 📜")
    st.write(f"**Certificado de:** {usuario['certificados']}")

elif menu == "Projetos":
    st.markdown('<div class="section"><h3>🛠 Projetos</h3></div>', unsafe_allow_html=True)
    projetos = str(usuario["projetos"]).split(";")
    for proj in projetos:
        with st.expander(f"🔹 {proj.strip()}"):
            st.write(f"**Descrição do projeto:** {usuario.get('descricao_projeto', 'Ainda estamos definindo os detalhes!')}")
            st.write(f"**Ferramentas utilizadas:** {usuario.get('ferramentas', 'Ferramentas não especificadas.')}") 
            st.write(f"**Data de início:** {usuario.get('inicio_projeto', 'Data não especificada.')}")
            st.write(f"**Status:** {usuario.get('status_projeto', 'Em andamento...')} ⚙️")

elif menu == "Premiações":
    st.markdown('<div class="section"><h3>🏆 Premiações e Conquistas</h3></div>', unsafe_allow_html=True)
    premiacoes = str(usuario["premiacoes"]).split(";")
    for prem in premiacoes:
        with st.expander(f"🥇 {prem.strip()}"):
            st.write(f"**Detalhes da premiação:** {usuario.get('detalhes_premiacao', 'Mais informações em breve!')}")
            st.write(f"**Ano da premiação:** {usuario.get('ano_premiacao', 'Ano não especificado.')}")

elif menu == "Links Externos":
    st.markdown('<div class="section"><h3>🔗 Links Externos</h3></div>', unsafe_allow_html=True)
    st.markdown(f"[🌐 GitHub]({usuario['github']})", unsafe_allow_html=True)
    st.markdown(f"[💼 LinkedIn]({usuario['linkedin']})", unsafe_allow_html=True)
    st.markdown(f"[📧 Email]({usuario['email']})", unsafe_allow_html=True)
