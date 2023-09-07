import json
from graphene_django.utils.testing import GraphQLTestCase
from graphql_example.models import Person, Address


class PeopleCreateTestCase(GraphQLTestCase):
    def test_people_create(self):
        """
        Test creating objects in database
        """
        # Create address object
        address = Address.objects.create(
            number=1234,
            street="Streetname Ave",
            city="Los Angeles",
            state=Address.States.CALIFORNIA
        )

        # Create person objects
        person = Person.objects.create(
            email="wjahugme@realema.il",
            name="Will Jahugme",
            address=address
        )

        # Fetch person
        created_person = Person.objects.all().first()

        # Check that fields match and aren't missing
        self.assertEqual(created_person.email, person.email)
        self.assertEqual(created_person.name, person.name)
        self.assertEqual(created_person.address.number, address.number)
        self.assertEqual(created_person.address.street, address.street)
        self.assertEqual(created_person.address.city, address.city)
        self.assertEqual(created_person.address.state, address.state)


class PeopleQueryTestCase(GraphQLTestCase):
    def create_sample_data(self) -> Person:
        """
        Create sample data for test case
        """
        # Create address object
        address = Address.objects.create(
            number=1234,
            street="Streetname Ave",
            city="Los Angeles",
            state=Address.States.CALIFORNIA
        )

        # Create person object
        person = Person.objects.create(
            email="wjahugme@realema.il",
            name="Will Jahugme",
            address=address
        )

        return person

    def test_people_query(self):
        """
        Test API /graphql endpoint
        """

        # Create sample data
        person = self.create_sample_data()

        # Define query
        query = """
        query {
            people {
                email
                name
                address {
                    number
                    street
                    city
                    state
                }
            }
        }
        """

        # query endpoint
        response = self.query(query)

        self.assertEqual(response.status_code, 200)

        # parse query content
        content = json.loads(response.content)

        # Check that response is a graphql response
        self.assertIn("data", content)
        self.assertIn("people", content["data"])
        self.assertEqual(1, len(content["data"]["people"]))

        created_person = content["data"]["people"][0]

        # Check that fields match
        self.assertEqual(created_person["email"], person.email)
        self.assertEqual(created_person["name"], person.name)
        self.assertEqual(created_person["address"]["number"],
                         person.address.number)
        self.assertEqual(created_person["address"]["street"],
                         person.address.street)
        self.assertEqual(created_person["address"]["city"],
                         person.address.city)
        self.assertEqual(created_person["address"]["state"],
                         person.address.state)