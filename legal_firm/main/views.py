from django.shortcuts import render
from main.models import LegalFirm


def show_legal_firm(request):
    firm = LegalFirm.objects.first()

    return render(request, 'main/legal_firm.html', {'firm': firm})
