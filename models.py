from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Users(models.Model):
    idu = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    passwd = fields.CharField(max_length=200)
    entry_date = fields.DatetimeField(null=True, auto_now_add=False)

    class Meta:
        table = 'users'
    
    class PydanticMeta:
        exclude = ["idu"]

User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)

class RulesUsers(models.Model):
    idru = fields.IntField(pk=True)
    idur = fields.ForeignKeyField("models.Users", related_name="items", null=True)
    is_superuser = fields.BooleanField(default=False)
    is_adviser = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = 'rulesusers'
    
RulesUser_Pydantic = pydantic_model_creator(RulesUsers, name="RulesUser")
RulesUserIn_Pydantic = pydantic_model_creator(RulesUsers, name="RulesUserIn", exclude_readonly=True)