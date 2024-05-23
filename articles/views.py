from datetime import date
from django.shortcuts import render

# Dummy data
posts_data = [
    {
        'slug': 'oorsprong-van-familienaam',
        'author': 'Ivo',
        'date': date(2022, 5, 27),
        'title': 'Oorsprong van Familienaam',
        'img': 'de_mallemolen.jpg',
        'excerpt': 'De wetenschap dat de naam Eijgenraem is voortgekomen uit de 16e eeuwse naam Ingenraem heeft tot geheel nieuwe inzichten geleid.',
        'content': '''
            Oorsprong en betekenis van de familienaam Ingen Raem, Ingenraem, Eijgenraem, Engenraem. 

            De wetenschap dat de naam Eijgenraem is voortgekomen uit de 16e eeuwse naam Ingenraem heeft tot geheel nieuwe inzichten geleid wat betreft de betekenis van de naam. 
            In het verleden is serieus gedacht aan een connectie met “glazen ramen”, zoals deze in de glastuinbouw gebruikt worden. 
            Ook de weversramen van de lakennijverheid, waarbij in Den Haag een onderscheid is ontstaan tussen eygen ramen en gemeene ramen(gezamenlijke ramen), 
            zijn als een mogelijke bron van de familienaam beschouwd. 

            Voor anderen was “Eijgenraam” een verbastering van het vermeende oorspronkelijke “Eggeraam”, ook het familiewapen-ontwerp is hierop gebaseerd. 

            Het Meertens instituut in Amsterdam geeft nog weer een andere betekenis: 

            Deze naam wordt wel verklaard uit de voornaam Ingelram of Engelram, welke Germaanse naam zou refereren aan de volksnaam de Angelen en als tweede lid het woord hrabna= raaf bevat. 
            De naam Ingenraem komt in de database van het Meertens instituut niet voor.
            '''
    },
    {
        'slug': 'oorsprong-van-familienaam',
        'author': 'Ivo',
        'date': date(2020, 5, 27),
        'title': 'Oorsprong van Familienaam',
        'img': 'de_mallemolen.jpg',
        'excerpt': 'De wetenschap dat de naam Eijgenraem is voortgekomen uit de 16e eeuwse naam Ingenraem heeft tot geheel nieuwe inzichten geleid.',
        'content': '''
            Oorsprong en betekenis van de familienaam Ingen Raem, Ingenraem, Eijgenraem, Engenraem. 

            De wetenschap dat de naam Eijgenraem is voortgekomen uit de 16e eeuwse naam Ingenraem heeft tot geheel nieuwe inzichten geleid wat betreft de betekenis van de naam. 
            In het verleden is serieus gedacht aan een connectie met “glazen ramen”, zoals deze in de glastuinbouw gebruikt worden. 
            Ook de weversramen van de lakennijverheid, waarbij in Den Haag een onderscheid is ontstaan tussen eygen ramen en gemeene ramen(gezamenlijke ramen), 
            zijn als een mogelijke bron van de familienaam beschouwd. 

            Voor anderen was “Eijgenraam” een verbastering van het vermeende oorspronkelijke “Eggeraam”, ook het familiewapen-ontwerp is hierop gebaseerd. 

            Het Meertens instituut in Amsterdam geeft nog weer een andere betekenis: 

            Deze naam wordt wel verklaard uit de voornaam Ingelram of Engelram, welke Germaanse naam zou refereren aan de volksnaam de Angelen en als tweede lid het woord hrabna= raaf bevat. 
            De naam Ingenraem komt in de database van het Meertens instituut niet voor.
            '''
    },
    {
        'slug': 'oorsprong-van-familienaam',
        'author': 'Ivo',
        'date': date(2021, 5, 27),
        'title': 'Oorsprong van Familienaam',
        'img': 'de_mallemolen.jpg',
        'excerpt': 'De wetenschap dat de naam Eijgenraem is voortgekomen uit de 16e eeuwse naam Ingenraem heeft tot geheel nieuwe inzichten geleid.',
        'content': '''
            Oorsprong en betekenis van de familienaam Ingen Raem, Ingenraem, Eijgenraem, Engenraem. 

            De wetenschap dat de naam Eijgenraem is voortgekomen uit de 16e eeuwse naam Ingenraem heeft tot geheel nieuwe inzichten geleid wat betreft de betekenis van de naam. 
            In het verleden is serieus gedacht aan een connectie met “glazen ramen”, zoals deze in de glastuinbouw gebruikt worden. 
            Ook de weversramen van de lakennijverheid, waarbij in Den Haag een onderscheid is ontstaan tussen eygen ramen en gemeene ramen(gezamenlijke ramen), 
            zijn als een mogelijke bron van de familienaam beschouwd. 

            Voor anderen was “Eijgenraam” een verbastering van het vermeende oorspronkelijke “Eggeraam”, ook het familiewapen-ontwerp is hierop gebaseerd. 

            Het Meertens instituut in Amsterdam geeft nog weer een andere betekenis: 

            Deze naam wordt wel verklaard uit de voornaam Ingelram of Engelram, welke Germaanse naam zou refereren aan de volksnaam de Angelen en als tweede lid het woord hrabna= raaf bevat. 
            De naam Ingenraem komt in de database van het Meertens instituut niet voor.
            '''
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def main_page(request):
    sorted_posts = sorted(posts_data, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'articles/index.html', {
        'posts': latest_posts,
    })

def posts(request):
    return render(request, 'articles/posts.html')

def post_page(request, slug):
    return render(request, 'articles/post_page.html')