from django.shortcuts import render
from get_data.models import Party, PartyPolicy, City, Gungu, Candidate 
import urllib.request
from urllib.parse import urlencode,quote_plus



def index(request):
    cities = City.objects
    gungus=Gungu.objects.filter(sd_name = City.objects.get(name='부산광역시'))
    candidates = Candidate.objects
    parties = Party.objects
    partypolicies = PartyPolicy.objects
    print(gungus)

    if request.GET.get('gungus'):
        temp_gungus = Gungu.objects.get(id=request.GET.get('gungus'))
        print(temp_gungus)
        target_candidates = candidates.filter(sggname=temp_gungus)
        # except:
        #     target_candidates = None
        # print([qs if qs.Exist else 'None' for qs in candidates.filter(sggname=Gungu.objects.get(name=temp_gungus))])
        context = {'cities' : cities, 'gungus' :gungus,'temp_gungus':temp_gungus, 'candidates':candidates,'target_candidates':target_candidates, 'parties':parties, 'partypolicies':partypolicies}
        return render(request, 'index.html', context)


    

    # temp_cities = request.GET.get('cities')
    context = {'cities' : cities, 'gungus' :gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies}
    return render(request, 'index.html', context)