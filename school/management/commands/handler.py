from school.models import Student,Studentclean
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'Migrate data from Student to Studentclean'

    def handle(self, *args, **options):
        # Step 1: Migrate data
        students = Student.objects.all()
        for student in students:
            student_clean_instance = Studentclean(
                name=student.name,
                roll=student.roll,
                city=student.city
            )
            student_clean_instance.save()
        students.delete()
        self.stdout.write(self.style.SUCCESS('Data migration and truncation completed successfully.'))