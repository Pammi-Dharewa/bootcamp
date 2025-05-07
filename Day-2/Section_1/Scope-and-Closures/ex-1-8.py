# Scope Error:
# Write a function that tries to access a local variable before assignment.


def scope_error():
    try:
        print(msg)  # Error: local variable referenced before assignment
        msg = "Hi"
    except UnboundLocalError as e:
        print("Error:", e)

scope_error()
# Output: Error: local variable 'msg' referenced before assignment
