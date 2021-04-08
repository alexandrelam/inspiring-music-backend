import core.login.schema
import graphene

from graphene_django.debug import DjangoDebug


class Query(
    core.login.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)

