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
        interests,
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
        if isinstance(interests, str):
            raise ValueError
        try:
            iter(interests)
        except TypeError:
            raise ValueError
        self.id = id
        self.name = name.title()
        self.affiliation = affiliation
        self.email = email
        self.citations = citations
        self.interests = interests

    def __repr__(self):
        return self.name
