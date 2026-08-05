import streamlit as st

from utils import inject_base_styles, photo_block, render_html

st.set_page_config(
    page_title="CalvertK9 — KC Registered Maltese Puppies",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_base_styles()

# ---------------------------------------------------------------------------
# NAVBAR
# ---------------------------------------------------------------------------
render_html("""
<div class="navbar">
    <a href="#top" class="nav-logo-wrap">
        <span class="crest">CK9</span>
        <span class="nav-logo">CalvertK9</span>
    </a>
    <div class="nav-links">
        <a href="#parents">Parents</a>
        <a href="#puppies">Puppies</a>
        <a href="#health">Health</a>
        <a href="#about">About</a>
        <a href="#contact" class="nav-cta">Contact</a>
    </div>
</div>
<div id="top"></div>
""")

# ---------------------------------------------------------------------------
# TRUST STRIP
# ---------------------------------------------------------------------------
render_html("""
<div class="trust-strip">
    <div class="trust-item">KC Registered</div>
    <div class="trust-item">Health-Tested Parents</div>
    <div class="trust-item">Home-Raised in Chelmsford, Essex</div>
    <div class="trust-item">7 Puppies in the Litter</div>
</div>
""")

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
render_html('<div class="hero-wrap">')
col1, col2 = st.columns([1.1, 1], gap="large")

with col1:
    render_html("""
    <div class="hero-badge">Maltese &middot; Home-Raised &middot; KC Registered</div>
    <div class="hero-title">Marley &amp; Bertie's Litter</div>
    <div class="hero-sub">
        Seven KC-registered Maltese puppies, home-raised in Chelmsford, Essex,
        from two much-loved, health-tested family dogs.
    </div>
    <div class="hero-actions">
        <a href="#puppies" class="btn-primary">Meet the puppies</a>
        <a href="#contact" class="btn-ghost">Get in touch</a>
    </div>
    <div class="hero-stats">
        <div class="stat"><div class="stat-num">7</div><div class="stat-label">Puppies</div></div>
        <div class="stat"><div class="stat-num">KC</div><div class="stat-label">Registered</div></div>
        <div class="stat"><div class="stat-num">Essex</div><div class="stat-label">Chelmsford</div></div>
    </div>
    """)

with col2:
    render_html(photo_block("hero", height=430))

render_html('</div>')

# ---------------------------------------------------------------------------
# MEET THE PARENTS
# ---------------------------------------------------------------------------
render_html('<div id="parents" class="section">')
render_html("""
<div class="section-kicker">Meet the Parents</div>
<div class="section-title">Marley and Bertie</div>
<div class="section-sub">Two loved family dogs, and the proud parents of this litter.</div>
""")

colM, colB = st.columns(2, gap="large")

with colM:
    render_html(f"""
        <div class="card" style="padding:26px;">
            {photo_block("marley", height=340, overlay_html='<span class="photo-tag">Dam</span>')}
            <div class="dog-name">Marley</div>
            <div class="dog-meta">PLACEHOLDER TEXT PLACEHOLDER TEXT</div>
            <div class="dog-meta"><strong>Health:</strong> PLACEHOLDER TEXT PLACEHOLDER TEXT</div>
        </div>
    """)

with colB:
    render_html(f"""
        <div class="card" style="padding:26px;">
            {photo_block("bertie", height=340, overlay_html='<span class="photo-tag">Sire</span>')}
            <div class="dog-name">Bertie</div>
            <div class="dog-meta">
                Bertie is our beautiful KC-registered Maltese with the most
                perfect personality — full of fun, always up for a cuddle,
                and a very loving family dog. He's well proven, having
                produced plenty of gorgeous puppies. Any questions, please
                don't hesitate to get in touch.
            </div>
            <div class="dog-meta"><strong>Age:</strong> 3 years, 5 months &middot; <strong>Breed:</strong> Maltese &middot; <strong>KC Registered</strong></div>
        </div>
    """)

render_html('</div>')

# ---------------------------------------------------------------------------
# MEET THE PUPPIES
# ---------------------------------------------------------------------------
render_html('<div id="puppies" class="section section-alt">')
render_html("""
<div class="section-kicker">Meet the Puppies</div>
<div class="section-title">Marley and Bertie's Litter</div>
<div class="section-sub">Seven happy, home-raised Maltese puppies. Get in touch if one has caught your eye.</div>
""")

# Edit puppy names / meta / status once known — replace the placeholder text.
puppies = [
    {"key": "puppy1", "name": "Puppy 1"},
    {"key": "puppy2", "name": "Puppy 2"},
    {"key": "puppy3", "name": "Puppy 3"},
    {"key": "puppy4", "name": "Puppy 4"},
    {"key": "puppy5", "name": "Puppy 5"},
    {"key": "puppy6", "name": "Puppy 6"},
    {"key": "puppy7", "name": "Puppy 7"},
]

cards = []
for p in puppies:
    cards.append(f"""
    <div class="card" style="padding:14px;">
        {photo_block(p['key'], height=170, radius=10)}
        <div class="puppy-name">{p['name']}</div>
        <div class="puppy-meta">PLACEHOLDER TEXT PLACEHOLDER TEXT</div>
    </div>
    """)

# grid-template-columns:repeat(3, 1fr) on .puppy-grid keeps every card the
# same width, even on the last, shorter row — so puppy 7 doesn't stretch.
render_html('<div class="puppy-grid">' + "".join(cards) + "</div>")

render_html('</div>')

# ---------------------------------------------------------------------------
# HEALTH & DOCUMENTS
# ---------------------------------------------------------------------------
render_html('<div id="health" class="section">')
render_html("""
<div class="section-kicker">Health &amp; Documents</div>
<div class="section-title">Every puppy leaves us with</div>
<div class="section-sub">The same standard of care and paperwork we'd want for a dog joining our own family.</div>
<div class="health-grid">
    <div class="health-item"><span class="health-check">&#10003;</span>Microchipped by collection date</div>
    <div class="health-item"><span class="health-check">&#10003;</span>Wormed and flea treated</div>
    <div class="health-item"><span class="health-check">&#10003;</span>KC registered by collection</div>
    <div class="health-item"><span class="health-check">&#10003;</span>Vaccinations up to date</div>
    <div class="health-item"><span class="health-check">&#10003;</span>Health checked by a vet</div>
</div>
""")
render_html('</div>')

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
render_html('<div id="about" class="section section-alt">')
render_html("""
<div class="section-kicker">About CalvertK9</div>
<div class="section-title">A family-raised litter, cared for from day one</div>
<div class="section-sub">
    Marley and Bertie's puppies have been raised at home in Chelmsford,
    Essex, surrounded by family life from birth. We're happy to answer any
    questions about their upbringing, health and temperament.
</div>
<div class="feature-grid">
    <div class="feature-box">
        <div class="feature-title">Raised at home</div>
        <div class="feature-desc">The puppies have grown up as part of our family, not in a kennel.</div>
    </div>
    <div class="feature-box">
        <div class="feature-title">Socialised early</div>
        <div class="feature-desc">Handled daily and gently introduced to everyday household life.</div>
    </div>
    <div class="feature-box">
        <div class="feature-title">Happy and healthy</div>
        <div class="feature-desc">Well-fed, well-loved, and ready for their new homes.</div>
    </div>
</div>
""")
render_html('</div>')

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
render_html('<div id="contact" class="section">')
render_html('<div class="contact-card">')

colL, colR = st.columns([1, 1], gap="large")
with colL:
    render_html("""
    <div class="section-kicker">Contact</div>
    <h2 style="font-size:26px; margin-bottom:12px;">Interested in one of our puppies?</h2>
    <p style="font-size:14.5px; line-height:1.7; max-width:440px; color:#5B6154; margin-bottom:20px;">
        Get in touch and we'll be happy to answer any questions.
    </p>
    <p style="font-size:14px; margin-bottom:4px;"><strong>CalvertK9</strong> &middot; Chelmsford, Essex</p>
    <p style="font-size:14px; margin-bottom:4px;">Email: hello@calvertk9.co.uk</p>
    <p class="contact-phone">Or call <strong>07777 777777</strong></p>
    """)

with colR:
    with st.form("enquiry_form"):
        st.text_input("Full name", placeholder="Jane Doe")
        st.text_input("Email address", placeholder="name@example.com")
        st.selectbox("I am interested in", ["A specific puppy", "General enquiry"])
        st.text_area("Message", placeholder="Tell us which puppy you are interested in", height=110)
        submitted = st.form_submit_button("Send enquiry")
        if submitted:
            st.success("Thank you — we will reply as soon as possible.")

render_html('</div>')
render_html('</div>')

# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
render_html("""
<div class="footer">
    <b>CalvertK9</b> — KC-registered Maltese puppies, home-raised in Chelmsford, Essex.
</div>
""")