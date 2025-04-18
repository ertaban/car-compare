import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64

st.title("🎈 Cihangir's app")
st.write(
    "This is the start of the new app!"
)

# Set page configuration
st.set_page_config(layout="wide", page_title="Car Class Navigator")

# Initialize session state if it doesn't exist
if 'current_car_class' not in st.session_state:
    st.session_state.current_car_class = "Mid-Size"  # Starting with mid-size

# Define car classes from small to large
car_classes = ["Compact", "Mid-Size", "Full-Size", "SUV", "Luxury"]

# Find current position and determine left/right car classes
current_index = car_classes.index(st.session_state.current_car_class)
left_class = car_classes[current_index - 1] if current_index > 0 else None
right_class = car_classes[current_index + 1] if current_index < len(car_classes) - 1 else None

# Function to get appropriate car icon for each class
def get_car_icon(car_class):
    # Using Font Awesome icons encoded in base64 for simplicity
    # In a real app, you might use actual car images
    icons = {
        "Compact": "fas fa-car",
        "Mid-Size": "fas fa-car-side",
        "Full-Size": "fas fa-car-alt",
        "SUV": "fas fa-truck-monster",
        "Luxury": "fas fa-car-luxury"
    }
    return icons.get(car_class, "fas fa-car")

# Function to navigate to a different car class
def navigate_to_class(new_class):
    st.session_state.current_car_class = new_class
    st.experimental_rerun()

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
        cursor: pointer;
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
    if left_class:
        st.markdown(f"""
        <div class="car-container" onclick="parent.postMessage({{action: 'navigate', class: '{left_class}'}}, '*')">
            <i class="fas fa-chevron-circle-left nav-icon left-arrow"></i>
            <div class="car-label">Go to {left_class}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # JavaScript to handle the click and communicate with Python
        st.markdown("""
        <script>
        document.querySelector('.left-arrow').addEventListener('click', function() {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'left_clicked'}, '*');
        });
        </script>
        """, unsafe_allow_html=True)
        
        # Handle the click with a button (hidden by CSS)
        if st.button("Navigate Left", key="left_nav", help=f"Go to {left_class} class"):
            navigate_to_class(left_class)
    else:
        st.markdown("""
        <div class="car-container">
            <i class="fas fa-chevron-circle-left nav-icon disabled"></i>
        </div>
        """, unsafe_allow_html=True)

with col2:
    # Current car class
    st.markdown(f"""
    <div class="car-container">
        <div>
            <i class="{get_car_icon(st.session_state.current_car_class)} car-icon"></i>
            <div class="car-label">{st.session_state.current_car_class}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    # Right navigation
    if right_class:
        st.markdown(f"""
        <div class="car-container" onclick="parent.postMessage({{action: 'navigate', class: '{right_class}'}}, '*')">
            <i class="fas fa-chevron-circle-right nav-icon right-arrow"></i>
            <div class="car-label">Go to {right_class}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Handle the click with a button
        if st.button("Navigate Right", key="right_nav", help=f"Go to {right_class} class"):
            navigate_to_class(right_class)
    else:
        st.markdown("""
        <div class="car-container">
            <i class="fas fa-chevron-circle-right nav-icon disabled"></i>
        </div>
        """, unsafe_allow_html=True)

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
