from django.template import Context, loader
from c5.dict.models import Reading, Cycle
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404


def reading(request, reading_id):
    #return HttpResponse("Bonjour tout le monde. Vous etes dans le detail du reading %s." % reading_id)
    reading_list = Reading.objects.all()
    t = loader.get_template('reading.svg')
    c = Context({
        'reading_list': reading_list,
    })
    return HttpResponse(t.render(c))

def cycle(request, reading_id):
    p = get_object_or_404(Cycle, pk=cycle_id)
    return render_to_response('cycle.svg', {'cycle': p})