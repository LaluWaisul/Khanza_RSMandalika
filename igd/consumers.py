from ralan.models import RegPeriksa
from ralan.serializers import RegPeriksaSerializer
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions

class PasienRegisterConsumer(GenericAsyncAPIConsumer):
    queryset = RegPeriksa.objects.all()
    permission_classes = (permissions.AllowAny)
    
    async def connect(self, **kwargs):
        await self.model_change.subscribe()
        return await super().connect()
    
    @model_observer(RegPeriksa)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)
        
    @model_change.serializer
    def model_serilize(self, instance, action, **kwargs):
        return dict(RegPeriksaSerializer(instance=instance).data, action=action.value)
    
    
class RegPasienConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        print(f'connection closed with code: {close_code}')
    
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json("message")
        sender = text_data_json("sender")
        
        print(message, sender)
        
        await self.send(text_data = json.dumps({
            'message': message,
            'sender': sender
        }))