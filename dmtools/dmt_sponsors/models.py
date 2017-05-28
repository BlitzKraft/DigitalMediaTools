from django.db import models




class Sponsor(models.Model):

    status_choices = ((str(1), 'Active'), (str(0), 'Inactive'),)
    feature_choices = ((str(1), 'Yes'), (str(0), 'No'),)

    dmt_name = models.CharField(
        max_length=100,
        verbose_name='Name',
    )
    dmt_url = models.CharField(
        max_length=250,
        verbose_name='URL',
    )
    dmt_user = models.CharField(
        max_length=25,
        verbose_name='Username',
    )
    dmt_password = models.CharField(
        max_length=25,
        verbose_name='Password',
    )
    dmt_email = models.CharField(
        max_length=250,
        verbose_name='Email',
    )
    dmt_feature = models.CharField(
        max_length=1,
        verbose_name='Feature',
        choices=feature_choices,
    )
    dmt_status = models.CharField(
        max_length=1,
        verbose_name='Status',
        choices=status_choices,
    )

    def __str__(self):
        return self.dmt_name

    def __int__(self):
        return self.pk

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'