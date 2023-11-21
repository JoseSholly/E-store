# import stripe
# from django.conf import settings
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from orders.models import Order


# @csrf_exempt
# def strife_webhook(request):
#     payload= request.body
#     sig_header= request.META['HTTP_STRIPE_SSIGNATURE']
#     event= None

#     try:
#         event= stripe.Webhook.construct_event(
#             payload,
#             sig_header,
#             settings.STRIPE_WEBHOOK_SECRET
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status= 400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invaid Signature
#         return HttpResponse(status=400)
#     if event.type == "checkout.session.completed":
#         session= event.data.object
#         if session.mode =='payment' and session.payment_status == 'paid':
#             try:
#                 order = Order.objects.get(id=event.data.client_reference_id)
#             except Order.DoesNotExist:
#                 return HttpResponse(404)
#             # mark order as paid
#             order.paid = True
#             order.save()

    
#     return HttpResponse(status=200)


import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid Signature
        return HttpResponse(status=400)

    if event.type == "checkout.session.completed":
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            handle_payment_success(session.client_reference_id)

    return HttpResponse(status=200)


def handle_payment_success(order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    # Mark order as paid
    order.paid = True
    order.save()
