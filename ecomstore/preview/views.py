from django.shortcuts import render

# Create your views here.
# thay thể render_to_response bởi render do render_to_response bị removed trong django 3+
def home(request):
    context = {'site_name': 'Music man'}
    return render(request, "index.html", context)