class Author:
    """
    Holds attributes based on author's information available at Google Scholar.
    Provides methods for comparison between instances.
    """
    def __init__(
        self,
        id,
        name,
        affiliation,
        email,
        citations,
    ):
        for _ in (
            id,
            name,
            affiliation,
            email,
        ):
            if not isinstance(_, str):
                raise ValueError
        if not isinstance(citations, int):
            raise ValueError
        self.id = id
        self.name = name.title()
        self.affiliation = affiliation
        self.email = email
        self.citations = citations

    def __repr__(self):
        return self.name
