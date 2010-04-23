from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import ModelForm

TICKET_STATUS_CHOICES = (
    ('new', 'New'),
    ('accepted', 'Accepted'),
    ('assigned', 'Assigned'),
    ('reopened', 'Reopened'),
    ('closed', 'Closed'),
)

class Ticket(models.Model):
    assigned_to = models.ForeignKey(User, null=True, blank=True)
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='new')
    description = models.TextField()
    created_on = models.DateTimeField('date created', auto_now_add=True)
    updated_on = models.DateTimeField('date updated', auto_now=True)

    def name(self):
        return self.description.split('\n', 1)[0]

    def __unicode__(self):
        return u'%s' % self.name()
    
    @models.permalink
    def get_absolute_url(self):
        return ('ticket-detail', [str(self.id)])

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('description',)

class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    fieldsets = (
        (None, {
            'fields': ('assigned_to', 'status', 'description'),
        }),
    )
    list_filter = ('status', 'assigned_to')
    list_display = ('id', 'name', 'status', 'assigned_to')
    search_fields = ['description']

admin.site.register(Ticket, TicketAdmin)
