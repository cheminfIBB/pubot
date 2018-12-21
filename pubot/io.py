from pubot.search import author as _find_author
import pandas as _pd


_AUTHOR_OBJECTS = 'AUTHOR_OBJECTS'


def authors_from_csv(
        filename,
        names_column,
        affiliations_column,
        sep='\t',
    ):
    """
    Returns an iterable of pubot.author.Author objects from a CSV file.

    Parameters
    -------
        filename: path

    Returns
    -------
    Iterable of pubot.author.Author objects.
    """
    dataframe = _pd.read_csv(
        filepath_or_buffer=filename,
        sep=sep,
    )
    dataframe[_AUTHOR_OBJECTS] = dataframe[[
        names_column,
        affiliations_column,
    ]].apply(
        lambda x: _find_author(
            name=x[names_column],
            affiliation=x[affiliations_column],
        ),
        axis=1,
    )
    return dataframe
