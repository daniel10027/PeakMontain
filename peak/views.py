from rest_framework.response import Response
from peak.models import Peak, WhiteListCountry, RejectedConnexion
from peak.serializers import PeakSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import geoip2.database
from .get_country import get_country_code
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def my_view(request):
    ip_address = request.META.get('REMOTE_ADDR')
    country_code = get_country_code(ip_address)
    print(country_code)
    if country_code == None  and not WhiteListCountry.is_country_allowed(country_code):
        objet = RejectedConnexion.objects.get_or_create(ip=ip_address,country_code=country_code)
        return HttpResponseForbidden()
    else:
        return redirect('home')

def Home(request):
    ip_address = request.META.get('REMOTE_ADDR')
    country_code = get_country_code(ip_address)
    print(country_code)
    if country_code == None  and not WhiteListCountry.is_country_allowed(country_code):
        objet = RejectedConnexion.objects.get_or_create(ip=ip_address,country_code=country_code)
        return HttpResponseForbidden()
    else:
        locations = []
        for data in Peak.objects.all():
            locations.append(data.full_url)

        result = []
        for item in locations:
            # supprimer les caractères inutiles
            item = item.replace('{', '').replace('}', '').replace('"', '')
            # diviser les valeurs
            lat, lng, name = item.split(', ')
            # créer un nouveau dictionnaire
            new_dict = {'lat': float(lat.split(': ')[1]), 'lng': float(lng.split(': ')[1]), 'name': name.split(': ')[1]}
            # ajouter le dictionnaire à la liste
            result.append(new_dict)
        context = {
            'locations':result
        }
        return render(request,'apis.html', context=context)

@api_view(['GET'])
def peakList(request):
    peaks = Peak.objects.all()
    serializer = PeakSerializer(peaks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def peakListInZone(request,lat1, long1, lat2, long2, lat3, long3, lat4, long4):
    peaks = Peak.objects.filter(latitude__gte=min(lat1, lat2, lat3, lat4),
                                latitude__lte=max(lat1, lat2, lat3, lat4),
                                longitude__gte=min(long1, long2, long3, long4),
                                longitude__lte=max(long1, long2, long3, long4)
                                )
    serializer = PeakSerializer(peaks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def peakDeatil(request, pk):
    peaks =  get_object_or_404(Peak, pk=pk)
    serializer = PeakSerializer(peaks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def peakCreate(request):
    serializer = PeakSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def peakUpdate(request, pk):
    peaks =  get_object_or_404(Peak, pk=pk)
    serializer = PeakSerializer(instance=peaks, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def peakDelete(request, pk):
    peaks =  get_object_or_404(Peak, pk=pk)
    peaks.delete()
    return Response("DELETED")

