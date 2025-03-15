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
    # Display the daily challenge
    daily_challenge = challenge.get_daily_challenge()
    
    st.header("Today's Challenge")
    st.write(f"### {daily_challenge}")
    
    # Create form for reflection
    with st.form("reflection_form"):
        reflection = st.text_area("Write your reflection:", height=150)
        submit = st.form_submit_button("Complete Challenge")
        
        if submit and reflection:
            challenge.complete_challenge(reflection)
            st.success("Great job! Your progress has been saved.")
            st.balloons()

else:  # Progress page
    st.header("Your Growth Mindset Journey")
    
    # Display stats
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Streak", f"{challenge.progress['streak']} days")
    with col2:
        st.metric("Total Challenges", len(challenge.progress['completed_challenges']))
    
    # Display recent reflections
    if challenge.progress["completed_challenges"]:
        st.subheader("Recent Reflections")
        for entry in reversed(challenge.progress["completed_challenges"][-5:]):
            with st.expander(f"Reflection from {entry['date']}"):
                st.write(entry['reflection'])
    else:
        st.info("Complete your first challenge to see your progress!") 