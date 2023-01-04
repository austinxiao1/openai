from django.db import models
from django.utils import timezone


OPEN_AI_MODELS = [
    ("text-davinci-003", "text-davinci-003"),
    ("text-curie-001", 'text-curie-001'),
    ("code-davinci-002", "code-davinci-002")
]

OPEN_AI_QUESTION_CATEGORY = [
    ("Q&A", "Q&A"),
    ("Summarize for a 2nd grader", "Summarize for a 2nd grader"),
    ("Text to command", 'Text to command'),
    ("Keywords", "Keywords"),
    ("Code Generation", "Code Generation")
]


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class OpenAIPlay(models.Model):
    question = models.CharField(max_length=30000)
    model = models.CharField(choices=OPEN_AI_MODELS,
                             max_length=300, default="text-davinci-003")
    answer = models.TextField(help_text="text from open ai", default="")
    full_response = models.TextField(help_text="response from open ai", default="")
    create_date = models.DateTimeField("date created")
    category = models.CharField(choices=OPEN_AI_QUESTION_CATEGORY,
                                max_length=300, default="Q&A")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.create_date)
        return f"'{self.question}' created on {date.strftime('%A, %d %B, %Y at %X')}"

class User(models.Model):
    username=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    def __str__(self):
        return self.username