import unittest
import uuid
import random


class AuthorTestsInit(unittest.TestCase):
    """
    Tests of the pubot.author.Author initialization.
    """
    def setUp(self):
        import pubot.author

        self.ref_id = str(uuid.uuid4()).split('-')[0]
        self.ref_name = 'Arnold Schwarzenegger'
        self.ref_affiliation = 'Institute of SkyNet SI'
        self.ref_email = 'arni@future.net'
        self.ref_citations = random.randint(0, 10000)
        self.ref_interests = ['Machine Learning', 'Doomsday devices', 'Miniguns',]

        self.test_author = pubot.author.Author(
            id=self.ref_id,
            name=self.ref_name,
            affiliation=self.ref_affiliation,
            email=self.ref_email,
            citations = self.ref_citations,
            interests = self.ref_interests,
        )

    def test_attribs(self):
        """
        Tests if pubot.author.Author object has proper attributes after init.
        """
        self.assertEqual(self.ref_id, self.test_author.id)
        self.assertEqual(self.ref_name, self.test_author.name)
        self.assertEqual(self.ref_affiliation, self.test_author.affiliation)
        self.assertEqual(self.ref_email, self.test_author.email)
        self.assertEqual(self.ref_citations, self.test_author.citations)
        self.assertEqual(self.ref_interests, self.test_author.interests)

    def test_attribs_fail(self):
        """
        Tests if pubot.author.Author object raises an exception when bad values
        passed to init.
        """
        import pubot.author
        with self.assertRaises(ValueError):
            pubot.author.Author(
                id=uuid.uuid4(),
                name=self.ref_name,
                affiliation=self.ref_affiliation,
                email=self.ref_email,
                citations=self.ref_citations,
                interests=self.ref_interests,
            )
            pubot.author.Author(
                id=self.ref_id,
                name=uuid.uuid4(),
                affiliation=self.ref_affiliation,
                email=self.ref_email,
                citations=self.ref_citations,
                interests=self.ref_interests,
            )
            pubot.author.Author(
                id=self.ref_id,
                name=self.ref_name,
                affiliation=uuid.uuid4(),
                email=self.ref_email,
                citations=self.ref_citations,
                interests=self.ref_interests,
            )
            pubot.author.Author(
                id=self.ref_id,
                name=self.ref_name,
                affiliation=self.ref_affiliation,
                email=uuid.uuid4(),
                citations=self.ref_citations,
                interests=self.ref_interests,
            )
            pubot.author.Author(
                id=self.ref_id,
                name=self.ref_name,
                affiliation=self.ref_affiliation,
                email=self.ref_email,
                citations=uuid.uuid4(),
                interests=self.ref_interests,
            )
            pubot.author.Author(
                id=self.ref_id,
                name=self.ref_name,
                affiliation=self.ref_affiliation,
                email=self.ref_email,
                citations=self.ref_citations,
                interests=uuid.uuid4(),
            )
            pubot.author.Author(
                id=self.ref_id,
                name=self.ref_name,
                affiliation=self.ref_affiliation,
                email=self.ref_email,
                citations=self.ref_citations,
                interests=self.ref_name,
            )

    def test_repr(self):
        """
        Tests if pubot.author.Author.__repr__ returns proper value.
        """
        self.assertEqual(self.ref_name, str(self.test_author))


class AuthorTestsComparisons(unittest.TestCase):
    """
    Tests of pubot.author.Author comparison magics.
    """
    def setUp(self):
        import pubot.author

        self.ref_citations_1, self.ref_citations_2 = (random.randint(0, 10000), random.randint(0, 10000))
        while self.ref_citations_1 < self.ref_citations_2:
            self.ref_citations_1, self.ref_citations_2 = (random.randint(0, 10000), random.randint(0, 10000))


        self.ref_id_1 = str(uuid.uuid4()).split('-')[0]
        self.ref_name_1 = 'Arnold Schwarzenegger'
        self.ref_affiliation_1 = 'Institute of SkyNet SI'
        self.ref_email_1 = 'arni@future.net'
        self.ref_interests_1 = ['Machine Learning', 'Doomsday devices', 'Miniguns',]

        self.ref_id_2 = str(uuid.uuid4()).split('-')[0]
        self.ref_name_2 = 'Sylvester Stallone'
        self.ref_affiliation_2 = 'Institute of Italian Stallions'
        self.ref_email_2 = 'sly@cliffhanger.org'
        self.ref_interests_2 = ['Mountain Climbing', 'Gym', 'Miniguns',]

        self.test_author_1 = pubot.author.Author(
            id=self.ref_id_1,
            name=self.ref_name_1,
            affiliation=self.ref_affiliation_1,
            email=self.ref_email_1,
            citations = self.ref_citations_1,
            interests = self.ref_interests_1,
        )
        self.test_author_2, self.test_author_3 = (
            pubot.author.Author(
                id=self.ref_id_2,
                name=self.ref_name_2,
                affiliation=self.ref_affiliation_2,
                email=self.ref_email_2,
                citations = self.ref_citations_2,
                interests = self.ref_interests_2,
        ),
            pubot.author.Author(
                id=self.ref_id_2,
                name=self.ref_name_2,
                affiliation=self.ref_affiliation_2,
                email=self.ref_email_2,
                citations = self.ref_citations_2,
                interests = self.ref_interests_2,
        ),
            )
# NOTE: This is a author_1 and author_2 hybrid for comparisons
        self.test_author_4 = pubot.author.Author(
            id=self.ref_id_2,
            name=self.ref_name_1,
            affiliation=self.ref_affiliation_1,
            email=self.ref_email_2,
            citations = self.ref_citations_2,
            interests = self.ref_interests_2,
        )

    def test_equal(self):
        """
        Tests if the same instances of pubot.author.Author are the same.
        """
        self.assertEqual(self.test_author_1, self.test_author_1)
        self.assertEqual(self.test_author_2, self.test_author_2)
        self.assertEqual(self.test_author_1, self.test_author_4)

    def test_not_equal(self):
        """
        Tests if the different instance of pubot.author.Author are not the same.
        """
        self.assertNotEqual(self.test_author_1, self.test_author_2)

    def test_greater(self):
        """
        Tests if the different instance of pubot.author.Author are not equal
        in the proper way.
        """
        self.assertGreater(self.test_author_1, self.test_author_2)

    def test_greater_equal(self):
        """
        Tests if the different instance of pubot.author.Author are not equal
        in the proper way.
        """
        self.assertGreaterEqual(self.test_author_1, self.test_author_2)
        self.assertGreaterEqual(self.test_author_2, self.test_author_3)

    def test_less_equal(self):
        """
        Tests if the different instance of pubot.author.Author are not equal
        in the proper way.
        """
        self.assertLessEqual(self.test_author_2, self.test_author_1)
        self.assertLessEqual(self.test_author_2, self.test_author_3)

    def test_lesser(self):
        """
        Tests if the different instance of pubot.author.Author are not equal
        in the proper way.
        """
        self.assertLess(self.test_author_2, self.test_author_1)


class PublicationTestsInit(unittest.TestCase):
    """
    Test of the pubot.publication.Publication initialization.
    """
    def setUp(self):
        import pubot.author
        import pubot.publication

        self.ref_author_id = str(uuid.uuid4()).split('-')[0]
        self.ref_name = 'Arnold Schwarzenegger'
        self.ref_affiliation = 'Institute of SkyNet SI'
        self.ref_email = 'arni@future.net'
        self.ref_citations = random.randint(0, 10000)
        self.ref_interests = ['Machine Learning', 'Doomsday devices', 'Miniguns',]

        self.ref_publication_id = str(uuid.uuid4()).split('-')[0]
        self.ref_title = "'Kill all humans - Bender's great dream"
        self.ref_abstract = """Whether to wipe-out all meatballs or not is
        still an open question for a robot. In this paper, we discuss ethics and
        methods for the robots' world domination."""
        self.ref_url = 'https://journal-of-robotics.org/papers/id=66'
        self.ref_citations = random.randint(0, 10000)
        self.ref_source = 'scholar'

        self.test_author = pubot.author.Author(
            id=self.ref_author_id,
            name=self.ref_name,
            affiliation=self.ref_affiliation,
            email=self.ref_email,
            citations = self.ref_citations,
            interests = self.ref_interests,
        )

        self.test_publication = pubot.publication.Publication(
            id=self.ref_publication_id,
            title=self.ref_title,
            abstract=self.ref_abstract,
            author=self.test_author,
            url=self.ref_url,
            citations=self.ref_citations,
            source=self.ref_source,
        )

    def test_attribs(self):
        """
        Tests if pubot.publication.Publication object has proper attributes
        after init.
        """
        self.assertEqual(self.ref_publication_id, self.test_publication.id)
