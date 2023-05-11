from marshmallow import Schema, fields
from .ability import AbilitySchema

class RoleSchema(Schema):
    uuid = fields.UUID()

    name = fields.Str()
    description = fields.Str()

    abilities = fields.Pluck(AbilitySchema, "name", many=True)

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
