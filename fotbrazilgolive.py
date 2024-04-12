import streamlit as st

if "admin_visible" not in st.session_state:
  st.session_state.admin_visible = True

def toggle_admin_page():
  st.session_state.admin_visible = not st.session_state.admin_visible

box_names = {
  0: "I009",
  1: "I833",
  2: "I040",
  3: "I856+I863",
  4: "I301",
  5: "I335",
  6: "I009",
  7: "I915",
  8: "I916",
  9: "I840",
  10: "I900",
  11: "I851",
  12: "I902",
  13: "I904",
  14: "I917",
  15: "I918",
  16: "I009",
  17: "I917",
  18: "I918",
  19: "I009",
  20: "I918"
}

if "box_data" not in st.session_state:
    st.session_state.box_data = [
        {"box_state": False, "reject_count": 0, "row_count": 0, "color": "blue"} for _ in range(21)
    ]


def toggle_box(box_index):
    current_state = st.session_state.box_data[box_index]["box_state"]
    st.session_state.box_data[box_index]["reject_count"] = st.session_state.box_data[i]["reject_count"]
    st.session_state.box_data[box_index]["row_count"] = st.session_state.box_data[i]["row_count"]
    st.session_state.box_data[box_index]["box_state"] = not current_state
    if not current_state:
        st.session_state.box_data[box_index]["color"] = "yellow"


# --- Admin Page ---
if st.session_state.admin_visible:
    st.title("Admin Page")
    for i in range(21):
        box_name = box_names[i]
        row_count = int(st.number_input(f"Row Count for {box_name}", key=f"row_{i}"))
        reject_count = int(st.number_input(f"Reject Count for {box_name}", key=f"reject_{i}"))

        st.session_state.box_data[i]["reject_count"] = reject_count
        st.session_state.box_data[i]["row_count"] = row_count

        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Animate {box_name}", key=f"animate_{i}"):
                if not st.session_state.box_data[i]["box_state"]:
                    toggle_box(i)
        with col2:
            if st.button(f"Stop {box_name}", key=f"stop_{i}"):
                toggle_box(i)

# --- Public Page ---
st.title("FOT Brazil ADL Current Status")

st.markdown("""
<style>
  .container {
    display: flex;
    flex-wrap: wrap;
    width: 800px;  /* Adjust container width if needed */
    justify-content: center;
    gap: 100px;  /* Add a gap property for spacing between boxes */
  }

  .box-and-arrow-and-square {
    display: flex;
    flex-direction: column;  /* Stack elements vertically */
    align-items: center;
    margin-right: 50px;
  }

  .arrow {
    width: 20px;
    height: 20px;
    border-left: 15px solid transparent;
    border-right: 15px solid transparent;
    border-top: 40px solid white; 
  }
  .square {
    width: 10px;
    height: 10px;
    border-left: 5px solid;
    border-right: 5px solid;
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
    font-size: 60px;  /* Increase font size for box name */
    font-weight: bold;  /* Add boldness for emphasis */
  }

  .small-box-name {
    font-size: 35px;  /* Increase font size for box name */
    color: black;
    text-align: center;
    font-weight: bold;  /* Add boldness for emphasis */
    justify-content: center;  /* Center the content horizontally */
    align-items: center;  /* Center the content vertically */
  }
  @keyframes pulse {
    0% { opacity: 0.15; }
    100% { opacity: 1; }
  }

  :root {
    --box-color: green;  /* Default box color */
  }
</style>
""", unsafe_allow_html=True)

# Display the boxes
st.markdown('<div class="container">', unsafe_allow_html=True)
for i in range(21):
    box_name = box_names[i]
    box_data = st.session_state.box_data[i]
    if box_data["box_state"]:
        st.markdown(f"""
      <div class="box-and-arrow-and-square">
        <div class="record-counts">
          <p>Inserts: {box_data['row_count']} <br> Rejects: {box_data['reject_count']}</p>
        </div>
        <div class="pulsing-box">
          <div class="box-name">{box_name}</div>  </div>
        <div class="square"></div>
        <div class="arrow"></div>  
      </div>
    """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
      <div class="box-and-arrow-and-square">
        <div class="record-counts">
          <p>Inserts: {box_data['row_count']} <br> Rejects: {box_data['reject_count']}</p>
        </div>
        <div style="width: 200px; height: 200px; background-color: lightblue; margin: 5px;"><div class="small-box-name">{box_name}</div></div>
        <div class="square"></div>
        <div class="arrow"></div> 
      </div>
    """, unsafe_allow_html=True)
st.markdown('</div>' f'<h1 style="text-align: center;">GO LIVE!!!</h1>', unsafe_allow_html=True)

if st.checkbox(""):
    toggle_admin_page()
