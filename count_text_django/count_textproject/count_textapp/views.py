from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.POST['text']
    
    include_blank_text = text.replace('\n','')
    include_blank_len_text = len(include_blank_text)

    exclude_blank_text = text.replace('\n','').replace('\r','').replace(' ','')
    exclude_blank_len_text = len(exclude_blank_text)

    return render(request, 'result.html', {'exclude_blank_len_text':exclude_blank_len_text, 'include_blank_len_text':include_blank_len_text})
