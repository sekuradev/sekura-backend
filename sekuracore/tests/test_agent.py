from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from sekuracore import views
from . import factories


class AgentGetTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get(reverse("agent"))

    def test_anonymous_user_cannot_retrieve_agent_list(self):
        self.request.user = AnonymousUser()
        response = views.Agent.as_view()(self.request)
        self.assertEqual(response.status_code, 401)

    def test_user_can_retrieve_agent_list(self):
        self.request.user = factories.UserFactory()
        response = views.Agent.as_view()(self.request)
        self.assertEqual(response.status_code, 200)


class AgentPostTest(TestCase):
    def test_register_agent_happy_case(self):
        self.factory = RequestFactory()
        with self.settings(PRESHARED_SECRET="foobar"):
            request = self.factory.post(reverse("agent-register"), {"preshared-secret": "foobar", "name": "agent"})
            request.user = AnonymousUser()
            response = views.AgentRegister.as_view()(request)
        self.assertEqual(response.status_code, 200)
