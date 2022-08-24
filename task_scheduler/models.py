from django.db import models
from authentication.models import TeamLeader,TeamMember

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    team_leader = models.ForeignKey(TeamLeader,on_delete=models.CASCADE,related_name='Team_Leader')
    team_members = models.ManyToManyField(TeamMember)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    class Status(models.TextChoices):
        Assigned = 'ASSIGNED', 'Assigned'
        In_progress = 'INPROGRESS','In Progress'
        under_review = 'UNDER_REVIEW','Under Review'
        Done = 'DONE','Done'
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=Status.choices)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"