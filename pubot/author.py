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
        for n, v, t in zip(
            ('id', 'name', 'affiliation', 'email', 'citations',),
            (id, name, affiliation, email, citations,),
            (str, str, str, str, int)
        ):
            if not isinstance(v, t):
                raise ValueError('{} must be {} not {}.'.format(n, t, type(v)))
        if isinstance(interests, str):
            raise ValueError('interests must be {} not {}.'.format(type(interests)))
        try:
            iter(interests)
        except TypeError:
            raise ValueError('interests must be {} not {}.'.format(type(interests)))
        self.id = id
        self.name = name.title()
        self.affiliation = affiliation
        self.email = email
        self.citations = citations
        self.interests = interests

    def __repr__(self):
        return self.name
