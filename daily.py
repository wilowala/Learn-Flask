from flask import redirect, url_for
from basics import intro

toDo = {
    "monday" : "Play football",
    "tuesday" : "Code",
    "wednesday" : "Go to gym",
    "thursday" : "Bake a cake",
    "friday" : "Attend a dance class",
    "saturday" : "Go to church",
    "sunday" : "Watch favorite series"
}

def get_all_to_do():
    return f"<ul>{to_to_do()}</ul>"

def to_to_do():
    li = ""
    for key in toDo:
        href = f"http://localhost:8000/day/{key}"
        li = li + f"<a href = {href}><li><h1>On:<b>{key}</b> we {toDo[key]}</h1></li></a>"
    return li

def get_the_to_do(key):
    baseUrl = f"http://localhost:8000/"
    return f"<h1>On this day, {key}</h1><h2> We {toDo[key]}</h2>"

# print(get_all_to_do())