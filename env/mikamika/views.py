from ssl import _create_unverified_context
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import MikamikaForm
from .forms import MikamikaUploadForm
from .models import Mikamika
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from collections import Counter
import re
from accounts.models import CustomUser
from .models import UserInfo
from .models import Comment
from .forms import CommentForm


def Index(request):
    template_name = 'index.html'

    atstore  = Mikamika.objects.distinct().values_list("store",flat=True).filter(todou='0')
    aostore  = Mikamika.objects.distinct().values_list("store",flat=True).filter(todou='1')
    akstore  = Mikamika.objects.distinct().values_list("store",flat=True).filter(todou='2')
    
    setatstore = set(atstore)
    tstore = random.sample(setatstore,10)

    setaostore = set(aostore)
    ostore = random.sample(setaostore,9)

    setakstore = set(akstore)
    kstore = random.sample(setakstore,10)

    context = {'tstore'  : tstore,
               'ostore'  : ostore,
               'kstore'  : kstore,}
    return render(request, template_name , context)
    

class TokooView(LoginRequiredMixin, CreateView):
      template_name = 'tokoo.html'
      login_url = '/login/'
      form_class = MikamikaForm
      model = Mikamika
      success_url = reverse_lazy('mikamika:mikamika_create_complete')
      

      def get_form_kwargs(self, *args, **kwargs):
          rstore = ugstore2
      #   rtodou = nugtodou2
          kwargs = super().get_form_kwargs(*args, **kwargs)
          kwargs.update({'rstore': rstore})
      #   kwargs.update({'rtodou': rtodou})
          return kwargs

      def form_valid(self, form):
          mikamika =  form.save(commit=False)
          mikamika.create_user=self.request.user
          mikamika.save()
          return super().form_valid(form)

class UserView(LoginRequiredMixin, CreateView):
      template_name = 'user.html'
      login_url = '/account/login/'
      form_class = MikamikaForm
      model = Mikamika
      success_url = reverse_lazy('mikamika:mikamika_create_complete')

      def form_valid(self, form):
          mikamika =  form.save(commit=False)
          mikamika.create_user=self.request.user
          mikamika.save()
          return super().form_valid(form)

def mikamika_create0(request,mttdou,mtstore):
    template_name = 'gfa.html'
    
    ttdou  = mttdou
    tstore = mtstore
    tsflag = mtstore
    
    if   ttdou == '東京':
         tdflag = '0'
    elif ttdou == '大阪':
         tdflag = '1'
    elif ttdou == '京都':
         tdflag = '2'

    mtuflag  = Mikamika.objects.values_list("create_user").filter(store=tsflag,todou=tdflag).exclude(create_user=9)
    setmtuflag = set(mtuflag)

    lenflag = len(setmtuflag)

    if  lenflag >=   1:
        stuflag = random.sample(setmtuflag,k=1)
        tuflag = stuflag[0]

        tstoretodou = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=tuflag).exclude(store=tstore).order_by('?').first()

        if tstoretodou == None:
           tgstore = '未登録'
           tgtdou  = '未登録'
        else:
           tgstore = tstoretodou[0]
           tgtdou  = tstoretodou[1]

           if   tgtdou == '0':
                tgtdou = '東京'
           elif tgtdou == '1':
                tgtdou = '大阪'
           elif tgtdou == '2':
                tgtdou = '京都' 

    else:
          tgstore = '未登録'
          tgtdou  = '未登録'
          
    context = {'tstore'    : tstore,
               'tgstore'   : tgstore,
               'ttdou'     : ttdou,
         #      'lenflag'     :lenflag,
               'tgtdou'    : tgtdou,}

    return render(request, template_name , context)

def mikamika_create(request,ttdou,tstore):
    template_name = 'fa.html'
    global ugstore2 #グローバル変数
  #  global nugtodou2 #グローバル変数
    
    ttdou = ttdou
    tstore = tstore 
       
   # mikamika = get_object_or_404(Mikamika,id='ed9e8b98-7b35-4e06-89dd-51d8f3c7ee60')
  #  mikamika.views += 1
  #  mikamika.save()

   # if mikamika.views > 2:
   #    mikamika.views = 0
   #    mikamika.save()

   #    return redirect('http://127.0.0.1:8000/accounts/login/')

    sosouser = Mikamika.objects.values_list("create_user").filter(store=tstore)

    setsosouser = set(sosouser)
    sosoflag = random.sample(setsosouser,k=1)
    suflag = sosoflag[0]
    ugstore = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=suflag).exclude(store=tstore).order_by('?').first()

    if ugstore == None:
       ugstore2 = '未登録'
       ugtodou  = '未登録'
       tgtdou  = '未登録'
       tgstore = '未登録'
    else:
       ugstore2 = ugstore[0]
       tgstore = ugstore[0]
       ugtodou2 = ugstore[1]

       if   ugtodou2 == '0':
            ugtodou = '東京'
            tgtdou = '東京'
       elif ugtodou2 == '1':
            ugtodou = '大阪'
            tgtdou = '東京'
       elif ugtodou2 == '2':
            ugtodou = '京都'
            tgtdou= '東京'

    context = {'tstore'  : tstore,
               'ttdou'   : ttdou,
               'ugstore2' : ugstore2,
               'ugtodou'  : ugtodou,
               'tgtdou'   : tgtdou,
               'tgstore'  : tgstore,}

    return render(request, template_name , context)


def mikamika_create2(request,ttdou,tstore,tgtdou,tgstore):
    template_name = 'fa2.html'
    global ugstore2 #グローバル変数
    global ugtodou #グローバル変数
    
    ttdou   = ttdou
    tstore  = tstore
    ttgtdou  = tgtdou
    ttgstore = tgstore

    mikamika = get_object_or_404(Mikamika,id='ed9e8b98-7b35-4e06-89dd-51d8f3c7ee60')
    mikamika.views += 1
    mikamika.save()

    if  mikamika.views > 1:
        mikamika.views = 0
        mikamika.save()

        return redirect('http://127.0.0.1:8000/accounts/login/')

    sosouser = Mikamika.objects.values_list("create_user").filter(store=tstore).filter(store=ttgstore)

    lenuser = len(sosouser)
    if  lenuser == 0:
     #   ugstore2 = '未登録'
     #   ugtodou  = '未登録'
         tgstore = '未登録'
         tgtdou  = '未登録'
    else:
        setsosouser = set(sosouser)
        sosoflag = random.sample(setsosouser,k=1)
        suflag = sosoflag[0]
        ugstore = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=suflag).exclude(store=tstore).order_by('?').first()

        if ugstore == None:
     #     ugstore2 = '未登録'
      #    ugtodou  = '未登録'
           tgstore = '未登録'
           tgtdou  = '未登録'
        else:
      #     ugstore2 = ugstore[0]
           tgstore = ugstore[0]
           ugtodou2 = ugstore[1]

        if   ugtodou2 == '0':
           #  ugtodou = '東京'
              tgtdou = '東京'
        elif ugtodou2 == '1':
           #  ugtodou = '大阪'
              tgtdou = '大阪'
        elif ugtodou2 == '2':
           #  ugtodou = '京都'
              tgtdou = '京都'

    context = {'tstore'  : tstore,
               'ttdou'   : ttdou,
           #    'ugstore2' : ugstore2,
            #   'ugtodou'  : ugtodou,
               'ttgtdou'  : ttgtdou,
               'ttgstore'  : ttgstore,
               'tgtdou'   : tgtdou,
               'tgstore'  : tgstore,}

    return render(request, template_name , context)


#def mikamika_create4(request,tstore):
   # template_name = 'fa4.html'
    #global ugstore2 #グローバル変数
    #global nugtodou2 #グローバル変数
    
   # ttstore = tstore 
   # ttstore == None

    #sostore  = Mikamika.objects.values_list("create_user").filter(hyouka='0')
    #gstore   = Mikamika.objects.values_list("create_user").filter(hyouka='1')

   # sgstore = set(gstore) & set(sostore)
    #setuflag = random.sample(sgstore,k=1)
   # uflag = setuflag[0]
   # usostore  = Mikamika.objects.values_list("store","todou").filter(hyouka='0',create_user=uflag).order_by('?').first()
   # ugstore   = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=uflag).order_by('?').first()

   # nugtodou2 = ugstore[1]
   # ugstore2 = ugstore[0]

   #  if   usostore[1] == '0':
   #       usotodou = '東京'
   #  elif usostore[1] == '1':
    #      usotodou = '大阪'
   #  elif usostore[1] == '2':
   #       usotodou = '京都'
    
   #  if   ugstore[1] == '0':
   #       ugtodou = '東京'
   #  elif ugstore[1] == '1':
    #      ugtodou = '大阪'
   #  elif ugstore[1] == '2':
  #        ugtodou = '京都'

   # usostore = usostore[0]
   # ugstore  = ugstore[0]

   # context = {'usostore'   : usostore,
        #        'ugstore'    : ugstore,
    #            'usotodou'   : usotodou,
    #            'ugtodou'    : ugtodou,
   #              'ustore2'   : ugstore2,
   #             'nugtodou2'  : nugtodou2,
   #             'mikamika'  : mikamika,}

#return render(request, template_name , context)


def mikamika_create3(request,tgtdou,tgstore):
    template_name = 'fa3.html'
   # global ugstore2 #グローバル変数
  #  global nugtodou2 #グローバル変数

    tgtdou  = tgtdou
    tgstore = tgstore
    
    gstore   = Mikamika.objects.values_list("create_user").filter(store=tgstore)

    lengstore = len(gstore)
    if lengstore == 0:
       ugtodou ='未登録'
       ugstore = '未登録'
    else:
       sgstore = set(gstore)
       setuflag = random.sample(sgstore,k=1)
       uflag = setuflag[0]
       ugstore   = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=uflag).exclude(store=tgstore).order_by('?').first()
      # ugstore2   = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=uflag).order_by('?').first()

       if  ugstore == None:
     #     ugstore2 = '未登録'
      #    ugtodou  = '未登録'
           ugstore = '未登録'
           ugtodou  = '未登録'
       else:
           if  ugstore[1] == '0':
                ugtodou = '東京'
           elif ugstore[1] == '1':
                ugtodou = '大阪'
           elif ugstore[1] == '2':
                ugtodou = '京都'

           ugstore  = ugstore[0]

  #  nugtodou2 = ugstore2[1]

  #  if   ugstore2[1] == '0':
 #        ugtodou2 = '東京'
 #   elif ugstore2[1] == '1':
  #       ugtodou2 = '大阪'
  #  elif ugstore2[1] == '2':
   # ugstore2  = ugstore2[0]
    
    context = { 'ugstore'    : ugstore,
                'ugtodou'    : ugtodou,
           #    'ugstore2'   : ugstore2,
           #    'ugtodou2'   : ugtodou2,
          #     'nugtodou2'  : nugtodou2,
               'tgtdou'    : tgtdou,
               'tgstore'   : tgstore,}

    return render(request, template_name , context)
    

class MikamikaCreateCompleteView(TemplateView):
    template_name = 'mikamika_create_complete.html'

@login_required
def  mikamika_user(request):
     template_name = 'user.html'

     global ugstore2 #グローバル変数
     global nugtodou2 #グローバル変数

     uflag = request.user
     
     uimage = Mikamika.objects.values_list("image",flat=True).filter(create_user=uflag).order_by("image").last()

     gcount = Mikamika.objects.values_list("store",flat=True).filter(hyouka='1',create_user=uflag).count()
     scount = Mikamika.objects.values_list("store",flat=True).filter(hyouka='0',create_user=uflag).count()
     
     ustore = Mikamika.objects.values_list("store" ,"hyouka").filter(create_user=uflag)
     
     count   = len(ustore)
     mstore  = list(ustore)
     muser   = list()
     for index in range(count):
         mstore[index] = Mikamika.objects.filter(store__in=ustore[index],hyouka__in=ustore[index]).exclude(create_user=uflag)
         mlist = list(mstore[index])
         muser.extend(mlist)
         
     if len(muser) == 0 or len(muser) == '':
         matti = 'ゼロ'
         mgstore = ('なし','なし')
         ugstore2 = '未登録'
         nugtodou2 = '0'
         nugtodou3 = ''
         mflag = 0
         mimage = None
         mage = None
     else:
         matti = max(muser,key=muser.count)
         mflag = matti.create_user.id
         mgstore = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=mflag)
         setmgstore = set(mgstore)
         mgstore = random.sample(setmgstore,k=1)
         
         ugstore2  = mgstore[0][0]
         nugtodou2 = mgstore[0][1]         

         if   nugtodou2 == '0':
              nugtodou3 = '東京'
         elif nugtodou2 == '1':
              nugtodou3 = '大阪'
         elif nugtodou2 == '2':
              nugtodou3 = '京都'
         

         mimage = Mikamika.objects.values_list("image",flat=True).filter(create_user=mflag).order_by("image").last()
         mage = CustomUser.objects.get(username='nnnn4649')

         usstore = UserInfo.objects.values_list("userstore","todou").filter(create_user=mflag)

         usstore2 = usstore[0][0]
         ustodou  = usstore[0][1]   

         
         if   ustodou == '0':
              ustodou2 = '東京'
         elif ustodou == '1':
              ustodou2 = '大阪'
         elif ustodou == '2':
              ustodou2 = '京都' 

         if  request.method == 'POST':
             commet1 = CommentForm(request.POST) 
             if commet1.is_valid():
                commet2 = commet1.cleaned_data["commet"]
            # commet1 = CommentForm(request.POST['commet']) 

             #if  comment.is_valid():
            #     comment.create_user = request.user.username
            #     comment.target = usstore2 
             comment = Comment(create_user=request.user,target_id=usstore2,commet=commet2)
             comment.save()
        
         comment_list = Comment.objects.filter(target=usstore2).order_by('-created_at') #Comment.objects.all()
         comecount = len(comment_list)


              # mikamika.create_user=self.request.user
              # mikamika.save()
              # return super().form_valid(form)
              # return redirect('http://127.0.0.1:8000/mikamika/user/')

     context = {'gcount'    :  gcount,
                'scount'    :  scount,
                'matti'     :  matti,
                'uflag'     :  uflag,
                'muser'     :  muser,
       #         'mlist'     :  mlist,
                'mgstore'   :  mgstore,
                 'mflag'    :  mflag,
                 'ugstore2' :  ugstore2,
                 'nugtodou2' :  nugtodou2,
                 'nugtodou3' :  nugtodou3,
                 'uimage' : uimage,
                 'mimage' : mimage,
                  'mage' : mage,
                  'usstore' : usstore,
                  'usstore2' : usstore2,
                  'ustodou' : ustodou,
                  'ustodou2' : ustodou2,
                  'comment_form' : CommentForm(),#{"create_user" : request.user}
                  'comment_list' : comment_list,
                  'comecount' : comecount,}
     return render(request, template_name , context)

@login_required
def  mikamika_ulist(request):
     template_name = 'ulist.html'

     uname = request.user
     uflag = uname.id

     gustore = Mikamika.objects.values_list("store",flat=True).filter(hyouka='1',create_user=uflag)
     sstore  = Mikamika.objects.values_list("store",flat=True).filter(hyouka='0',create_user=uflag)

     gupk = Mikamika.objects.values_list("id",flat=True).filter(hyouka='1',create_user=uflag)
     supk = Mikamika.objects.values_list("id",flat=True).filter(hyouka='0',create_user=uflag)
     
     mgustore = list(zip(gupk,gustore)) 
     msustore = list(zip(supk,sstore))
    
     context = {'mgustore'  : mgustore,
                'msustore'  : msustore,
                'sstore'   :  sstore,
                'supk'     :  supk,
                'gupk'     :  gupk,
                'gustore'  :  gustore,}

     return render(request, template_name , context)


class MikamikaListView(ListView): 
      template_name = 'mikamika_list.html'
      model = Mikamika


@login_required
def  mikamika_udetail(request):
      template_name = 'udetail.html'
      gustore = 1
      sstore = 1
      context = {'gustore'  :  gustore,
                 'sstore'   :   sstore,}
      return render(request, template_name , context)

#@login_required
class UupdateView(UpdateView):
      template_name = 'uupdate.html'
      model = Mikamika
      form_class = MikamikaForm
      #fields = ('store', 'bikou','hyouka','todou')
      success_url = reverse_lazy('mikamika:mikamika_ulist')


      def form_valid(self, form):
          mikamika = form.save(commit=False)
          mikamika.updated_at = timezone.now()
          mikamika.save()
          return super().form_valid(form)


class UDeleteView(DeleteView):
    template_name = 'udelete.html'
    model = Mikamika
    success_url = reverse_lazy('mikamika:mikamika_ulist')


class MikamikaDetailView(DetailView):
    template_name = 'mikamika_detail.html'
    model = Mikamika

class MikamikaUpdateView(UpdateView):
    template_name = 'mikamika_update.html'
    model = Mikamika
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('mikamika:mikamika_list')

    def form_valid(self, form):
        mikamika = form.save(commit=False)
        mikamika.updated_at = timezone.now()
        mikamika.save()
        return super().form_valid(form)


#from django.http import HttpResponseBadRequest
def mikamika_upload(request):
    context = {'uploadform' : MikamikaUploadForm(),
              # 'id': None,
               'url': None,}

    if request.method == 'POST':
        mikamika = MikamikaUploadForm(request.POST, request.FILES) 
        if mikamika.is_valid():
           mikamika.save(commit=False)
           mikamika.image = request.FILES['image']
           upload_image= mikamika.save()
           #context['id'] = upload_image.id
           context['url']= upload_image.image.url
           #return render(request,'user.html',context)
           return redirect('http://127.0.0.1:8000/mikamika/user/')
        #else:
          # return HttpResponseBadRequest("bad")
    return render(request, 'upload.html', context)

def mikamika_chat(request):

    return render(request, 'mikamika_chat.html')

from accounts.forms import AccountForm
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView):
  #form_class = UserCreationForm
  form_class = AccountForm
  success_url = reverse_lazy('mikamika:index')
  template_name = 'signup.html'


def mikamika_create4(request):
    template_name = 'ufa.html'
    global ugstore2 #グローバル変数
  #  global nugtodou2 #グローバル変数
    
    #mikamika = get_object_or_404(Mikamika,id='5341ebb0-4e6f-462c-9bb6-517f83beda3c')
   # mikamika.views += 1
   # mikamika.save()

    sostore  = Mikamika.objects.values_list("create_user").filter(hyouka='0')
    gstore   = Mikamika.objects.values_list("create_user").filter(hyouka='1')

    sgstore = set(gstore) & set(sostore)
    lenflag = len(sgstore)

    if lenflag >= 1:
       setuflag = random.sample(sgstore,k=1)
       uflag = setuflag[0]
       usostore  = Mikamika.objects.values_list("store","todou").filter(hyouka='0',create_user=uflag).order_by('?').first()
       ugstore   = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=uflag).exclude(store=usostore).order_by('?').first()

       
      # nugtodou2 = ugstore[1]
       #ugstore2 = ugstore[0]

       if usostore == None:
          usotodou = '未登録'
          usostore = '未登録'
       else:
         if   usostore[1] == '0':
              usotodou = '東京'
         elif usostore[1] == '1':
              usotodou = '大阪'
         elif usostore[1] == '2':
              usotodou = '京都'
    
       if  ugstore == None:
           ugtodou  = '未登録'
           ugstore  = '未登録'
       else:
         if   ugstore[1] == '0':
              ugtodou = '東京'
         elif ugstore[1] == '1':
              ugtodou = '大阪'
         elif ugstore[1] == '2':
              ugtodou = '京都'

       usostore = usostore[0]
       ugstore  = ugstore[0]
       ugstore2 = ugstore
    
    else:
        usotodou = '未登録'
        usostore = '未登録'
        ugtodou  = '未登録'
        ugstore  = '未登録'

    context = {'usostore'   : usostore,
               'ugstore'    : ugstore,
               'usotodou'   : usotodou,
               'ugtodou'    : ugtodou,
                'ugstore2'   : ugstore2,}
        #       'nugtodou2'  : nugtodou2,}
     #          'mikamika'  : mikamika,}

    return render(request, template_name , context)


from inquiries.forms import InquiryForm

class InquiriesView(generic.FormView):
 template_name = "inquiries.html"   
 form_class = InquiryForm
 success_url = reverse_lazy('mikamika:index')

 def form_valid(self,form):
   form.send_email()
   return super().form_valid(form) 
 

class CommentView(CreateView):
      model = Comment
      form_class = CommentForm
     # comment_list = Comment.objects.all()
      success_url = reverse_lazy('mikamika:mikamika_user')

      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = '100'
        return context
      #def form_valid(self, form):
     #   post_pk = self.kwargs.get('pk')
     #   post = get_object_or_404(Comment, pk=post_pk)

     #   comment = form.save(commit=False)
     #   comment.target = post
     #   comment.save()

      #  return redirect('mikamika:mikamika_comment', pk=post_pk)

def mikamika_testcreate(request,mttdou,mtstore):
    template_name = 'tfa.html'
    
    ttdou  = mttdou
    tstore = mtstore
    tsflag = mtstore
    
    if   ttdou == '東京':
         tdflag = '0'
    elif ttdou == '大阪':
         tdflag = '1'
    elif ttdou == '京都':
         tdflag = '2'

    mtuflag  = Mikamika.objects.values_list("create_user").filter(store=tsflag,todou=tdflag).exclude(create_user=9)
    setmtuflag = set(mtuflag)

    lenflag = len(setmtuflag)

    if  lenflag >=   1:
        stuflag = random.sample(setmtuflag,k=1)
        tuflag = stuflag[0]

        tstoretodou = Mikamika.objects.values_list("store","todou").filter(hyouka='1',create_user=tuflag).exclude(store=tstore).order_by('?').first()

        if tstoretodou == None:
           tgstore = '未登録'
           tgtdou  = '未登録'
        else:
           tgstore = tstoretodou[0]
           tgtdou  = tstoretodou[1]

           if   tgtdou == '0':
                tgtdou = '東京'
           elif tgtdou == '1':
                tgtdou = '大阪'
           elif tgtdou == '2':
                tgtdou = '京都' 

    else:
          tgstore = '未登録'
          tgtdou  = '未登録'
          
    context = {'tstore'    : tstore,
               'tgstore'   : tgstore,
               'ttdou'     : ttdou,
         #      'lenflag'     :lenflag,
               'tgtdou'    : tgtdou,}

    return render(request, template_name , context)