import base64
from django.core import signing
from django.db import models

class MemberManager(models.Manager):
    def get_by_unsubscribe_key(self, key):
        if isinstance(key, unicode):
            key = key.encode('ascii', 'ignore')
        decoded_key =  base64.urlsafe_b64decode(key + '=' * (-len(key) % 4))
        try:
            unsigned = signing.loads(decoded_key)
        except signing.BadSignature:
            raise self.model.DoesNotExist
        return super(MemberManager, self).get(email=unsigned['email'])

class Member(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    signup_time = models.DateTimeField(auto_now_add=True)
    is_subscribed = models.BooleanField(default=True)
    unsubscribed_time = models.DateTimeField(blank=True, null=True)
    objects = MemberManager()

    def __unicode__(self):
        return self.email

    @property
    def unsubscribe_key(self):
        signed = signing.dumps({'email': self.email})
        return base64.urlsafe_b64encode(signed).strip('=')

