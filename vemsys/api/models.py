from typing import Any
from django.db import models
from random import randint, choice


# Generate unique string code of 10 digit
class VendorCode():
    id_counter: int = 999

    def __init__(self):
        self.name = self.value()
        VendorCode.id_counter += 1

    def value(self) -> str:
        zerovalue = ['A', 'B', 'C', 'X', 'Y', 'Z']
        mainstr = ""
        count = VendorCode.id_counter
        for i in range(8):
            x = (ord('C') + count % 20)
            count //= 20
            if x == ord('C') or x >= ord('X'):
                mainstr += choice(zerovalue)
            else:
                mainstr += chr(x)
        A, Z = ord('A'), ord('Z')
        mainstr += chr(randint(A, Z))
        mainstr += chr(randint(A, Z))
        return mainstr[::-1]

    def __str__(self) -> str:
        return self.name
    

# Model for vendors
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(
        max_length=10,
        primary_key=True,
        null=False,
        editable=False,
    )
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name
    
    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     super().__init__(*args, **kwargs)
    #     x = VendorCode()
    #     self.vendor_code = x.name


