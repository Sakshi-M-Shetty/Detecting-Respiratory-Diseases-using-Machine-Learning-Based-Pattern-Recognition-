import streamlit as st
import pandas as pd
import plotly.express as px

st.title(" Model Performance")

metrics = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],

    "Value":[
        96.8,
        95.9,
        95.6,
        95.7
    ]
})

st.dataframe(
    metrics,
    use_container_width=True
)

fig = px.bar(
    metrics,
    x="Metric",
    y="Value",
    text="Value",
    title="Performance Metrics"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

cm = pd.DataFrame(
[
[620,10,5,2],
[8,610,12,3],
[6,15,605,4],
[3,4,6,622]
],
columns=[
"Healthy",
"COPD",
"Asthma",
"Restrictive"
],
index=[
"Healthy",
"COPD",
"Asthma",
"Restrictive"
]
)

fig2 = px.imshow(
    cm,
    text_auto=True,
    title="Confusion Matrix"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)