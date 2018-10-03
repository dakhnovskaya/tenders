from django.shortcuts import render
from .models import Tender
from django.shortcuts import render, get_object_or_404
from .form import TenderForm
from django.shortcuts import redirect


def tender_list(request):
    tenders = Tender.objects.all()
    return render(request, 'tenders_api/tender_list.html', {'tenders': tenders})


def tender_detail(request, pk):
    tender = get_object_or_404(Tender, pk=pk)
    return render(request, 'tenders_api/tender_detail.html', {'tender': tender})


def tender_new(request):
    if request.method == "POST":
        form = TenderForm(request.POST)
        if form.is_valid():
            tender = form.save()
            return redirect('tender_detail', pk=tender.pk)
    else:
        form = TenderForm()
    return render(request, 'tenders_api/tender_edit.html', {'form': form})


def tender_edit(request, pk):
    tender = get_object_or_404(Tender, pk=pk)
    if request.method == "POST":
        form = TenderForm(request.POST, instance=tender)
        if form.is_valid():
            tender = form.save()
            return redirect('tender_detail', pk=tender.pk)
    else:
        form = TenderForm(instance=tender)
    return render(request, 'tenders_api/tender_edit.html', {'form': form})

