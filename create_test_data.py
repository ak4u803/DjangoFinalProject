import os
import django
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Import models after Django setup
from onlinecourse.models import Instructor, Course, Lesson, Question, Choice

def create_test_data():
    # Get or create admin user
    try:
        admin_user = User.objects.get(username='admin')
        print("Admin user already exists")
    except User.DoesNotExist:
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin'
        )
        print("Created admin user")

    # Add admin as an Instructor
    instructor, created = Instructor.objects.get_or_create(
        user=admin_user,
        defaults={
            'full_time': True,
            'total_learners': 0
        }
    )
    if created:
        print("Created instructor for admin")
    else:
        print("Instructor for admin already exists")

    # Create course
    course, created = Course.objects.get_or_create(
        name="Learning Django",
        defaults={
            'description': "Django is an extremely popular and fully featured server-side web framework, written in Python",
            'pub_date': timezone.now().date(),
            'total_enrollment': 0
        }
    )
    if created:
        print("Created course 'Learning Django'")
        # Add instructor to course
        course.instructors.add(instructor)
        print("Added admin as instructor to course")
    else:
        print("Course 'Learning Django' already exists")

    # Create lesson
    lesson, created = Lesson.objects.get_or_create(
        title="What is Django",
        course=course,
        defaults={
            'order': 0,
            'content': "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It's open source."
        }
    )
    if created:
        print("Created lesson 'What is Django'")
    else:
        print("Lesson 'What is Django' already exists")

    # Create question
    question, created = Question.objects.get_or_create(
        content="Is Django a Python framework",
        course=course,
        defaults={
            'grade': 100
        }
    )
    if created:
        print("Created question 'Is Django a Python framework'")
    else:
        print("Question 'Is Django a Python framework' already exists")

    # Create choices
    choice1, created = Choice.objects.get_or_create(
        question=question,
        content="Yes",
        defaults={
            'is_correct': True
        }
    )
    if created:
        print("Created choice 'Yes' (correct)")
    else:
        print("Choice 'Yes' already exists")

    choice2, created = Choice.objects.get_or_create(
        question=question,
        content="No",
        defaults={
            'is_correct': False
        }
    )
    if created:
        print("Created choice 'No' (incorrect)")
    else:
        print("Choice 'No' already exists")

    print("\nTest data creation completed!")
    print("You can now log in to the admin interface with:")
    print("Username: admin")
    print("Password: admin (if you used the default)")

if __name__ == '__main__':
    create_test_data()
