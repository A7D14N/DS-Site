import streamlit as st

st.set_page_config(
    page_title="Brightpaw Kennels — Puppies & Training",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLE
# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300..700&family=Inter:wght@300;400;500;600;700&display=swap');

:root{
    --cream:#FBF6EE;
    --cream-dark:#F1E8D8;
    --ink:#211D1A;
    --ink-soft:#5B534A;
    --amber:#FF7A3D;
    --amber-dark:#E3611F;
    --sage:#6E8F6C;
    --line:#E7DECB;
}

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
    color:var(--ink);
}

#MainMenu{visibility:hidden;}
header[data-testid="stHeader"]{background:transparent;}
footer{visibility:hidden;}
[data-testid="stToolbar"]{display:none;}

.stApp{
    background:var(--cream);
}

.block-container{
    padding-top:0rem;
    padding-bottom:0rem;
    max-width:100%;
}

h1,h2,h3,h4{
    font-family:'Fraunces', serif;
    letter-spacing:-0.02em;
}

section[data-testid="stForm"]{
    border:none;
    background:transparent;
}

/* ---------- NAVBAR ---------- */
.navbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:22px 60px;
    background:var(--cream);
    border-bottom:1px solid var(--line);
    position:sticky;
    top:0;
    z-index:999;
}
.nav-logo{
    font-family:'Fraunces', serif;
    font-size:26px;
    font-weight:700;
    color:var(--ink);
    text-decoration:none;
}
.nav-logo span{color:var(--amber);}
.nav-links a{
    margin-left:34px;
    text-decoration:none;
    color:var(--ink-soft);
    font-weight:500;
    font-size:15px;
    transition:color 0.2s ease;
}
.nav-links a:hover{color:var(--amber-dark);}
.nav-cta{
    background:var(--ink);
    color:var(--cream)!important;
    padding:10px 22px;
    border-radius:100px;
    font-weight:600!important;
}
.nav-cta:hover{background:var(--amber-dark)!important; color:white!important;}

/* ---------- HERO ---------- */
.hero-wrap{
    padding:70px 60px 40px 60px;
    display:flex;
    gap:50px;
    align-items:center;
    flex-wrap:wrap;
}
.hero-badge{
    display:inline-block;
    background:var(--cream-dark);
    color:var(--ink-soft);
    padding:7px 16px;
    border-radius:100px;
    font-size:13px;
    font-weight:600;
    letter-spacing:0.03em;
    margin-bottom:22px;
    border:1px solid var(--line);
}
.hero-title{
    font-size:56px;
    line-height:1.08;
    font-weight:600;
    margin-bottom:18px;
    color:var(--ink);
}
.hero-title em{
    font-style:italic;
    color:var(--amber-dark);
}
.hero-sub{
    font-size:18px;
    color:var(--ink-soft);
    line-height:1.65;
    max-width:480px;
    margin-bottom:30px;
}
.hero-stats{
    display:flex;
    gap:38px;
    margin-top:36px;
}
.hero-stat-num{
    font-family:'Fraunces', serif;
    font-size:30px;
    font-weight:700;
    color:var(--ink);
}
.hero-stat-label{
    font-size:13px;
    color:var(--ink-soft);
}

/* ---------- BUTTONS ---------- */
.btn-primary{
    display:inline-block;
    background:var(--amber);
    color:white!important;
    padding:15px 32px;
    border-radius:100px;
    font-weight:600;
    text-decoration:none;
    font-size:15px;
    box-shadow:0 10px 24px -8px rgba(255,122,61,0.55);
    transition:all 0.2s ease;
    margin-right:14px;
}
.btn-primary:hover{
    background:var(--amber-dark);
    transform:translateY(-2px);
}
.btn-ghost{
    display:inline-block;
    padding:15px 30px;
    border-radius:100px;
    font-weight:600;
    text-decoration:none;
    font-size:15px;
    border:1.5px solid var(--ink);
    color:var(--ink)!important;
    transition:all 0.2s ease;
}
.btn-ghost:hover{
    background:var(--ink);
    color:var(--cream)!important;
}

/* ---------- IMAGE PLACEHOLDERS ---------- */
.img-ph{
    width:100%;
    border-radius:22px;
    display:flex;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    color:#FFF8EF;
    font-weight:600;
    text-align:center;
    background:repeating-linear-gradient(135deg, #E3611F, #E3611F 14px, #FF8A50 14px, #FF8A50 28px);
    position:relative;
    overflow:hidden;
    border:1px solid rgba(0,0,0,0.05);
}
.img-ph::before{
    content:"";
    position:absolute;
    inset:0;
    background:rgba(33,29,26,0.32);
}
.img-ph-label{
    position:relative;
    z-index:2;
    font-size:15px;
    letter-spacing:0.02em;
}
.img-ph-icon{
    position:relative;
    z-index:2;
    font-size:34px;
    margin-bottom:6px;
}

/* ---------- SECTIONS ---------- */
.section{
    padding:80px 60px;
}
.section-alt{
    background:var(--cream-dark);
}
.section-kicker{
    color:var(--amber-dark);
    font-weight:700;
    font-size:13px;
    letter-spacing:0.12em;
    text-transform:uppercase;
    margin-bottom:10px;
}
.section-title{
    font-size:38px;
    font-weight:600;
    margin-bottom:14px;
    max-width:640px;
}
.section-sub{
    color:var(--ink-soft);
    font-size:16px;
    max-width:560px;
    line-height:1.6;
    margin-bottom:10px;
}

/* ---------- CARDS ---------- */
.card{
    background:white;
    border-radius:20px;
    padding:22px;
    border:1px solid var(--line);
    height:100%;
    transition:transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover{
    transform:translateY(-4px);
    box-shadow:0 20px 40px -20px rgba(33,29,26,0.25);
}
.tag{
    display:inline-block;
    background:var(--sage);
    color:white;
    font-size:11.5px;
    font-weight:700;
    padding:4px 11px;
    border-radius:100px;
    letter-spacing:0.03em;
    margin-bottom:12px;
}
.tag-amber{background:var(--amber);}
.dog-name{
    font-family:'Fraunces', serif;
    font-size:21px;
    font-weight:700;
    margin:6px 0 2px 0;
}
.dog-meta{
    color:var(--ink-soft);
    font-size:14px;
    margin-bottom:10px;
}
.dog-price{
    font-weight:700;
    font-size:17px;
    color:var(--amber-dark);
    margin-bottom:14px;
}
.mini-link{
    color:var(--ink);
    font-weight:600;
    font-size:14px;
    text-decoration:none;
    border-bottom:2px solid var(--amber);
}

.training-icon{
    font-size:30px;
    margin-bottom:14px;
}
.training-name{
    font-family:'Fraunces', serif;
    font-size:20px;
    font-weight:700;
    margin-bottom:8px;
}
.training-desc{
    color:var(--ink-soft);
    font-size:14.5px;
    line-height:1.55;
    margin-bottom:14px;
}
.training-price{
    font-weight:700;
    font-size:15px;
    color:var(--ink);
}

.stat-box{
    text-align:center;
    padding:26px 10px;
}
.stat-num{
    font-family:'Fraunces', serif;
    font-size:38px;
    font-weight:700;
    color:var(--amber-dark);
}
.stat-label{
    font-size:14px;
    color:var(--ink-soft);
    margin-top:4px;
}

.testimonial{
    background:white;
    border-radius:20px;
    padding:26px;
    border:1px solid var(--line);
    height:100%;
}
.stars{
    color:var(--amber);
    font-size:15px;
    margin-bottom:10px;
}
.quote{
    font-size:15px;
    color:var(--ink);
    line-height:1.6;
    margin-bottom:16px;
    font-style:italic;
}
.author{
    font-weight:700;
    font-size:14px;
}
.author-sub{
    color:var(--ink-soft);
    font-size:13px;
}

/* ---------- CONTACT ---------- */
.contact-wrap{
    background:var(--ink);
    border-radius:28px;
    padding:56px;
    color:var(--cream);
}
.contact-wrap h2{color:var(--cream);}
.contact-wrap p{color:#C9C2B6;}
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stSelectbox"] div[data-baseweb="select"]{
    background:#2C2823!important;
    color:var(--cream)!important;
    border-radius:12px!important;
    border:1px solid #46403A!important;
}
label{
    color:#D8D2C6!important;
    font-weight:500!important;
    font-size:14px!important;
}
div[data-testid="stFormSubmitButton"] button{
    background:var(--amber);
    color:white;
    border:none;
    border-radius:100px;
    padding:12px 30px;
    font-weight:700;
    margin-top:10px;
}
div[data-testid="stFormSubmitButton"] button:hover{
    background:var(--amber-dark);
    color:white;
}

/* ---------- FOOTER ---------- */
.footer{
    padding:44px 60px;
    text-align:center;
    color:var(--ink-soft);
    font-size:13.5px;
    border-top:1px solid var(--line);
}
.footer b{color:var(--ink);}

@media (max-width:900px){
    .hero-title{font-size:38px;}
    .navbar, .hero-wrap, .section{padding-left:24px; padding-right:24px;}
    .nav-links{display:none;}
}
</style>
""", unsafe_allow_html=True)


def img_ph(label, icon="🐾", height=260):
    return f"""
    <div class="img-ph" style="height:{height}px;">
        <div class="img-ph-icon">{icon}</div>
        <div class="img-ph-label">{label}</div>
    </div>
    """


# ----------------------------------------------------------------------------
# NAVBAR
# ----------------------------------------------------------------------------
st.markdown("""
<div class="navbar">
    <a href="#top" class="nav-logo">Bright<span>paw</span> Kennels</a>
    <div class="nav-links">
        <a href="#dogs">Puppies</a>
        <a href="#training">Training</a>
        <a href="#why">Why Us</a>
        <a href="#reviews">Reviews</a>
        <a href="#contact" class="nav-cta">Enquire Now</a>
    </div>
</div>
<div id="top"></div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
col1, col2 = st.columns([1.1, 1], gap="large")

with col1:
    st.markdown("""
    <span class="hero-badge">🐶 12 Happy Litters Rehomed in 2025</span>
    <div class="hero-title">Raising loyal dogs, <em>from puppyhood to well-mannered pal.</em></div>
    <div class="hero-sub">
        Brightpaw Kennels breeds healthy, well-socialised puppies and offers expert-led
        training programmes so your new best friend fits right into family life —
        happily, confidently, and calmly.
    </div>
    <a href="#dogs" class="btn-primary">Meet the Puppies</a>
    <a href="#training" class="btn-ghost">Explore Training</a>
    <div class="hero-stats">
        <div><div class="hero-stat-num">17 yrs</div><div class="hero-stat-label">Breeding Experience</div></div>
        <div><div class="hero-stat-num">340+</div><div class="hero-stat-label">Dogs Trained</div></div>
        <div><div class="hero-stat-num">4.9★</div><div class="hero-stat-label">Average Rating</div></div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(img_ph("Hero Image — Golden Retriever Puppy in Field", "🐕", 440), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# TRUST STRIP
# ----------------------------------------------------------------------------
st.markdown('<div class="section" style="padding-top:10px; padding-bottom:10px;">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("15+", "Breeds Available"),
    ("100%", "Health-Checked Litters"),
    ("30", "Day Puppy Guarantee"),
    ("24/7", "New-Owner Support"),
]
for c, (num, label) in zip([c1, c2, c3, c4], stats):
    with c:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{num}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# DOGS FOR SALE
# ----------------------------------------------------------------------------
st.markdown('<div id="dogs" class="section">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">Available Now</div>
<div class="section-title">Meet the pups looking for their forever home</div>
<div class="section-sub">Every puppy is vet-checked, microchipped, and raised in a loving home environment
before they meet you. Scroll through our current litters below.</div>
""", unsafe_allow_html=True)

st.write("")

dogs = [
    {"name": "Biscuit", "breed": "Golden Retriever", "age": "8 weeks", "price": "£1,850",
     "tag": "Ready Now", "icon": "🐕", "desc": "Playful, cuddly, and great with kids. Mum and Dad both health-tested."},
    {"name": "Nala", "breed": "French Bulldog", "age": "10 weeks", "price": "£2,600",
     "tag": "Ready Now", "icon": "🐶", "desc": "Calm and affectionate, loves lounging and short walks."},
    {"name": "Rex", "breed": "German Shepherd", "age": "6 weeks", "price": "£1,600",
     "tag": "2 Left", "icon": "🐺", "desc": "Confident and alert, a natural fit for active families."},
    {"name": "Poppy", "breed": "Cavapoo", "age": "9 weeks", "price": "£1,950",
     "tag": "New Litter", "icon": "🐩", "desc": "Hypoallergenic coat, gentle temperament, great first dog."},
]

cols = st.columns(4, gap="medium")
for c, dog in zip(cols, dogs):
    with c:
        st.markdown(f"""
        <div class="card">
            {img_ph(f"{dog['name']} the {dog['breed']}", dog['icon'], 190)}
            <span class="tag tag-amber">{dog['tag']}</span>
            <div class="dog-name">{dog['name']}</div>
            <div class="dog-meta">{dog['breed']} · {dog['age']}</div>
            <div class="dog-price">{dog['price']}</div>
            <div class="dog-meta" style="margin-bottom:14px;">{dog['desc']}</div>
            <a href="#contact" class="mini-link">Enquire about {dog['name']} →</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# TRAINING PROGRAMS
# ----------------------------------------------------------------------------
st.markdown('<div id="training" class="section section-alt">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">Training Programmes</div>
<div class="section-title">Confident dogs don't happen by accident</div>
<div class="section-sub">Whether you're welcoming a brand-new puppy or working through
tricky habits with an older dog, our certified trainers build a plan around your goals.</div>
""", unsafe_allow_html=True)

st.write("")

programs = [
    ("🐾", "Puppy Foundations", "4-week course covering house training, socialisation, and basic obedience for puppies 8–16 weeks.", "From £220"),
    ("🎯", "Obedience Mastery", "6-week programme for recall, loose-lead walking, and reliable commands in real-world settings.", "From £340"),
    ("🧠", "Behavioural Rehab", "1-to-1 sessions for reactivity, anxiety, or resource guarding, tailored to your dog's history.", "From £95 / session"),
    ("🏡", "Board & Train", "2-week residential stay where your dog trains daily with our team and comes home transformed.", "From £950"),
]

cols = st.columns(4, gap="medium")
for c, (icon, name, desc, price) in zip(cols, programs):
    with c:
        st.markdown(f"""
        <div class="card">
            <div class="training-icon">{icon}</div>
            <div class="training-name">{name}</div>
            <div class="training-desc">{desc}</div>
            <div class="training-price">{price}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# WHY CHOOSE US
# ----------------------------------------------------------------------------
st.markdown('<div id="why" class="section">', unsafe_allow_html=True)
colA, colB = st.columns([1, 1.1], gap="large")

with colA:
    st.markdown(img_ph("Trainer Working With Puppy Outdoors", "🎾", 420), unsafe_allow_html=True)

with colB:
    st.markdown("""
    <div class="section-kicker">Why Brightpaw</div>
    <div class="section-title" style="max-width:520px;">Bred with care. Trained with patience. Loved from day one.</div>
    """, unsafe_allow_html=True)

    features = [
        ("🩺", "Health-First Breeding", "Every litter is bred from health-tested parents with full vet records shared before you buy."),
        ("🎓", "Certified Trainers", "Our team is accredited in force-free, positive-reinforcement methods only."),
        ("🏠", "Raised in a Home", "No kennels or cages — our puppies grow up around family life, noise, and people."),
        ("📞", "Lifetime Support", "Questions at week 2 or year 12? We're one call away for the life of your dog."),
    ]
    for icon, title, desc in features:
        st.markdown(f"""
        <div style="display:flex; gap:16px; margin-bottom:22px; align-items:flex-start;">
            <div style="font-size:24px;">{icon}</div>
            <div>
                <div style="font-weight:700; font-size:16px; margin-bottom:3px;">{title}</div>
                <div style="color:var(--ink-soft); font-size:14.5px; line-height:1.5;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# TESTIMONIALS
# ----------------------------------------------------------------------------
st.markdown('<div id="reviews" class="section section-alt">', unsafe_allow_html=True)
st.markdown("""
<div class="section-kicker">Happy Families</div>
<div class="section-title">Loved by owners across the country</div>
""", unsafe_allow_html=True)

st.write("")

reviews = [
    ("★★★★★", "We picked up our Cavapoo from Brightpaw last spring and the whole process felt calm and honest. She's the sweetest addition to our family.", "Hannah M.", "Owner of Biscuit the Cavapoo"),
    ("★★★★★", "The Board & Train programme fixed leash pulling we'd struggled with for two years. Our trainer sent daily updates and videos — worth every penny.", "Callum R.", "Owner of Duke the Labrador"),
    ("★★★★★", "Puppy Foundations gave us real structure in week one. House training took days, not months. Couldn't recommend the team more.", "Priya S.", "Owner of Milo the Sheepdog"),
]

cols = st.columns(3, gap="medium")
for c, (stars, quote, author, sub) in zip(cols, reviews):
    with c:
        st.markdown(f"""
        <div class="testimonial">
            <div class="stars">{stars}</div>
            <div class="quote">“{quote}”</div>
            <div class="author">{author}</div>
            <div class="author-sub">{sub}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# CONTACT / ENQUIRY
# ----------------------------------------------------------------------------
st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
st.markdown('<div class="contact-wrap">', unsafe_allow_html=True)

colL, colR = st.columns([1, 1.2], gap="large")

with colL:
    st.markdown("""
    <div class="section-kicker" style="color:#FF9A63;">Get In Touch</div>
    <h2 style="font-size:32px; margin-bottom:14px;">Ready to bring your new best friend home?</h2>
    <p style="font-size:15px; line-height:1.6; max-width:400px;">
        Tell us a bit about what you're looking for — a puppy, training, or both —
        and our team will get back to you within 24 hours.
    </p>
    <p style="margin-top:26px; font-size:14.5px;">📍 42 Meadow Lane, Cotswold, UK</p>
    <p style="font-size:14.5px;">📞 01234 567 890</p>
    <p style="font-size:14.5px;">✉️ hello@brightpawkennels.co.uk</p>
    """, unsafe_allow_html=True)

with colR:
    with st.form("enquiry_form", clear_on_submit=True):
        fc1, fc2 = st.columns(2)
        with fc1:
            name = st.text_input("Full Name", placeholder="Jane Appleseed")
        with fc2:
            phone = st.text_input("Phone Number", placeholder="07123 456789")
        email = st.text_input("Email Address", placeholder="jane@email.com")
        interest = st.selectbox(
            "What are you interested in?",
            ["Buying a puppy", "Training services", "Both", "General enquiry"],
        )
        message = st.text_area("Your Message", placeholder="Tell us about your ideal dog or training goals...", height=110)
        submitted = st.form_submit_button("Send Enquiry →")

        if submitted:
            if name and email:
                st.success(f"Thanks {name.split()[0]}! We've received your enquiry and will be in touch shortly. 🐾")
                st.balloons()
            else:
                st.warning("Please fill in at least your name and email so we can get back to you.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.markdown("""
<div class="footer">
    <b>Brightpaw Kennels</b> — Ethically bred puppies & expert dog training since 2008.<br>
    © 2026 Brightpaw Kennels. All rights reserved. · Placeholder content for demo purposes.
</div>
""", unsafe_allow_html=True)