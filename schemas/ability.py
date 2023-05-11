from marshmallow import Schema, fields

class AbilitySchema(Schema):
    uuid = fields.UUID()

    name = fields.Str()
    description = fields.Str()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
