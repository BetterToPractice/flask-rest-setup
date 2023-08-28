from project.extensions import ma


class UserSchema(ma.Schema):
    id = ma.Integer()
    username = ma.String()
    name = ma.String()
    email = ma.String()


users_schema = UserSchema(many=True)
user_schema = UserSchema()
