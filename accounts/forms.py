from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('email', 'password', 'password2')#,'address')
        model = get_user_model()

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            #self.fields['username'].label = 'Display Name'
            self.fields['email'].label = "Email Address"
            self.fields['password'].label = 'Enter Password'
            self.fields['password2'].label = 'Confirm Password'
        #    self.fields['address'].label = 'Enter Address'
