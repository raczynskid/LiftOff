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


def get_user_lifts_unique(request):
    return Lift.objects.filter(session__user_id=request.user) \
        .order_by().values('type').distinct().values_list("type", flat=True)


def get_last_weight(type, user):
    return Lift.objects.filter(session__user_id=user, type=type) \
        .order_by().values('session__date').values_list('weight').first()

def get_set_values_per_last_lift(type, user):
    last_session = Lift.objects.filter(session__user_id=user, type=type)\
        .order_by().values('session__date').values_list('session__date').first()[0]
    sets = Set.objects.filter(lift__type=type, lift__session__user_id=user, lift__session__date=last_session)
    return [set.reps for set in sets]
