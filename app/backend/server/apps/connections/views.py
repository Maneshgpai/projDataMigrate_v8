from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from apps.connections.models import SourceConnectionDtls, DestinationConnectionDtls
from apps.connections.serializers import SourceConnectionDtlsSerializer, DestinationConnectionDtlsSerializer
from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def sourceConnectionApi(request,id=0):
    if request.method=='GET':
        sourceConnectionDtls = SourceConnectionDtls.objects.all()
        SourceConnectionDtls_Serializer=SourceConnectionDtlsSerializer(sourceConnectionDtls,many=True)
        return JsonResponse(SourceConnectionDtls_Serializer.data,safe=False)
    elif request.method=='POST':
        print('Apps.connections.views> connectSrcApp > sourceConnectionApi > POST ********************')
        SourceConnectionDtls_data=JSONParser().parse(request)
        SourceConnectionDtls_Serializer=SourceConnectionDtlsSerializer(data=SourceConnectionDtls_data)
        print(SourceConnectionDtls_data)
        if SourceConnectionDtls_Serializer.is_valid():
            SourceConnectionDtls_Serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        SourceConnectionDtls_data=JSONParser().parse(request)
        sourceConnectionId=SourceConnectionDtls.objects.get(SrcId=SourceConnectionDtls_data['SrcId'])
        SourceConnectionDtls_Serializer=SourceConnectionDtlsSerializer(sourceConnectionId,data=SourceConnectionDtls_data)
        if SourceConnectionDtls_Serializer.is_valid():
            SourceConnectionDtls_Serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        sourceConnectionId=SourceConnectionDtls.objects.get(SrcId=id)
        sourceConnectionId.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def destConnectionApi(request,id=0):
    if request.method=='GET':
        destinationConnectionDtls = DestinationConnectionDtls.objects.all()
        DestinationConnectionDtls_Serializer=DestinationConnectionDtlsSerializer(destinationConnectionDtls,many=True)
        return JsonResponse(DestinationConnectionDtls_Serializer.data,safe=False)
    elif request.method=='POST':
        DestinationConnectionDtls_data=JSONParser().parse(request)
        DestinationConnectionDtls_Serializer=DestinationConnectionDtlsSerializer(data=DestinationConnectionDtls_data)
        if DestinationConnectionDtls_Serializer.is_valid():
            DestinationConnectionDtls_Serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        DestinationConnectionDtls_data=JSONParser().parse(request)
        DestConnectionId=DestinationConnectionDtls.objects.get(DestId=DestinationConnectionDtls_data['DestId'])
        DestinationConnectionDtls_Serializer=DestinationConnectionDtlsSerializer(DestConnectionId,data=DestinationConnectionDtls_data)
        if DestinationConnectionDtls_Serializer.is_valid():
            DestinationConnectionDtls_Serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        DestConnectionId=DestinationConnectionDtls.objects.get(DestId=id)
        DestConnectionId.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)