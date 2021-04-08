from .models import Hero
from graphene import Node, Schema, Field
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class HeroNode(DjangoObjectType):
    class Meta:
        model = Hero
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["name", "alias"]

class Query(object):
    hero = Node.Field(HeroNode)
    all_hero = DjangoFilterConnectionField(HeroNode)
