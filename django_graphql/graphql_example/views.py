# from django.shortcuts import render
from graphene_django.views import GraphQLView
from graphql_example.schema import schema


class GetPersonView(GraphQLView):
    schema = schema
