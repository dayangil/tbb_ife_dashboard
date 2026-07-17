# -*- coding: utf-8 -*-
"""
app.py
------
TBB - İFE Stratejik Ortaklık Sunumu (Streamlit)

Çalıştırmak için:
    pip install -r requirements.txt
    streamlit run app.py

Bu dosya sadece GÖRÜNTÜLEME mantığını içerir. Sunum içeriği data.py'de,
not/değerlendirme kalıcılığı feedback_store.py'de tutulur.
"""

import streamlit as st

from data import SECTIONS, SECTION_ORDER
from feedback_store import load_feedback, add_feedback, clear_feedback

# --------------------------------------------------------------------------
# SAYFA AYARLARI
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="TBB - İFE Stratejik Ortaklık Sunumu",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------
# STİL (Kurumsal / Bankacılık teması: lacivert + altın vurgu)
# --------------------------------------------------------------------------
st.markdown(
    """
    <style>
        :root {
            --ife-navy: #0B1F3A;
            --ife-navy-light: #16305C;
            --ife-gold: #C8A24A;
            --ife-bg: #F5F7FA;
        }
        .main { background-color: var(--ife-bg); }

        /* Başlık bandı */
        .ife-header {
            background: linear-gradient(135deg, var(--ife-navy) 0%, var(--ife-navy-light) 100%);
            padding: 1.6rem 2rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            border-left: 6px solid var(--ife-gold);
        }
        .ife-header h1 {
            color: white;
            font-size: 1.6rem;
            margin: 0;
        }
        .ife-header p {
            color: #C9D3E0;
            margin: 0.3rem 0 0 0;
            font-size: 0.95rem;
        }

        /* İçerik kartı */
        .ife-card {
            background: white;
            border: 1px solid #E3E7EE;
            border-left: 4px solid var(--ife-gold);
            border-radius: 10px;
            padding: 1.1rem 1.3rem;
            margin-bottom: 0.9rem;
        }
        .ife-card h4 {
            margin: 0 0 0.4rem 0;
            color: var(--ife-navy);
            font-size: 1.05rem;
        }

        /* Detay kutusu */
        .ife-detail {
            background: #F8F6EF;
            border: 1px solid #E9DFC3;
            border-radius: 10px;
            padding: 1rem 1.3rem;
            white-space: pre-line;
            line-height: 1.55;
            color: #1F2A3D;
        }

        .ife-badge {
            display: inline-block;
            background: var(--ife-navy);
            color: white;
            padding: 0.15rem 0.6rem;
            border-radius: 999px;
            font-size: 0.75rem;
            margin-bottom: 0.5rem;
        }

        section[data-testid="stSidebar"] {
            background-color: var(--ife-navy);
        }
        section[data-testid="stSidebar"] * {
            color: #EDEFF3 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# SIDEBAR - NAVİGASYON
# --------------------------------------------------------------------------
st.sidebar.markdown("## 🤝 TBB - İFE")
st.sidebar.caption("Stratejik Ortaklık Sunumu")
st.sidebar.markdown("---")

nav_labels = ["🏠 Ana Sayfa"] + [
    f"{SECTIONS[key]['icon']} {SECTIONS[key]['title']}" for key in SECTION_ORDER
] + ["📝 Değerlendirme ve Notlar"]

nav_keys = ["home"] + SECTION_ORDER + ["feedback"]

selected_label = st.sidebar.radio("Bölüm seçin", nav_labels, label_visibility="collapsed")
selected_key = nav_keys[nav_labels.index(selected_label)]

# --------------------------------------------------------------------------
# ÜST BAŞLIK
# --------------------------------------------------------------------------
st.markdown(
    """
    <div class="ife-header">
        <h1>TBB - İFE Stratejik Ortaklık Sunumu</h1>
        <p>Sektörel değerlendirme ve önerilen iş birliği modelleri</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------------------------------
# YARDIMCI: bir bölümü kart + genişletilebilir detay olarak göster
# --------------------------------------------------------------------------
def render_section(section_key: str):
    section = SECTIONS[section_key]
    st.subheader(f"{section['icon']} {section['title']}")
    st.caption(section["menu_desc"])
    st.write("")

    for idx, item in section["items"].items():
        with st.expander(f"**{idx}.** {item['baslik']}"):
            st.markdown(
                f'<div class="ife-detail">{item["detay"]}</div>',
                unsafe_allow_html=True,
            )


# --------------------------------------------------------------------------
# ANA SAYFA
# --------------------------------------------------------------------------
def render_home():
    st.markdown("### Sunuma Genel Bakış")
    cols = st.columns(len(SECTION_ORDER))
    for col, key in zip(cols, SECTION_ORDER):
        section = SECTIONS[key]
        with col:
            st.markdown(
                f"""
                <div class="ife-card" style="min-height: 150px;">
                    <span class="ife-badge">{len(section['items'])} madde</span>
                    <h4>{section['icon']} {section['title']}</h4>
                    <p style="font-size:0.85rem; color:#5A6472;">{section['menu_desc']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.info(
        "Soldaki menüden ilgili bölümü seçin. Her başlığın üzerine tıklandığında "
        "detaylı değerlendirme ve önerilen çözüm görüntülenir."
    )


# --------------------------------------------------------------------------
# GERİ BİLDİRİM SAYFASI
# --------------------------------------------------------------------------
def render_feedback():
    st.subheader("📝 Değerlendirme ve Toplantı Notları")
    st.caption("Girilen notlar kalıcı olarak saklanır; sayfa kapatılıp yeniden açıldığında korunur.")

    with st.form("feedback_form", clear_on_submit=True):
        c1, c2 = st.columns([1, 2])
        isim = c1.text_input("Ad Soyad")
        yorum = c2.text_area("Değerlendirme / not", height=80)
        submitted = st.form_submit_button("Kaydet")
        if submitted:
            if yorum.strip():
                add_feedback(isim, yorum)
                st.success("Not kaydedildi.")
            else:
                st.warning("Lütfen bir not girin.")

    st.markdown("---")
    st.markdown("#### Kayıtlı Notlar")
    entries = load_feedback()
    if not entries:
        st.write("Henüz eklenmiş not yok.")
    else:
        for i, fb in enumerate(reversed(entries), 1):
            st.markdown(
                f"""
                <div class="ife-card">
                    <span class="ife-badge">{fb.get('tarih', '')}</span>
                    <h4>{fb['isim']}</h4>
                    <p>{fb['yorum']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with st.expander("⚠️ Tüm notları temizle"):
            if st.button("Evet, tüm notları sil", type="primary"):
                clear_feedback()
                st.rerun()


# --------------------------------------------------------------------------
# YÖNLENDİRME
# --------------------------------------------------------------------------
if selected_key == "home":
    render_home()
elif selected_key == "feedback":
    render_feedback()
else:
    render_section(selected_key)
