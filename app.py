import streamlit as st
import pandas as pd

# Title of the app
st.title("📈 Line Chart Visualization App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Read file based on type
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("📋 Data Preview")
        st.write(df.head())

        # Column selection
        st.subheader("⚙️ Select Columns for Line Chart")
        numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

        if len(numeric_columns) >= 2:
            x_axis = st.selectbox("Select X-axis", df.columns)
            y_axis = st.selectbox("Select Y-axis", numeric_columns)

            # Line Chart
            st.subheader("📊 Line Chart")
            st.line_chart(df.set_index(x_axis)[y_axis])
        else:
            st.warning("The file must contain at least two numeric columns for visualization.")

    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Please upload a file to start.")
