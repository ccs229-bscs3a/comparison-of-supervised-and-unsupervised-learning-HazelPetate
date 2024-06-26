#Input the relevant libraries
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import datasets, metrics
import time

# Define the Streamlit app
def app():

    st.subheader('Supervised Learning, Classification, and KNN with Breast Cancer Wisconsin Dataset')
    text = """**Supervised Learning:**
    \nSupervised learning is a branch of machine learning where algorithms learn from labeled data. 
    This data consists of input features (X) and corresponding outputs or labels (y). The algorithm learns a 
    mapping function from the input features to the outputs, allowing it to predict the labels for 
    unseen data points.
    \n**Classification:**
    Classification is a specific task within supervised learning where the labels belong to discrete 
    categories. The goal is to build a model that can predict the category label of a new data 
    point based on its features.
    \n**K-Nearest Neighbors (KNN):**
    KNN is a simple yet powerful algorithm for both classification and regression tasks. 
    \n**The Breast Cancer Wisconsin Dataset:**
    The Breast Cancer Wisconsin dataset is a popular benchmark dataset in machine learning. It contains information about 569
    instances that would differ from two different class: Malignant, and Benign. 
    \n**KNN Classification with Breast Cancer:**
    \n1. **Training:**
    * The KNN algorithm stores the entire Breast Cancer Wisconsin dataset (features and labels) as its training data.
    \n2. **Prediction:**
    * When presented with a breast cancer data (unknown species), KNN calculates the distance (often Euclidean distance) 
    between this cancers's features and all the cancers in the training data.
    * The user defines the value of 'k' (number of nearest neighbors). KNN identifies the 'k' closest 
    data points (cancer) in the training set to the new flower.
    * KNN predicts the class label (Malignant or Benign) for the new cancer based on the majority vote among its 
    'k' nearest neighbors. For example, if three out of the five nearest neighbors belong to Malinant, 
    the new flower is classified as Malignant.
    **Choosing 'k':**
    The value of 'k' significantly impacts KNN performance. A small 'k' value might lead to overfitting, where the 
    model performs well on the training data but poorly on unseen data. Conversely, a large 'k' value might not 
    capture the local patterns in the data and lead to underfitting. The optimal 'k' value is often determined 
    through experimentation.
    \n**Advantages of KNN:**
    * Simple to understand and implement.
    * No complex model training required.
    * Effective for datasets with well-defined clusters."""
    st.write(text)
    k = st.sidebar.slider(
        label="Select the value of k:",
        min_value= 2,
        max_value= 10,
        value=5,  # Initial value
    )

    if st.button("Begin"):
        # Load the Breast Cancer dataset
        breastcancer = datasets.load_breastcancer()
        X = breastcancer.data  # Features
        y = breastcancer.target  # Target labels (species)

        # KNN for supervised classification (reference for comparison)

        # Define the KNN classifier with k=5 neighbors
        knn = KNeighborsClassifier(n_neighbors=k)

        # Train the KNN model
        knn.fit(X, y)

        # Predict the cluster labels for the data
        y_pred = knn.predict(X)
        st.write('Confusion Matrix')
        cm = confusion_matrix(y, y_pred)
        st.text(cm)
        st.subheader('Performance Metrics')
        st.text(classification_report(y, y_pred))

        # Get unique class labels and color map
        unique_labels = list(set(y_pred))
        colors = plt.cm.get_cmap('viridis')(np.linspace(0, 1, len(unique_labels)))

        fig, ax = plt.subplots(figsize=(8, 6))

        for label, color in zip(unique_labels, colors):
            indices = y_pred == label
            # Use ax.scatter for consistent plotting on the created axis
            ax.scatter(X[indices, 0], X[indices, 1], label=breastcancer.target_names[label], c=color)

        # Add labels and title using ax methods
        ax.set_xlabel('Malignant')
        ax.set_ylabel('Benign')
        ax.set_title('Malignant vs Benign Colored by Predicted Breast Cancer Class')

        # Add legend and grid using ax methods
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)


#run the app
if __name__ == "__main__":
    app()
