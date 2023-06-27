import matplotlib.pyplot as plt
import numpy as np

def plot_feature_importances_panda_dataset(model,dataset):
	n_features = dataset.data.shape[1]
	plt.barh(range(n_features), model.feature_importances_, 
align='center' )
	plt.yticks(np.arange(n_features), dataset.feature_names)
	plt.xlabel("Importance des paramètres")
	plt.ylabel("Paramètres")
	plt.ylim(-1,n_features)

