from .models import WrapperClass, EntrainementClass, PartitionClass, AnneeClass
from django.contrib.auth.models import User
from graphene import Node, Schema, Field
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["username", "email", "first_name", "last_name"]


class WrapperNode(DjangoObjectType):
    class Meta:
        model = WrapperClass
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["name", "quiz"]


class EntrainementNode(DjangoObjectType):
    class Meta:
        model = EntrainementClass
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["wrapper", "val"]


class PartitionNode(DjangoObjectType):
    class Meta:
        model = PartitionClass
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["nuance", "structure"]


class AnneeNode(DjangoObjectType):
    class Meta:
        model = AnneeClass
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["user", "annee", "note",
                         "rythme", "partition", "instruments"]


class Query(object):
    user = Node.Field(UserNode)
    all_user = DjangoFilterConnectionField(UserNode)

    wrapper = Node.Field(WrapperNode)
    all_wraper = DjangoFilterConnectionField(WrapperNode)

    entrainement = Node.Field(EntrainementNode)
    all_entrainement = DjangoFilterConnectionField(EntrainementNode)

    partition = Node.Field(PartitionNode)
    all_partition = DjangoFilterConnectionField(PartitionNode)

    annee = Node.Field(AnneeNode)
    all_annee = DjangoFilterConnectionField(AnneeNode)
