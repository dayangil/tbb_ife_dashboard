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

from data import SECTIONS, SECTION_ORDER, BROCHURE
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

view_mode = st.sidebar.radio(
    "Görünüm Modu",
    ["📄 TBB Sunum (Broşür)", "🏢 İç Ekip Görünümü"],
    index=0,
    label_visibility="collapsed",
)
st.sidebar.markdown("---")

if view_mode == "🏢 İç Ekip Görünümü":
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
# TBB SUNUM (BROŞÜR) — Dış sunum görünümü
# --------------------------------------------------------------------------
def render_brochure():
    st.markdown(
        """
        <style>
            .brochure-hero {
                background: linear-gradient(135deg, #0B1F3A 0%, #16305C 100%);
                padding: 2.2rem 2.5rem;
                border-radius: 14px;
                margin-bottom: 2rem;
                border-left: 8px solid #C8A24A;
            }
            .brochure-hero h1 {
                color: white;
                font-size: 1.8rem;
                margin: 0 0 0.3rem 0;
            }
            .brochure-hero p {
                color: #C9D3E0;
                margin: 0.2rem 0;
                font-size: 1rem;
            }
            .program-card {
                background: white;
                border: 1px solid #E3E7EE;
                border-radius: 14px;
                padding: 1.6rem 1.8rem;
                margin-bottom: 1.6rem;
                box-shadow: 0 2px 10px rgba(11,31,58,0.06);
            }
            .program-image {
                width: 100%;
                border-radius: 10px;
                margin-bottom: 1rem;
                max-height: 220px;
                object-fit: cover;
            }
            .level-badge {
                display: inline-block;
                background: #EEF1F5;
                color: #0B1F3A;
                font-weight: 600;
                padding: 0.2rem 0.8rem;
                border-radius: 999px;
                font-size: 0.78rem;
                margin-left: 0.6rem;
            }
            .price-row {
                display: flex;
                gap: 1rem;
                flex-wrap: wrap;
                margin-top: 1rem;
            }
            .price-card {
                background: #0B1F3A;
                color: white;
                border-radius: 10px;
                padding: 0.9rem 1.2rem;
                flex: 1;
                min-width: 180px;
            }
            .price-card .price-label {
                font-size: 0.78rem;
                color: #C9D3E0;
                margin-bottom: 0.2rem;
            }
            .price-card .price-value {
                font-size: 1.25rem;
                font-weight: 700;
                color: #C8A24A;
            }
            .price-card .price-duration {
                font-size: 0.78rem;
                color: #C9D3E0;
                margin-top: 0.2rem;
            }
            .program-badge {
                display: inline-block;
                background: #C8A24A;
                color: #0B1F3A;
                font-weight: 700;
                padding: 0.25rem 0.9rem;
                border-radius: 999px;
                font-size: 0.8rem;
                margin-bottom: 0.7rem;
            }
            .program-card h2 {
                color: #0B1F3A;
                margin: 0 0 0.2rem 0;
                font-size: 1.4rem;
            }
            .program-tagline {
                color: #C8A24A;
                font-weight: 600;
                font-size: 0.95rem;
                margin-bottom: 0.8rem;
            }
            .program-summary {
                color: #384357;
                line-height: 1.55;
                margin-bottom: 1rem;
            }
            .module-list, .audience-list {
                margin: 0;
                padding-left: 1.1rem;
            }
            .module-list li, .audience-list li {
                margin-bottom: 0.35rem;
                color: #1F2A3D;
            }
            .meta-row {
                display: flex;
                gap: 1.5rem;
                flex-wrap: wrap;
                margin-top: 1.1rem;
                padding-top: 1rem;
                border-top: 1px solid #EEF1F5;
                font-size: 0.85rem;
                color: #5A6472;
            }
            .meta-row strong { color: #0B1F3A; }
            .closing-box {
                background: #F8F6EF;
                border: 1px solid #E9DFC3;
                border-radius: 14px;
                padding: 1.6rem 1.8rem;
                margin-top: 1rem;
            }
            .closing-box h3 { color: #0B1F3A; margin-top: 0; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    event = BROCHURE["event_info"]
    st.markdown(
        f"""
        <div class="brochure-hero">
            <h1>{event['title']}</h1>
            <p>{event['subtitle']}</p>
            <p>{event['partner_line']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for program in BROCHURE["programs"]:
        modules_html = "".join(f"<li>{m}</li>" for m in program["modules"])
        audience_html = "".join(f"<li>{a}</li>" for a in program["audience"])

        price_cards_html = "".join(
            f"""<div class="price-card">
                <div class="price-label">{p['label']}</div>
                <div class="price-value">{p['price']}</div>
                <div class="price-duration">{p['duration']}</div>
            </div>"""
            for p in program.get("price_options", [])
        )
        image_html = ""
        if program.get("image"):
            image_html = f'<img class="program-image" src="{program["image"]}" alt="{program["title"]}">'

        instructor = program.get("instructor")
        instructor_html = ""
        if instructor:
            linkedin_html = ""
            if instructor.get("linkedin"):
                link_text = "LinkedIn Profili →" if "linkedin.com" in instructor["linkedin"] else "Detaylı Özgeçmiş →"
                linkedin_html = (
                    f'<a href="{instructor["linkedin"]}" target="_blank" '
                    f'style="color:#0B1F3A; text-decoration:underline; font-size:0.85rem;">'
                    f'{link_text}</a>'
                )
            expertise_chips = "".join(
                f'<span style="display:inline-block; background:#EEF1F5; color:#0B1F3A; '
                f'padding:0.2rem 0.7rem; border-radius:999px; font-size:0.78rem; '
                f'margin:0.2rem 0.3rem 0.2rem 0;">{exp}</span>'
                for exp in instructor.get("expertise", [])
            )
            initials = "".join(part[0] for part in instructor["name"].split()[:2]).upper()
            instructor_html = f"""
            <div style="margin-top:1.2rem; padding-top:1.1rem; border-top:1px solid #EEF1F5; display:flex; gap:1rem; align-items:flex-start;">
                <div style="flex-shrink:0; width:52px; height:52px; border-radius:50%; background:#0B1F3A; color:#C8A24A; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:1.1rem;">{initials}</div>
                <div style="flex:1; min-width:200px;">
                    <div style="font-weight:700; color:#0B1F3A; font-size:1rem;">{instructor['name']}
                        <span style="font-weight:400; color:#5A6472; font-size:0.85rem;">— {instructor['title']}</span>
                    </div>
                    <p style="color:#384357; font-size:0.88rem; line-height:1.5; margin:0.35rem 0 0.5rem 0;">{instructor['bio']}</p>
                    <div>{expertise_chips}</div>
                    {f'<div style="margin-top:0.5rem;">{linkedin_html}</div>' if linkedin_html else ""}
                </div>
            </div>
            """

        st.markdown(
            f"""
            <div class="program-card">
                {image_html}
                <span class="program-badge">{program['badge']}</span>
                <span class="level-badge">{program.get('level', '')}</span>
                <h2>{program['title']}</h2>
                <div class="program-tagline">{program['tagline']}</div>
                <div class="program-summary">{program['summary']}</div>
                <div style="display:flex; gap:2rem; flex-wrap:wrap;">
                    <div style="flex:1; min-width:220px;">
                        <strong>Eğitim İçeriği</strong>
                        <ul class="module-list">{modules_html}</ul>
                    </div>
                    <div style="flex:1; min-width:220px;">
                        <strong>Hedef Kitle</strong>
                        <ul class="audience-list">{audience_html}</ul>
                    </div>
                </div>
                <div class="meta-row">
                    <span><strong>Format:</strong> {program['format']}</span>
                    <span><strong>Süre:</strong> {program['duration']}</span>
                </div>
                <div class="meta-row">
                    <span>{program['authority']}</span>
                </div>
                <div class="price-row">{price_cards_html}</div>
                {instructor_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    closing = BROCHURE["closing"]
    st.markdown(
        f"""
        <div class="closing-box">
            <h3>{closing['title']}</h3>
            <p>{closing['text']}</p>
        </div>
        """,
        unsafe_allow_html=True,
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
if view_mode == "📄 TBB Sunum (Broşür)":
    render_brochure()
else:
    if selected_key == "home":
        render_home()
    elif selected_key == "feedback":
        render_feedback()
    else:
        render_section(selected_key)
