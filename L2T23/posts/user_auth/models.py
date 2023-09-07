from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, default='Content')
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    @classmethod
    def create(cls, title, content):
        newpost = cls(title=title, content=content, votes=0)
        newpost.save()

'''
class Choice(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
'''
