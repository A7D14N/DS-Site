import streamlit as st

from utils import inject_base_styles, render_html

st.set_page_config(
    page_title="CalvertK9 — KC Registered Maltese Puppies",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_base_styles()

# ---------------------------------------------------------------------------
# Page-specific styles for this simple, text-only landing page.
# ---------------------------------------------------------------------------
render_html("""
<style>
.home-simple{
    min-height:82vh;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:56px 24px 8px 24px;
    box-sizing:border-box;
}
.home-simple-crest{
    width:56px; height:56px; border-radius:50%;
    border:1.5px solid var(--ink);
    display:flex; align-items:center; justify-content:center;
    font-family:'Fraunces', serif; font-weight:700; font-size:16px;
    letter-spacing:0.02em; color:var(--ink);
    margin-bottom:24px;
}
.home-simple-eyebrow{
    font-size:12.5px; letter-spacing:0.14em; text-transform:uppercase;
    color:var(--ink-soft); margin-bottom:16px;
}
.home-simple-title{
    font-family:'Fraunces', serif; font-size:clamp(38px, 8vw, 68px);
    font-weight:700; letter-spacing:0.01em; color:var(--ink);
    margin-bottom:18px; line-height:1.05;
}
.home-simple-sub{
    font-size:17px; line-height:1.75; color:var(--ink-soft);
    max-width:560px; margin:0 auto 28px auto;
}
.home-simple-pills{
    display:flex; justify-content:center; gap:10px; flex-wrap:wrap;
    margin-bottom:34px;
}
.home-simple-pill{
    background:var(--paper-dim); border:1px solid var(--line);
    color:var(--ink-soft); font-size:11.5px; font-weight:600;
    letter-spacing:0.05em; text-transform:uppercase;
    padding:7px 16px; border-radius:999px;
}
.home-simple-facts{
    display:flex; gap:40px; flex-wrap:wrap; justify-content:center;
    margin:36px auto 0 auto; padding-top:26px; border-top:1px solid var(--line);
    max-width:460px;
}
.home-simple-fact-num{
    font-family:'Fraunces', serif; font-size:22px; font-weight:700; color:var(--ink);
}
.home-simple-fact-label{
    font-size:11px; color:var(--ink-soft); text-transform:uppercase;
    letter-spacing:0.06em; margin-top:2px;
}
.home-simple-btn-row{max-width:280px; margin:0 auto;}
@media (max-width:600px){
    .home-simple{padding:44px 20px 4px 20px; min-height:auto;}
    .home-simple-sub{font-size:15.5px;}
    .home-simple-facts{gap:26px; margin-top:28px;}
}
</style>
""")

# ---------------------------------------------------------------------------
# CONTENT
# ---------------------------------------------------------------------------
render_html('<div class="home-simple">')

render_html("""
<div class="home-simple-crest">CK9</div>
<div class="home-simple-eyebrow">Chelmsford, Essex &middot; KC Registered Maltese</div>
<div class="home-simple-title">CalvertK9</div>
<div class="home-simple-sub">
    Home-raised Maltese puppies from health-tested, KC-registered
    parents. Meet Marley, Bertie, and their beautiful litter of seven.
</div>
<div class="home-simple-pills">
    <span class="home-simple-pill">KC Registered</span>
    <span class="home-simple-pill">Health Tested</span>
    <span class="home-simple-pill">Home-Raised</span>
</div>
""")

render_html('<div class="home-simple-btn-row">')
if st.button("Meet the Pups", use_container_width=True):
    st.switch_page("pages/1_Meet_the_Puppies.py")
render_html('</div>')

render_html("""
<div class="home-simple-facts">
    <div><div class="home-simple-fact-num">7</div><div class="home-simple-fact-label">Puppies</div></div>
    <div><div class="home-simple-fact-num">KC</div><div class="home-simple-fact-label">Registered</div></div>
    <div><div class="home-simple-fact-num">Essex</div><div class="home-simple-fact-label">Chelmsford</div></div>
</div>
""")

render_html('</div>')