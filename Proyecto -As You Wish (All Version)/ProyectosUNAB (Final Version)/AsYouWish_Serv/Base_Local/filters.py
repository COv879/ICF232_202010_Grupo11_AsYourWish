import django_filters
from .models import Local
Mes_Select= [('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),('Septiembre','Septiembre'),('Octubre','Octube'),('Noviembre','Noviembre'),('Diciembre','Diciembre'),]


class Filtro_LocalPago(django_filters.FilterSet):
    Anno = django_filters.CharFilter(label='Año')
    Mes = django_filters.ChoiceFilter(label='Mes', choices = Mes_Select)
    class Meta:
        model = Local
        fields = ('Anno', 'Mes',)