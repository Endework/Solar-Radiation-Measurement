import pandas as pd
import plotly.express as px
import streamlit as st


# Load the data
st.set_page_config(page_title="Solar dashboard",page_icon=":bar_chart:", layout="wide")

   
df=pd.read_csv(r'all_data.csv')

# Sidebar filter
Country = st.sidebar.multiselect(
    "Select the Country:",
    options=df['country'].unique(),
    default=df["country"].unique()
)

# Apply the filter
df_selection = df[df['country'].isin(Country)]

# Calculate the updated KPIs
average_ghi = df_selection['GHI'].mean()
average_amb_temp = df_selection['Tamb'].mean()

# Display the KPIs
left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Average Solar Radiation (GHI):")
    st.subheader(f"{round(average_ghi)} W/m²")
with right_column:
    st.subheader("Average Ambient Temperature:")
    st.subheader(f"{round(average_amb_temp)} °C")
st.markdown("---")

# Main chart


left_column, right_column = st.columns(2)
with left_column:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d')
fig_ws = px.line(df, x='Timestamp', y=['WS', 'WSgust', 'WSstdev'], title='Wind Speed Analysis')
st.plotly_chart(fig_ws)

# Wind direction plot
fig_wd = px.line(df, x='Timestamp', y=['WD', 'WDstdev'], title='Wind Direction Analysis')
st.plotly_chart(fig_wd)
with right_column:
    fig = px.line(df , x='Timestamp', y=['TModA', 'TModB', 'Tamb'],
              labels={'Timestamp': 'Timestamp', 'value': 'Temperature (°C)'},
              title='Temperature Trends')

# Customize the plot (optional)
fig.update_traces(mode='lines+markers')
#fig.update_layout(width=800, height=500)

# Display the plot in Streamlit
st.plotly_chart(fig)
st.markdown("---")
