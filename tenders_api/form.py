from django import forms
from .models import Tender


class TenderForm(forms.ModelForm):

    class Meta:
        model = Tender
        fields = ('deadline_app', 'date_publication', 'customer', 'brief_description',
                  'initial_price', 'contract_guarantee', 'place_performance',
                  'category', 'procurement_stage', 'type_purchase',
                  )
