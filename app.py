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

from data import SECTIONS, SECTION_ORDER, BROCHURE, IFE_LOGO_WHITE, IFRS_LOGO, TBB_LOGO
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
def _html_block(text: str) -> str:
    """Collapse a multi-line HTML f-string into one CommonMark-safe block.

    st.markdown() already dedents/strips its input (see Streamlit's
    string_util.clean_text), so indentation alone is not the issue. The real
    problem is a blank line left in the middle of a <div> block — e.g. from
    an optional field like an unset instructor or authority note rendering
    as an empty string on its own template line — which still ends the
    raw-HTML block early, so everything after it falls back to a literal
    Markdown code block. Dropping blank lines (without touching indentation,
    which Streamlit's own dedent will normalize on the final combined
    string) keeps the whole card inside one continuous HTML block.
    """
    return "\n".join(line for line in text.splitlines() if line.strip())


def render_brochure_styles():
    st.markdown(
        """
        <style>
            .brochure-hero {
                background: linear-gradient(135deg, #0B1F3A 0%, #16305C 100%);
                padding: 2.2rem 2.5rem;
                border-radius: 14px;
                margin-bottom: 1.5rem;
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
            .event-tagline {
                color: #C8A24A !important;
                font-weight: 700;
                font-size: 1.02rem !important;
            }
            .hero-logos {
                display: flex;
                align-items: center;
                gap: 0.7rem;
                margin-bottom: 1rem;
            }
            .hero-logo-divider {
                color: #C8A24A;
                font-size: 1.1rem;
                font-weight: 700;
            }
            .tbb-logo-chip {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background: white;
                border-radius: 8px;
                padding: 0.3rem 0.6rem;
                height: 40px;
                box-sizing: border-box;
            }
            .tbb-logo-chip img {
                height: 28px;
            }
            .ifrs-banner {
                background: #F8F6EF;
                border-left: 6px solid #C8A24A;
                border-radius: 10px;
                padding: 1rem 1.4rem;
                margin-bottom: 1.5rem;
                color: #0B1F3A;
                font-size: 0.95rem;
                font-weight: 600;
                line-height: 1.5;
                display: flex;
                align-items: center;
                gap: 1rem;
            }
            .ifrs-banner-logo {
                height: 32px;
                flex-shrink: 0;
            }
            .section-block {
                background: #EEF3FA;
                border-left: 5px solid #0B1F3A;
                border-radius: 10px;
                padding: 1.1rem 1.4rem;
                margin-bottom: 1.5rem;
            }
            .section-block h2 {
                color: #0B1F3A;
                font-size: 1.15rem;
                margin: 0 0 0.5rem 0;
            }
            .section-block p {
                color: #1F2A3D;
                font-size: 0.95rem;
                font-weight: 500;
                line-height: 1.6;
                margin: 0;
            }
            .role-grid {
                display: flex;
                gap: 0.8rem;
                flex-wrap: wrap;
                margin-top: 0.6rem;
            }
            .role-chip {
                flex: 1;
                min-width: 200px;
                background: white;
                border: 1px solid #D7E1F0;
                border-radius: 8px;
                padding: 0.7rem 0.9rem;
            }
            .role-label {
                color: #0B1F3A;
                font-weight: 700;
                font-size: 0.85rem;
                margin-bottom: 0.2rem;
            }
            .role-text {
                color: #384357;
                font-size: 0.82rem;
                line-height: 1.4;
            }
            .instructors-section {
                margin-bottom: 1.8rem;
            }
            .instructors-title {
                color: #0B1F3A;
                font-size: 1.1rem;
                margin: 0 0 0.8rem 0;
            }
            .instructor-grid {
                display: flex;
                gap: 0.8rem;
                flex-wrap: wrap;
            }
            .instructor-chip {
                flex: 1;
                min-width: 220px;
                background: white;
                border: 1px solid #E3E7EE;
                border-radius: 10px;
                padding: 0.8rem 1rem;
                display: flex;
                align-items: center;
                gap: 0.8rem;
            }
            .instructor-avatar {
                flex-shrink: 0;
                width: 42px;
                height: 42px;
                border-radius: 50%;
                background: #0B1F3A;
                color: #C8A24A;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 700;
                font-size: 0.95rem;
            }
            .instructor-name {
                color: #0B1F3A;
                font-weight: 700;
                font-size: 0.92rem;
            }
            .instructor-role {
                color: #5A6472;
                font-size: 0.78rem;
                margin-top: 0.1rem;
            }
            .program-card {
                background: white;
                border: 1px solid #E3E7EE;
                border-radius: 14px;
                padding: 1.8rem 2rem;
                margin-bottom: 1.8rem;
                box-shadow: 0 3px 14px rgba(11,31,58,0.08);
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
            .price-note-badge {
                display: inline-block;
                background: #EEF1F5;
                color: #0B1F3A;
                font-weight: 600;
                padding: 0.6rem 1.1rem;
                border-radius: 10px;
                font-size: 0.9rem;
                margin-top: 1rem;
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
                font-size: 1.45rem;
            }
            .program-tagline {
                color: #C8A24A;
                font-weight: 600;
                font-size: 0.98rem;
                margin-bottom: 1rem;
                line-height: 1.4;
            }
            .outcomes-list, .module-list, .audience-list {
                margin: 0;
                padding-left: 1.1rem;
            }
            .module-list li, .audience-list li {
                margin-bottom: 0.35rem;
                color: #1F2A3D;
            }
            .method-box {
                background: #F8F6EF;
                border-radius: 8px;
                padding: 0.8rem 1rem;
                margin-top: 1rem;
                font-size: 0.88rem;
                color: #384357;
                line-height: 1.5;
            }
            .method-box strong { color: #0B1F3A; }
            .levels-strip {
                display: flex;
                gap: 0.6rem;
                flex-wrap: wrap;
                margin-top: 1.1rem;
            }
            .level-pill {
                background: #0B1F3A;
                color: #EDEFF3;
                border-radius: 999px;
                padding: 0.35rem 0.9rem;
                font-size: 0.78rem;
                font-weight: 600;
            }
            .level-pill .level-num {
                color: #C8A24A;
                font-weight: 700;
                margin-right: 0.3rem;
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
            .authority-badge {
                background: #F8F6EF;
                border-left: 4px solid #C8A24A;
                border-radius: 8px;
                padding: 0.7rem 1rem;
                margin-top: 1rem;
                font-size: 0.85rem;
                color: #384357;
            }
            .authority-badge strong { color: #0B1F3A; }
            .course-link {
                margin-top: 1.1rem;
            }
            .course-link a {
                color: #0B1F3A;
                font-weight: 600;
                font-size: 0.85rem;
                text-decoration: underline;
            }
            .component-card {
                background: #FAFBFD;
                border: 1px solid #E3E7EE;
                border-radius: 12px;
                padding: 1.2rem 1.4rem;
                margin-top: 1.4rem;
            }
            .component-name {
                color: #0B1F3A;
                font-weight: 700;
                font-size: 1.02rem;
            }
            .component-note {
                color: #5A6472;
                font-size: 0.85rem;
                font-style: italic;
                margin-top: 0.3rem;
            }
            .second-phase-heading {
                color: #0B1F3A;
                font-size: 1.3rem;
                font-weight: 700;
                margin: 2.6rem 0 0.4rem 0;
                border-top: 2px solid #E3E7EE;
                padding-top: 1.6rem;
            }
            .secondary-card {
                background: #FAFAFA;
                border: 1px solid #E7E7E7;
                border-radius: 10px;
                padding: 1.2rem 1.4rem;
                margin-bottom: 1.2rem;
            }
            .secondary-card h3 {
                color: #384357;
                font-size: 1.05rem;
                margin: 0.4rem 0 0.3rem 0;
            }
            .secondary-badge {
                display: inline-block;
                background: #D9DEE5;
                color: #384357;
                font-weight: 700;
                padding: 0.2rem 0.8rem;
                border-radius: 999px;
                font-size: 0.72rem;
            }
            .secondary-intro {
                color: #5A6472;
                font-size: 0.85rem;
                line-height: 1.5;
                margin-bottom: 0.9rem;
            }
            .cert-grid {
                display: flex;
                gap: 0.7rem;
                flex-wrap: wrap;
            }
            .cert-item {
                flex: 1;
                min-width: 220px;
                background: white;
                border: 1px solid #E7E7E7;
                border-radius: 8px;
                padding: 0.7rem 0.9rem;
            }
            .cert-name {
                color: #384357;
                font-weight: 700;
                font-size: 0.85rem;
            }
            .cert-use-case {
                color: #5A6472;
                font-size: 0.78rem;
                margin-top: 0.2rem;
                line-height: 1.4;
            }
            .cert-career {
                color: #8A93A0;
                font-size: 0.72rem;
                margin-top: 0.3rem;
                font-style: italic;
            }
            .theme-strip {
                display: flex;
                gap: 0.4rem;
                flex-wrap: wrap;
                margin-bottom: 1rem;
            }
            .theme-chip {
                display: inline-block;
                background: #EFEFEF;
                color: #384357;
                font-size: 0.74rem;
                padding: 0.25rem 0.7rem;
                border-radius: 999px;
            }
            .mini-program-card {
                background: white;
                border: 1px solid #E7E7E7;
                border-radius: 8px;
                padding: 0.9rem 1.1rem;
                margin-top: 0.8rem;
            }
            .mini-program-title {
                color: #384357;
                font-weight: 700;
                font-size: 0.9rem;
            }
            .mini-program-tagline {
                color: #8A93A0;
                font-size: 0.78rem;
                margin: 0.2rem 0 0.5rem 0;
            }
            .instructor-note {
                color: #8A93A0;
                font-size: 0.78rem;
                font-style: italic;
                margin-top: 0.5rem;
            }
            .closing-box {
                background: #F8F6EF;
                border: 1px solid #E9DFC3;
                border-radius: 14px;
                padding: 1.6rem 1.8rem;
                margin-top: 1.6rem;
            }
            .closing-box h3 { color: #0B1F3A; margin-top: 0; }
            .closing-box p { color: #384357; margin-bottom: 0; line-height: 1.6; }
            .bespoke-card {
                background: #F5F5F5;
                border: 1px dashed #9AA5B1;
                border-radius: 12px;
                padding: 1.2rem 1.5rem;
                margin-top: 1rem;
            }
            .bespoke-badge {
                display: inline-block;
                background: #9AA5B1;
                color: white;
                font-weight: 700;
                letter-spacing: 0.04em;
                padding: 0.2rem 0.7rem;
                border-radius: 999px;
                font-size: 0.72rem;
                margin-bottom: 0.5rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _render_instructor_html(instructor):
    if not instructor:
        return ""
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
    return _html_block(
        f"""
        <div style="margin-top:0.4rem; margin-bottom:1rem; padding-bottom:1rem; border-bottom:1px solid #EEF1F5; display:flex; gap:1rem; align-items:flex-start;">
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
    )


def _render_price_html(price_options):
    return "".join(
        f"""<div class="price-card">
            <div class="price-label">{p['label']}</div>
            <div class="price-value">{p['price']}</div>
            <div class="price-duration">{p['duration']}</div>
        </div>"""
        for p in price_options
    )


def _render_course_link_html(source_url):
    if not source_url:
        return ""
    return (
        f'<div class="course-link"><a href="{source_url}" '
        f'target="_blank">ife.com.tr\'de İçerik Sayfası →</a></div>'
    )


def _component_card_html(component):
    instructor_html = _render_instructor_html(component.get("instructor"))
    price_html = _render_price_html(component.get("price_options", []))
    note_html = f'<div class="component-note">{component["note"]}</div>' if component.get("note") else ""
    authority_html = (
        f'<div class="authority-badge">{component["authority"]}</div>'
        if component.get("authority") else ""
    )
    link_html = _render_course_link_html(component.get("source_url"))

    return _html_block(
        f"""
        <div class="component-card">
            <div class="component-name">{component['name']} <span class="level-badge">{component.get('level', '')}</span></div>
            {note_html}
            {instructor_html}
            <div class="meta-row">
                <span><strong>Format:</strong> {component.get('format', '')}</span>
                <span><strong>Süre:</strong> {component.get('duration', '')}</span>
            </div>
            {authority_html}
            <div class="price-row">{price_html}</div>
            {link_html}
        </div>
        """
    )


def _render_main_program(program):
    audience_html = "".join(f"<li>{a}</li>" for a in program.get("audience", []))
    scope_html = "".join(f"<li>{s}</li>" for s in program.get("scope", []))
    levels_html = "".join(
        f'<div class="level-pill"><span class="level-num">{i + 1}</span>{lvl}</div>'
        for i, lvl in enumerate(program.get("levels", []))
    )

    image_html = ""
    if program.get("image"):
        image_html = f'<img class="program-image" src="{program["image"]}" alt="{program["title"]}">'

    instructor_html = _render_instructor_html(program.get("instructor"))

    meta_html = ""
    if program.get("format") or program.get("duration"):
        meta_html = (
            f'<div class="meta-row">'
            f'<span><strong>Format:</strong> {program.get("format", "")}</span>'
            f'<span><strong>Süre:</strong> {program.get("duration", "")}</span>'
            f'</div>'
        )

    pricing_html = ""
    if program.get("pricing_note"):
        pricing_html = f'<div class="price-note-badge">{program["pricing_note"]}</div>'

    link_html = _render_course_link_html(program.get("source_url"))

    components_html = "".join(_component_card_html(c) for c in program.get("components", []))

    st.markdown(
        _html_block(
            f"""
            <div class="program-card">
                {image_html}
                <span class="program-badge">{program['badge']}</span>
                <span class="level-badge">{program.get('level', '')}</span>
                <h2>{program['title']}</h2>
                <div class="program-tagline">{program['benefit']}</div>
                <div style="display:flex; gap:2rem; flex-wrap:wrap;">
                    <div style="flex:1; min-width:220px;">
                        <strong>Hedef Katılımcılar</strong>
                        <ul class="audience-list">{audience_html}</ul>
                    </div>
                    <div style="flex:1; min-width:220px;">
                        <strong>Program Kapsamı</strong>
                        <ul class="module-list">{scope_html}</ul>
                    </div>
                </div>
                <div class="method-box"><strong>Uygulama Yöntemi:</strong> {program.get('method', '')}</div>
                <div class="authority-badge"><strong>Beklenen Kurumsal Çıktı:</strong> {program.get('outcome', '')}</div>
                <div class="levels-strip">{levels_html}</div>
                {instructor_html}
                {meta_html}
                {pricing_html}
                {link_html}
                {components_html}
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def _render_cert_group(group):
    cert_items_html = "".join(
        f"""<div class="cert-item">
            <div class="cert-name">{c['name']}</div>
            <div class="cert-use-case">{c['use_case']}</div>
            <div class="cert-career">{c['career']}</div>
        </div>"""
        for c in group["certifications"]
    )
    st.markdown(
        _html_block(
            f"""
            <div class="secondary-card">
                <span class="secondary-badge">{group['badge']}</span>
                <h3>{group['title']}</h3>
                <p class="secondary-intro">{group['intro']}</p>
                <div class="cert-grid">{cert_items_html}</div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def _render_theme_group(group):
    themes_html = "".join(f'<span class="theme-chip">{t}</span>' for t in group.get("themes", []))

    programs_html = ""
    for prog in group.get("programs", []):
        audience_html = "".join(f"<li>{a}</li>" for a in prog.get("audience", []))
        price_html = _render_price_html(prog.get("price_options", []))
        link_html = _render_course_link_html(prog.get("source_url"))
        instructor_note_html = (
            f'<div class="instructor-note">{prog["instructor_note"]}</div>'
            if prog.get("instructor_note") else ""
        )
        programs_html += _html_block(
            f"""
            <div class="mini-program-card">
                <div class="mini-program-title">{prog['title']}</div>
                <div class="mini-program-tagline">{prog['tagline']}</div>
                <ul class="audience-list">{audience_html}</ul>
                <div class="meta-row">
                    <span><strong>Format:</strong> {prog.get('format', '')}</span>
                    <span><strong>Süre:</strong> {prog.get('duration', '')}</span>
                </div>
                {instructor_note_html}
                <div class="price-row">{price_html}</div>
                {link_html}
            </div>
            """
        )

    bespoke_html = ""
    bespoke = group.get("bespoke")
    if bespoke:
        bespoke_html = _html_block(
            f"""
            <div class="bespoke-card">
                <span class="bespoke-badge">{bespoke['status_label']}</span>
                <h4 style="color:#0B1F3A; margin:0.3rem 0;">{bespoke['title']}</h4>
                <p style="color:#5A6472; font-size:0.9rem; line-height:1.5; margin:0;">{bespoke['note']}</p>
            </div>
            """
        )

    st.markdown(
        _html_block(
            f"""
            <div class="secondary-card">
                <span class="secondary-badge">{group['badge']}</span>
                <h3>{group['title']}</h3>
                <p class="secondary-intro">{group['intro']}</p>
                <div class="theme-strip">{themes_html}</div>
                {programs_html}
                {bespoke_html}
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def render_brochure():
    render_brochure_styles()

    event = BROCHURE["event_info"]
    st.markdown(
        _html_block(
            f"""
            <div class="brochure-hero">
                <div class="hero-logos">
                    <img src="{IFE_LOGO_WHITE}" alt="İFE Logo" style="height:40px;">
                    <span class="hero-logo-divider">×</span>
                    <span class="tbb-logo-chip"><img src="{TBB_LOGO}" alt="Türkiye Bankalar Birliği Logo"></span>
                </div>
                <h1>{event['title']}</h1>
                <p class="event-tagline">{event['tagline']}</p>
                <p>{event['opening_statement']}</p>
                <p>{event['positioning']}</p>
                <p style="font-size:0.82rem; opacity:0.85;">{event['credentials_line']}</p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        _html_block(
            f"""
            <div class="ifrs-banner">
                <img src="{IFRS_LOGO}" alt="IFRS Foundation" class="ifrs-banner-logo">
                <span>{event['ifrs_partnership']}</span>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    tbb_strength = BROCHURE["tbb_strength"]
    st.markdown(
        _html_block(
            f"""
            <div class="section-block">
                <h2>{tbb_strength['title']}</h2>
                <p>{tbb_strength['text']}</p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    why_partnership = BROCHURE["why_partnership"]
    st.markdown(
        _html_block(
            f"""
            <div class="section-block">
                <h2>{why_partnership['title']}</h2>
                <p>{why_partnership['text']}</p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    model = BROCHURE["partnership_model"]
    roles_html = "".join(
        f"""<div class="role-chip">
            <div class="role-label">{r['label']}</div>
            <div class="role-text">{r['text']}</div>
        </div>"""
        for r in model["roles"]
    )
    st.markdown(
        _html_block(
            f"""
            <div class="section-block">
                <h2>{model['title']}</h2>
                <div class="role-grid">{roles_html}</div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    for program in BROCHURE["main_programs"]:
        _render_main_program(program)

    delivery_model = BROCHURE["delivery_model"]
    st.markdown(
        _html_block(
            f"""
            <div class="section-block">
                <h2>{delivery_model['title']}</h2>
                <p>{delivery_model['text']}</p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    instructors = []
    for p in BROCHURE["main_programs"]:
        if p.get("instructor"):
            instructors.append(p["instructor"])
        for c in p.get("components", []):
            if c.get("instructor"):
                instructors.append(c["instructor"])

    if instructors:
        instructor_cards_html = "".join(
            f"""<div class="instructor-chip">
                <div class="instructor-avatar">{"".join(part[0] for part in i["name"].split()[:2]).upper()}</div>
                <div>
                    <div class="instructor-name">{i['name']}</div>
                    <div class="instructor-role">{i['title']}</div>
                </div>
            </div>"""
            for i in instructors
        )
        st.markdown(
            _html_block(
                f"""
                <div class="instructors-section">
                    <h2 class="instructors-title">Eğitmenlerimiz</h2>
                    <div class="instructor-grid">{instructor_cards_html}</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.markdown('<div class="second-phase-heading">İkinci Faz Programları</div>', unsafe_allow_html=True)
    for group in BROCHURE["second_phase"]:
        if "certifications" in group:
            _render_cert_group(group)
        else:
            _render_theme_group(group)

    closing = BROCHURE["pilot_next_steps"]
    st.markdown(
        _html_block(
            f"""
            <div class="closing-box">
                <h3>{closing['title']}</h3>
                <p>{closing['text']}</p>
            </div>
            """
        ),
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
