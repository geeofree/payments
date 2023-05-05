from marshmallow import Schema, fields

class RoleSchema(Schema):
    id = fields.Int()
    uuid = fields.UUID()

    name = fields.Str()
    description = fields.Str()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
