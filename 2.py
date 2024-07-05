import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Mall_Customers.csv')

# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Select relevant features for clustering
features = ['Annual Income (k$)', 'Spending Score (1-100)']

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[features])



# From the elbow plot, choose the number of clusters, say 5
n_clusters = 5

# Create the K-means model
kmeans = KMeans(n_clusters=n_clusters, random_state=42)

# Fit the model and predict the cluster labels
data['Cluster'] = kmeans.fit_predict(data_scaled)

# Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'], c=data['Cluster'], cmap='viridis', s=50)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segments')
plt.show()

# Display the first few rows with cluster labels
print(data.head())