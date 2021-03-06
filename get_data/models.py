from django.db import models

# Create your models here.


class Party(models.Model):
    name = models.CharField('정당이름',max_length=100,)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    
class PartyPolicy(models.Model):
    name = models.ForeignKey(Party,on_delete=models.CASCADE)
    number = models.IntegerField('순번')
    title = models.CharField('제목',max_length=255)
    category = models.CharField('분야', max_length=255)
    desc = models.TextField('내용',)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)

    def flexible_title(self):
        if len(self.title)>18:
            return self.title[:18] + "..."
        
        return self.title





class City(models.Model):
    name = models.CharField('행정구역',max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Gungu(models.Model):
    sd_name = models.ForeignKey(City,models.CASCADE)
    name = models.CharField('군구이름', max_length=100)

    sgg_name = models.CharField('선거구이름',max_length=100)
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.sgg_name


class Candidate(models.Model):
    candi_id = models.CharField('후보자ID', max_length=200)
    sggname = models.ForeignKey(Gungu, models.CASCADE)
    giho_num = models.CharField('기호', max_length=100)
    jdname = models.ForeignKey(Party, models.CASCADE)
    name = models.CharField('이름', max_length=200)
    gender = models.CharField('성별', max_length=10)
    birth = models.CharField('생년월일', max_length=100)
    age = models.IntegerField('연령',)
    addr = models.CharField('주소', max_length=200)
    job = models.CharField('직업', max_length=200)
    edu = models.CharField('학력', max_length=255)
    career1 = models.CharField('경력1', max_length=255)
    career2 = models.CharField('경력2', max_length=255)
    status = models.CharField('등록상태', max_length=200)

    attend = models.CharField('본회의 출석률',max_length=100)

    promise1 = models.TextField('교육', blank=True)
    promise2 = models.TextField('재난/코로나', blank=True)
    promise3 = models.TextField('여성/노인/장애인/어린이', blank=True)
    promise4 = models.TextField('도시개발', blank=True)
    promise5 = models.TextField('소상공인/자영업자', blank=True)
    promise6 = models.TextField('청년/일자리', blank=True)  

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)


