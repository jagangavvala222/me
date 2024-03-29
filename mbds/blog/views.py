

# Create your views here.
from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect


###eeeee




def HomeView(request):
    return render(request,'blog/homrintro.html')
from taggit.models import Tag
def post_list_view(request,tag_slug=None):#we requried display the posts based on tags also
    post_list=Post.objects.all()# we get all records
    tag=None# if person not passing slug (not clicking slug) tag value is None
    if tag_slug:#if person click the tag  the tag_slug=not None the if exiguted
        tag=get_object_or_404(Tag,slug=tag_slug)#
        post_list=post_list.filter(tags__in=[tag])#filter the post based on tags

    paginator=Paginator(post_list,4)# It means per page 3 records are taken
    page_number=request.GET.get('page')#to get the current page number
    try:
        post_list=paginator.page(page_number)#related to this page display list
    except PageNotAnInteger: #if I am not sending any page number display first page
        post_list =paginator.page(1)
    except EmptyPage:#if reach last page after that no pages such case display last pages
        post_list=paginator.page(paginator.num_pages) # display the last page






    return render(request,'blog/post_list.html',{'post_list':post_list,'tag':tag})
from django.views.generic import ListView
from blog.forms import commentform
class PostListview(ListView):
    model=Post
    paginate_by=2# per page two posts
    #we know class based ListView default template post_list.html


def post_detail_view(request,year,month,day,post):#here we take threee arguments year ,month ,day and posts
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year, publish__month=month ,publish__day=day)
    # i provovide values of the slug,status,year,month,and day based these create a post object if one of these values missing display error page 404
    comments=post.comments.filter(active=True)#we get all comments related this post
    csubmit=False#comment not submited
    if request.method=='POST':
        form=commentform(request.POST)#get end user submited comment
        if form.is_valid():
            new_comment=form.save(commit=False)#we get end user submitted comment and not saved into the data base
            new_comment.post=post#post is assigened to post field
            new_comment.save()#save the  post
            csubmit=True
    else:#if method is not posts
        form=commentform()#display form



    return render(request,'blog/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})
from django.core.mail import send_mail
from blog.forms import EmailForm

def MailSendView(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False#default send is falase
    if request.method=='POST':# when ever fill the form and click send mail button the request is post method
        form=EmailForm(request.POST)#create form object with data
        if form.is_valid():# chek validations
            cd=form.cleaned_data# This method returns the clean data, which is then inserted into the cleaned_data dictionary of the form.# it is end user submited form data
            #cleaned_data is dictionary which is stores all form fields
            subject="{}({}) recomeds you read '{}'".format(cd['name'],cd['email'],post.title)
            #post_url=post.get_absolute_url()# it gives absloute url means    2019/05/11/indian-army/  total url means http://127.0.0.1:8000/2019/05/11/indian-army/
            post_url=request.build_absolute_uri(post.get_absolute_url())#gives main url means http://127.0.0.1:8000 and post.get_absolute_url() gives 2019/05/11/indian-army/
            #finalyy this post_url gives total url  http://127.0.0.1:8000/2019/05/15/data-science/
            message="Reat post at :\n {}\n\n{}\'s Comments:\n{}".format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'jaganblogspot@gmail.com',[cd['to']])#cd is dict cd['to']='recever mail' ,recever mail put in list [cd['to']]
            #send_mail('subject','message','sender mail',['recever mail'])
            sent=True
            print('status code of mail',sent)
    else:#if method is not post method display form end user
        form=EmailForm()


    return render(request,'blog/sharebyemail.html',{'post':post,'form':form,'sent':sent})



#def mail_send_view(request,id):# here id is primarary key of post
#    post=get_object_or_404(Post,id=id,status='published')
#    form=EmailForm()
#    return render(request,'blog/sharebyemail.html',{'post':post,'form':form})
from django.shortcuts import render

# Create your views here.


from blog import forms

# Create your views here.
def thanksview(request):
    return render(request,'blog/thanks.html')
def contactview(request):
    form=forms.ContactForm()
    if request.method=='POST':
        form=forms.ContactForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return thanksview(request)
            print("message send  sucess fully")
    return render(request,'blog/reg.html',{'form':form})



def Introview(request):



    return render(request,'blog/introduce.html')
