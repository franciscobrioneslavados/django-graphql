import graphene

from core.apps.students import schema

class Query(schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

