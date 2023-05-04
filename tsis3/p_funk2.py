# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]




def f1():
    a = input("Wrire movie name: ")
    for key in movies:
        if key.get("name") == a:
            if int(key.get("imdb")) > 5.5:
                print("True")
                break
            else:
                print("False")
                break

f1()

def f2():
    for key in movies:
        if key.get("imdb") > 5.5:
            print(key.get("name"))



def f3():
    a = input("Write category: ")
    for key in movies:
        if key.get("category") == a:
            print(key.get("name"))


def f4():
    for key in movies:
        a = 0
        b = 0
        b += 1
        a += int(key.get("imdb"))

    print(a / b)


def f5():
    a = input("Write category: ")
    b = 0
    c = 0
    for key in movies:
        if key.get("category") == a:
            b += 1
            c += key.get("imdb")
        input(c / b)
