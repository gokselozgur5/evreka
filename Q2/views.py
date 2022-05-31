from django.http import JsonResponse
from django.shortcuts import render
from .models import Bin,Meta_Operation,Operation

# Create your views here.
def getCollectionFrequency(request):
    if request.method == "POST":
        #Assumed operation will be input.
        operationId = request.POST.get("operationid")
        operation = Operation.objects.get(id=operationId)
        operationData = Meta_Operation.objects.filter(operation = operation)
        resultJson = []
        for data in operationData:
            bin = Bin.objects.get(id=data.bin.id)
            resultJson.append({"Collection Frequency": bin.collection_frequency})
            
        
        return JsonResponse(resultJson, safe=False)
    return JsonResponse({"Error":"There is no post request"})
