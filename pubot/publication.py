import urllib.parse
import pubot.author


class Publication:
    """
    Holds attributes of publication. Provides methods for comparison between
    instances.
    """
    def __init__(
        self,
        id,
        title,
        abstract,
        author,
        url,
        citations,
        source,

    ):
        for n, v, t in zip(
            (id, title, abstract, url, citations, source),
            (id, title, abstract, url, citations, source),
            (str, str, str, str, int, str)
        ):
            if not isinstance(v, t):
                raise ValueError('{} must be {} not {}.'.format(n, t, type(v)))
        if not isinstance(author, pubot.author.Author):
            raise ValueError('author must be {} not {}.'.format(pubot.author.Author, type(v)))
        if urllib.parse.urlparse(url).scheme not in ['https', 'http']:
            raise ValueError('url must be a proper URL not {}'.format(type(url)))

        self.id = id
        self.title = title.title()
        self.abstract = abstract
        self.author = author
        self.url = url
        self.citations = citations
        self.source = source

    def __repr__(self):
        return self.title

    def __lt__(
        self,
        other
    ):
        return self.citations < other.citations

    def __le__(
        self,
        other
    ):
        return self.citations <= other.citations

    def __gt__(
        self,
        other
    ):
        return self.citations > other.citations

    def __ge__(
        self,
        other
    ):
        return self.citations >= other.citations

    def __ne__(
        self,
        other
    ):
        return self.title.lower() != other.title.lower() and self.author != other.author

    def __eq__(
        self,
        other
    ):
        return self.title.lower() == other.title.lower() and self.author == other.author

    def __hash__(self):
        return hash(
            self.title.lower(),
            self.abstract.lower(),
            self.author,
            )
