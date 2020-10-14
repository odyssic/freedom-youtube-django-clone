from django.shortcuts import render
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from .forms import LoginForm, RegisterForm, NewImageForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Image, Comment
import string, random
from django.core.files.storage import FileSystemStorage
import os
from wsgiref.util import FileWrapper


# ====================================home==============================

# home page - shows a few recent videos  (8)

class HomeView(View):
    template_name = 'index.html'
    def get(self, request):
        most_recent_images = Image.objects.order_by('-datetime')[:8]
        
        return render(request, 'core/index.html', {'menu_active_item': 'home', 'most_recent_images': most_recent_images})



# ==================================image===============================



class NewImage(View):
    template_name = 'new_image.html'

    def get(self, request):
        if request.user.is_authenticated == False:
            #return HttpResponse('You have to be logged in, in order to upload a image.')
            return HttpResponseRedirect('/register')
        
        form = NewImageForm()
        return render(request, 'core/new_image.html', {'form':form})

    def post(self, request):
        # pass filled out HTML-Form from View to NewImageForm()
        form = NewImageForm(request.POST, request.FILES)
            

        if form.is_valid():
            # create a new image Entry
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']

            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path = random_char+image.name

            fs = FileSystemStorage(location = os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            filename = fs.save(path, image)
            file_url = fs.url(filename)

            print(fs)
            print(filename)
            print(file_url)

            new_image = Image(title=title,
                            user=request.user,
                            path=path,
                            )
            new_image.save()
            
            # redirect to detail view template of an Image
            return HttpResponseRedirect('/image/{}'.format(new_image.id))
        else:
            return HttpResponse('Your form is not valid. Go back and try again.')

        


class ImageFileView(View):
    
    def get(self, request, file_name):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = FileWrapper(open(BASE_DIR+'/'+file_name, 'rb'))
        response = HttpResponse(file, content_type='image/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response
        

# to view am image

class ImageView(View):
    template_name = 'image.html'

    def get(self, request, id):
        #fetch image from DB by ID
        image_by_id = Image.objects.get(id=id)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_by_id.path = 'http://localhost:8000/get_image/'+image_by_id.path
        # type in own URL for a database access
        context = {'image':image_by_id}
        
        if request.user.is_authenticated:
            print('user signed in')
            comment_form = CommentForm()
            context['form'] = comment_form

        
        comments = Comment.objects.filter(image__id=id).order_by('-datetime')[:5]
        print(comments)
        context['comments'] = comments
        return render(request, 'core/image.html', context)



# ====================================Registration==============================        


class LoginView(View):
    template_name = 'login.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            #logout(request)
            return HttpResponseRedirect('/')

        form = LoginForm()
        return render(request, 'core/login.html', {'form': form})

    def post(self, request):
        # pass filled out HTML-Form from View to LoginForm()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # create a new entry in table 'logs'
                login(request, user)
                print('success login')
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('login')
        return HttpResponse('This is Login view. POST Request.')

# logout view

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

class RegisterView(View):
    template_name = 'register.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            print('already logged in. Redirecting.')
            print(request.user)
            return HttpResponseRedirect('/')
        form = RegisterForm()
        return render(request, 'core/register.html', {'form': form})

    def post(self, request):
        # pass filled out HTML-Form from View to RegisterForm()
        form = RegisterForm(request.POST)
        if form.is_valid():
            # create a User account
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/login')
        return HttpResponse('This is Register view. POST Request.')

# ======================comments==========================

class CommentView(View):
    template_name = 'comment.html'

    def post(self, request):
        # pass filled out HTML-Form from View to CommentForm()
        form = CommentForm(request.POST)
        image=""
        if form.is_valid():
            # create a Comment DB Entry
            text = form.cleaned_data['text']
            image_id = request.POST['image']
            image = Image.objects.get(id=image_id)
            
            new_comment = Comment(text=text, user=request.user, image=image)
            new_comment.save()
            return HttpResponseRedirect('/image/{}'.format(str(image_id)))
        return HttpResponse('This is Register view. POST Request.')





