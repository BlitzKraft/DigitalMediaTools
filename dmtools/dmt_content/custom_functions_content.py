from django.utils.crypto import get_random_string
from django.template.defaultfilters import slugify
from dmtools.custom_vars import SITES_ROOT, ZIP_PATH
from dmt_sponsors.models import Sponsor
from dmt_content.models import Content
from glob import glob
import os, re, zipfile, shutil, ffmpy, requests, json


def content_site_folder(sid):
    site = Sponsor.objects.all()
    for s in site:
        if int(sid) == s.pk:
            return s.site_folder


def content_generate_folder(add=''):
    allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if add != '':
        allowed = allowed + add
    return get_random_string(25, allowed_chars=allowed)


def content_unzipme(zip, path):
    fh = open(zip, 'rb')
    z = zipfile.ZipFile(fh)
    folder = re.sub(r"\.zip$", '', zip.split('/')[-1])
    for name in z.namelist():
        z.extract(name, path + '/')

    content_rename_files(path + folder)
    return folder


def content_rename_files(path):
    path = path + '/'
    files = glob(path + '*.mp4')
    files.extend(glob(path + '*.MP4'))
    files.extend(glob(path + '*.jpg'))
    files.extend(glob(path + '*.JPG'))

    for f in files:
        fname = f.split('/')[-1].lower()
        os.rename(f, path + fname)


def content_slug(d):
    return slugify(d['content_title'])


def content_change_assigned_site(d):
    content = Content.objects.filter(content_slug=d['content_slug'])
    for c in content:
        current_sid = c.content_siteid
        current_folder = c.content_folder

    if d['content_siteid'] != current_sid:
        new_site_folder = content_site_folder(d['content_siteid'])
        old_site_folder = content_site_folder(current_sid)

        dest = SITES_ROOT + new_site_folder + '/' + current_folder
        src = SITES_ROOT + old_site_folder + '/' + current_folder
        shutil.copytree(src, dest, ignore=None)
        shutil.rmtree(src)

    return d['content_siteid']


def content_duration(d):

    tup_resp = FFprobe(
        inputs={d: None},
        global_options=[
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format', '-show_streams']
    ).run(stdout=subprocess.PIPE)
    meta = json.loads(tup_resp[0].decode('utf-8'))
    return meta['streams'][0]['duration']


def content_videos(d):
    path = d + '/'
    files = glob(path + '*.mp4')

    for f in files:
        duration = content_duration(f)

        if 60 > duration:
            print('trailer')
        elif duration < 60 and 120 > duration:
            print('2 min')


    pass


def content_setup(d):
    zip_path = CONTENT_PATH + d['content_zip_file']

    if os.path.isfile(zip_path):
        folder_name = content_generate_folder()
        site_folder = content_site_folder(d['content_siteid'])
        folder_path = SITES_ROOT + site_folder + '/'

        if not os.path.isdir(folder_path + re.sub(r"\.zip$", '', zip_path.split('/')[-1])):
            dirty_folder = content_unzipme(zip_path, folder_path)
            dirty_folder = re.sub(r".zip$", '', dirty_folder)
            os.rename(folder_path + dirty_folder, folder_path + folder_name)

            # Process Videos
            videos = content_videos(folder_path + folder_name)

            #os.unlink(zip_path)
            return folder_name
        else:
            folder_name = content_generate_folder()
            folder_path = SITES_ROOT + content_site_folder(d['content_siteid']) + '/'
            dirty_folder = content_unzipme(zip_path, folder_path)
            dirty_folder = re.sub(r"\.zip$", '', dirty_folder)
            os.rename(folder_path + dirty_folder, folder_path + folder_name)

            #os.unlink(zip_path)
            return folder_name

    else:
        pass


