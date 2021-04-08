from .models import Hero, Note, Entrainement
from graphene import Node, Schema, Field
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class HeroNode(DjangoObjectType):
    class Meta:
        model = Hero
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["name", "alias"]

class NoteNode(DjangoObjectType):
    class Meta:
        model = Note
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["quizz"]

class EntrainementNode(DjangoObjectType):
    class Meta:
        model = Entrainement
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["note", "state"]

class Query(object):
    hero = Node.Field(HeroNode)
    all_hero = DjangoFilterConnectionField(HeroNode)

    note = Node.Field(NoteNode)
    all_note = DjangoFilterConnectionField(NoteNode)

    entrainement = Node.Field(EntrainementNode)
    all_entrainement = DjangoFilterConnectionField(EntrainementNode)
