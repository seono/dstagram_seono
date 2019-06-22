from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Photo

from django.contrib.auth.mixins import LoginRequiredMixin       #권한 제한하는 건데 @login_required라는 decorator는 함수형 (def)뷰에서 사용 지금은 클래스 형 뷰->Mixin사용

class PhotoListView(LoginRequiredMixin,ListView):
     model = Photo
     template_name="photo/list.html"
    
class PhotoUploadView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'                         #사용할 템플릿

    def form_valid(self, form):                                 #업로드를 끝낸 후 이동할 페이지 호출할 메소드
        form.instance.author_id = self.request.user.id          #작성자는 현재 로그인한 사용자
        if form.is_valid():                                     #입력된 값을 검증
            form.instance.save()                                
            return redirect('/')                                #메인페이지로 이동
        else:
            return self.render_to_response({'form':form})       #이상이 있을시 작성된 내용을 그대로 작성 페이지에 표시

class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'

class PhotoDetailView(LoginRequiredMixin,DetailView):
    model = Photo
