import seaborn as sns; sns.set()  # for plot styling
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


class Clustering:
    def __init__(self, df_input):
        isinstance(df_input, pd.DataFrame)

        self.df = df_input
        self.data_to_cluster = df_input.to_numpy()
        self.plt = plt
        self.set_plot_mode(False)

    def set_plot_mode(self, status):
        if status:
            mpl.use('TkAgg')
        else:
            mpl.use('agg')

    def startProcessing(self):
        self.preProcessing()
        self.methodClustering()
        self.posProcessing()

    def showData(self):
        self.plt.show()

    def preProcessing(self):
        pass

    def methodClustering(self):
        pass

    def posProcessing(self):
        pass


class KMeansMethod(Clustering):

    def __init__(self, df_input, alpha=0.5, s_clustering=200, s_processing=50, n_clusters=4):
        super(KMeansMethod, self).__init__(df_input)
        self.alpha = alpha
        self.s_clustering = s_clustering
        self.s_processing = s_processing
        self.n_cluster = n_clusters

    def preProcessing(self):
        pass

    def methodClustering(self):
        self.kmeans = KMeans(n_clusters=self.n_cluster)
        self.kmeans.fit(self.data_to_cluster)
        self.y_kmeans = self.kmeans.predict(self.data_to_cluster)
        self.plt.scatter(self.data_to_cluster[:, 0], self.data_to_cluster[:, 1], c=self.y_kmeans, s=self.s_clustering, cmap='viridis')

    def posProcessing(self):
        centers = self.kmeans.cluster_centers_
        self.plt.scatter(centers[:, 0], centers[:, 1], c='black', s=self.s_processing, alpha=self.alpha)

    def get_plt(self):
        return self.plt

    def get_clusters(self):
        return self.y_kmeans

class KMeansMethod(Clustering):

    def __init__(self, df_input, alpha=0.5, s_clustering=200, s_processing=50, n_clusters=4):
        super(KMeansMethod, self).__init__(df_input)
        self.alpha = alpha
        self.s_clustering = s_clustering
        self.s_processing = s_processing
        self.n_cluster = n_clusters

    def preProcessing(self):
        pass

    def methodClustering(self):
        self.kmeans = KMeans(n_clusters=self.n_cluster)
        self.kmeans.fit(self.data_to_cluster)
        self.y_kmeans = self.kmeans.predict(self.data_to_cluster)
        self.plt.scatter(self.data_to_cluster[:, 0], self.data_to_cluster[:, 1], c=self.y_kmeans, s=self.s_clustering, cmap='viridis')

    def posProcessing(self):
        centers = self.kmeans.cluster_centers_
        self.plt.scatter(centers[:, 0], centers[:, 1], c='black', s=self.s_processing, alpha=self.alpha)

    def get_plt(self):
        return self.plt

    def get_clusters(self):
        return self.y_kmeans

