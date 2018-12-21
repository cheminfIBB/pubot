from pubot.author import Author as _Author
import scholarly as _sch


def author(
    name,
    affiliation,
    ):
    """
    Returns pubot.author.Author objects by searching online.

    Parameters
    -------
        name: str
    Name of the author to find.

    Returns
    -------
        pubot.author.Author objects.
    """
    authors_query = _sch.search_author(name)
    authors = [i.fill() for i in authors_query]
    for author in authors:
        if affiliation in author:
            return _Author(
                id=author.id,

            )
