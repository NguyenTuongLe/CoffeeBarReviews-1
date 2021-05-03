import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import CoffeeBar


class CoffeeBarModelTests(TestCase):

    def test_was_published_recently_with_future_coffeeBar(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_coffeeBar = CoffeeBar(pub_date=time)
        self.assertIs(future_coffeeBar.was_published_recently(), False)

    def test_was_published_recently_with_old_coffeeBar(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_coffeeBar = CoffeeBar(created_at=time)
        self.assertIs(old_coffeeBar.was_published_recently(), False)

    def test_was_published_recently_with_recent_coffeeBar(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_coffeeBar = CoffeeBar(created_at=time)
        self.assertIs(recent_coffeeBar.was_published_recently(), True)


class CoffeeBarIndexViewTests(TestCase):
    def test_no_coffeeBars(self):
        response = self.client.get(reverse('reviews:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Không có quán cà phê nào")
        self.assertQuerysetEqual(response.context['latest_coffeeBar_list'], [])

    def test_past_coffeeBar(self):
        create_coffeeBar(name="Past coffeeBar.", days=-30)
        response = self.client.get(reverse('reviews:index'))
        self.assertQuerysetEqual(
            response.context['latest_coffeeBar_list'],
            ['<CoffeeBar: Past coffeeBar.>']
        )

    def test_future_coffeeBar(self):
        create_coffeeBar(name="Future coffeeBar.", days=30)
        response = self.client.get(reverse('reviews:index'))
        self.assertContains(response, "Không có quán cà phê nào.")
        self.assertQuerysetEqual(response.context['latest_coffeeBar_list'], [])

    def test_future_coffeeBar_and_past_coffeeBar(self):
        create_coffeeBar(name="Past coffeeBar.", days=-30)
        create_coffeeBar(name="Future coffeeBar.", days=30)
        response = self.client.get(reverse('reviews:index'))
        self.assertQuerysetEqual(
            response.context['latest_coffeeBar_list'],
            ['<CoffeeBar: Past coffeeBar.>']
        )

    def test_two_past_coffeeBars(self):
        create_coffeeBar(name="Past coffeeBar 1.", days=-30)
        create_coffeeBar(name="Past coffeeBar 2.", days=-5)
        response = self.client.get(reverse('reviews:index'))
        self.assertQuerysetEqual(
            response.context['latest_coffeeBar_list'],
            ['<CoffeeBar: Past coffeeBar 2.>', '<CoffeeBar: Past coffeeBar 1.>']
        )

class CoffeeBarDetailViewTests(TestCase):
    def test_future_coffeeBar(self):
        future_coffeeBar = create_coffeeBar(name='Future CoffeeBar.', days=5)
        url = reverse('reviews:detail', args=(future_coffeeBar.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_coffeeBar(self):
        past_coffeeBar = create_coffeeBar(name='Past CoffeeBar.', days=-5)
        url = reverse('reviews:detail', args=(past_coffeeBar.id,))
        response = self.client.get(url)
        self.assertContains(response, past_coffeeBar.name)


def create_coffeeBar(name, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return CoffeeBar.objects.create(name=name, created_at=time)