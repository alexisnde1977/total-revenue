from django.shortcuts import HttpResponse
from django.template import loader
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadTsvForm
from .models import Revenue
import os
import csv


def save_file(file):
    """
    Takes in-memory file and writes to the disk

    Parameters
    ----------
    - file : InMemoryUploadedFile, an in-memory .tsv file
    """

    with open(file.name, 'wb+') as saved:
        for chunk in file.chunks():
            saved.write(chunk)


def save_to_db(name):
    """
    Takes a .tsv file name, reads it, and saves the data into a SQLite3 database

    Parameters
    ----------
    - name : String representing a .tsv file name
    """

    # Opens .tsv file
    with open(name) as tsv:
        # Gets rows of .tsv file
        rows = csv.reader(tsv, delimiter='\t')
        next(rows) # Skips header

        # Loops through each row of .tsv file
        for row in rows:
            # Saves a new Revenue object
            revenue = Revenue(
                item=row[0],
                item_description=row[1],
                item_price=float(row[2]),
                item_count=int(row[3]),
                vendor=row[4],
                vendor_address=row[5]
            )
            revenue.save()


@csrf_exempt
def index(request):
    """
    Data.tsv upload page
    """
    try:
        # Gets HTML for form page
        template = loader.get_template('tsv/index.html')
        if request.method == 'POST': # If form is submitted
            # If upload button was pressed
            if 'submit' in request.POST:
                # Throws error if not .tsv file type
                if not request.FILES['tsv'].name.endswith('.tsv'):
                    raise NameError

                # Saves .tsv data into database
                save_file(request.FILES['tsv']) # Saves the in-memory file to disk
                save_to_db(request.FILES['tsv'].name) # Saves .tsv data to database
                os.remove(request.FILES['tsv'].name) # Deletes the saved file

                # Creates form context
                form = UploadTsvForm(request.POST, request.FILES)
                context = {
                    'form' : form
                }
                
                return total(request)
            elif 'purge' in request.POST: # If purge button was pressed
                Revenue.objects.all().delete() # Removes all Revenue objects from database
                
                # Creates form context
                form = UploadTsvForm()
                context = {
                    'form' : form,
                    'purge' : True
                }
        else: # If form hasn't been submitted
            # Creates form context
            form = UploadTsvForm()
            context = {
                'form' : form
            }
    except MultiValueDictKeyError: # No file uploaded
        # Sets relevant form and error
        form = UploadTsvForm()
        context = {
            'form' : form,
            'error' : 'Please upload a file.'
        }
    except NameError: # Not a .tsv file
        # Sets relevant form and error
        form = UploadTsvForm()
        context = {
            'form' : form,
            'error' : 'Your file was not a .tsv file.'
        }
    except: # Catch-all for errors
        form = UploadTsvForm()
        context = {
            'form' : form,
            'error' : 'An error occurred. Please try again.'
        }

    return HttpResponse(template.render(context, request))


@csrf_exempt
def total(request):
    """
    Total Revenue Display Page
    """

    # Loads HTML for total revenue page
    template = loader.get_template('tsv/total.html')

    # Gets total revenue from database
    revenues = Revenue.objects.all()
    total = 0
    for rev in revenues:
        total += rev.item_price * rev.item_count

    # Creates context with total revenue
    context = {
        'total' : total
    }

    return HttpResponse(template.render(context, request))
