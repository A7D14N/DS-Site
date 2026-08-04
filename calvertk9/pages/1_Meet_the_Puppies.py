import base64
import os

import streamlit as st

st.set_page_config(
    page_title="CalvertK9 — Home-raised Puppies",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# IMAGE HANDLING
# Put your photos in the "images" folder next to this file, using these
# exact names (any of .jpg / .jpeg / .png / .webp is fine):
#   hero.jpg      -> big banner photo (optional)
#   marley.jpg    -> Marley (mum)
#   bertie.jpg    -> Bertie (dad)
#   puppy1.jpg ... puppy7.jpg -> the seven puppies
# If a file isn't found yet, a soft blank box is shown instead, so the
# site always runs — just drop photos in later and refresh.
# ---------------------------------------------------------------------------

IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")
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


def render_html(html):
    """st.markdown(..., unsafe_allow_html=True) but safe against Python
    source indentation. If the HTML we build is indented (because it sits
    inside a for-loop or a `with column:` block), Markdown treats those
    leading spaces as a code block and prints tags like `</div>` as literal
    text instead of rendering them. Stripping leading whitespace from every
    line avoids that.
    """
    lines = [line.lstrip() for line in html.strip().split("\n")]
    st.markdown("\n".join(lines), unsafe_allow_html=True)


def photo_block(name, height=280, radius=22):
    """Renders a clean, fixed-size photo in a rounded box.
    Falls back to a plain empty box (no text/paths shown) if the photo
    hasn't been added yet.
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
        img_tag = f'<img src="data:{mime};base64,{encoded}" style="width:100%; height:100%; object-fit:cover; display:block;" />'
    else:
        img_tag = ""

    return (
        f'<div class="photo-box" style="height:{height}px; border-radius:{radius}px;">'
        f"{img_tag}"
        f"</div>"
    )


render_html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300..700&family=Inter:wght@300;400;500;600;700&display=swap');

:root{
    --background:#F8F4EE;
    --surface:#FFFFFF;
    --surface-soft:#F2ECE4;
    --text:#26221D;
    --text-muted:#6D655E;
    --accent:#AC7A45;
    --accent-dark:#8E5F35;
    --border:#DFD6C9;
}

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
    color:var(--text);
    background:var(--background);
}

#MainMenu{visibility:hidden;}
header[data-testid="stHeader"]{background:transparent;}
footer{visibility:hidden;}
[data-testid="stToolbar"]{display:none;}

.stApp{background:var(--background);}
.block-container{padding-top:0rem; padding-bottom:0rem; max-width:100%;}

h1,h2,h3,h4{font-family:'Fraunces', serif; letter-spacing:-0.02em;}

.navbar{display:flex; justify-content:space-between; align-items:center; padding:24px 60px; background:transparent;}
.nav-logo{font-family:'Fraunces', serif; font-size:26px; font-weight:700; color:var(--text); text-decoration:none;}
.nav-links a{margin-left:30px; text-decoration:none; color:#000; font-weight:500; font-size:15px; transition:color 0.2s ease;}
.nav-links a:hover{color:var(--accent-dark);}
.nav-cta{background:var(--accent); color:#000!important; padding:12px 26px; border-radius:999px; font-weight:600!important;}
.nav-cta:hover{background:var(--accent-dark)!important;}

.hero-wrap{padding:72px 56px 40px 56px; display:flex; gap:64px; align-items:flex-start; flex-wrap:wrap;}
.hero-copy{max-width:650px;}
.hero-badge{display:inline-block; background:var(--surface); color:#000; padding:9px 18px; border-radius:999px; font-size:13px; font-weight:600; letter-spacing:0.12em; margin-bottom:20px; border:1px solid var(--border);}
.hero-title{font-size:58px; line-height:1.02; font-weight:700; margin-bottom:18px; color:#000;}
.hero-sub{font-size:19px; color:#000; line-height:1.7; margin-bottom:30px;}
.hero-actions{display:flex; flex-wrap:wrap; gap:14px; margin-bottom:8px;}

.btn-primary{display:inline-block; background:var(--accent); color:#000!important; padding:16px 34px; border-radius:999px; font-weight:600; text-decoration:none; font-size:15px; transition:all 0.2s ease;}
.btn-primary:hover{background:var(--accent-dark); transform:translateY(-1px);}
.btn-ghost{display:inline-block; padding:16px 34px; border-radius:999px; font-weight:600; text-decoration:none; font-size:15px; border:1.5px solid var(--text); color:var(--text)!important; transition:all 0.2s ease;}
.btn-ghost:hover{background:var(--surface-soft); color:#000!important;}

/* Photo boxes — clean rounded box, image fills it, plain background if no image yet */
.photo-box{width:100%; height:100%; overflow:hidden; background:linear-gradient(180deg, #E9E3DA 0%, #F6F1E9 100%); border:1px solid var(--border);}
.photo-box img{width:100%; height:100%; object-fit:cover; display:block;}

.card{overflow:hidden;}

.section{padding:78px 60px;}
.section-alt{background:var(--surface);}
.section-kicker{color:var(--accent-dark); font-weight:700; font-size:13px; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:10px;}
.section-title{font-size:36px; font-weight:700; margin-bottom:14px; max-width:680px; color:#000;}
.section-sub{color:#000; font-size:16px; max-width:620px; line-height:1.68; margin-bottom:18px;}

.card{background:var(--surface); border-radius:24px; padding:18px; border:1px solid var(--border); height:100%;}
.tag{display:inline-block; background:var(--accent); color:#000; font-size:11px; font-weight:700; padding:5px 12px; border-radius:999px; letter-spacing:0.03em; margin-bottom:12px;}
.tag-muted{background:var(--surface-soft); color:#000;}
.dog-name{font-family:'Fraunces', serif; font-size:22px; font-weight:700; margin:14px 0 6px 0; color:#000;}
.dog-meta{color:#000; font-size:14px; margin-bottom:10px; line-height:1.65;}

.puppy-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:18px; justify-items:center; width:100%; max-width:1100px; margin:0 auto;}
.puppy-card{width:100%; min-width:0;}
.puppy-name{font-family:'Fraunces', serif; font-size:17px; font-weight:700; margin:12px 0 4px 0; color:#000;}
.puppy-meta{color:#000; font-size:13px;}
.badge-available{display:inline-block; background:#DCE8DC; color:#2F5A2F; font-size:11px; font-weight:700; padding:4px 10px; border-radius:999px; margin-top:8px;}
.badge-reserved{display:inline-block; background:#EDE0D3; color:#8E5F35; font-size:11px; font-weight:700; padding:4px 10px; border-radius:999px; margin-top:8px;}

.feature-row{display:flex; gap:16px; margin-bottom:22px; align-items:flex-start;}
.feature-badge{width:46px; height:46px; border-radius:18px; background:var(--surface-soft); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--accent-dark);}
.feature-title{font-weight:700; font-size:16px; margin-bottom:6px; color:#000;}
.feature-desc{color:#000; font-size:14.5px; line-height:1.7;}

.contact-simple{text-align:center; padding:20px 0 10px 0;}
.contact-phone{font-size:16px; margin-top:18px; color:#000;}
.contact-phone strong{color:#000;}

.footer{padding:44px 60px; text-align:center; color:var(--text-muted); font-size:13.5px; border-top:1px solid var(--border);}
.footer b{color:var(--text);}

@media (max-width:900px){
    .hero-title{font-size:38px;}
    .navbar, .hero-wrap, .section{padding-left:24px; padding-right:24px;}
    .nav-links{display:none;}
    .puppy-card{flex:0 0 100%;}
}
</style>
""")

# ---------------------------------------------------------------------------
# NAVBAR
# ---------------------------------------------------------------------------
render_html("""
<div class="navbar">
    <a href="#top" class="nav-logo">CalvertK9</a>
    <div class="nav-links">
        <a href="#parents">Parents</a>
        <a href="#puppies">Puppies</a>
        <a href="#about">About</a>
        <a href="#contact" class="nav-cta">Contact</a>
    </div>
</div>
<div id="top"></div>
""")

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
render_html('<div class="hero-wrap">')
col1, col2 = st.columns([1.1, 1], gap="large")

with col1:
    render_html("""
    <div class="hero-badge">Home-raised · Health-tested parents</div>
    <div class="hero-title">CalvertK9</div>
    <div class="hero-sub">
        Home-raised puppies from health-tested parents.<br>
        Meet Marley, Bertie and their beautiful litter.
    </div>
    <div class="hero-actions">
        <a href="#puppies" class="btn-primary">Meet the puppies</a>
        <a href="#contact" class="btn-ghost">Get in touch</a>
    </div>
    """)

with col2:
    render_html(photo_block("hero", height=520))

render_html('</div>')

# ---------------------------------------------------------------------------
# MEET THE PARENTS
# ---------------------------------------------------------------------------
render_html('<div id="parents" class="section">')
render_html("""
<div class="section-kicker">Meet the Parents</div>
<div class="section-title">Marley and Bertie</div>
<div class="section-sub">Loved family dogs and the proud parents of this litter.</div>
""")

colM, colB = st.columns(2, gap="large")

with colM:
    render_html(f"""
        <div class="card" style="padding:28px;">
            {photo_block("marley", height=420)}
            <span class="tag">Mum</span>
            <div class="dog-name">Marley</div>
            <div class="dog-meta">A gentle, affectionate mum who has taken wonderful care of her litter.</div>
            <div class="dog-meta"><strong>Health:</strong> Add health testing details here.</div>
        </div>
    """)

with colB:
    render_html(f"""
        <div class="card" style="padding:28px;">
            {photo_block("bertie", height=420)}
            <span class="tag tag-muted">Dad</span>
            <div class="dog-name">Bertie</div>
            <div class="dog-meta">A friendly, easy-going dad with a lovely temperament.</div>
            <div class="dog-meta"><strong>Health:</strong> Add health testing details here.</div>
        </div>
    """)

render_html('</div>')

# ---------------------------------------------------------------------------
# MEET THE PUPPIES
# ---------------------------------------------------------------------------
render_html('<div id="puppies" class="section section-alt">')
render_html("""
<div class="section-kicker">Meet the Puppies</div>
<div class="section-title">Marley and Bertie's litter</div>
<div class="section-sub">Seven happy, home-raised puppies. Get in touch if one has caught your eye.</div>
""")

# Edit the details below once puppies are named / have known genders or status.
puppies = [
    {"key": "puppy1", "name": "Puppy 1", "gender": "", "status": ""},
    {"key": "puppy2", "name": "Puppy 2", "gender": "", "status": ""},
    {"key": "puppy3", "name": "Puppy 3", "gender": "", "status": ""},
    {"key": "puppy4", "name": "Puppy 4", "gender": "", "status": ""},
    {"key": "puppy5", "name": "Puppy 5", "gender": "", "status": ""},
    {"key": "puppy6", "name": "Puppy 6", "gender": "", "status": ""},
    {"key": "puppy7", "name": "Puppy 7", "gender": "", "status": ""},
]

PUPPY_COLS = 3
for i in range(0, len(puppies), PUPPY_COLS):
    row = puppies[i:i + PUPPY_COLS]
    # Always create the full number of columns, even on the last, shorter
    # row — otherwise a lone puppy (e.g. puppy 7) gets a column that
    # stretches to the full row width and looks oversized.
    cols = st.columns(PUPPY_COLS, gap="large")
    for idx, col in enumerate(cols):
        if idx >= len(row):
            continue  # leave this column empty to preserve equal widths

        p = row[idx]
        badge = ""
        if p["status"].lower() == "available":
            badge = '<span class="badge-available">Available</span>'
        elif p["status"].lower() == "reserved":
            badge = '<span class="badge-reserved">Reserved</span>'

        meta = " · ".join([v for v in [p["gender"]] if v])

        with col:
            render_html(f"""
                <div class="card" style="padding:22px;">
                    {photo_block(p['key'], height=200, radius=16)}
                    <div style="margin-top:18px;">
                        <div class="puppy-name">{p['name']}</div>
                        <div class="puppy-meta">{meta}</div>
                        {badge}
                    </div>
                </div>
            """)

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
render_html('<div id="about" class="section">')
render_html("""
<div class="section-kicker">About CalvertK9</div>
<div class="section-title">A family-raised litter, cared for from day one</div>
<div class="section-sub">
    Marley and Bertie's puppies have been raised at home, surrounded by family life
    from birth. We're happy to answer any questions about their upbringing, health
    and temperament.
</div>
""")

features = [
    ("Raised at home", "The puppies have grown up as part of our family, not in a kennel."),
    ("Socialised early", "Handled daily and gently introduced to everyday household life."),
    ("Happy and healthy", "Well-fed, well-loved, and ready for their new homes."),
]
for title, desc in features:
    render_html(f"""
    <div class="feature-row">
        <div class="feature-badge">•</div>
        <div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
    </div>
    """)

render_html('</div>')

# ---------------------------------------------------------------------------
# CONTACT — simple: just a button and a phone number
# ---------------------------------------------------------------------------
render_html('<div id="contact" class="section section-alt">')

render_html("""
<div class="contact-simple">
    <a href="mailto:replacewithrealemail@gmail.com" class="btn-primary" style="display:inline-flex; align-items:center; gap:10px;">
        📧 Contact us
    </a>
    <div class="contact-phone">Or call us directly at <strong>07777777777</strong></div>
</div>
""")

render_html('</div>')

render_html("""
<div class="footer">
    <b>CalvertK9</b> — Home-raised puppies from health-tested parents.
</div>
""")