from django import http
from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse

from . import models
from . import views


class MemberTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.member = models.Member.objects.create(email="me@example.com")

    def test_signing(self):
        member_via_key = models.Member.objects.get_by_unsubscribe_key(
                                                    self.member.unsubscribe_key)
        self.assertEqual(self.member.pk, member_via_key.pk)

    def test_signup(self):
        email = 'me2@example.com'
        request = self.factory.post(reverse('launchpad_signup'),
                                    {'email': email})
        response = views.Signup.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('launchpad_success'))
        member = models.Member.objects.get(email=email)

    def test_good_unsubscribe(self):
        key = self.member.unsubscribe_key
        request = self.factory.post(reverse('launchpad_unsubscribe',
                                            args=(key,)))
        response = views.Unsubscribe.as_view()(request, key=key)
        self.assertEqual(response.status_code, 200)
        member = models.Member.objects.get(pk=self.member.pk)
        self.assertFalse(member.is_subscribed)

    def test_bad_unsubscribe(self):
        bad_key = "notavalidkey9876543210"
        request = self.factory.post(reverse('launchpad_unsubscribe',
                                            args=(bad_key,)))
        self.assertRaises(http.Http404, views.Unsubscribe.as_view(), request, key=bad_key)