from marshmallow import Schema, fields

class UserSchema(Schema):
  FirstName = fields.Str()
  LastName = fields.Str()
  Username = fields.Str()
  Password = fields.Str()
  source = fields.Int()
