import streamlit as st
import os

st.set_page_config(
    page_title="CalvertK9 — Home-raised Puppies",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# IMAGE HANDLING
# Put your photos in the "images" folder next to this file, using these
# exact names (any of .jpg / .jpeg / .png is fine):
#   hero.jpg      -> big banner photo (optional)
#   marley.jpg    -> Marley (mum)
#   bertie.jpg    -> Bertie (dad)
#   puppy1.jpg ... puppy7.jpg -> the seven puppies
# If a file isn't found yet, a soft placeholder box is shown instead, so the
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



def photo_block(name, height=280, radius=22, label=None):
    path = find_image(name)

    if path:
        st.image(path, width=min(height, 260))
    else:
        st.markdown(
            f"""
            <div class="img-ph" style="height:{height}px; border-radius:{radius}px;">
                <div class="img-ph-label">
                    Add images/{name}.jpg<br>
                    {label or name}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown("""
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

.hero-wrap{padding:72px 60px 40px 60px; display:flex; gap:48px; align-items:center; flex-wrap:wrap;}
.hero-copy{max-width:580px;}
.hero-badge{display:inline-block; background:var(--surface); color:#000; padding:9px 18px; border-radius:999px; font-size:13px; font-weight:600; letter-spacing:0.12em; margin-bottom:20px; border:1px solid var(--border);}
.hero-title{font-size:54px; line-height:1.04; font-weight:700; margin-bottom:18px; color:#000;}
.hero-sub{font-size:18px; color:#000; line-height:1.7; margin-bottom:30px;}
.hero-actions{display:flex; flex-wrap:wrap; gap:14px; margin-bottom:8px;}

.btn-primary{display:inline-block; background:var(--accent); color:#000!important; padding:16px 34px; border-radius:999px; font-weight:600; text-decoration:none; font-size:15px; transition:all 0.2s ease;}
.btn-primary:hover{background:var(--accent-dark); transform:translateY(-1px);}
.btn-ghost{display:inline-block; padding:16px 34px; border-radius:999px; font-weight:600; text-decoration:none; font-size:15px; border:1.5px solid var(--text); color:var(--text)!important; transition:all 0.2s ease;}
.btn-ghost:hover{background:var(--surface-soft); color:#000!important;}

/* Placeholder boxes (shown until a real photo is added) */
.img-ph{width:100%; display:flex; align-items:center; justify-content:center; height:100%; color:#000; font-weight:600; text-align:center; background:linear-gradient(180deg, #E9E3DA 0%, #F6F1E9 100%); border:1px solid var(--border); position:relative; overflow:hidden;}
.img-ph::before{content:""; position:absolute; inset:0; background:linear-gradient(135deg, rgba(255,255,255,0.45), transparent 50%);}
.img-ph-label{position:relative; z-index:1; font-size:13px; letter-spacing:0.02em; line-height:1.6; padding:0 20px;}

/* Real photo boxes */
.photo-box{width:100%; overflow:hidden; border:1px solid var(--border);}
.photo-box img{width:100%; height:100%; object-fit:cover; display:block;}

.section{padding:78px 60px;}
.section-alt{background:var(--surface);}
.section-kicker{color:var(--accent-dark); font-weight:700; font-size:13px; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:10px;}
.section-title{font-size:36px; font-weight:700; margin-bottom:14px; max-width:680px; color:#000;}
.section-sub{color:#000; font-size:16px; max-width:620px; line-height:1.68; margin-bottom:18px;}

.card{background:var(--surface); border-radius:24px; padding:24px; border:1px solid var(--border); height:100%; transition:transform 0.2s ease, box-shadow 0.2s ease;}
.card:hover{transform:translateY(-4px); box-shadow:0 20px 40px rgba(30,25,20,0.08);}
.tag{display:inline-block; background:var(--accent); color:#000; font-size:11.5px; font-weight:700; padding:6px 14px; border-radius:999px; letter-spacing:0.03em; margin-bottom:14px;}
.tag-muted{background:var(--surface-soft); color:#000;}
.dog-name{font-family:'Fraunces', serif; font-size:24px; font-weight:700; margin:16px 0 6px 0; color:#000;}
.dog-meta{color:#000; font-size:14.5px; margin-bottom:10px; line-height:1.7;}

.puppy-grid{display:flex; flex-wrap:wrap; gap:24px; justify-content:center;}
.puppy-card{flex:0 0 30%; min-width:220px;}
.puppy-name{font-family:'Fraunces', serif; font-size:19px; font-weight:700; margin:14px 0 4px 0; color:#000;}
.puppy-meta{color:#000; font-size:13.5px;}
.badge-available{display:inline-block; background:#DCE8DC; color:#2F5A2F; font-size:11.5px; font-weight:700; padding:4px 12px; border-radius:999px; margin-top:8px;}
.badge-reserved{display:inline-block; background:#EDE0D3; color:#8E5F35; font-size:11.5px; font-weight:700; padding:4px 12px; border-radius:999px; margin-top:8px;}

.feature-row{display:flex; gap:16px; margin-bottom:22px; align-items:flex-start;}
.feature-badge{width:46px; height:46px; border-radius:18px; background:var(--surface-soft); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--accent-dark);}
.feature-title{font-weight:700; font-size:16px; margin-bottom:6px; color:#000;}
.feature-desc{color:#000; font-size:14.5px; line-height:1.7;}

.contact-wrap{background:var(--surface); border-radius:28px; padding:56px; color:#000;}
.contact-wrap h2{color:#000;}
.contact-wrap p{color:#000;}
.stButton button{background:var(--accent); color:#000; border:none; border-radius:999px; padding:14px 32px; font-weight:700;}
.stButton button:hover{background:var(--accent-dark);}

.footer{padding:44px 60px; text-align:center; color:var(--text-muted); font-size:13.5px; border-top:1px solid var(--border);}
.footer b{color:var(--text);}

@media (max-width:900px){
    .hero-title{font-size:38px;}
    .navbar, .hero-wrap, .section{padding-left:24px; padding-right:24px;}
    .nav-links{display:none;}
    .puppy-card{flex:0 0 100%;}
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# NAVBAR
# ---------------------------------------------------------------------------
st.markdown("""
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
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 0.95], gap="large")

with col1:
    st.markdown("""
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
    """, unsafe_allow_html=True)

with col2:
    photo_block("hero", height=260, label="Hero photo")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# MEET THE PARENTS
# ---------------------------------------------------------------------------
st.markdown('<div id="parents" class="section">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">Meet the Parents</div>
<div class="section-title">Marley and Bertie</div>
<div class="section-sub">Loved family dogs and the proud parents of this litter.</div>
""", unsafe_allow_html=True)

colM, colB = st.columns(2, gap="large")

with colM:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        photo_block("marley", height=220, label="Marley")
        st.markdown("""
            <span class="tag">Mum</span>
            <div class="dog-name">Marley</div>
            <div class="dog-meta">A gentle, affectionate mum who has taken wonderful care of her litter.</div>
            <div class="dog-meta"><strong>Health:</strong> Add health testing details here.</div>
        </div>
        """, unsafe_allow_html=True)

with colB:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        photo_block("bertie", height=220, label="Bertie")
        st.markdown("""
            <span class="tag tag-muted">Dad</span>
            <div class="dog-name">Bertie</div>
            <div class="dog-meta">A friendly, easy-going dad with a lovely temperament.</div>
            <div class="dog-meta"><strong>Health:</strong> Add health testing details here.</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# MEET THE PUPPIES
# ---------------------------------------------------------------------------
st.markdown('<div id="puppies" class="section section-alt">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">Meet the Puppies</div>
<div class="section-title">Marley and Bertie's litter</div>
<div class="section-sub">Seven happy, home-raised puppies. Get in touch if one has caught your eye.</div>
""", unsafe_allow_html=True)

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

st.markdown('<div class="puppy-grid">', unsafe_allow_html=True)
for p in puppies:
    badge = ""
    if p["status"].lower() == "available":
        badge = '<span class="badge-available">Available</span>'
    elif p["status"].lower() == "reserved":
        badge = '<span class="badge-reserved">Reserved</span>'

    meta = " · ".join([v for v in [p["gender"]] if v])

    with st.container():
        st.markdown('<div class="puppy-card">', unsafe_allow_html=True)
        st.markdown('<div class="card" style="padding:16px;">', unsafe_allow_html=True)
        photo_block(p['key'], height=160, radius=16, label=p['name'])
        st.markdown(f"""
            <div class="puppy-name">{p['name']}</div>
            <div class="puppy-meta">{meta}</div>
            {badge}
        </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">About CalvertK9</div>
<div class="section-title">A family-raised litter, cared for from day one</div>
<div class="section-sub">
    Marley and Bertie's puppies have been raised at home, surrounded by family life
    from birth. We're happy to answer any questions about their upbringing, health
    and temperament.
</div>
""", unsafe_allow_html=True)

features = [
    ("Raised at home", "The puppies have grown up as part of our family, not in a kennel."),
    ("Socialised early", "Handled daily and gently introduced to everyday household life."),
    ("Happy and healthy", "Well-fed, well-loved, and ready for their new homes."),
]
for title, desc in features:
    st.markdown(f"""
    <div class="feature-row">
        <div class="feature-badge">•</div>
        <div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
st.markdown('<div id="contact" class="section section-alt">', unsafe_allow_html=True)
st.markdown('<div class="contact-wrap">', unsafe_allow_html=True)

colL, colR = st.columns([1, 1], gap="large")
with colL:
    st.markdown("""
    <div class="section-kicker">Contact</div>
    <h2 style="font-size:32px; margin-bottom:14px;">Interested in one of our puppies?</h2>
    <p style="font-size:15px; line-height:1.7; max-width:460px; margin-bottom:26px;">
        Get in touch and we'll be happy to answer any questions.
    </p>
    <p style="font-size:14.5px; margin-bottom:6px;">CalvertK9</p>
    <p style="font-size:14.5px;">Email: hello@calvertk9.co.uk</p>
    """, unsafe_allow_html=True)

with colR:
    with st.form('enquiry_form'):
        st.text_input('Full name', placeholder='Jane Doe')
        st.text_input('Email address', placeholder='name@example.com')
        st.selectbox('I am interested in', ['A specific puppy', 'General enquiry'])
        st.text_area('Message', placeholder='Tell us which puppy you are interested in', height=120)
        submitted = st.form_submit_button('Send enquiry')
        if submitted:
            st.success('Thank you — we will reply as soon as possible.')

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <b>CalvertK9</b> — Home-raised puppies from health-tested parents.
</div>
""", unsafe_allow_html=True)