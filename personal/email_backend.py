from django.core.mail.backends.smtp import EmailBackend


class PSBackend(EmailBackend):
    def send_messages(self, email_messages):
        for msg in email_messages:
            try:
                msg.content_subtype = 'html'
            except:
                pass
        super(PSBackend, self).send_messages(email_messages)
