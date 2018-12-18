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
    ):
        for _ in (
            id,
            name,
            affiliation,
            email,
        ):
            if not isinstance(_, str):
                raise ValueError
        self.id = id
        self.name = name.title()
        self.affiliation = affiliation
        self.email = email

    def __repr__(self):
        return self.name
