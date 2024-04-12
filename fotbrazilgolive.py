import streamlit as st

# Session State Management - Create box data if it doesn't exist
if "box_data" not in st.session_state:
  st.session_state.box_data = [
      {"box_state": False, "reject_count": 0, "row_count": 0, "color": "blue"} for _ in range(21)
  ]

# Function to toggle box animation and modify counts
def toggle_box(box_index):
  current_state = st.session_state.box_data[box_index]["box_state"]
  # Update animation state based on current state
  st.session_state.box_data[box_index]["reject_count"] = st.session_state.box_data[i]["reject_count"]
  st.session_state.box_data[box_index]["row_count"] = st.session_state.box_data[i]["row_count"]
  st.session_state.box_data[box_index]["box_state"] = not current_state
  # Update record counts and color only when animation starts
  if not current_state:
    # Set color to yellow when animation stops (example)
    st.session_state.box_data[box_index]["color"] = "yellow"

# --- Admin Page ---
st.title("Admin Page")

# Buttons for each box with additional input fields
for i in range(21):
  box_name = f"Box {i + 1}"

  # Input fields
  row_count = int(st.number_input(f"Row Count for {box_name}", key=f"row_{i}"))
  reject_count = int(st.number_input(f"Reject Count for {box_name}", key=f"reject_{i}"))

  # Update counts in session state
  st.session_state.box_data[i]["reject_count"] = reject_count
  st.session_state.box_data[i]["row_count"] = row_count

  # Buttons - Animate & Stop
  col1, col2 = st.columns(2)
  with col1:
    if st.button(f"Animate {box_name}"):
      # Start animation only if not currently animating
      if not st.session_state.box_data[i]["box_state"]:
        toggle_box(i)
  with col2:
    if st.button(f"Stop {box_name}"):
      # Stop animation and update color
      toggle_box(i)


# --- Public Page ---
st.title("ADL Brazil FOT")

st.markdown("""
<style>
  .container {
    display: flex;
    flex-wrap: wrap;
    width: 800px;  /* Adjust container width if needed */
    justify-content: center;
    gap: 100px;  /* Add a gap property for spacing between boxes */
  }

  .box-and-arrow {
    display: flex;
    flex-direction: column;  /* Stack elements vertically */
    align-items: center;
    margin-right: 50px;
  }

  .arrow {
    width: 30px;
    height: 60px;
    border-left: 15px solid transparent;
    border-right: 15px solid transparent;
    border-top: 40px solid white; 
  }

  .pulsing-box {
    width: 250px;
    height: 250px;
    background-color: var(--box-color);  /* Use variable for color */
    margin: 5px;
    display: flex;  /* Make the box a flex container */
    justify-content: center;  /* Center the content horizontally */
    align-items: center;  /* Center the content vertically */
    animation: pulse 2s infinite alternate;
  }

  .record-counts {
    text-align: center;
    margin-bottom: 0px;
    margin-top: 15px;
  }

  .box-name {
    text-align: center;
    font-size: 50px;  /* Increase font size for box name */
    font-weight: bold;  /* Add boldness for emphasis */
  }
  
  .small-box-name {
    font-size: 20px;  /* Increase font size for box name */
    color: black;
    text-align: center;
    font-weight: bold;  /* Add boldness for emphasis */
  }

  @keyframes pulse {
    0% { opacity: 0.15; }
    100% { opacity: 1; }
  }

  :root {
    --box-color: blue;  /* Default box color */
  }
</style>
""", unsafe_allow_html=True)

# Display the boxes
st.markdown('<div class="container">', unsafe_allow_html=True)
for i in range(21):
  box_name = f"Box {i + 1}"
  box_data = st.session_state.box_data[i]
  if box_data["box_state"]:
    st.markdown(f"""
      <div class="box-and-arrow">
        <div class="record-counts">
          <p>Inserts: {box_data['row_count']} <br> Rejects: {box_data['reject_count']}</p>
        </div>
        <div class="pulsing-box">
          <div class="box-name">{box_name}</div>  </div>
        <div class="arrow"></div>  
      </div>
    """, unsafe_allow_html=True)
  else:
    st.markdown(f"""
      <div class="box-and-arrow">
        <div class="record-counts">
          <p>Inserts: {box_data['row_count']} <br> Rejects: {box_data['reject_count']}</p>
        </div>
        <div style="width: 100px; height: 100px; background-color: lightblue; margin: 5px;"><div class="small-box-name">{box_name}</div></div>
        <div class="arrow"></div> 
      </div>
    """, unsafe_allow_html=True)
st.markdown('</div>' f'<h1 style="text-align: center;">GO LIVE!!!</h1>', unsafe_allow_html=True)

