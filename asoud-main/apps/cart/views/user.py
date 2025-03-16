from rest_framework import views, status, permissions
from rest_framework.response import Response
from utils.response import ApiResponse
from apps.cart.models import (
    Order,
    OrderItem
)
from apps.cart.serializers.user import(
    OrderSerializer,
    OrderCreateSerializer,
    OrderItemSerializer
)
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class OrderCreateView(views.APIView):
    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = serializer.save(user=request.user)
        
        if obj.items.first().product:
            user_id = obj.items.first().product.market.user.id
        else:
            user_id = obj.items.first().affiliate.market.user.id

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{user_id}",
            {
                "type": "send_notification",
                "data": {
                    "type": "order",
                    "message": "New Order Added",
                    "order": {
                        "id": str(obj.id),
                    },
                }
            }
        )

        serialized_data = OrderSerializer(obj).data

        return Response(
            ApiResponse(
                success=True,
                code=200,
                data=serialized_data
            )
        )

class OrderListView(views.APIView):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)

        serializer = OrderSerializer(orders, many=True)
        return Response(
            ApiResponse(
                success=True,
                code=200,
                data=serializer.data
            )
        )

class OrderDetailView(views.APIView):
    def get(self, request, pk:str):
        try:
            order = Order.objects.get(id=pk)

            serializer = OrderSerializer(order)
            return Response(
                ApiResponse(
                    success=True,
                    code=200,
                    data=serializer.data
                )
            )
        
        except Exception as e:
            return Response(
                ApiResponse(
                    success=False,
                    code=500,
                    error=str(e)
                )
            )

class OrderUpdateView(views.APIView):
    def put(self, request, pk:str):
        try:
            order = Order.objects.get(id=pk)

            serializer = OrderCreateSerializer(order, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)

            obj = serializer.save(user=request.user)

            if obj.items.first().product:
                user_id = obj.items.first().product.market.user.id
            else:
                user_id = obj.items.first().affiliate.market.user.id

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"user_{user_id}",
                {
                    "type": "send_notification",
                    "data": {
                        "type": "order",
                        "message": "An Order Updated",
                        "order": {
                            "id": str(obj.id),
                        },
                    }
                }
            )

            serialized_data = OrderSerializer(obj).data

            return Response(
                ApiResponse(
                    success=True,
                    code=200,
                    data=serialized_data
                )
            )
        except Exception as e:
            return Response(
                ApiResponse(
                    success=False,
                    code=500,
                    error=str(e)
                )
            )

class OrderDeleteView(views.APIView):
    def delete(self, request, pk:str):
        try:
            order = Order.objects.get(id=pk)

            order.delete()
        
            return Response(
                ApiResponse(
                    success=True,
                    code=204,
                )
            )
        
        except Exception as e:
            return Response(
                ApiResponse(
                    success=False,
                    code=500,
                    error=str(e)
                )
            )
