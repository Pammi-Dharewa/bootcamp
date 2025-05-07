def role_required(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') != role:
                raise PermissionError(f"User needs role {role}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@role_required('admin')
def delete_data(user):
    print("Data deleted.")

admin_user = {'name': 'Pammi', 'role': 'admin'}
delete_data(admin_user)
