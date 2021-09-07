from graphene import String, ObjectType

class repoType(ObjectType):
  name = String(required=True)
  repo = String(required=True)