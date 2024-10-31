import streamlit as st
import numpy as np
import pandas as pd

# Set the title of the app
st.title("Interactive Histogram with Multiplier")

# Generate dummy data
data = np.random.normal(loc=0, scale=1, size=1000)

# Create an input slider to multiply the values
multiplier = st.slider("Select a multiplier for the histogram values:", 0.1, 25.0, 1.0)

# Multiply the data by the selected multiplier
modified_data = data * multiplier

# Create a histogram using Pandas
hist_values, bin_edges = np.histogram(modified_data, bins=30)
hist_df = pd.DataFrame({
    "Bins": bin_edges[:-1],   # The left edges of the bins
    "Frequency": hist_values  # The counts in each bin
})

# Plot the histogram using Streamlit's bar chart
st.bar_chart(hist_df.set_index("Bins"))

# Show the selected multiplier for reference
st.write(f"Current multiplier: {multiplier}")
