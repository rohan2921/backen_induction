from django.core.files.storage import FileSystemStorage
from django.db import connection
from django.db.models import F, Count
from django.shortcuts import render
from rest_framework import viewsets, status, filters, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView

from .models import (
    Service,
    ShippingAgency,
    Car,
    Bill,
    Truck,
    RandomEntries,
    AbstractVehicle, FileUpload
)

from .serializers import (
    BillSerializer,
    CarSerializer,
    ServiceSerializer,
    ShippingAgencySerializer,
    TruckSerializer, RandomEntriesSerializer, AbstractVehicleSerializer
)

from django import forms


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    ordering_fields = (
        "id",
        "lp_number",
        "color",
        "wheel_count",
        "model_name",
        "vehicle_price",
        "my_bills"
    )
    search_fields = (
        "id",
        "lp_number",
        "color",
        "wheel_count",
        "model_name",
        "vehicle_price",
        "my_bills"
    )

    @action(detail=False, methods=['GET'])
    def get_all_cars(self, request):
        print(request.GET)
        cars = self.queryset
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class TruckViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

    ordering_fields = (
        "id",
        "lp_number",
        "color",
        "wheel_count",
        "model_name",
        "vehicle_price",
        "works_for",
        "services"
    )
    search_fields = (
        "id",
        "lp_number",
        "color",
        "wheel_count",
        "model_name",
        "vehicle_price",
        "works_for",
        "services"
    )


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    ordering_fields = (
        "from_city",
        "to_city",
        "purpose"
    )
    search_fields = (
        "from_city",
        "to_city",
        "purpose"
    )


class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

    ordering_fields = (
        "title",
        "description",
        "amount"
    )
    search_fields = (
        "title",
        "description",
        "amount"
    )


class ShippingAgencyViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingAgencySerializer
    queryset = ShippingAgency.objects.all()

    ordering_fields = (
        "name"
    )
    search_fields = (
        "name"
    )


class FirstSViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

    @action(detail=False, methods=['GET'])
    def apply_params(self, request):
        q = {k: v for k, v in request.GET.items() if v}
        list_after_filtering = Truck.objects.filter(**q)
        for obj in list_after_filtering:
            print(obj.works_for.name)
        no_of_queries = connection.queries
        return Response({"Number of queries are": len(no_of_queries) - 2})


class SecondScenarioViewSet(viewsets.ModelViewSet):
    serializer_class = AbstractVehicleSerializer
    queryset = AbstractVehicle.objects.all()

    @action(detail=False, methods=['GET'])
    def add_and_get_id(self, request):
        id_list = AbstractVehicle.objects.values_list(F('id') + 100)
        return Response({"ids": id_list})


class ThirdScenarioViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingAgencySerializer
    queryset = ShippingAgency.objects.all()

    @action(detail=False, methods=['GET'])
    def get_count_of_relations(self, request):
        shipping_agencies = ShippingAgency.objects.annotate(Count("truck"))
        print(shipping_agencies)
        print("here")
        lst = shipping_agencies.values_list('id', 'name', 'truck__count')
        return_list = []
        for tup in lst:
            temp_dic = {"id": tup[0], tup[2]: "count of trucks related to " + tup[1]}
            return_list.append(temp_dic)
        return Response(return_list)


class FourthViewSet(viewsets.ModelViewSet):
    queryset = RandomEntries.objects.all()
    serializer_class = RandomEntriesSerializer

    @action(detail=False, methods=['GET'])
    def populate(self, request):
        lst = []
        for i in range(100000):
            text = "random " + str(i)
            ob = RandomEntries(flag=text)
            lst.append(ob)
        if lst:
            RandomEntries.objects.bulk_create(lst)
        return Response({"response": "successfully populated database"})


class FifthScenarioViewSet(APIView):
    def post(self, request):
        strings = request.data['strings']
        count = RandomEntries.objects.filter(flag__in=strings).count()
        return Response({"message": count})


class SixthViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

    @action(detail=False, methods=['GET'])
    def print_all_fields(self, request):
        q_s = self.queryset
        for truck_obj in q_s:
            print(truck_obj.id, truck_obj.works_for.name, truck_obj.services.all(), truck_obj.showroom_set.all(),
                  truck_obj.c_book.book_number)

        no_of_queries = connection.queries
        return Response({"Number of queries are": len(no_of_queries) - 2})


class SeventhViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

    @action(detail=False, methods=['GET'])
    def print_all_fields(self, request):
        q_s = Truck.objects.select_related('works_for').select_related('c_book').prefetch_related('services').all()
        for truck_obj in q_s:
            print(truck_obj.id, truck_obj.works_for.name, truck_obj.services.all(), truck_obj.showroom_set.all(),
                  truck_obj.c_book.book_number)

        no_of_queries = connection.queries
        return Response({"Number of queries are": len(no_of_queries) - 2})


class EighthScenarioViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

    @action(detail=False, methods=['GET'])
    def apply_all_methods(self, request):
        only = Truck.objects.only('max_capacity')
        defer = Truck.objects.defer('max_capacity')
        values = Truck.objects.values('id', 'model_name')
        values_list = Truck.objects.values_list('id', 'model_name')

        return Response({
            "only": self.serializer_class(only, many=True).data,
            "defer": self.serializer_class(defer, many=True).data,
            "values": values,
            "values_list": values_list,
        })


class NinthScenarioViewSet(APIView):

    def post(self, request):
        json_data = request.data
        for json_obj in json_data:
            if 'id' in json_obj:
                RandomEntries.objects.filter(id=json_obj['id']).update(flag=json_obj['name'])
            else:
                RandomEntries.objects.create(flag=json_obj['name'])
        return Response({"message": "done"})


class TenthScenarioViewSet(APIView):

    def post(self, request):
        ids = request.data['ids']
        length = len(ids)
        if not ids:
            return Response({"oops": "ids not given"})
        for i_d in ids[:length // 2]:
            if RandomEntries.objects.filter(id=i_d).exists():
                with connection.cursor() as cursor:
                    cursor.execute(f'DELETE from vehicles_randomentries where id={i_d}')
        for i_d in ids[length // 2:]:
            if RandomEntries.objects.filter(id=i_d).exists():
                RandomEntries.objects.get(id=i_d).delete()
        return Response({"message": "finished"})


class EleventhScenarioViewSet(viewsets.ModelViewSet):
    serializer_class = AbstractVehicleSerializer
    queryset = AbstractVehicle.objects.all()

    @action(detail=False, methods=['GET'])
    def get_objects(self, request):
        params = request.GET
        if not params:
            count = AbstractVehicle.objects.all().count()
            return Response({"Count of rows": count})
        if not AbstractVehicle.objects.filter(id=params['id']).exists() or params['data'].lower() == 'false':
            return Response({"message": "false"})

        return Response(self.serializer_class(AbstractVehicle.objects.get(id=params['id'])).data)


def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        FileUpload.objects.create(file_field=uploaded_file_url)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')
