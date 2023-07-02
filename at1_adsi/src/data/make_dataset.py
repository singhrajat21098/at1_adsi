# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
import pandas as pd


from data_cleaning_utils import removeOutliers


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    data = pd.read_csv('../../../'+input_filepath)
    data.drop('Id', axis=1, inplace=True)
    data = data[data['GP'] > 0]
    data = removeOutliers(data, 'GP', 3)
    data = removeOutliers(data, 'MIN', 3)
    data = removeOutliers(data, 'PTS', 3)
    data.drop('FGM', axis=1, inplace=True)
    data.drop('3P Made', axis=1, inplace=True)
    data.drop('3P Made', axis=1, inplace=True)
    FT_percent = 100* data['FTM']/data['FTA']
    data['FT%'] = FT_percent
    data = data[(data['FT%'] > 0) & (data['FT%'] < 100)]
    data.drop('FTM', axis=1, inplace=True)
    data = removeOutliers(data, 'OREB', 3)
    data = removeOutliers(data, 'DREB', 3)
    data.drop('REB', axis=1, inplace=True)
    data = removeOutliers(data, 'AST', 3)
    data = removeOutliers(data, 'STL', 3)
    data = removeOutliers(data, 'BLK', 3)
    data = removeOutliers(data, 'TOV', 3)
    data.to_csv('../../../'+output_filepath, index=False)








if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then


    main()
