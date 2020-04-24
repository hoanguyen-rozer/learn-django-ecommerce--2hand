from django.shortcuts import render
from django.utils.http import is_safe_url
# Create your views here.

import stripe
from django.http import HttpResponse, JsonResponse

stripe.api_key = 'sk_test_u7cis2zbqN2oQmy7SflQuu1X00iCYdUUXf'

STRIPE_PUB_KEY = 'pk_test_W1bM1qmnrcOQ780IojSHaUcY00AOjvrMTI'

def payment_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    context = {
        'publish_key': STRIPE_PUB_KEY,
        'next_url': next_url,
    }
    return render(request, 'billing/payment_method.html', context)

def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        print(request.POST)
        return JsonResponse({'message': 'Done'})
    return HttpResponse('error', status_code=401)
