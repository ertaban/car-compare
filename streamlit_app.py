# Import libraries
import streamlit as st

# Set page configuration - MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(layout="wide", page_title="Car Class Navigator")

# Import other libraries after st.set_page_config()
import base64

# Initialize session state if it doesn't exist
if 'current_car_class' not in st.session_state:
    st.session_state.current_car_class = "Mid-Size"  # Starting with mid-size

# Define car classes from small to large
car_classes = ["Compact", "Mid-Size", "Full-Size", "SUV", "Luxury"]

# Find current position and determine left/right car classes
current_index = car_classes.index(st.session_state.current_car_class)
left_class = car_classes[current_index - 1] if current_index > 0 else None
right_class = car_classes[current_index + 1] if current_index < len(car_classes) - 1 else None

# Function to navigate to a different car class
def navigate_to_class(new_class):
    st.session_state.current_car_class = new_class
    st.rerun()  # Using st.rerun() instead of st.experimental_rerun()

# Custom CSS for styling
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<style>
    .car-container {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 2rem;
    }
    .car-icon {
        font-size: 5rem;
        margin: 0 2rem;
    }
    .nav-icon {
        font-size: 3rem;
        cursor: pointer;
        transition: transform 0.3s;
    }
    .nav-icon:hover {
        transform: scale(1.2);
    }
    .left-arrow {
        color: #4287f5;
    }
    .right-arrow {
        color: #f54242;
    }
    .car-label {
        margin-top: 0.5rem;
        font-weight: bold;
    }
    .disabled {
        opacity: 0.3;
        cursor: default;
    }
</style>
""", unsafe_allow_html=True)

# Create the layout
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    # Left navigation
    st.markdown("<div class='car-container'>", unsafe_allow_html=True)
    if left_class:
        if st.button("← Smaller", key="left_nav", help=f"Go to {left_class} class"):
            navigate_to_class(left_class)
        st.markdown(f"<div class='car-label'>{left_class}</div>", unsafe_allow_html=True)
    else:
        st.button("← Smaller", key="left_nav_disabled", disabled=True)
        st.markdown("<div class='car-label'>&nbsp;</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Current car class - using emojis instead of Font Awesome for better compatibility
    car_emojis = {
        "Compact": "🚗",
        "Mid-Size": "🚙",
        "Full-Size": "🚘",
        "SUV": "🚓",
        "Luxury": "🏎️"
    }
    current_emoji = car_emojis.get(st.session_state.current_car_class, "🚗")
    
    st.markdown(f"""
    <div class="car-container">
        <div>
            <div style="font-size: 5rem; text-align: center;">{current_emoji}</div>
            <div class="car-label">{st.session_state.current_car_class}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    # Right navigation
    st.markdown("<div class='car-container'>", unsafe_allow_html=True)
    if right_class:
        if st.button("Larger →", key="right_nav", help=f"Go to {right_class} class"):
            navigate_to_class(right_class)
        st.markdown(f"<div class='car-label'>{right_class}</div>", unsafe_allow_html=True)
    else:
        st.button("Larger →", key="right_nav_disabled", disabled=True)
        st.markdown("<div class='car-label'>&nbsp;</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Display current car class details
st.markdown("---")
st.header(f"{st.session_state.current_car_class} Class Details")
st.write(f"You are currently viewing the {st.session_state.current_car_class} car class.")

# Placeholder for additional car details
car_details = {
    "Compact": "Small, fuel-efficient cars ideal for city driving and tight parking spaces.",
    "Mid-Size": "Balanced size and comfort, suitable for small families and everyday use.",
    "Full-Size": "Spacious sedans with ample legroom and trunk space for longer trips.",
    "SUV": "High clearance vehicles with optional 4-wheel drive and more cargo space.",
    "Luxury": "Premium vehicles with high-end features, materials, and performance."
}

st.write(car_details.get(st.session_state.current_car_class, ""))
