from django.core.mail import send_mail
from django import forms
from ..models import Contact
from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext as _
from django.conf import settings

def CheckMail(value):
    if not re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", value):
        raise ValidationError('メールアドレスの形式が違います')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'mail', 'text',)
        labels = {
            'name': "Name ",
            'mail': "Mail ",
            'text': "Contact ",
            }

    # メール送信
    def SendContactMail(self):
        mail = self.cleaned_data['mail']
        name = self.cleaned_data['name']
        text = self.cleaned_data['text']
        subject = "問い合わせ"
        message = "---以下問い合わせ内容---"
        message += "\n\n"
        message += "名前：" + name + "\n\n"
        message += "連絡先：" + mail + "\n\n"
        message += "内容：" + text + "\n\n"
        from_email = getattr(settings, "MAIL_ADDR_FROM", None)
        recipient_list = [
            getattr(settings, "MAIL_ADDR_TO", None)
        ]

        send_mail(subject, message, from_email, recipient_list)

    # メールチェック
    def clean_mail(self):
        mail = self.cleaned_data['mail']
        if mail:
            if not re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", mail):
                raise ValidationError(
                    _("メールアドレス形式が正しくありません。"),
                    code="mail format error"
                )
        return mail
