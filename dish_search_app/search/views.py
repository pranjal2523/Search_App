from django.shortcuts import render
from search.models import Dish

def search_dish(request):
    
    if request.method == "GET":
        return render(request, 'search/search.html')
    
    if request.method == "POST":
        query = request.POST.get('query')
        submitted_query = query  # Store the submitted query
        if query:
            dishes = Dish.objects.filter(name__icontains=query)
            if dishes.exists():
                empty = {"isEmpty" : False }   

            else:
                empty = {"isEmpty" : True}
        else:
           empty = {"isEmpty" : True}
           dishes = []
            
        #print(empty)
        # if not dishes[0].name:
        #     empty = True
        # else: 
        #     empty = False 
        # print(empty)   
        return render(request, 'search/search.html', {'dishes': dishes,  'empty':empty, 'submitted_query': submitted_query})
    