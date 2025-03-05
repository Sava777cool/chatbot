from tortoise import fields
from tortoise.models import Model


class ChatHistory(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="chats")
    message = fields.TextField()
    response = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
