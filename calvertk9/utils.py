"""
Shared helpers for the CalvertK9 site.

Both Home.py and pages/1_Meet_the_Puppies.py import from here, so the image
lookup, the whitespace-safe HTML renderer, and the design system (colors,
type, components) only live in one place.
"""

import base64
import os

import streamlit as st

# images/ sits next to this file (project root), regardless of which page
# imports it — this is more reliable than counting os.path.dirname() calls
# based on how deep the calling file happens to be nested.
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(APP_ROOT, "images")
EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp"]


def find_image(name):
    """Look up images/<name>.(jpg|jpeg|png|webp), case-insensitive."""
    if not os.path.isdir(IMG_DIR):
        return None
    target = name.lower()
    for fname in os.listdir(IMG_DIR):
        stem, ext = os.path.splitext(fname)
        if stem.lower() == target and ext.lower() in EXTENSIONS:
            return os.path.join(IMG_DIR, fname)
    return None


def render_html(html):
    """st.markdown(..., unsafe_allow_html=True) but safe against Python
    source indentation.

    If the HTML string is built inside a for-loop or a `with column:` block,
    it inherits that Python indentation. Markdown treats any line indented
    4+ spaces as a code block, so a stray closing tag like `</div>` gets
    printed as literal text instead of being rendered. Stripping leading
    whitespace from every line avoids that.
    """
    lines = [line.lstrip() for line in html.strip().split("\n")]
    st.markdown("\n".join(lines), unsafe_allow_html=True)


def photo_block(name, height=280, radius=14, overlay_html=""):
    """Render a photo in a clean rounded box.

    overlay_html lets you stamp a small tag or badge on top of the photo
    (e.g. a "Sire" label, an "Available" pill) instead of listing it below
    the image, which keeps cards compact.

    Falls back to a plain, empty box (no filename/text shown) if the photo
    hasn't been added to images/ yet.
    """
    path = find_image(name)

    if path:
        ext = os.path.splitext(path)[1].lower()
        mime = {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".webp": "image/webp",
        }[ext]
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        img_tag = f'<img src="data:{mime};base64,{encoded}" alt="{name}" />'
    else:
        img_tag = ""

    return (
        f'<div class="photo-box" style="height:{height}px; border-radius:{radius}px;">'
        f"{img_tag}{overlay_html}"
        f"</div>"
    )


BASE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,400..600&family=Inter:wght@400;500;600;700&display=swap');

:root{
    --ink:#1E231C;
    --ink-soft:#5B6154;
    --paper:#FAF6ED;
    --paper-dim:#F0E8D6;
    --surface:#FFFFFF;
    --brass:#9C7A2A;
    --brass-deep:#7A5E20;
    --line:#DED2AE;
    --good:#3E6B4A;
    --good-bg:#E3EDE0;
    --hold:#8C5A26;
    --hold-bg:#F1E4D2;
}

html, body, [class*="css"]{ font-family:'Inter', sans-serif; color:var(--ink); background:var(--paper); }
#MainMenu{visibility:hidden;}
header[data-testid="stHeader"]{background:transparent;}
footer{visibility:hidden;}
[data-testid="stToolbar"]{display:none;}
[data-testid="stSidebarNav"]{display:none;}
section[data-testid="stSidebar"]{display:none;}
.stApp{background:var(--paper);}
.block-container{padding-top:0rem; padding-bottom:0rem; max-width:100%;}
h1,h2,h3,h4{font-family:'Fraunces', serif; letter-spacing:-0.01em;}

/* Navbar */
.navbar{display:flex; justify-content:space-between; align-items:center; padding:18px 56px;}
.nav-logo-wrap{display:flex; align-items:center; gap:10px; text-decoration:none;}
.crest{width:32px; height:32px; border-radius:50%; border:1.5px solid var(--ink); display:flex; align-items:center; justify-content:center; font-family:'Fraunces', serif; font-weight:700; font-size:10px; letter-spacing:0.02em; color:var(--ink); flex-shrink:0;}
.nav-logo{font-family:'Fraunces', serif; font-size:22px; font-weight:700; color:var(--ink);}
.nav-links a{margin-left:28px; text-decoration:none; color:var(--ink); font-weight:500; font-size:14.5px; transition:color 0.15s ease;}
.nav-links a:hover{color:var(--brass-deep);}
.nav-cta{background:var(--brass); color:var(--ink)!important; padding:10px 22px; border-radius:999px; font-weight:600!important;}
.nav-cta:hover{background:var(--brass-deep); color:var(--paper)!important;}

/* Trust strip */
.trust-strip{display:flex; flex-wrap:wrap; justify-content:center; background:var(--paper-dim); border-top:1px solid var(--line); border-bottom:1px solid var(--line);}
.trust-item{padding:10px 24px; font-size:12px; font-weight:600; color:var(--ink-soft); text-transform:uppercase; letter-spacing:0.05em; border-right:1px solid var(--line);}
.trust-item:last-child{border-right:none;}

/* Hero (puppies page) */
.hero-wrap{padding:52px 56px 8px 56px; display:flex; gap:56px; align-items:flex-start; flex-wrap:wrap;}
.hero-badge{display:inline-block; background:var(--surface); color:var(--ink-soft); padding:8px 16px; border-radius:999px; font-size:12px; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:18px; border:1px solid var(--line);}
.hero-title{font-size:46px; line-height:1.06; font-weight:700; margin-bottom:14px; color:var(--ink);}
.hero-sub{font-size:16.5px; color:var(--ink-soft); line-height:1.7; margin-bottom:26px; max-width:480px;}
.hero-actions{display:flex; flex-wrap:wrap; gap:12px;}
.hero-stats{display:flex; gap:34px; margin-top:32px; padding-top:22px; border-top:1px solid var(--line); flex-wrap:wrap;}
.stat-num{font-family:'Fraunces', serif; font-size:24px; font-weight:700; color:var(--ink);}
.stat-label{font-size:11.5px; color:var(--ink-soft); text-transform:uppercase; letter-spacing:0.06em; margin-top:2px;}

.btn-primary{display:inline-block; background:var(--brass); color:var(--ink)!important; padding:14px 30px; border-radius:999px; font-weight:600; text-decoration:none; font-size:14.5px; transition:all 0.15s ease;}
.btn-primary:hover{background:var(--brass-deep); color:var(--paper)!important; transform:translateY(-1px);}
.btn-ghost{display:inline-block; padding:14px 30px; border-radius:999px; font-weight:600; text-decoration:none; font-size:14.5px; border:1.5px solid var(--ink); color:var(--ink)!important; transition:all 0.15s ease;}
.btn-ghost:hover{background:var(--paper-dim);}

/* Photo boxes */
.photo-box{position:relative; width:100%; overflow:hidden; background:linear-gradient(180deg, #ECE4CF 0%, #F6F1E4 100%); border:1px solid var(--line);}
.photo-box img{width:100%; height:100%; object-fit:cover; display:block;}
.photo-tag{position:absolute; top:12px; left:12px; background:var(--ink); color:var(--paper); font-family:'Fraunces', serif; font-style:italic; font-size:12.5px; padding:4px 12px; border-radius:999px; letter-spacing:0.02em;}
.photo-badge{position:absolute; top:12px; right:12px; font-size:10.5px; font-weight:700; padding:5px 11px; border-radius:999px; letter-spacing:0.03em; text-transform:uppercase;}
.badge-available{background:var(--good-bg); color:var(--good);}
.badge-reserved{background:var(--hold-bg); color:var(--hold);}

/* Sections */
.section{padding:52px 56px; border-top:1px solid var(--line);}
.section-alt{background:var(--surface);}
.section-kicker{color:var(--brass-deep); font-weight:700; font-size:12px; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:8px;}
.section-title{font-size:30px; font-weight:700; margin-bottom:10px; max-width:680px; color:var(--ink);}
.section-sub{color:var(--ink-soft); font-size:15px; max-width:600px; line-height:1.65; margin-bottom:6px;}

/* Cards */
.card{background:var(--surface); border-radius:12px; padding:20px; border:1px solid var(--line); height:100%;}
.dog-name{font-family:'Fraunces', serif; font-size:21px; font-weight:700; margin:16px 0 6px 0; color:var(--ink);}
.dog-meta{color:var(--ink-soft); font-size:13.5px; margin-bottom:8px; line-height:1.6;}
.dog-meta strong{color:var(--ink);}

.puppy-grid{display:grid; grid-template-columns:repeat(3, 1fr); gap:18px;}
.puppy-name{font-family:'Fraunces', serif; font-size:16.5px; font-weight:700; margin:14px 0 2px 0; color:var(--ink);}
.puppy-meta{color:var(--ink-soft); font-size:12.5px;}

/* About / feature grid — hairline "spec sheet" look, no numbering since
   these three points aren't a sequence */
.feature-grid{display:grid; grid-template-columns:repeat(3, 1fr); gap:1px; background:var(--line); border:1px solid var(--line); border-radius:12px; overflow:hidden; margin-top:10px;}
.feature-box{background:var(--surface); padding:26px 24px; position:relative;}
.feature-box::before{content:""; position:absolute; top:24px; left:24px; width:26px; height:2px; background:var(--brass);}
.feature-title{font-weight:700; font-size:15px; margin:16px 0 6px 0; color:var(--ink);}
.feature-desc{color:var(--ink-soft); font-size:13.5px; line-height:1.65;}

/* Health & documents checklist */
.health-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1px; background:var(--line); border:1px solid var(--line); border-radius:12px; overflow:hidden; margin-top:16px;}
.health-item{background:var(--surface); padding:18px 20px; display:flex; align-items:center; gap:12px; font-size:14px; color:var(--ink); font-weight:500;}
.health-check{width:22px; height:22px; border-radius:50%; background:var(--good-bg); color:var(--good); display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:700; flex-shrink:0;}

/* Contact */
.contact-card{background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:36px; margin-top:8px;}
.contact-phone{font-size:14.5px; color:var(--ink-soft); margin-top:14px;}
.contact-phone strong{color:var(--ink);}
.stButton button{background:var(--brass); color:var(--ink); border:none; border-radius:999px; padding:12px 28px; font-weight:700; font-size:14px;}
.stButton button:hover{background:var(--brass-deep); color:var(--paper);}

/* Footer */
.footer{padding:36px 56px; text-align:center; color:var(--ink-soft); font-size:13px; border-top:1px solid var(--line);}
.footer b{color:var(--ink);}

/* Home page — full-bleed hero */
.home-hero{position:relative; width:100%; height:92vh; min-height:560px; display:flex; align-items:center; justify-content:center; overflow:hidden;}
.home-hero-bg{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0;}
.home-hero-placeholder{position:absolute; inset:0; width:100%; height:100%; background:linear-gradient(180deg, #C9B79A 0%, #EDE3D4 100%); z-index:0;}
.home-hero::after{content:""; position:absolute; inset:0; background:linear-gradient(180deg, rgba(20,16,12,0.38) 0%, rgba(20,16,12,0.55) 100%); z-index:1;}
.home-hero-content{position:relative; z-index:2; text-align:center; color:#FFFFFF; padding:0 24px; max-width:720px;}
.home-crest{width:52px; height:52px; border-radius:50%; border:1.5px solid rgba(255,255,255,0.85); display:flex; align-items:center; justify-content:center; font-family:'Fraunces', serif; font-weight:700; font-size:15px; letter-spacing:0.02em; margin:0 auto 22px auto;}
.home-hint{font-size:12.5px; letter-spacing:0.14em; text-transform:uppercase; opacity:0.9; margin-bottom:16px;}
.home-title{font-family:'Fraunces', serif; font-size:60px; font-weight:700; letter-spacing:0.02em; margin-bottom:18px; text-shadow:0 6px 30px rgba(0,0,0,0.35);}
.home-sub{font-size:17px; line-height:1.7; max-width:540px; margin:0 auto; text-shadow:0 2px 14px rgba(0,0,0,0.3); color:#F5F1EA;}
.home-badges{display:flex; justify-content:center; gap:10px; flex-wrap:wrap; margin-top:24px;}
.home-badge-pill{background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.4); color:#fff; font-size:11.5px; font-weight:600; letter-spacing:0.05em; text-transform:uppercase; padding:6px 14px; border-radius:999px;}
.home-cta-wrap{display:flex; justify-content:center; position:relative; z-index:3; margin-top:-108px; padding-bottom:36px;}

@media (max-width:900px){
    .hero-title{font-size:32px;}
    .home-title{font-size:40px;}
    .navbar, .hero-wrap, .section{padding-left:22px; padding-right:22px;}
    .nav-links{display:none;}
    .puppy-grid{grid-template-columns:1fr 1fr;}
    .feature-grid{grid-template-columns:1fr;}
}
@media (max-width:560px){
    .puppy-grid{grid-template-columns:1fr;}
}
</style>
"""


def inject_base_styles():
    render_html(BASE_CSS)