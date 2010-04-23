from django.conf.urls.defaults import *
from django.db.models import permalink
from models import Ticket, TicketForm

OBJ_ID = r'^(?P<object_id>\d+)/'

qs = Ticket.objects.all()
# generic list/object views
info = {
    'queryset': Ticket.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', info, name='ticket-list'),
    url(OBJ_ID+'$', 'object_detail', info, name='ticket-detail'),
)

"""
info_up = {
    'form_class': TicketForm,
    'login_required': False,
}
urlpatterns += patterns('django.views.generic.create_update',
    url(r'^new/$', 'create_object', info_up, name='ticket-new'),
    url(OBJ_ID+r'/edit/$', 'update_object', info_up, name='ticket-edit'),
    url(OBJ_ID+r'/delete/$', 'delete_object', {
        'login_required': False,
        'model': Ticket,
        'post_delete_redirect': permalink(lambda: ('ticket-list',))
    }, name='ticket-edit'),
)
"""
