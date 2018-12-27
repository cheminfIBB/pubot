import unittest
import uuid
import random
import pandas as pd


class AuthorInitTests(unittest.TestCase):
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


class AuthorComparisonsTests(unittest.TestCase):
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


class PublicationInitTests(unittest.TestCase):
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

    def test_attribs_fail(self):
        """
        Tests if pubot.publication.Publication object raises an exception when
        bad values are passed to init.
        """
        import pubot.publication
        with self.assertRaises(ValueError):
            pubot.publication.Publication(
                id=uuid.uuid4(),
                title=self.ref_title,
                abstract=self.ref_abstract,
                author=self.test_author,
                url=self.ref_url,
                citations=self.ref_citations,
                source=self.ref_source,
            )
            pubot.publication.Publication(
                id=self.ref_id,
                title=uuid.uuid4(),
                abstract=self.ref_abstract,
                author=self.test_author,
                url=self.ref_url,
                citations=self.ref_citations,
                source=self.ref_source,
            )
            pubot.publication.Publication(
                id=self.ref_id,
                title=self.ref_title,
                abstract=uuid.uuid4(),
                author=self.test_author,
                url=self.ref_url,
                citations=self.ref_citations,
                source=self.ref_source,
            )
            pubot.publication.Publication(
                id=self.ref_id,
                title=self.ref_title,
                abstract=self.ref_abstract,
                author=uuid.uuid4(),
                url=self.ref_url,
                citations=self.ref_citations,
                source=self.ref_source,
            )
            pubot.publication.Publication(
                id=self.ref_id,
                title=self.ref_title,
                abstract=self.ref_abstract,
                author=self.test_author,
                url=uuid.uuid4(),
                citations=self.ref_citations,
                source=self.ref_source,
            )
            pubot.publication.Publication(
                id=self.ref_id,
                title=self.ref_title,
                abstract=self.ref_abstract,
                author=self.test_author,
                url=self.ref_url,
                citations=uuid.uuid4(),
                source=self.ref_source,
            )
            pubot.publication.Publication(
                id=self.ref_id,
                title=self.ref_title,
                abstract=self.ref_abstract,
                author=self.test_author,
                url=self.ref_url,
                citations=self.ref_citations,
                source=uuid.uuid4(),
            )
        def test_repr(self):
            """
            Tests if pubot.publication.Publication.__repr__ returns proper
            value.
            """
            self.assertEqual(self.ref_title, str(self.test_publication))


class PublicationComparisonTests(unittest.TestCase):
    """
    Tests of pubot.publication.Publication comparison magics.
    """
    def setUp(self):
        """
        """
        import pubot.author
        import pubot.publication

        self.ref_author_citations_1, self.ref_author_citations_2 = (random.randint(0, 10000), random.randint(0, 10000))
        while self.ref_author_citations_1 < self.ref_author_citations_2:
            self.ref_author_citations_1, self.ref_author_citations_2 = (random.randint(0, 10000), random.randint(0, 10000))

        self.ref_publication_citations_1, self.ref_publication_citations_2 = (random.randint(0, 10000), random.randint(0, 10000))
        while self.ref_publication_citations_1 < self.ref_publication_citations_2:
            self.ref_publication_citations_1, self.ref_publication_citations_2 = (random.randint(0, 10000), random.randint(0, 10000))

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

        self.ref_publication_id_1 = str(uuid.uuid4()).split('-')[0]
        self.ref_title_1 = "'Kill all humans - Bender's great dream"
        self.ref_abstract_1 = """Whether to wipe-out all meatballs or not is
        still an open question for a robot. In this paper, we discuss ethics and
        methods for the robots' world domination."""
        self.ref_url_1 = 'https://journal-of-robotics.org/papers/id=66'
        self.ref_source_1 = 'scholar'

        self.ref_publication_id_2 = str(uuid.uuid4()).split('-')[0]
        self.ref_title_2 = "Hanging-out - the handbook of rock climbing."
        self.ref_abstract_2 = """Letting one's girlfriend go from the summit
        may be challenging for friendship. In this study, we propose a novel
        way of recovery from the trauma, allowing for rapid return to the
        best activity in the world - rock climbing."""
        self.ref_url_2 = 'https://journal-of-grip-and-guns.org/papers/id=69'
        self.ref_source_2 = 'scholar'

        self.ref_publication_citations_3 = self.ref_publication_citations_2 + 1

        self.test_author_1, self.test_author_2 = (
            pubot.author.Author(
                id=self.ref_id_1,
                name=self.ref_name_1,
                affiliation=self.ref_affiliation_1,
                email=self.ref_email_1,
                citations = self.ref_author_citations_1,
                interests = self.ref_interests_1,
            ),
            pubot.author.Author(
                id=self.ref_id_2,
                name=self.ref_name_2,
                affiliation=self.ref_affiliation_2,
                email=self.ref_email_2,
                citations = self.ref_author_citations_2,
                interests = self.ref_interests_2,
            ),
        )

        self.test_publication_1, self.test_publication_2, self.test_publication_3 = (
            pubot.publication.Publication(
                id=self.ref_id_1,
                title=self.ref_title_1,
                abstract=self.ref_abstract_1,
                author=self.test_author_1,
                url=self.ref_url_1,
                citations=self.ref_publication_citations_1,
                source=self.ref_source_1,
            ),
            pubot.publication.Publication(
                id=self.ref_id_2,
                title=self.ref_title_2,
                abstract=self.ref_abstract_2,
                author=self.test_author_2,
                url=self.ref_url_2,
                citations=self.ref_publication_citations_2,
                source=self.ref_source_2,
            ),
            pubot.publication.Publication(
                id=self.ref_id_2,
                title=self.ref_title_2,
                abstract=self.ref_abstract_2,
                author=self.test_author_2,
                url=self.ref_url_2,
                citations=self.ref_publication_citations_3,
                source=self.ref_source_2,
            ),
        )

    def test_equal(self):
        """
        Tests if the same instances of pubot.publication.Publication are the same.
        """
        self.assertEqual(self.test_publication_1, self.test_publication_1)
        self.assertEqual(self.test_publication_2, self.test_publication_2)
        # self.assertEqual(self.test_publication_1, self.test_publication_4)

    def test_not_equal(self):
        """
        Tests if the different instance of pubot.publication.Publication are not the same.
        """
        self.assertNotEqual(self.test_publication_1, self.test_publication_2)

    def test_greater(self):
        """
        Tests if the different instance of pubot.publication.Publication are not equal
        in the proper way.
        """
        self.assertGreater(self.test_publication_1, self.test_publication_2)

    def test_greater_equal(self):
        """
        Tests if the different instance of pubot.publication.Publication are not equal
        in the proper way.
        """
        self.assertGreaterEqual(self.test_publication_1, self.test_publication_2)
        # self.assertGreaterEqual(self.test_publication_2, self.test_publication_3)

    def test_less_equal(self):
        """
        Tests if the different instance of pubot.publication.Publication are not equal
        in the proper way.
        """
        self.assertLessEqual(self.test_publication_2, self.test_publication_1)
        self.assertLessEqual(self.test_publication_2, self.test_publication_2)

    def test_lesser(self):
        """
        Tests if the different instance of pubot.publication.Publication are not equal
        in the proper way.
        """
        self.assertLess(self.test_publication_2, self.test_publication_1)


class SearchTests(unittest.TestCase):
    """
    Tests if the pubot.search.
    """
    def setUp(self):
        import pubot.author
        import pubot.search

        self.ref_id = '4MGHwSYAAAAJ'
        self.ref_name = 'Pawel Siedlecki'
        self.ref_affiliation = 'Institute of Biochemistry and Biophysics PAS'
        self.ref_email = '@ibb.waw.pl'
        self.ref_citations = 1009
        self.ref_interests = [
            'cheminformatics',
            'structural biology',
            'target discovery',
        ]

        self.ref_author = pubot.author.Author(
            id=self.ref_id,
            name=self.ref_name,
            affiliation=self.ref_affiliation,
            email=self.ref_email,
            citations = self.ref_citations,
            interests = self.ref_interests,
        )

        self.test_search_result = pubot.search.author(
            name=self.ref_name,
            affiliation=self.ref_affiliation
        )

    def test_author(self):
        """
        Tests if pubot.search.author returns proper value.
        """
        self.assertEqual(self.ref_author, self.test_search_result)


class IOTests(unittest.TestCase):
    """
    Tests of the pubot.io.
    """
    def setUp(self):
        import pubot.author
        import pubot.io

        self.ref_citations_1, self.ref_citations_2 = (
            random.randint(0, 10000),
            random.randint(0, 10000),
        )
        while self.ref_citations_1 < self.ref_citations_2:
            self.ref_citations_1, self.ref_citations_2 = (
                random.randint(0, 10000),
                random.randint(0, 10000),
            )


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

        self.test_author_csv_filename = 'test_data/IOTests/test_authors.csv'
        self.test_names_column = 'AUTHORS'
        self.test_affiliations_column = 'AFFILIATION'
        self.test_sep = ','


        self.ref_author_1, self.ref_author_2 = (
            pubot.author.Author(
                id=self.ref_id_1,
                name=self.ref_name_1,
                affiliation=self.ref_affiliation_1,
                email=self.ref_email_1,
                citations = self.ref_citations_1,
                interests = self.ref_interests_1,
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
        self.ref_authors = [self.ref_author_1, self.ref_author_2]

        self.test_authors_from_csv = pubot.io.authors_from_csv(
            filename=self.test_author_csv_filename,
            names_column=self.test_affiliations_column,
            affiliations_column=self.test_affiliations_column,
            sep=self.test_sep,
        )

    def test_authors_from_csv(self):
        """
        Tests if pubot.author.Author objects are properly created from a column
        from the CSV file.
        """
        self.assertCountEqual(self.ref_authors, self.test_authors_from_csv)
