from marshmallow import Schema, fields
from .role import RoleSchema

class UserSchema(Schema):
    uuid = fields.UUID()

    username = fields.Str(required=True)
    email = fields.Str()

    first_name = fields.Str()
    last_name = fields.Str()
    date_of_birth = fields.Date()

    roles = fields.Pluck(RoleSchema, 'name', many=True)

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
