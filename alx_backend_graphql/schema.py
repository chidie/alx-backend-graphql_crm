import graphene

class CRMQuery(graphene.ObjectType):
    # later you will add customer, leads, etc.
    pass

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")

schema = graphene.Schema(query=Query)

