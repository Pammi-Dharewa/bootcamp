@dataclass
class AdminUser(User):
    access_level: int

admin = AdminUser("Admin", 35, access_level=5)
print(admin)
