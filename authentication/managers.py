from django.contrib.auth.models import AbstractUser,BaseUserManager
from .models import User

class TeamLeaderManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Roles.TeamLeader)
        
class TeamMemberManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Roles.TeamMember)