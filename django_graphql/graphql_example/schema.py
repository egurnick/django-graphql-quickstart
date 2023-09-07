import graphene
from graphene_django.types import DjangoObjectType
from graphql_example.models import Person, Address


class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class PersonType(DjangoObjectType):
    class Meta:
        model = Person

    email = graphene.String()
    name = graphene.String()
    address = graphene.Field(AddressType)


class Query(graphene.ObjectType):
    people = graphene.List(
        PersonType,
        page=graphene.Int(default_value=None),
        pageSize=graphene.Int(default_value=None)
    )

    def resolve_people(self, info, page, pageSize):
        result = Person.objects.all()

        # Page indexing starts at 1
        # If page=0 or pageSize=0, return all
        if (page is not None) and (pageSize is not None):
            start_index = page * pageSize
            end_index = start_index + pageSize
            return result[start_index: end_index]

        return result


schema = graphene.Schema(query=Query)
