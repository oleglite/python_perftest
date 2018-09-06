import json

from django import forms
from django.views.generic import View
from django.http import JsonResponse, HttpResponse

from .models import Record


class RecordForm(forms.ModelForm):
    owner = forms.CharField(min_length=5, max_length=128, required=True)
    expires_at = forms.DateTimeField(required=False)
    customer = forms.CharField(max_length=128, required=False)
    total_budget = forms.FloatField(min_value=0, required=False)

    class Meta:
        exclude = []
        model = Record


class RecordCreate(View):
    http_method_names = ['post']

    def post(self, request):
        data = json.loads(request.body)
        form = RecordForm(data)

        if not form.is_valid():
            return JsonResponse({'ok': False}, status=400)

        record = form.save()
        return JsonResponse({'ok': True, 'id': record.id}, status=201)


class RecordRead(View):
    http_method_names = ['get']

    def get(self, request, record_id):
        record = Record.objects.get(id=record_id)
        return JsonResponse(
            {
                'summary': record.summary,
                'description': record.description,
                'project': record.project,
                'region': record.region,
                'total_budget': record.total_budget,
                'info': record.info,
                'purpose': record.purpose,
                'department': record.department,
                'business': record.business,
                'is_budget': record.is_budget,
                'customer': record.customer,
                'owner': record.owner,
                'approved_by': record.approved_by,
                'created_at': record.created_at,
                'updated_at': record.updated_at,
                'expires_at': record.expires_at,
                'closed': record.closed,
            },
            status=200
        )


def index(request):
    return HttpResponse("Hello")
