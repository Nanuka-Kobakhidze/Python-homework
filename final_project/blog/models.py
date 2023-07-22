from django.db import models
from django.urls import reverse
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def get_vote_count(self):
        upvotes = self.vote_set.filter(vote_type="up").count()
        downvotes = self.vote_set.filter(vote_type="down").count()
        return upvotes - downvotes


class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.Post.pk})


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_type = models.CharField(
        choices=(("up", "Upvote"), ("down", "Downvote")), max_length=5
    )

    def __str__(self):
        return f"{self.user.username} - {self.vote_type}"
