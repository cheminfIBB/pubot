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
        self.id = id
        self.name = name
        self.affiliation = affiliation
        self.email = email

    def __repr__(self):
        return self.name
