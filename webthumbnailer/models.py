from datetime import datetime
import string
import os

from django.conf import settings
from django.db import models

from utils import run_cmd, make_hash


class ApiKey(models.Model):
    key = models.CharField(primary_key=True, max_length=32, blank=True)
    secret = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)

    def generate_key(self, size=32, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        if not self.secret:
            self.secret = self.generate_key()
        self.last_change = datetime.now()
        super(ApiKey, self).save()


class Thumbnail(models.Model):
    url = models.CharField(primary_key=True, max_length=256)
    hash = models.CharField(max_length=32)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    generation_ms = models.IntegerField()

    def generate_thumbnail(self):
        start = datetime.now()
        run_cmd('cutycapt --url=%s --out=%s' % (self.url, self.path))
        finish = datetime.now()
        duration = finish - start
        self.generation_ms = duration.microseconds / 1000

    def save(self, *args, **kwargs):
        now = datetime.now()
        if not self.created:
            self.created = now
            self.generate_thumbnail()
        self.updated = now
        super(Thumbnail, self).save()

    def get_hash(self):
        if not self.hash:
            self.hash = make_hash(self.url)
        return self.hash

    @property
    def path(self):
        fn = '%s.png' % self.get_hash()
        return os.path.join(settings.WEBTHUMBNAILER_CACHE_ROOT, fn)

    @property
    def uri(self):
        fn = '%s.png' % self.get_hash()
        return os.path.join(settings.WEBTHUMBNAILER_CACHE_URL, fn)
