import uuid
from django.db import models
from users.models import User


# Create your models here.
class Ticket(models.Model):
    status_choices=(
    ('Active','Active'),
    ('Resolved','Resolved'),
    ('Pending','Pending')
    )
    ticket_id=models.UUIDField(default=uuid.uuid4)
    ticket_title=models.CharField(max_length=100)
    customer=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='customer')
    engineer=models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='engineer',null=True,blank=True)
    ticket_description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    is_resloved=models.BooleanField(default=False)
    status=models.CharField(max_length=15,choices=status_choices)
    last_modified=models.DateTimeField(auto_now=True)
    Severity=models.CharField(max_length=5,choices=(('A','A'),('B','B')),default='B')
    is_assigned_to_engineer = models.BooleanField(default=False)
    resolution_steps =models.TextField(null=True,blank=True)

    def __str__(self) :
        return self.ticket_title