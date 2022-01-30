import datetime
from django.test import TestCase
from tinyapp.models import User, Url



def shortURLCreator(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return x


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="Luke",
            last_name="Peterson",
            username="LP",
            email="LP@example.com",
            is_staff=False,
            is_active=True,
            is_superuser=False
        )
        self.user.set_password("bootcamp")
        self.user.save()


        self.url_1 = Url.objects.create(
            short_url='DBRKpV',
            long_url='http://www.microsoft.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url_2 = Url.objects.create(
            short_url='R4kWx8',
            long_url='https://www.aritzia.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url_3 = Url.objects.create(
            short_url='JoGAIa',
            long_url='https://www.youtube.com/',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url_4 = Url.objects.create(
            short_url='NGW65u',
            long_url='https://www.freecodecamp.org/',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url_4 = Url.objects.create(
            short_url='usU25P',
            long_url='http://www.KLM.ca',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        