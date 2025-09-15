
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def cluster_customers(df, n_clusters=3):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)
    return df