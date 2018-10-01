from django.shortcuts import render

def tender_list(request):
    return render(request, 'tenders_api/tender_list.html', {})
