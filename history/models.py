from django.db import models

# Create your models here.

class SearchData(models.Model):
    search_query = models.CharField(max_length=500, null=True, blank=True)
    search_result = models.CharField(max_length=2000, null=True, blank=True)
    searched_at = models.DateField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return str(self.search_query)
