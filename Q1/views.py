from datetime import datetime, timedelta
import json
from django.http import HttpResponse, JsonResponse
from .models import NavigationRecord, Vehicle
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def lastpoint(request):
    if request.method == "POST":
        #post vehicle plate as vplate
        hours = 48
        plate = request.POST.get("vplate")
        vehicle = Vehicle.objects.get(plate = plate)
        lastSpecifiedHours = datetime.now() - timedelta(hours=hours)
        print(lastSpecifiedHours)
        result= NavigationRecord.objects.filter(vehicle=vehicle, datetime=lastSpecifiedHours)
        print(result)
        resultjson = json.loads(serializers.serialize('json', result))

    return JsonResponse(resultjson, safe=False)
