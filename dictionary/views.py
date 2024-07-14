from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect
from .models import Entry

# Utils 
from .src.extract_word_info import extract_word_info
from .src.obtain_entry_suggestions import obtain_entry_suggestions

# Create your views here.
 
def index(request):
    # Load the template
    template = loader.get_template("dictionary/index.html")

    # Set the context
    text_to_show = """
Καούρ εκάνατε! Εγκείνι ενι το πρώκιου ηλεκτρονικό Τσακώνικο λεξικό!"""
    context = {
        "text_to_show": text_to_show,
    }

    return HttpResponse(template.render(context, request))

def entry(request, entry):
    # Load the template
    template = loader.get_template("dictionary/entry.html")

    # Set the context
    tsakonian = entry

    try:
        entry = get_object_or_404(Entry, tsakonian = tsakonian)
        greek = entry.greek
    except:
        greek = "Δεν βρέθηκε η λέξη στο λεξικό."

    context = {
        "tsakonian": tsakonian,
        "greek": greek,
    }

    return HttpResponse(template.render(context, request))

def search(request):
    query = request.GET.get('q').strip().lower()
    direction = request.GET.get('direction')
    orthography = request.GET.get('orthography')
    print(direction)

    # If the request is empty, go back to the main page
    if not request.GET.get('q'):
        return redirect('/dictionary/')
    
    # Otherwise, redirect to the entry page
    else:
        return redirect(f'/dictionary/{direction}/{query}')

def tsakonian(request, 
              entry,
              **kwargs):
    # Load the template
    template = loader.get_template("dictionary/tsakonian.html")

    # Search for entries that contain the Greek word in the Greek column
    # match ortography:
    #     case "nowakowski":
    #         results = Entry.objects.filter(nowakowski = entry)
    #     case "kostakis":
    #         results = Entry.objects.filter(kostakis = entry)
    results = Entry.objects.filter(nowakowski = entry)

    # Set the context
    context = {
        "tsakonian" : entry,
    }

    # If there are results, build a list with the following format:
    # i. Greek word
    if results:
       greek_list = [entry for entry in results]
       context['greek_list'] = greek_list
    
    # Otherwise, return an empty list
    else:
        # Extract full list of Tsakonian words
        tsakonian_list = Entry.objects.all()
        tsakonian_list = [entry.nowakowski for entry in tsakonian_list if isinstance(entry.nowakowski, str)]
        close_suggestions = obtain_entry_suggestions(entry, tsakonian_list, threshold = 3)
        context['close_suggestions'] = close_suggestions

    # If there is only one result, add the information on top of the page
    if len(results) == 1:
        context['top_info'] = True

        # Extract word information
        if results[0].paradigm is not None:
            word_info = extract_word_info(entry, results[0].paradigm)
            context.update(word_info)

    elif len(results) > 1:
        # Generate notes for each entry
        for result in results:
            if result.paradigm is not None:
                paradigm = result.paradigm
                word_info = extract_word_info(entry, paradigm)
                print(word_info)
                # Add notes to result
                result.notes = word_info['notes']          
        
        # Print context for debug
        print(context)                

    return HttpResponse(template.render(context, request))

def greek(request, entry):
    # Load the template
    template = loader.get_template("dictionary/greek.html")

    # Set the context
    greek = entry

    # Search for entries that contain the Greek word in the Greek column
    reverse_results = Entry.objects.filter(greek = greek)

    # If there are results, build a list with the following format:
    # Tsakonian word — Greek word
    if reverse_results:
       tsakonian_list = [f'{entry.nowakowski} — {entry.greek}' for entry in reverse_results]
    
    # Otherwise, return an empty list
    else:
        tsakonian_list = []
    
    context = {
        "greek": greek,
        "tsakonian_list": tsakonian_list,
    }

    return HttpResponse(template.render(context, request))
    
def writing_extension(request):
    # Load the template
    template = loader.get_template("dictionary/writing_extension.html")

    # Set the context
    context = {}

    return HttpResponse(template.render(context, request))