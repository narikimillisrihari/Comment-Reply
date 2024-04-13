from django.forms import ModelForm
from fbapp.models import Fb_model,Add_post,SignUp,Comment,comment_reply

class Fb_model_form(ModelForm):
    class Meta():
        model=Fb_model
        fields="__all__"

class Add_post_form(ModelForm):
    class Meta():
        model=Add_post
        fields=['post_title','post_comment','post_urls','post_image','add_comment']
        # fields="__all__"

class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        # fields="__all__"
        fields=['name','body','addpost']


class comment_reply_form(ModelForm):
    class Meta():
        model=comment_reply
        fields="__all__"
