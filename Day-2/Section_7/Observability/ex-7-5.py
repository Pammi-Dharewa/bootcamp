def health_check():
    # Here, we can add more system checks like database, memory, etc.
    return {"status": "OK", "message": "System is running smoothly"}

print(health_check())
