from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect
from .models import Entry

# Utils 
from .src.extract_word_info import extract_word_info
from .src.obtain_entry_suggestions import obtain_entry_suggestions

def index(request):
    # Load the template
    template = loader.get_template("dictionary/pages/index.html")

    # Set the context
    text_to_show = """
Καούρ εκάνατε! Εγκείνι ενι το πρώκιου ηλεκτρονικό Τσακώνικο λεξικό!"""
    context = {
        "text_to_show": text_to_show,
    }

    return HttpResponse(template.render(context, request))

def entry(request, entry):
    # Load the template
    template = loader.get_template("dictionary/pages/entry.html")

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
    
    # Redirect to the appropriate page
    match direction:
        case "TS-EL":
            return tsakonian(request, query, orthography)
        case "EL-TS":
            return greek(request, query, orthography)
        case _:
            raise ValueError("Invalid direction")
    
def tsakonian(request, 
              entry: str,
              orthography: str = "nowakowski"):
    # Load the template
    template = loader.get_template("dictionary/pages/tsakonian.html")

    # Search for entries that contain the Greek word in the Greek column
    match orthography:
        case "nowakowski":
            results = Entry.objects.filter(nowakowski = entry)
        case "kostakis":
            results = Entry.objects.filter(kostakis = entry)

    # Set the context
    context = {
        "tsakonian" : entry,
        "direction" : 'TS-EL',
        "orthography" : orthography
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
        match orthography:
            case 'nowakowski':
                tsakonian_list = [entry.nowakowski for entry in tsakonian_list if isinstance(entry.nowakowski, str)]
            case 'kostakis':
                tsakonian_list = [entry.kostakis for entry in tsakonian_list if isinstance(entry.kostakis, str)]
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

def greek(request: object, 
          entry: str,
          orthography: str = "nowakowski"):
    # Load the template
    template = loader.get_template("dictionary/pages/greek.html")

    # Set the context
    context = {
        "greek": entry,
        "direction" : "EL-TS",
        "orthography" : orthography
    }

    # Search for entries that contain the Greek word in the Greek column
    reverse_results = Entry.objects.filter(greek = entry)

    # If there are results, build a list with the following format:
    # Tsakonian word — Greek word
    if reverse_results:
        match orthography:
            case "nowakowski":
                tsakonian_list = [f'{result.nowakowski} — {result.greek}' for result in reverse_results]
            case "kostakis":
                tsakonian_list = [f'{result.kostakis} — {result.greek}' for result in reverse_results]
        context['tsakonian_list'] = tsakonian_list
    
    # Otherwise, provide suggestions
    else:
        # Extract full list of Greek words
        greek_list = Entry.objects.all()
        greek_list = [entry.greek for entry in greek_list if isinstance(entry.greek, str)]
        close_suggestions = obtain_entry_suggestions(entry, 
                                                     greek_list, 
                                                     threshold = 3)
        context['close_suggestions'] = close_suggestions

    print(context)
        
    return HttpResponse(template.render(context, request))
    
def writing_extension(request):
    # Load the template
    template = loader.get_template("dictionary/pages/writing_extension.html")

    # Set the context
    context = {}

    return HttpResponse(template.render(context, request))

def preservation_strategy(request):
        # Load the template
    template = loader.get_template("dictionary/pages/preservation_strategy.html")

    # Set the context
    context = {}

    return HttpResponse(template.render(context, request))