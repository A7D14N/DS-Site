import streamlit as st
import base64
import os

st.set_page_config(
    page_title="CalvertK9 — Home-raised Puppies",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# IMAGE HANDLING
# Put your hero photo in images/home_hero.jpg (or .jpeg / .png / .webp).
# This is separate from images/hero.jpg, which is used by the puppies page.
# Until it's added, a soft placeholder is shown so the page still runs.
# ---------------------------------------------------------------------------

IMG_DIR = os.path.join(os.path.dirname(__file__), "images")
EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp"]


def find_image(name):
    if not os.path.isdir(IMG_DIR):
        return None
    target = name.lower()
    for fname in os.listdir(IMG_DIR):
        stem, ext = os.path.splitext(fname)
        if stem.lower() == target and ext.lower() in EXTENSIONS:
            return os.path.join(IMG_DIR, fname)
    return None


def image_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300..700&family=Inter:wght@300;400;500;600;700&display=swap');

:root{
    --background:#F8F4EE;
    --accent:#AC7A45;
    --accent-dark:#8E5F35;
    --border:#DFD6C9;
}

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
    background:var(--background);
}

#MainMenu{visibility:hidden;}
header[data-testid="stHeader"]{background:transparent;}
footer{visibility:hidden;}
[data-testid="stToolbar"]{display:none;}
[data-testid="stSidebarNav"]{display:none;}
section[data-testid="stSidebar"]{display:none;}

.stApp{background:var(--background);}
.block-container{padding-top:0rem; padding-bottom:0rem; max-width:100%;}

h1,h2,h3,h4{font-family:'Fraunces', serif;}

.home-hero{
    position:relative;
    width:100%;
    height:92vh;
    min-height:560px;
    display:flex;
    align-items:center;
    justify-content:center;
    overflow:hidden;
}
.home-hero-bg{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
    object-fit:cover;
    z-index:0;
}
.home-hero-placeholder{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
    background:linear-gradient(180deg, #C9B79A 0%, #EDE3D4 100%);
    z-index:0;
}
.home-hero::after{
    content:"";
    position:absolute;
    inset:0;
    background:linear-gradient(180deg, rgba(20,16,12,0.42) 0%, rgba(20,16,12,0.5) 100%);
    z-index:1;
}
.home-hero-content{
    position:relative;
    z-index:2;
    text-align:center;
    color:#FFFFFF;
    padding:0 24px;
    max-width:760px;
}
.home-hint{
    font-size:13px;
    letter-spacing:0.1em;
    text-transform:uppercase;
    opacity:0.85;
    margin-bottom:18px;
}
.home-title{
    font-family:'Fraunces', serif;
    font-size:76px;
    font-weight:700;
    letter-spacing:0.03em;
    margin-bottom:22px;
    text-shadow:0 6px 30px rgba(0,0,0,0.35);
}
.home-sub{
    font-size:19px;
    line-height:1.75;
    max-width:560px;
    margin:0 auto;
    text-shadow:0 2px 14px rgba(0,0,0,0.3);
    color:#F5F1EA;
}

.home-cta-wrap{
    display:flex;
    justify-content:center;
    position:relative;
    z-index:3;
    margin-top:-110px;
    padding-bottom:40px;
    background:transparent;
}
.stButton{display:flex; justify-content:center;}
.stButton button{
    background:var(--accent);
    color:#000;
    border:none;
    border-radius:999px;
    padding:18px 46px;
    font-weight:700;
    font-size:16px;
    transition:all 0.2s ease;
}
.stButton button:hover{
    background:var(--accent-dark);
    transform:translateY(-1px);
}

@media (max-width:900px){
    .home-title{font-size:46px;}
    .home-sub{font-size:16px;}
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
hero_path = find_image("home_hero")
if hero_path:
    ext = os.path.splitext(hero_path)[1].lstrip(".")
    b64 = image_to_b64(hero_path)
    hero_bg_html = f'<img class="home-hero-bg" src="data:image/{ext};base64,{b64}" alt="CalvertK9" />'
else:
    hero_bg_html = '<div class="home-hero-placeholder"></div>'

st.markdown(f"""
<div class="home-hero">
    {hero_bg_html}
    <div class="home-hero-content">
        <div class="home-title">CALVERTK9</div>
        <div class="home-sub">
            Home-raised puppies from health-tested parents. Every litter is welcomed
            into family life from day one, and gently cared for until they're ready
            to meet their new home.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

if not hero_path:
    st.caption("Add images/home_hero.jpg to replace this placeholder with your own photo.")

# ---------------------------------------------------------------------------
# CTA BUTTON — navigates to the puppies page
# ---------------------------------------------------------------------------
st.markdown('<div class="home-cta-wrap">', unsafe_allow_html=True)
if st.button("Meet the Pups"):
    st.switch_page("1_Meet_the_Puppies")
st.markdown('</div>', unsafe_allow_html=True)