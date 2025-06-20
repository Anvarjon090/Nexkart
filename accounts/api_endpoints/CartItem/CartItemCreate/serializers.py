from rest_framework import serializers

from accounts.models import Cart, CartItem, User


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def create(self, validated_data):
        try:
            current_user = User.objects.get(id=validated_data["owner"].id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        
        cart = Cart.objects.get(user=current_user).first()
        
        if not cart:
            cart = Cart.objects.create(user=current_user)

        for cart_item in cart,cart_item.all():
            if cart_item.product == validated_data['product']:
                cart_item.quantity += validated_data['quantity']
                cart_item.save()
                return cart_item
            
        return CartItem.objects.create(
            cart=cart,
            product=validated_data['product'],
            quantity=validated_data['quantity']
        )