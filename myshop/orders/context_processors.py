from .models import Order
from django.shortcuts import get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required

# @login_required
# def order_processor(request):
#     order_id = None
#     if request.user.is_authenticated:
#         try:
#             # Get order from user's session
#             order_id = request.session['order_id']
#         except KeyError:
#             # Get latest order for user
#             try:
#                 order = get_object_or_404(Order, user=request.user, paid=True)
#                 order_id = order.id
#                 request.session['order_id'] = order_id

#             except Order.DoesNotExist:
#                 pass
#     return {'order_id': order_id,
#             }


