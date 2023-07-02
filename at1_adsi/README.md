NBA_data_experiments
==============================

# NBA Player Classification

This project focuses on classifying NBA players based on various attributes and statistics. The goal is to predict the classification or longevity of rookie players in the NBA using machine learning techniques. The project includes data cleaning, exploratory data analysis, and multiple experiments using Jupyter notebooks.

## Installation

To install the project dependencies, please make sure you have [Python](https://www.python.org/downloads/) installed on your system. Then, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/nba-player-classification.git
   ```

2. Navigate to the project directory:

   ```bash
   cd nba-player-classification
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment (optional but recommended):

   - For Windows:

     ```bash
     env\Scripts\activate
     ```

   - For Unix or Linux:

     ```bash
     source env/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

This will install all the necessary packages and libraries required for running the project.

## Usage

To get started with the project, follow the steps below:

1. Run the `Data_cleaning.ipynb` notebook in the `notebooks` folder. This notebook handles data cleaning and preprocessing tasks to prepare the dataset for analysis and modeling.

2. After running the data cleaning notebook, proceed to run the `eda.ipynb` notebook. This notebook focuses on exploratory data analysis, providing insights and visualizations to understand the dataset and player attributes.

3. Next, you can explore the experiment notebooks in the following order:

   a. `experiment1.ipynb`
   b. `experiment2.ipynb`
   c. `experiment3.ipynb`

   These notebooks contain different experiments and approaches to classifying NBA players based on their statistics. Each notebook builds upon the previous one, exploring various machine learning algorithms and techniques for classification.

4. Lastly, the final submission test set results can be found in the `data/processed/testset_submission.csv` file. This file contains the predictions made by the trained model on the test set. You can analyze and evaluate the performance of the model using this file.

## Conclusion

This project provides a comprehensive analysis of NBA player classification, focusing on predicting the longevity of rookie players. By following the installation instructions and running the provided notebooks, you can explore the data, perform experiments, and analyze the results. The project aims to contribute to the understanding and evaluation of NBA player performance and career prospects.

For more details and information, please refer to the individual notebooks and code files within the repository.

Feel free to contribute, provide feedback, or report any issues through GitHub. Enjoy exploring NBA player classification!


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
