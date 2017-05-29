from django.db import models
from dmtools.custom_vars import SITES_ROOT, ZIP_PATH
from dmt_sponsors.models import Sponsor
import glob


sponsor_list = ()
status_choices = ((str(1), 'Active'), (str(0), 'Inactive'))
hasMovie_choices = ((str(1), 'Yes'), (str(0), 'No'))
zip_choices = ()
CONTENT_PATH = ZIP_PATH


class Content(models.Model):

    zips = glob.glob(ZIP_PATH + '*.zip')
    for z in zips:
        z2 = z.split('/')[-1]
        tmp = tuple([(str(z2), str(z2))])
        zip_choices = zip_choices + tmp

    test = list(Sponsor.objects.filter(dmt_status='1'))
    for item in test:
        tmp = tuple([(str(int(item)), str(item))])
        sponsor_list = sponsor_list + tmp

    content_title = models.CharField(
        max_length=250,
        verbose_name='Title',
    )

    content_sponsor = models.CharField(
        max_length=10,
        default='',
        verbose_name='Sponsor',
        choices=sponsor_list,
    )

    content_slug = models.CharField(max_length=250, default='')
    content_description = models.TextField(
        verbose_name='Description',
        default='',
    )
    content_has_movie = models.CharField(
        max_length=1,
        choices=hasMovie_choices,
        default='0',
        verbose_name='Has Movie',
    )
    content_folder = models.CharField(max_length=250, default='',)
    content_status = models.CharField(
        max_length=1,
        choices=status_choices,
        default='1',
        verbose_name='Status',
    )
    content_zip_file = models.CharField(
        max_length=250,
        blank='-',
        verbose_name='Content',
        choices=zip_choices,
    )

    content_used = models.CharField(
        max_length=3,
        choices=[],
        default='No',
    )

    def __str__(self):
        return self.content_title

    class Meta:
        verbose_name = 'Update'
        verbose_name_plural = 'Updates'