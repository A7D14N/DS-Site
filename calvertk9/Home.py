import base64
import os

import streamlit as st

from utils import find_image, inject_base_styles, render_html

st.set_page_config(
    page_title="CalvertK9 — KC Registered Maltese Puppies",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_base_styles()

# ---------------------------------------------------------------------------
# HERO
# Put your hero photo in images/home_hero.jpg (or .jpeg / .png / .webp).
# Until it's added, a soft placeholder is shown so the page still runs.
# ---------------------------------------------------------------------------
hero_path = find_image("home_hero")
if hero_path:
    ext = os.path.splitext(hero_path)[1].lstrip(".")
    with open(hero_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    hero_bg_html = f'<img class="home-hero-bg" src="data:image/{ext};base64,{b64}" alt="CalvertK9" />'
else:
    hero_bg_html = '<div class="home-hero-placeholder"></div>'

render_html(f"""
<div class="home-hero">
    {hero_bg_html}
    <div class="home-hero-content">
        <div class="home-crest">CK9</div>
        <div class="home-hint">Chelmsford, Essex &middot; KC Registered Maltese</div>
        <div class="home-title">CALVERTK9</div>
        <div class="home-sub">
            Home-raised Maltese puppies from health-tested, KC-registered
            parents. Meet Marley, Bertie, and their beautiful litter of seven.
        </div>
        <div class="home-badges">
            <span class="home-badge-pill">KC Registered</span>
            <span class="home-badge-pill">Health Tested</span>
            <span class="home-badge-pill">Home-Raised</span>
        </div>
    </div>
</div>
""")

if not hero_path:
    st.caption("Add images/home_hero.jpg to replace this placeholder with your own photo.")

# ---------------------------------------------------------------------------
# CTA BUTTON — navigates to the puppies page
# ---------------------------------------------------------------------------
render_html('<div class="home-cta-wrap">')
if st.button("Meet the Pups"):
    st.switch_page("pages/1_Meet_the_Puppies.py")
render_html('</div>')