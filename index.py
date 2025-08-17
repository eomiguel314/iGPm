
import streamlit as st
from datetime import date

# Classe Projeto
class Projeto:
    def __init__(self, nome, descricao, inicio, status):
        self.nome = nome
        self.descricao = descricao
        self.inicio = inicio
        self.status = status

# Classe Usuario
class Usuario:
    def __init__(self, nome, email, funcao, entrada, ativo=True, projetos=None, habilidades=None, bio="", foto=None, professor=None):
        self.nome = nome
        self.email = email
        self.funcao = funcao
        self.entrada = entrada
        self.ativo = ativo
        self.projetos = projetos or []
        self.habilidades = habilidades or []
        self.bio = bio
        self.foto = foto
        self.professor = professor

    def perfil_base(self):
        st.markdown("""
        <style>
        .perfil-title {
            text-align: center;
            font-size: 2em;
            font-weight: 700;
            margin-bottom: 10px;
            color: #333;
        }
        .perfil-sub {
            text-align: center;
            font-size: 1em;
            color: #666;
            margin-bottom: 25px;
        }
        .perfil-img {
            display: block;
            margin: 0 auto 20px auto;
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        .perfil-section {
            margin-top: 30px;
        }
        .section-title {
            font-size: 1.2em;
            font-weight: 700;
            color: #444;
            margin-bottom: 10px;
            padding-bottom: 5px;
        }
        .badge {
            display: inline-block;
            background-color: #f1f1f1;
            border-radius: 20px;
            padding: 5px 12px;
            margin: 3px;
            font-size: 0.9em;
            color: #333;
        }
        </style>
        """, unsafe_allow_html=True)

        # Criar duas colunas
        col1, col2 = st.columns(2)

        # ---- COLUNA 1 ----
        with col1:
            st.markdown(f'<img src="{self.foto or "https://cdn-icons-png.flaticon.com/512/149/149071.png"}" class="perfil-img">', unsafe_allow_html=True)
            st.markdown(f'<div class="perfil-title">{self.nome}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="perfil-sub">{self.funcao} | {"🟢 Ativo" if self.ativo else "🔴 Inativo"}</div>', unsafe_allow_html=True)

            st.markdown('<div class="perfil-section">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Informações</div>', unsafe_allow_html=True)
            st.markdown(f"- **Email:** {self.email}")
            st.markdown(f"- **Entrada no laboratório:** {self.entrada.strftime('%d/%m/%Y')}")
            st.markdown('</div>', unsafe_allow_html=True)

            if self.professor:
                st.markdown('<div class="perfil-section">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">Professor</div>', unsafe_allow_html=True)
                st.badge(self.professor, color="blue")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="perfil-section">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Bio</div>', unsafe_allow_html=True)
            st.markdown(self.bio or "*Este membro ainda não escreveu uma bio.*")
            st.markdown('</div>', unsafe_allow_html=True)

        # ---- COLUNA 2 ----
        with col2:
            st.markdown('<div class="perfil-section">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Projetos</div>', unsafe_allow_html=True)
            if self.projetos:
                for projeto in self.projetos:
                    with st.expander(f"🔹 {projeto.nome}"):
                        st.markdown(f"**Descrição:** {projeto.descricao}")
                        st.markdown(f"**Data de Início:** {projeto.inicio.strftime('%d/%m/%Y')}")
                        st.markdown(f"**Status:** {projeto.status}")
            else:
                st.markdown("*Nenhum projeto cadastrado.*")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="perfil-section">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
            if self.habilidades:
                badges = " ".join([f'<span class="badge">{h}</span>' for h in self.habilidades])
                st.markdown(badges, unsafe_allow_html=True)
            else:
                st.markdown("*Nenhuma habilidade informada.*")
            st.markdown('</div>', unsafe_allow_html=True)


def dados_exemplo():
    projetos = [
        Projeto(
            nome="Robô Seguidor de Linha",
            descricao="Projeto para construir um robô capaz de seguir uma linha preta em um percurso definido.",
            inicio=date(2024, 9, 1),
            status="Em andamento"
        ),
        Projeto(
            nome="Drone",
            descricao="Drone para inspeção automatizada usando visão computacional.",
            inicio=date(2023, 11, 15),
            status="Finalizado"
        ),
        Projeto(
            nome="iGP",
            descricao="Sistema inteligente para gerenciamento de plantas automatizadas.",
            inicio=date(2025, 2, 20),
            status="Em andamento"
        )
    ]

    usuario = Usuario(
        nome="Karllos Miguel",
        email="k.miguel@ifro.edu",
        funcao="Membro",
        entrada=date(2025, 4, 1),
        ativo=True,
        projetos=projetos,
        habilidades=["Python", "Arduino", "Streamlit", "OpenCV", "Eletrônica"],
        bio="",
        foto="https://poltronanerd.com.br/wp-content/uploads/2021/07/Rick-and-Morty-Pickle-Rick-capa.jpg",
        professor="Prof. Anderson"
    )
    usuario.perfil_base()


if __name__ == "__main__":
    st.set_page_config(page_title="Perfil do Membro", layout="wide")  # melhor para 2 colunas
    st.title("🤖 - iGPm")
    dados_exemplo()