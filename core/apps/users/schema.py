import graphene
from graphene_django import DjangoObjectType
from .models import *


class UsersType(DjangoObjectType):
    class Meta:
        model = Users


class Query(graphene.ObjectType):
    users = graphene.List(UsersType)

    def resolve_users(self, info, **kwargs):
        return Users.objects.all()
