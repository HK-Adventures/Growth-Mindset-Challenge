import streamlit as st

# Set up the page config first
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

# Then import and initialize other components
from growth_mindset_challenge import GrowthMindsetChallenge

# Initialize the challenge class
@st.cache_resource
def get_challenge_instance():
    return GrowthMindsetChallenge()

challenge = get_challenge_instance()

st.title("Growth Mindset Daily Challenge 🌱")

# Sidebar for navigation
page = st.sidebar.radio("Navigate to", ["Daily Challenge", "Progress"])

if page == "Daily Challenge":
    # Add category selection
    category = st.selectbox(
        "Choose a challenge category:",
        ["Random"] + list(challenge.challenges.keys()),
        format_func=lambda x: x.title()
    )
    
    # Get challenge based on category
    if category == "Random":
        daily_challenge = challenge.get_daily_challenge()
    else:
        daily_challenge = challenge.challenges[category][
            st.session_state.get('challenge_index', 0)
        ]
    
    # Display challenge section
    st.header("Today's Challenge")
    st.info(f"### {daily_challenge}")
    
    # Add some motivation
    st.markdown("""
    ### Why This Matters
    Taking time to reflect on your growth helps to:
    - Reinforce positive mindset patterns
    - Track your progress over time
    - Build resilience and persistence
    - Identify areas of improvement
    """)
    
    # Create form for reflection
    with st.form("reflection_form"):
        st.markdown("### Your Reflection")
        st.markdown("Take a moment to think about the challenge and write your thoughts below:")
        reflection = st.text_area(
            "What did you learn? How did you grow? What insights did you gain?",
            height=150
        )
        submit = st.form_submit_button("Complete Challenge ✨")
        
        if submit:
            if reflection.strip():
                challenge.complete_challenge(reflection)
                st.success("🎉 Amazing work! Your reflection has been saved.")
                st.balloons()
            else:
                st.error("Please write a reflection before submitting.")

else:  # Progress page
    st.header("Your Growth Mindset Journey")
    
    # Display stats with descriptions
    st.subheader("📊 Your Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Streak 🔥", f"{challenge.progress['streak']} days")
        st.caption("Number of consecutive days you've completed challenges")
    with col2:
        st.metric("Total Challenges 🎯", len(challenge.progress['completed_challenges']))
        st.caption("Total number of challenges you've completed")
    
    # Display recent reflections
    if challenge.progress["completed_challenges"]:
        st.subheader("📝 Recent Reflections")
        for entry in reversed(challenge.progress["completed_challenges"][-5:]):
            with st.expander(f"Reflection from {entry['date']}"):
                st.markdown(f"*{entry['reflection']}*")
    else:
        st.info("✨ Complete your first challenge to start your growth journey!")
        
    # Add motivational quote
    st.markdown("---")
    st.markdown("""
    > "The mind is like a muscle - the more you exercise it, the stronger it gets."
    """) 