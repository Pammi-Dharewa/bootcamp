class Flexible:
    def __getattr__(self, name):
        return f"{name} is not set"

obj = Flexible()
print(obj.missing_attr)  # missing_attr is not set
