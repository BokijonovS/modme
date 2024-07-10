from django.contrib.auth.models import Group, Permission


def permission(role, perms_list):
    for i in perms_list:
        role.permissions.add(Permission.objects.get(codename=i))


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

teacher, created = Group.objects.get_or_create(name='Teacher')
permission(teacher, teacher_permissions)

student, created = Group.objects.get_or_create(name='Student')
permission(student, student_permissions)

ceo, created = Group.objects.get_or_create(name='CEO')
permission(ceo, [perm.codename for perm in Permission.objects.all()])

superadmin, created = Group.objects.get_or_create(name='SuperAdmin')
permission(superadmin, [perm.codename for perm in Permission.objects.all()])

admin, created = Group.objects.get_or_create(name='Admin')
permission(admin, admin_permissions)

hr, created = Group.objects.get_or_create(name='HR')
permission(hr, hr_permissions)

