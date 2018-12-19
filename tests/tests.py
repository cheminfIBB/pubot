import unittest
import uuid
import random


class AuthorTests(unittest.TestCase):
    """
    Tests of the pubot.author.
    """
    def setUp(self):
        import pubot.author

        self.ref_id = str(uuid.uuid4()).split('-')[0]
        self.ref_name = 'Arnold Schwarzenegger'
        self.ref_affiliation = 'Institute of SkyNet SI'
        self.ref_email = 'arni@future.net'
        self.ref_citations = random.randint(0, 10000)

        self.test_author = pubot.author.Author(
            id=self.ref_id,
            name=self.ref_name,
            affiliation=self.ref_affiliation,
            email=self.ref_email,
            citations = self.ref_citations,
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
            )
            pubot.author.Author(
                id=self.ref_id,
                name=uuid.uuid4(),
                affiliation=self.ref_affiliation,
                email=self.ref_email,
                citations=self.ref_citations,
            )
            pubot.author.Author(
                id=self.ref_id,
                name=self.ref_name,
                affiliation=uuid.uuid4(),
                email=self.ref_email,
                citations=self.ref_citations,
            )
            pubot.author.Author(
                id=self.ref_id,
                name=self.ref_name,
                affiliation=self.ref_affiliation,
                email=uuid.uuid4(),
                citations=self.ref_citations,
            )
            pubot.author.Author(
                id=self.ref_id,
                name=self.ref_name,
                affiliation=self.ref_affiliation,
                email=self.ref_email,
                citations=uuid.uuid4(),
            )

    def test_repr(self):
        """
        Tests if pubot.author.Author.__repr__ returns proper value.
        """
        self.assertEqual(self.ref_name, str(self.test_author))
