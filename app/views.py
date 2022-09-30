from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
import json
from django.db import transaction


class PostJSONAPIVIew(APIView):
    @transaction.atomic
    def post(self, request):
        with open('app/uniq.json') as f:
            data = json.load(f)
        for i in data:
            Meteric.objects.create(metering_code=i['METERING_CODE'],timestamp_utc=i['TIMESTAMP_UTC'])

