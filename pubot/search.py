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
    for author in authors_query:
        if affiliation in author.affiliation:
            return _Author(
                id=author.id,
                name=author.name,
                affiliation=author.affiliation,
                email=author.email,
                citations=author.citedby,
                interests=author.interests,
            )
