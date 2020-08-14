from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from gqlapp.models import ProductModel
import graphene


class Products(DjangoObjectType):
    class Meta:
        model = ProductModel
        filter_fields = ['id', 'segment', 'country', 'product']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    product = relay.Node.Field(Products)
    all_products = DjangoFilterConnectionField(Products)

    def resolve_product(self, info):
        return ProductModel.objects.all()


schema = graphene.Schema(query=Query)
