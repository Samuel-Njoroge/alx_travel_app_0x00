from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    property = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking by {self.user} for {self.property} from {self.check_in} to {self.check_out}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    property = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()  # 1-5 rating expected
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Review by {self.user} for {self.property} - {self.rating} stars"
