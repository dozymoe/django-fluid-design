# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from datetime import datetime
import logging
from io import BytesIO, StringIO
import re
#-
from bs4 import BeautifulSoup
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import Paginator
from django.template import Context, Template
from django.test import SimpleTestCase as BaseTestCase, override_settings
from PIL import Image
#-
from .forms import DummyForm

DATETIME_PATTERN = '%Y-%m-%d %H:%M:%S'
TIMEZONES = (
    ('option-1', "Time zone 1"),
    ('option-2', "Time zone 2"),
    ('option-3', "Time zone 3"),
)

_logger = logging.getLogger(__name__)


def pretty_html(value):
    soup = BeautifulSoup(value, 'lxml')
    if soup.html:
        soup.html.unwrap()
        if soup.body:
            soup.body.unwrap()

    htmlio = StringIO(soup.prettify())
    beautiful_html = ''
    for line in htmlio.readlines():
        count = len(line) - len(line.lstrip(' ')) # count leading spaces
        line = re.sub(r'\s\s+', ' ', line)
        beautiful_html += (count * 2 - count) * ' ' + line
    return beautiful_html


def compare_template(template, expected, context=None, **kwargs):
    if context is None:
        im_io = BytesIO()
        im = Image.new(mode='RGB', size=(200, 200))
        im.save(im_io, 'PNG')
        im_size = im_io.tell()
        im_io.seek(0)

        files = {
            'image': InMemoryUploadedFile(im_io, None,
                'path/image.png', 'image/png', im_size, None),
            'image_multi': InMemoryUploadedFile(im_io, None,
                'Lorem ipsum dolor sit amet consectetur adipisicing elit. '
                'Libero vero sapiente illum reprehenderit molestiae '
                'perferendis voluptatem temporibus laudantium ducimus magni '
                'voluptatum veniam, odit nesciunt corporis numquam maxime '
                'sunt excepturi sint!.png',
                'image/png', im_size, None),
            'image_invalid': InMemoryUploadedFile(im_io, None,
                'color', 'image/png', im_size, None),
        }
        form1 = DummyForm(data={
                'text': "a text",
                'choice': ['val1'],
                'choice2': 'red',
                'started_at': datetime.strptime('2022-02-03 01:02:03',
                    DATETIME_PATTERN),
                'started_at_missing': '',
                'stopped_at': datetime.strptime('2022-10-04 11:30:40',
                    DATETIME_PATTERN),
                'stopped_at_missing': '',
                'number': 0,
                'number_must': 24,
                'number_help': 1,
                'number_invalid': 'a',
                'number_helpinvalid': 'a'},
                files=files)
        form1.is_valid()
        form2 = DummyForm(data={
                'text': "a text",
                'choice': ['val1', 'val3'],
                'choice2': 'red',
                'started_at': datetime.strptime('2022-02-03 01:02:03',
                    DATETIME_PATTERN),
                'started_at_missing': '',
                'stopped_at': datetime.strptime('2022-10-04 11:30:40',
                    DATETIME_PATTERN),
                'stopped_at_missing': '',
                'number': 24,
                'number_must': 24,
                'number_help': 1,
                'number_invalid': 'a',
                'number_helpinvalid': 'a'},
                files=files)
        form2.is_valid()

        pager = Paginator(range(100), 10)
        context = Context({
                'form1': form1,
                'form2': form2,
                'page': pager.page(3),
                'page_first': pager.page(1),
                'page_last': pager.page(10),
                'timezones': TIMEZONES})
    else:
        context = Context(context)

    if kwargs:
        context.push(kwargs)
    return (
        pretty_html(expected),
        pretty_html(Template(template).render(context)),
    )


@override_settings(LANGUAGE_CODE="en_US", LANGUAGES=(('en', 'English'),))
class SimpleTestCase(BaseTestCase):
    pass
