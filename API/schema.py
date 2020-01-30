from marshmallow import Schema, fields

class ArticleSchema(Schema):
  text = fields.Str()
  
class CoauthorSchema(Schema):
  name =fields.Str()
  commonArticle= fields.Int()
  
class UserSchema(Schema):
  FirstName = fields.Str()
  LastName = fields.Str()
  Username = fields.Str()
  Password = fields.Str()
  source = fields.Int()
  profile= fields.Str()
  articles=fields.List(fields.Nested(ArticleSchema), required=True)
  coauthors=fields.List(fields.Nested(CoauthorSchema), required=True)
