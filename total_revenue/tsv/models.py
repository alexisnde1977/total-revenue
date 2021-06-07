from django.db import models

# Revenue Model
class Revenue(models.Model):
    """
    Represents one item within a specific source file
    """

    item = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField(decimal_places=2, max_digits=20)
    item_count = models.IntegerField()
    vendor = models.CharField(max_length=100)
    vendor_address = models.CharField(max_length=200)
