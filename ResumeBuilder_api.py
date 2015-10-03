import table
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

REQUEST_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
)

class VirtualClassRequest(messages.Message):
    username = messages.StringField(1)
class VirtualClassResponse(messages.Message):
    

@endpoints.api(name = 'virtualclassendpoints', version='1', description = "Backend endpoints for cirtual class")
class VirtualClassApi(remote.Service):
    
    @endpoints.method(VirtualClassRequest, VirtualClassResponse, path = 'getAllInfo', http_method = 'GET'  name = "getAllInfo")
    def get_all_info(self, request):
        
        
APPLICATION = endpoints.api_server([])
    