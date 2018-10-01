from django.shortcuts import render
from .models import Tender


def tender_list(request):
    tenders = Tender.objects.all()
    return render(request, 'tenders_api/tender_list.html', {'tenders': tenders})
