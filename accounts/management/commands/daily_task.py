# from django.utils import timezone
# from django.core.management.base import BaseCommand
# from accounts.models import DailyStudentStat, Student
#
#
# class Command(BaseCommand):
#     help = 'Description of the task to be performed'
#
#     def handle(self, *args, **kwargs):
#         instances = DailyStudentStat.objects.create(
#             date=timezone.now().today(),
#             total_count=Student.objects.count()
#         )
#         self.stdout.write(self.style.SUCCESS('Successfully completed the daily task'))
