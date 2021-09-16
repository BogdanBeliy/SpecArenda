from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, View
from .models import Ad, Organization, PaprentCategory


class CatigoriesView(ListView):
    context_object_name = 'categories'
    template_name = 'web/categories.html'
    queryset = PaprentCategory.objects.all()


class AdsByCategory(ListView):
    template_name = 'web/ads_list.html'
    context_object_name = 'ads_by_cat'

    def get_queryset(self):
        return Ad.objects.filter(category__slug=self.kwargs['slug'])


class OrganisationDetailView(View):
    def get(self, request, slug):
        org_detail = get_object_or_404(Organization, slug=slug)
        return render(request, 'organisations/org_detail.html', {'org_detail': org_detail})
    

    
    
    
    


        
