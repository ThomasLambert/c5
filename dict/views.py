from django.template import Context, loader, RequestContext
from c5.dict.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from pcsets import pcset


#1W2X3F4R1M5LH6789

#123456789XH
#123456789RH

def reading(request, reading_id):
    #return HttpResponse("Bonjour tout le monde. Vous etes dans le detail du reading %s." % reading_id)
    reading_list = Reading.objects.all()
    t = loader.get_template('reading.svg')
    c = Context({
        'reading_list': reading_list,
    })
    return HttpResponse(t.render(c))

def shapes(request, slug):
    unslug = slug.split('+')
    shape_list = [list(pcset.PcSet(sh)) for sh in unslug]
    return render_to_response('dict/embed.svg',
		{'shape_list': shape_list},
		context_instance=RequestContext(request,{}, [svg_processor]))


def voicedict(request, voicetype, reading_id):
#    try:
    reading = Reading.objects.get(pk=reading_id)
#    except Reading.DoesNotExist:
#	raise Http404
    return render_to_response('dict/dict.svg',
		{'reading': reading},
		context_instance=RequestContext(request,{}, [svg_processor]))


def svg_processor(request):
	# constants that can be used in templates
	px = 10
	py = 20
	# Circle svg coordinates
	coord = [[None]*2 for i in range(12)]
	coord[11][0] = px + 221.917
	coord[11][1] = py + 104.308
	coord[10][0] = px + 113.940
	coord[10][1] = py + 212.284
	coord[9][0] = px + 74.418
	coord[9][1] = py + 359.785
	coord[8][0] = px + 113.940
	coord[8][1] = py + 507.284
	coord[7][0] = px + 221.918
	coord[7][1] = py + 615.261
	coord[6][0] = px + 369.418
	coord[6][1] = py + 654.783
	coord[5][0] = px + 516.916
	coord[5][1] = py + 615.261
	coord[4][0] = px + 624.894
	coord[4][1] = py + 507.283
	coord[3][0] = px + 664.416
	coord[3][1] = py + 359.784
	coord[2][0] = px + 624.893
	coord[2][1] = py + 212.285
	coord[1][0] = px + 516.916
	coord[1][1] = py + 104.307
	coord[0][0] = px + 369.417
	coord[0][1] = py + 64.785

	return {'bg': 'FFFFFF',
		'draw': '000000',
		'size': 400,
		'coord': coord,
	}
