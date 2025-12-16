import streamlit as st

st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and select the region")

sale_target = st.number_input("Enter Monthly Sales Target(in USD):",
                              min_value = 0.00,
                              value = 50000.00,
                              step = 1000,
                              format = "%.2f" )
region = st.selectbox(
  "Select Region", 
  ["North", "South", "East", "West"] )

if st.button("Submit"):
  st.write("###Submission Summary###")
  st.write(f"**Monthly Sales Target:** ${sales_target:,.2f}")
  st.write(f"**Selected Region:** {region}")
  st.success("Dashborad updated successfully")
  if sale_target > 100000:
    st.write(f"Great! You have set an ambitious target!")
