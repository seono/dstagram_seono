from django.contrib import admin
from .models import Photo
# Register your models here.

admin.site.register(Photo)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']  #목록에 보일 필드를 설정
    raw_id_fields = ['author']                          #ForeignKey 필드의 경우 연결된 모델의 객체 목록을 출력하고 선택해야 하는데 목롤이 너무 길 경우 불편 -> raw_id_fields : 값을 써넣는 형태로 바뀜
    list_filter = ['created','updated','author']        #필터 기능을 사용할 필드를 선택
    search_fields = ['text','created']                  #검색 기능을 통해 검색할 필드를 선택
    ordering = ['-updated','-created']                  #모델의 기본 정렬 값 대신 관리자 사이트에서 기본적으로 사용할 정렬값을 설정
