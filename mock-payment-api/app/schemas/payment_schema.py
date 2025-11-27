def payment_serializer(payment) -> dict:
    return {
        "id": str(payment["_id"]),
        "order_id": payment["order_id"],
        "amount": payment["amount"],
        "currency": payment["currency"],
        "status": payment["status"],
        "created_at": payment["created_at"]
    }

def list_payments(payments) -> list:
    return [payment_serializer(payment) for payment in payments]
