from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Session(models.Model):
    date = models.DateField(default=now)
    user_id = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user_id} session on {self.date.isoformat()} " \
               f"lifts: {[l.type for l in Lift.objects.filter(session=self.id)]}"


class Lift(models.Model):
    type = models.CharField(max_length=50)
    weight = models.PositiveIntegerField(default=0)
    session = models.ForeignKey(Session, related_name='lifts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} at {self.weight}kg {self.session.date.isoformat()}"


class Set(models.Model):
    set_number = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    lift = models.ForeignKey(Lift, related_name="sets", on_delete=models.CASCADE)

    class Meta:
        ordering = ["set_number"]

    def __str__(self):
        return f"Set {self.set_number}:" \
               f" {self.reps} reps of {self.lift}kg on {self.lift.session.date.isoformat()}"


def get_user_sessions(request):
    return Session.objects.filter(user_id=request.user)


def get_user_lifts(request):
    return Lift.objects.filter(session__user_id=request.user).order_by().values('type').distinct()
