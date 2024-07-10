from django.contrib.auth.models import Group, Permission


def permission(role, perms_list):
    for i in perms_list:
        role.permissions.add(Permission.objects.get(codename=i))


teacher_permissions = [
    "view_group",
]

teacher, created = Group.objects.get_or_create(name='Teacher')
permission(teacher, teacher_permissions)

student, created = Group.objects.get_or_create(name='Student')
permission(student, teacher_permissions)

ceo, created = Group.objects.get_or_create(name='CEO')
permission(ceo, [perm.codename for perm in Permission.objects.all()])

admin, created = Group.objects.get_or_create(name='Admin')
permission(admin, teacher_permissions)
