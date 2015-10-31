from django.forms import ModelForm


from models import Message


class MessageForm(ModelForm):
    def save(self, request, commit=True):
        instance = super(MessageForm, self).save(commit=False)
        instance.log_ip(request)

        if commit:
            instance.save()
        return instance

    class Meta:
        model = Message
        fields = ['email', 'subject', 'message']
