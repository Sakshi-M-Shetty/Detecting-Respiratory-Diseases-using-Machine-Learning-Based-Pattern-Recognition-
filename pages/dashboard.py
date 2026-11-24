import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Respiratory Disease Detection Dashboard")

df = pd.read_csv("respiratory_dataset.csv")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Total Patients", len(df))

with col2:
    st.metric("Diseases", df["Disease"].nunique())

with col3:
    st.metric("Features", 8)

with col4:
    st.metric("Model Accuracy", "96.8%")

st.markdown("---")

col1,col2 = st.columns(2)

with col1:

    disease_count = df["Disease"].value_counts()

    fig = px.pie(
        values=disease_count.values,
        names=disease_count.index,
        title="Disease Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

with col2:

    fig = px.histogram(
        df,
        x="FEV1",
        color="Disease",
        title="FEV1 Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(df.head(20),use_container_width=True)