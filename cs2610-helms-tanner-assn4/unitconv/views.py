import json

from django.http import JsonResponse
from django.shortcuts import render

from unitconv.models import Convert


# Create your views here.
def convert(request):
    resp = {}
    if 'from' not in request.GET or 'value' not in request.GET or 'to' not in request.GET:
        resp['error'] = "Usage; ?from={type}&value={valueOfYourGold}&to={unitToConvertTo}"
        resp['success'] = False
    else:
        fr = request.GET['from']
        val = request.GET['value']
        to = request.GET['to']
        if not val.replace(".", "").replace("-", "").isnumeric():
            resp['usage'] = "Usage; ?from={type}&value={valueOfYourGold}&to={unitToConvertTo}"
            resp['success'] = False
            resp['error'] = f"The value must be a float!"
            return JsonResponse(resp)
        if float(val) < 0:
            resp['usage'] = "Usage; ?from={type}&value={valueOfYourGold}&to={unitToConvertTo}"
            resp['success'] = False
            resp['error'] = f"The value can not be negative!"
            return JsonResponse(resp)
        factor = Convert.objects.filter(Name=fr)
        if len(factor) < 1:
            resp['error'] = f"The format {fr} is not a supported type"
            resp['usage'] = "Usage; ?from={type}&value={valueOfYourGold}&to={unitToConvertTo}"
            resp['success'] = False
            return JsonResponse(resp)
        factor = factor[0].Factor
        factor2 = Convert.objects.filter(Name=to)
        if len(factor2) < 1:
            resp['error'] = f"The format {to} is not a supported type"
            resp['usage'] = "Usage; ?from={type}&value={valueOfYourGold}&to={unitToConvertTo}"
            resp['success'] = False
            return JsonResponse(resp)
        factor2 = factor2[0].Factor
        value = float(val) * factor / factor2
        resp['units'] = to
        resp['value'] = value
    return JsonResponse(resp)
