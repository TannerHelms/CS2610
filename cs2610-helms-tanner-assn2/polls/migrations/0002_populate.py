# This file was created by running this command:
#   python manage.py makemigrations --empty polls --name populate

from django.db import migrations
from django.utils import timezone


def populate_db(apps, schema_editor):
    """
    This is a new function that I define myself.  It takes two parameters.

    The first parameter `apps` is an application registry which enables access
    to my models without needing to use the import statement.  The details are
    a bit involved, but the application registry lets me access previous
    versions of my models; importing the classes via the import statement would
    only let me use those classes as they exist right now.

    The second parameter `schema_editor` may be used when I change the layout
    of fields in a model.  Since we are only interested in creating new
    records right now, we can ignore it.
    """

    Choice = apps.get_model('polls', 'Choice')
    Question = apps.get_model('polls', 'Question')

    # Add new questions about Pizza
    # Remember to call the .save() method for each new object!
    pizza_q = Question(question_text="Best kind of pizza?", pub_date=timezone.now())
    pizza_q.save()

    pepperoni = Choice(question=pizza_q, choice_text="Carnivore", votes=27)
    pepperoni.save()

    hawaiian = Choice(question=pizza_q, choice_text="The Real Dill", votes=13)
    hawaiian.save()

    combination = Choice(question=pizza_q, choice_text="Marghie", votes=42)
    combination.save()

    meat_lovers = Choice(question=pizza_q, choice_text="Carmen", votes=78)
    meat_lovers.save()

    # Add new questions about James Bond
    jamesbond_q = Question(question_text="Best James Bond actor?", pub_date=timezone.now())
    jamesbond_q.save()

    sean = Choice(question=jamesbond_q, choice_text="Sean Connery", votes=92)
    sean.save()

    pierce = Choice(question=jamesbond_q, choice_text="Pierce Brosnan", votes=47)
    pierce.save()

    roger = Choice(question=jamesbond_q, choice_text="Roger Moore", votes=29)
    roger.save()

    daniel = Choice(question=jamesbond_q, choice_text="daniel craig", votes=44)
    daniel.save()


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        # I must add this call to `migrations.RunPython()` myself
        migrations.RunPython(populate_db)
    ]
