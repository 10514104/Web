from django.shortcuts import render




def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return render(request, 'main/main.html')
