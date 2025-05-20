import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import tree
import streamlit as st
from web_functions import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')
    st.title("Visualisasi Prediksi Batu Ginjal")

    # Gunakan satu kali checkbox dan simpan hasilnya
    conf_matrix = st.checkbox("Plot Confusion Matrix")
    decision_tree = st.checkbox("Plot Decision Tree")

    model = None
    score = None

    if conf_matrix or decision_tree:
        model, score = train_model(x, y)

    if conf_matrix:
        plt.figure(figsize=(10, 6))
        ConfusionMatrixDisplay.from_estimator(
            model, x, y,
            display_labels=['nockd', 'ckd'],
            cmap=plt.cm.Blues
        )
        st.pyplot(plt.gcf())

    if decision_tree:
        dot_data = tree.export_graphviz(
            decision_tree=model,
            max_depth=3,
            out_file=None,
            filled=True,
            rounded=True,
            feature_names=x.columns,
            class_names=['nockd', 'ckd']
        )
        st.graphviz_chart(dot_data)
