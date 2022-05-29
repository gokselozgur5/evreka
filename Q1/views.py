from datetime import datetime, timedelta, timezone
import json
from django.http import JsonResponse
from .models import NavigationRecord, Vehicle
from django.core import serializers


def lastpoint(request):
    if request.method == "POST":
        #post vehicle plate as vplate
        plate = request.POST.get("vplate")
        #hours can be got with post if necessary
        hours = 48
        vehicle = Vehicle.objects.get(plate = plate)
        lastSpecifiedHours = datetime.now(tz=timezone.utc) - timedelta(hours=hours)
        resultJson = []
        #Cached result for optimization
        results= NavigationRecord.objects.filter(vehicle=vehicle, datetime__gte=lastSpecifiedHours).values()
        print(list(results))
    return JsonResponse(list(results), safe=False)
