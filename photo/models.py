from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Photo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_photos')   # ForeignKey값을 이용하여 User 테이블과 이어줌 on_delete인수는 연결된 모델이 삭제될 경우 현제 모델값의 처리를 결정
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)                                       #auto_now_add는 객체가 추가될 때 자동으로 값을 설정
    updated = models.DateTimeField(auto_now=True)                                           #auto_now 수정될때마다
    
    class Meta:
        ordering = ['-updated']                                                             #모델의 객체들 정렬 기준

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])                           # 객체의 상세 페이지의 주소를 변환하는 메소드. 객체를 추가하거나 수정했을 때 이동할 주소를 위해 호출