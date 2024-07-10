from django.contrib.auth.models import Group, Permission


def assign_permissions(group, permission_codenames):
    for codename in permission_codenames:
        try:
            permission = Permission.objects.get(codename=codename)
            group.permissions.add(permission)
        except Exception:
            print(f"Permission with codename '{codename}' does not exist.")


teacher_permissions = [
    "view_group",
    "view_student",
    "change_teacher",
    "view_course",
]

student_permissions = [
    "view_student",
    "change_student",
    "view_course",
]

admin_permissions = [
    "view_logentry",
    "add_logentry",
    "add_permission",
    "view_permission",
    "add_group",
    "change_group",
    "delete_group",
    "view_group",
    "add_student",
    "change_student",
    "delete_student",
    "view_student",
    "add_course",
    "change_course",
    "delete_course",
    "view_course",
    "add_group",
    "change_group",
    "delete_group",
    "view_group",
]

hr_permissions = [
    "add_user",
    "change_user",
    "delete_user",
    "view_user",
    "add_teacher",
    "change_teacher",
    "delete_teacher",
    "view_teacher",
    "add_course",
    "change_course",
    "delete_course",
    "view_course",
    "view_room",
]


teacher_group, created = Group.objects.get_or_create(name='Teacher')
assign_permissions(teacher_group, teacher_permissions)

student, created1 = Group.objects.get_or_create(name='Student')
assign_permissions(student, [])

ceo, created2 = Group.objects.get_or_create(name='CEO')
assign_permissions(ceo, [perm.codename for perm in Permission.objects.all()])

superadmin, created3 = Group.objects.get_or_create(name='SuperAdmin')
assign_permissions(superadmin, [perm.codename for perm in Permission.objects.all()])

admin, created4 = Group.objects.get_or_create(name='Admin')
assign_permissions(admin, admin_permissions)

hr, created5 = Group.objects.get_or_create(name='HR')
assign_permissions(hr, hr_permissions)
