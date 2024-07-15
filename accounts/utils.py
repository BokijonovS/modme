# utils.py
from django.utils import timezone
from .models import DailyStudentStat

def calculate_daily_change():
    today = timezone.now().date()
    yesterday = today - timezone.timedelta(days=1)

    try:
        today_stat = DailyStudentStat.objects.get(date=today)
        yesterday_stat = DailyStudentStat.objects.get(date=yesterday)

        if yesterday_stat.total_count == 0:
            return 'No data for comparison'

        change_percentage = ((today_stat.total_count - yesterday_stat.total_count) / yesterday_stat.total_count) * 100
        return f"{change_percentage:.2f}% change compared to yesterday"
    except DailyStudentStat.DoesNotExist:
        return 'No data available for today or yesterday'
