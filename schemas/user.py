from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    uuid = fields.UUID()

    username = fields.Str()
    password = fields.Str()
    email = fields.Str()

    first_name = fields.Str()
    last_name = fields.Str()
    date_of_birth = fields.Date()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
