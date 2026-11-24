import streamlit as st
import pandas as pd
import plotly.express as px

st.title(" Data Visualization")

file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if file:

    df = pd.read_csv(file)

    st.dataframe(df.head())

    st.markdown("---")

    fig1 = px.scatter(
        df,
        x="FVC",
        y="FEV1",
        color="Disease",
        title="FVC vs FEV1"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    fig2 = px.box(
        df,
        x="Disease",
        y="FEV1_FVC",
        color="Disease",
        title="FEV1/FVC Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    corr = df.select_dtypes(
        include="number"
    ).corr()

    fig3 = px.imshow(
        corr,
        text_auto=True,
        title="Feature Correlation"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    fig4 = px.histogram(
        df,
        x="PEF",
        color="Disease",
        title="PEF Analysis"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )