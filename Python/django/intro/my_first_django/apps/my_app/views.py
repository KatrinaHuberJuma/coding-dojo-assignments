from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    context = {
    	"name": "Kat",
    	"favorite_color": "green",
    	"pets": ["Raindrop", "Cassie", "Hobbit"]
    }
    return render(request, "my_app/index.html", context)


def new(request):
    return HttpResponse("NEW THING OMG!")


def display(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def create(request):
    # print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*+*+*+")
    response = redirect('/blogs')
    return response


def show(request, blog_id):
    # print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*+*+*+")
    url_string = "placeholder to later display blog number: ", str(blog_id)
    return HttpResponse(url_string) # TODO: why is this a different font?


def edit(request, blog_id):
    # print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*+*+*+")
    url_string = "placeholder to later EDIT blog number: ", str(blog_id)
    return HttpResponse(url_string) # TODO: why is this a different font?

def destroy(request, blog_id):
    print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+"+ str(blog_id)+"*+*+*+*+*+*+*+*+*+*+*+*+**+*+*+*+")
    response = redirect('/')
    return response
