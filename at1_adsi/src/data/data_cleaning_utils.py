

def removeOutliers(data, column, num_std = 2):
    "This function removes outliers from a pandas series using the standard deviation method"
    mean = data[column].mean()
    std = data[column].std()
    cut_off = std * num_std
    lower, upper = mean - cut_off, mean + cut_off
    data = data[(data[column] < upper) & (data[column] > lower)]
    return data

    