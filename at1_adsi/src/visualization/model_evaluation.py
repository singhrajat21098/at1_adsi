# Importing all the necessary libraries for Data visulaization

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score


def plot_confusion_matrix(actual_values, predicted_values, title = "Confusion Matrix" ,cmap=plt.cm.Blues):

    """This function plots the confusion matrix for the model evaluation"""

    return sns.heatmap(confusion_matrix(actual_values, predicted_values), annot = True, cmap = cmap, fmt="d").set_title(title)


def plot_roc_curve(actual_values, predicted_prob, model_name):

    """This function plots the ROC curve for the model evaluation"""

    fpr, tpr, thresholds = roc_curve(actual_values, predicted_prob)
    plt.plot(fpr, tpr, label = 'ROC curve (area = %0.2f)' % roc_auc_score(actual_values, predicted_prob))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.05])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate or (1 - Specifity)')
    plt.ylabel('True Positive Rate or (Sensitivity)')
    plt.title('ROC Curve for ' + model_name)
    plt.legend(loc="lower right")
    plt.show()

    return None 



