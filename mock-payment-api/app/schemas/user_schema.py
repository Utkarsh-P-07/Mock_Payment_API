def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "created_at": user["created_at"]
    }

def list_users(users) -> list:
    return [user_serializer(user) for user in users]
