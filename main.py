import streamlit as st

st.set_page_config(
    page_title="Willow Creek Dogs",
    page_icon="🐕",
    layout="wide"
)

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: Georgia, serif;
}

.main{
    padding-top:20px;
}

.hero{
    background:#f4f4f4;
    padding:50px;
    border-radius:12px;
    border:1px solid #dddddd;
}

.section-title{
    font-size:34px;
    margin-top:35px;
    margin-bottom:10px;
    font-weight:bold;
}

.card{
    border:1px solid #d8d8d8;
    border-radius:10px;
    padding:20px;
    background:white;
    margin-bottom:20px;
}

.image-box{
    border:2px dashed #999999;
    height:260px;
    display:flex;
    justify-content:center;
    align-items:center;
    color:#666666;
    background:#fafafa;
    border-radius:8px;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:40px;
    padding-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "",
    [
        "Home",
        "Available Dogs",
        "Training",
        "Testimonials",
        "FAQ",
        "Contact"
    ]
)

if page == "Home":

    st.markdown("""
    <div class="hero">
    <h1>Willow Creek Dogs</h1>

    <h3>Quality Raised Dogs & Professional Training</h3>

    <p>
    Welcome to Willow Creek Dogs, where responsible breeding, early
    socialization, and professional training come together to produce
    confident, healthy companions. Every dog is raised in a clean,
    family-focused environment with plenty of daily interaction and
    individualized care.
    </p>

    <p>
    We believe every family deserves a well-adjusted companion. From the
    earliest weeks of life, our dogs are introduced to everyday sights,
    sounds, people, and routines to encourage confidence and a calm
    temperament.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">About Us</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])

    with col1:

        st.markdown("""
        <div class="image-box">
        Your Family Photo Here
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.write("""
For years we have dedicated ourselves to raising healthy, well-socialized dogs
that are suited for both active households and quiet family environments.

Every puppy receives regular health checks, age-appropriate vaccinations,
careful nutrition, and continuous socialization throughout the early stages
of development.

Our commitment extends beyond the day your puppy goes home. We remain available
to answer questions, offer guidance, and provide continued support throughout
your dog's life.
""")

    st.markdown('<div class="section-title">Why Families Choose Us</div>', unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown("""
<div class="card">
<h3>Health First</h3>

Routine veterinary care, health screenings, proper nutrition, and a clean
environment help every puppy get the best possible start.
</div>
""", unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="card">
<h3>Early Socialization</h3>

Each puppy is exposed to everyday household experiences, people, and handling
to encourage confidence and adaptability.
</div>
""", unsafe_allow_html=True)

    with c3:
        st.markdown("""
<div class="card">
<h3>Lifetime Support</h3>

We enjoy staying connected with families and are always happy to answer
questions as your companion grows.
</div>
""", unsafe_allow_html=True)

elif page == "Available Dogs":

    st.title("Available Dogs")

    dogs = [

        {
            "name":"Bella",
            "age":"12 Weeks",
            "description":"Bella is a confident and affectionate puppy with an easy-going personality. She enjoys spending time outdoors, learns quickly, and has begun basic leash work."
        },

        {
            "name":"Cooper",
            "age":"14 Weeks",
            "description":"Cooper is energetic, intelligent, and eager to learn. He has demonstrated excellent recall during introductory training sessions and enjoys meeting new people."
        },

        {
            "name":"Sadie",
            "age":"10 Weeks",
            "description":"Sadie is gentle and observant with a calm disposition. She enjoys quiet interaction and adapts well to new environments."
        }

    ]

    for dog in dogs:

        left,right = st.columns([1,2])

        with left:

            st.markdown(f"""
            <div class="image-box">
            Photo of {dog["name"]}
            </div>
            """, unsafe_allow_html=True)

        with right:

            st.markdown(f"""
<div class="card">

<h2>{dog["name"]}</h2>

<b>Age:</b> {dog["age"]}

<br><br>

{dog["description"]}

<br><br>

Additional placeholder information may be added here regarding vaccinations,
microchipping, temperament testing, feeding schedules, registration paperwork,
health guarantees, or any other details prospective owners may find helpful.

</div>
""", unsafe_allow_html=True)

        st.divider()

elif page == "Training":

    st.title("Training Services")

    st.write("""
Whether your goal is basic manners or advanced obedience, we offer structured
training programs designed to build confidence, consistency, and clear
communication between owner and dog.

Each program is tailored to the individual dog's temperament and learning
style while emphasizing positive reinforcement and reliable behaviors.
""")

    col1,col2,col3=st.columns(3)

    with col1:

        st.markdown("""
<div class="card">

<h3>Puppy Foundations</h3>

Basic commands

House manners

Crate introduction

Socialization

Confidence building

Leash introduction

</div>
""", unsafe_allow_html=True)

    with col2:

        st.markdown("""
<div class="card">

<h3>Obedience</h3>

Sit

Stay

Come

Loose leash walking

Place command

Impulse control

</div>
""", unsafe_allow_html=True)

    with col3:

        st.markdown("""
<div class="card">

<h3>Advanced Programs</h3>

Long distance recall

Public manners

Distraction work

Reliable obedience

Confidence development

Owner coaching

</div>
""", unsafe_allow_html=True)

    st.markdown("## Training Gallery")

    g1,g2,g3=st.columns(3)

    for g in [g1,g2,g3]:
        with g:
            st.markdown("""
<div class="image-box">
Training Photo
</div>
""", unsafe_allow_html=True)

elif page == "Testimonials":

    st.title("Client Testimonials")

    for i in range(4):

        st.markdown("""
<div class="card">

"Our experience from beginning to end was exceptional. The communication,
professionalism, and attention given to every puppy was immediately apparent.
Our dog adjusted quickly to our home and continues to be a wonderful family
companion."

<br><br>

<strong>— Client Name</strong>

</div>
""", unsafe_allow_html=True)

elif page == "FAQ":

    st.title("Frequently Asked Questions")

    with st.expander("Are the puppies vaccinated?"):
        st.write("""
Placeholder information describing vaccination schedules,
veterinary examinations, and health documentation.
""")

    with st.expander("Can I reserve a puppy?"):
        st.write("""
Placeholder information regarding deposits,
reservation procedures, and pickup dates.
""")

    with st.expander("Do you offer training after purchase?"):
        st.write("""
Placeholder information describing available training
packages and continued support.
""")

    with st.expander("Can I visit before choosing a puppy?"):
        st.write("""
Placeholder information explaining appointment scheduling,
visitor policies, and meeting available puppies.
""")

elif page == "Contact":

    st.title("Contact")

    st.write("""
We welcome inquiries regarding available puppies, future litters,
training services, and general questions.

Complete the form below and we will respond as soon as possible.
""")

    name = st.text_input("Name")

    email = st.text_input("Email")

    phone = st.text_input("Phone")

    message = st.text_area("Message", height=180)

    if st.button("Submit Inquiry"):
        st.success("Thank you. Your inquiry has been received.")

    st.markdown("## Location")

    st.markdown("""
<div class="image-box">
Map or Kennel Photo
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">

<hr>

Willow Creek Dogs

Responsible Breeding • Professional Training • Lifetime Support

© 2026 Willow Creek Dogs. All rights reserved.

</div>
""", unsafe_allow_html=True)