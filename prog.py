from grahene import ObjectType, String, Schema

class Query(ObjectType):
    hello = Srting(name=String(default_value='stranger'))
    goodbye = String()

    def resolve_hello(self, info, name):
        return f'Hello {name}'

    def resolve_goobye(self, info):
        return 'See ya!'

schema = Schema(query=Query)