import uuid
from .hotels_model import Hotel
from django.db import models

class Room(models.Model):
    uid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    hotel = models.ForeignKey(Hotel , on_delete= models.CASCADE, null=True)
    room_no = models.IntegerField(null=True)
    ROOM_TYPE = (
        ('S', 'Suite'),
        ('SA', 'Studio_Apartment'),
        ('PS', 'Presidential_Suite'),
        ('ES', 'Executive_Suite'),
        ('DHR', 'Deluxe_Hotel_Rooms'),
        ('SHR', 'Studio_Hotel_Rooms'),
        ('ROHR', 'Room_Only_Hotel_Rooms'),
        ('SSR', 'Standard_Suite_Rooms'),
        ('PSHR', 'Presidential_Suite_Hotel_Rooms'),
        ('ASHB', 'Apartment_Style_Hotel_Bedroom'),
    )
    room_type = models.CharField(max_length=4, null= True, choices=ROOM_TYPE)
    room_image = models.ImageField(null=True)
    max_guest = models.IntegerField(null=True)
    availability= models.BooleanField(default=False)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Rooms'
    def __str__(self):
        return str(self.room_no)