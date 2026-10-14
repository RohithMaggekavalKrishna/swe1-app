from django.db import migrations
from django.utils import timezone

QUESTION_TEXT = "What's your favorite programming language?"


def create_sample_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Choice = apps.get_model("polls", "Choice")
    if Question.objects.filter(question_text=QUESTION_TEXT).exists():
        return
    question = Question.objects.create(
        question_text=QUESTION_TEXT, pub_date=timezone.now()
    )
    for text in ["Python", "Java", "JavaScript"]:
        Choice.objects.create(question=question, choice_text=text, votes=0)


def remove_sample_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Question.objects.filter(question_text=QUESTION_TEXT).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_sample_poll, remove_sample_poll),
    ]
