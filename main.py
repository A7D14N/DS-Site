import streamlit as st

st.set_page_config(
    page_title="Calvert Canine Pets — Parent Dogs & Litters",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
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
.nav-links a{margin-left:30px; text-decoration:none; color:var(--text-muted); font-weight:500; font-size:15px; transition:color 0.2s ease;}
.nav-links a:hover{color:var(--accent-dark);}
.nav-cta{background:var(--accent); color:white!important; padding:12px 26px; border-radius:999px; font-weight:600!important;}
.nav-cta:hover{background:var(--accent-dark)!important;}

.hero-wrap{padding:72px 60px 40px 60px; display:flex; gap:48px; align-items:center; flex-wrap:wrap;}
.hero-copy{max-width:580px;}
.hero-badge{display:inline-block; background:var(--surface); color:var(--text-muted); padding:9px 18px; border-radius:999px; font-size:13px; font-weight:600; letter-spacing:0.12em; margin-bottom:20px; border:1px solid var(--border);}
.hero-title{font-size:54px; line-height:1.04; font-weight:700; margin-bottom:18px;}
.hero-sub{font-size:18px; color:var(--text-muted); line-height:1.7; margin-bottom:30px;}
.hero-actions{display:flex; flex-wrap:wrap; gap:14px; margin-bottom:34px;}
.hero-stats{display:flex; gap:32px; flex-wrap:wrap;}
.stat-block{display:flex; flex-direction:column; gap:8px;}
.stat-number{font-family:'Fraunces', serif; font-size:30px; font-weight:700; color:var(--accent-dark);}
.stat-label{font-size:14px; color:var(--text-muted);}

.btn-primary{display:inline-block; background:var(--accent); color:white!important; padding:16px 34px; border-radius:999px; font-weight:600; text-decoration:none; font-size:15px; transition:all 0.2s ease;}
.btn-primary:hover{background:var(--accent-dark); transform:translateY(-1px);}
.btn-ghost{display:inline-block; padding:16px 34px; border-radius:999px; font-weight:600; text-decoration:none; font-size:15px; border:1.5px solid var(--text); color:var(--text)!important; transition:all 0.2s ease;}
.btn-ghost:hover{background:var(--text); color:var(--surface)!important;}

.img-ph{width:100%; border-radius:22px; display:flex; align-items:center; justify-content:center; height:100%; min-height:220px; color:var(--text-muted); font-weight:700; text-align:center; background:linear-gradient(180deg, #E9E3DA 0%, #F6F1E9 100%); border:1px solid var(--border); position:relative;}
.img-ph::before{content:""; position:absolute; inset:0; background:linear-gradient(135deg, rgba(255,255,255,0.45), transparent 50%); border-radius:22px;}
.img-ph-label{position:relative; z-index:1; font-size:14px; letter-spacing:0.12em; text-transform:uppercase;}

.section{padding:78px 60px;}
.section-alt{background:var(--surface);}
.section-kicker{color:var(--accent-dark); font-weight:700; font-size:13px; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:10px;}
.section-title{font-size:36px; font-weight:700; margin-bottom:14px; max-width:680px;}
.section-sub{color:var(--text-muted); font-size:16px; max-width:560px; line-height:1.68; margin-bottom:18px;}

.card{background:var(--surface); border-radius:24px; padding:24px; border:1px solid var(--border); height:100%; transition:transform 0.2s ease, box-shadow 0.2s ease;}
.card:hover{transform:translateY(-4px); box-shadow:0 20px 40px rgba(30,25,20,0.08);}
.tag{display:inline-block; background:var(--accent); color:white; font-size:11.5px; font-weight:700; padding:6px 14px; border-radius:999px; letter-spacing:0.03em; margin-bottom:14px;}
.tag-muted{background:var(--surface-soft); color:var(--text-muted);}
.dog-name{font-family:'Fraunces', serif; font-size:22px; font-weight:700; margin:10px 0 6px 0;}
.dog-meta{color:var(--text-muted); font-size:14px; margin-bottom:10px; line-height:1.65;}
.dog-price{font-weight:700; font-size:16px; color:var(--accent-dark); margin-bottom:14px;}
.mini-link{color:var(--accent-dark); font-weight:600; font-size:14px; text-decoration:none; border-bottom:2px solid transparent; transition:border-color 0.2s ease;}
.mini-link:hover{border-color:var(--accent-dark);}

.feature-row{display:flex; gap:16px; margin-bottom:22px; align-items:flex-start;}
.feature-badge{width:46px; height:46px; border-radius:18px; background:var(--surface-soft); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--accent-dark);}
.feature-title{font-weight:700; font-size:16px; margin-bottom:6px;}
.feature-desc{color:var(--text-muted); font-size:14.5px; line-height:1.7;}

.contact-wrap{background:var(--text); border-radius:28px; padding:56px; color:var(--surface);}
.contact-wrap h2{color:var(--surface);}
.contact-wrap p{color:#D8CFC6;}
.contact-input, .contact-textarea{background:#2D2A27!important; color:var(--surface)!important; border-radius:14px!important; border:1px solid #4A443D!important;}
.contact-label{color:#C8BFB6!important; font-weight:500!important; font-size:14px!important;}
.stButton button{background:var(--accent); color:white; border:none; border-radius:999px; padding:14px 32px; font-weight:700;}
.stButton button:hover{background:var(--accent-dark);}

.footer{padding:44px 60px; text-align:center; color:var(--text-muted); font-size:13.5px; border-top:1px solid var(--border);}
.footer b{color:var(--text);}

@media (max-width:900px){
    .hero-title{font-size:38px;}
    .navbar, .hero-wrap, .section{padding-left:24px; padding-right:24px;}
    .nav-links{display:none;}
}
</style>
""", unsafe_allow_html=True)


def img_ph(height=260):
    return f"""
    <div class="img-ph" style="height:{height}px;">
        <div class="img-ph-label">IMAGE</div>
    </div>
    """

st.markdown("""
<div class="navbar">
    <a href="#top" class="nav-logo">Calvert Canine <span>Pets</span></a>
    <div class="nav-links">
        <a href="#parents">Parents</a>
        <a href="#litters">Litters</a>
        <a href="#about">About</a>
        <a href="#contact" class="nav-cta">Contact</a>
    </div>
</div>
<div id="top"></div>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 0.95], gap="large")

with col1:
    st.markdown("""
    <div class="hero-badge">Family-raised pedigree parents</div>
    <div class="hero-title">Calvert Canine Pets</div>
    <div class="hero-sub">
        Showcasing all our parent dogs and the litters they produce. Clear health details,
        pedigrees and temperament notes for every mum, dad and available litter.
    </div>
    <div class="hero-actions">
        <a href="#parents" class="btn-primary">View parents</a>
        <a href="#litters" class="btn-ghost">Browse litters</a>
    </div>
    <div class="hero-stats">
        <div class="stat-block">
            <div class="stat-number">20+</div>
            <div class="stat-label">Years in breeding</div>
        </div>
        <div class="stat-block">
            <div class="stat-number">All</div>
            <div class="stat-label">Parents health screened</div>
        </div>
        <div class="stat-block">
            <div class="stat-number">Home raised</div>
            <div class="stat-label">Puppies from family kennels</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(img_ph(420), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section" style="padding-top:22px; padding-bottom:22px;">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
for col, title, subtitle in zip(
    [c1, c2, c3, c4],
    ["Health screened", "Pedigree records", "Home environment", "Owner support"],
    ["Parents carefully examined", "Clear lineage details", "Raised in family rooms", "Advice when you need it"]
):
    with col:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{title}</div>
            <div class="stat-label">{subtitle}</div>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="parents" class="section">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">Parent Dogs</div>
<div class="section-title">Detailed information for every mum and dad dog</div>
<div class="section-sub">Each parent card includes breed, age, health status, temperament and the litters they have produced.</div>
""", unsafe_allow_html=True)

parents = [
    {
        "name": "Calvert Luna",
        "role": "Dam",
        "breed": "English Cocker Spaniel",
        "age": "5 years",
        "health": "Hip scored, eye tested, DNA clear",
        "temperament": "Calm, affectionate and excellent with children.",
        "litters": "2024 Spring, 2025 Autumn",
    },
    {
        "name": "Calvert Aspen",
        "role": "Dam",
        "breed": "Labrador Retriever",
        "age": "6 years",
        "health": "Elbow scored, heart checked, clear PRA",
        "temperament": "Easy going, confident and very sociable.",
        "litters": "2023 Summer, 2025 Spring",
    },
    {
        "name": "Calvert Archer",
        "role": "Sire",
        "breed": "Golden Retriever",
        "age": "7 years",
        "health": "Hip scored, elbow scored, cardiac checked",
        "temperament": "Patient, steady and focused on family life.",
        "litters": "2024 Spring, 2025 Spring",
    },
    {
        "name": "Calvert Jasper",
        "role": "Sire",
        "breed": "Border Collie",
        "age": "5 years",
        "health": "Eye tested, spine clear, genetic screening complete",
        "temperament": "Alert, intelligent and gentle with pups.",
        "litters": "2023 Autumn, 2024 Autumn",
    },
]

cols = st.columns(4, gap="medium")
for col, dog in zip(cols, parents):
    with col:
        st.markdown(f"""
        <div class="card">
            {img_ph(190)}
            <span class="tag tag-muted">{dog['role']}</span>
            <div class="dog-name">{dog['name']}</div>
            <div class="dog-meta">{dog['breed']} · {dog['age']}</div>
            <div class="dog-price">Health profile</div>
            <div class="dog-meta">{dog['health']}</div>
            <div class="dog-meta">{dog['temperament']}</div>
            <div class="dog-meta"><strong>Litters:</strong> {dog['litters']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="litters" class="section section-alt">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">Current Litters</div>
<div class="section-title">Available and upcoming litters from our breeding pairs</div>
<div class="section-sub">Each litter listing includes expected dates, breed combination and current availability.</div>
""", unsafe_allow_html=True)

litters = [
    {
        "parents": "Calvert Luna & Calvert Archer",
        "breed": "English Cocker Spaniel",
        "expected": "May 2026",
        "availability": "5 puppies expected",
        "notes": "Gentle family companions with steady temperaments.",
    },
    {
        "parents": "Calvert Aspen & Calvert Jasper",
        "breed": "Labrador Retriever x Border Collie",
        "expected": "June 2026",
        "availability": "Reserved, waiting list open",
        "notes": "Athletic, intelligent pups suited to active households.",
    },
    {
        "parents": "Calvert Luna & Calvert Jasper",
        "breed": "Spaniel x Collie",
        "expected": "August 2026",
        "availability": "Planning stage",
        "notes": "Balanced nature, gentle with children and other pets.",
    },
]

cols = st.columns(3, gap="medium")
for col, litter in zip(cols, litters):
    with col:
        st.markdown(f"""
        <div class="card">
            {img_ph(240)}
            <span class="tag">{litter['breed']}</span>
            <div class="dog-name">{litter['parents']}</div>
            <div class="dog-meta"><strong>Expected:</strong> {litter['expected']}</div>
            <div class="dog-meta"><strong>Availability:</strong> {litter['availability']}</div>
            <div class="dog-meta">{litter['notes']}</div>
            <a href="#contact" class="mini-link">Enquire about this litter →</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">About Us</div>
<div class="section-title">Calvert Canine Pets is a family-run breeder of thoughtfully matched litters</div>
<div class="section-sub">We focus on health, temperament and long-term well-being for every dog we place. Our approach is transparent and personal.</div>
""", unsafe_allow_html=True)

colA, colB = st.columns([1.05, 0.95], gap="large")
with colA:
    st.markdown(img_ph(420), unsafe_allow_html=True)

with colB:
    features = [
        ("Health screening for all parents", "Every parent dog is fully assessed with hip, elbow, eye and DNA tests before breeding."),
        ("Home raised puppies", "Litters are reared within family life and socialised from the first days."),
        ("Pedigree and temperament", "Parents are selected for stable temperament, breed standard and compatible pairing."),
        ("Clear communication", "We share all health records, breeding plans and litter updates with every buyer."),
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

st.markdown('<div id="contact" class="section section-alt">', unsafe_allow_html=True)
st.markdown('<div class="contact-wrap">', unsafe_allow_html=True)

colL, colR = st.columns([1, 1], gap="large")
with colL:
    st.markdown("""
    <div class="section-kicker">Contact</div>
    <h2 style="font-size:32px; margin-bottom:14px;">Get in touch to discuss a litter or parent dog</h2>
    <p style="font-size:15px; line-height:1.7; max-width:460px; margin-bottom:26px; color:#D8CFC6;">
        Please share the type of puppy or parent dog you are interested in and we will provide available litters,
        planned pairings and health records for every breeding dog.
    </p>
    <p style="font-size:14.5px; margin-bottom:6px;">Calvert Canine Pets</p>
    <p style="font-size:14.5px; margin-bottom:6px;">Oak Vale, Cotswolds, UK</p>
    <p style="font-size:14.5px;">Email: hello@calvertcaninepets.co.uk</p>
    """, unsafe_allow_html=True)

with colR:
    with st.form('enquiry_form'):
        st.text_input('Full name', placeholder='Jane Doe')
        st.text_input('Email address', placeholder='name@example.com')
        st.selectbox('I am interested in', ['Available litters', 'Upcoming litters', 'Parent dog details', 'General enquiry'])
        st.text_area('Message', placeholder='Tell us what you are looking for', height=120)
        submitted = st.form_submit_button('Send enquiry')
        if submitted:
            st.success('Thank you for your enquiry. We will reply with details as soon as possible.')

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <b>Calvert Canine Pets</b> — Pedigree parents, family-raised litters and clear health information.
</div>
""", unsafe_allow_html=True)
