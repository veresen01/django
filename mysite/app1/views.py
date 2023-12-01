from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def log(view_func):
    def wrapper(request):
        logger.info(f'The view function was called {view_func.__name__}')
        return view_func(request)
    return wrapper
@log
def index(request):
     html='''
     <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Главная</title>
    </head>
    <body>
    <h1>Главная</h1>
    
        
    </body>
    </html>
    '''
     return HttpResponse(html)

@log
def about(request):
    html = '''
    <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Обо мне</title>
   </head>
   <body>
   <h1>Меня зовут Юрий</h1>


   </body>
   </html>
   '''
    return HttpResponse(html)