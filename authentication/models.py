from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class User(AbstractUser):
    class Roles(models.TextChoices):
        User = 1,'User'
        TeamLeader = 2, 'Team Leader'
        TeamMember = 3, 'Team Member'

    base_role = Roles.User
    role = models.CharField(max_length=50,choices=Roles.choices)

    def save(self,*args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args,**kwargs)

class TeamLeaderManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Roles.TeamLeader)

class TeamLeader(User):

    base_role = User.Roles.TeamLeader
    teamleader = TeamLeaderManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "only for Team Leader"

class TeamMemberManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Roles.TeamMember)

class TeamMember(User):

    base_role = User.Roles.TeamMember
    teammember = TeamMemberManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "only for Team Member"

