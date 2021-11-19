from django.db import models


class Kudo(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey('authentication.Department', related_name='deps', on_delete=models.CASCADE)
    team = models.ForeignKey('authentication.Team', related_name='teams', on_delete=models.CASCADE)
    employee = models.ForeignKey('authentication.Employee', related_name='emp', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('authentication.Employee', related_name='kudoer', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


