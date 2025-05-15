import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Simple Drone Design Assisting Bot ---
st.title("🚀 Drone Design Assisting Bot")

st.write("""
Welcome! I can help you with basic drone design suggestions. 
Just input your requirements, and I’ll recommend components.
""")

# User Inputs
mission_type = st.selectbox("Select Mission Type", ["Racing", "Aerial Photography", "Payload Delivery", "Survey/Mapping"])
payload_weight = st.number_input("Payload Weight (grams)", min_value=0)
flight_time = st.number_input("Desired Flight Time (minutes)", min_value=1)
frame_size = st.slider("Frame Size (in mm)", min_value=150, max_value=650, value=450, step=50)
propeller_diameter = st.selectbox("Propeller Diameter (in inches)", [5, 6, 8, 10, 12, 15])

if st.button("Get Recommendations"):
    # Simple logic (placeholder)
    if mission_type == "Racing":
        st.success("✅ Recommended: Lightweight carbon fiber frame, 2306 2400KV motors, 5-inch propellers, 4S LiPo battery (1500mAh)")
    elif mission_type == "Aerial Photography":
        st.success("✅ Recommended: 450mm frame, 2212 920KV motors, 10-inch propellers, 3S or 4S LiPo (5200mAh), gimbal for camera")
    elif mission_type == "Payload Delivery":
        if payload_weight > 1000:
            st.success("✅ Recommended: Heavy-lift frame, 3510 or larger motors, 15-inch props, 6S LiPo (10000mAh), strong ESCs")
        else:
            st.success("✅ Recommended: Medium-lift quad, 2814 700KV motors, 12-inch props, 4S or 6S battery")
    elif mission_type == "Survey/Mapping":
        st.success("✅ Recommended: Fixed-wing airframe, efficient motor, 10-12 inch props, long-range 4S or 6S battery")

    # Basic flight time warning
    if flight_time > 30:
        st.warning("⚠ High flight time! Consider using larger batteries or fixed-wing designs for endurance.")

# --- Draw Drone Skeleton in Sidebar ---
def draw_drone(frame_size, prop_dia):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim(-frame_size/2 - 100, frame_size/2 + 100)
    ax.set_ylim(-frame_size/2 - 100, frame_size/2 + 100)
    ax.set_aspect('equal')
    ax.axis('off')

    # Motor positions
    motors = [
        (-frame_size/2, frame_size/2),
        (frame_size/2, frame_size/2),
        (frame_size/2, -frame_size/2),
        (-frame_size/2, -frame_size/2),
    ]

    # Draw frame lines
    for i in range(4):
        x1, y1 = 0, 0
        x2, y2 = motors[i]
        ax.plot([x1, x2], [y1, y2], 'k-', lw=2)

    # Draw motors and propellers
    for x, y in motors:
        ax.add_patch(plt.Circle((x, y), 20, color='red'))
        ax.add_patch(plt.Circle((x, y), prop_dia * 12.7 / 2, fill=False, linestyle='--'))

    # Draw center and payload mount
    ax.add_patch(plt.Rectangle((-30, -30), 60, 60, fill=True, color='blue', alpha=0.4))
    ax.text(0, 0, "Payload", ha='center', va='center', fontsize=8, color='white')

    ax.set_title("Drone Skeleton (Top View)", fontsize=10)
    return fig

# Show in sidebar
with st.sidebar:
    st.markdown("### 📐 Drone Skeleton Diagram")
    fig = draw_drone(frame_size, propeller_diameter)
    st.pyplot(fig)

st.write("\n💡 Want a more advanced version? Let me know!")
