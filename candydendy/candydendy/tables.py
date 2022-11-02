import django_tables2 as tables
from candydendy.models import Candy


class CandyTable(tables.Table):
    company_email = tables.Column()
    company_site = tables.Column()
    class Meta:
        orderable = False
        model = Candy


class CandyTableFree(tables.Table):
    class Meta:
        orderable = False
        model = Candy
        fields = ('name', 'type', 'calories')