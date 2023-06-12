# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class BreadcrumbTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Breadcrumb %}{% endBreadcrumb %}
"""
        expected = """
<nav aria-label="breadcrumb">
  <ol class="nj-breadcrumb">
  </ol>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Breadcrumb %}
  {% BreadcrumbItem current=True %}Home{% endBreadcrumbItem %}
{% endBreadcrumb %}
"""
        expected = """
<nav aria-label="breadcrumb">
  <ol class="nj-breadcrumb">
    <li class="nj-breadcrumb__item" aria-current="page">Home</li>
  </ol>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% Breadcrumb %}
  {% BreadcrumbItem %}Home{% endBreadcrumbItem %}
  {% BreadcrumbItem current=True %}Library{% endBreadcrumbItem %}
{% endBreadcrumb %}
"""
        expected = """
<nav aria-label="breadcrumb">
  <ol class="nj-breadcrumb">
    <li class="nj-breadcrumb__item"><a href="#" class="nj-link nj-link--sm nj-link--grayed">Home</a></li>
    <li class="nj-breadcrumb__item" aria-current="page">Library</li>
  </ol>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% Breadcrumb %}
  {% BreadcrumbItem %}Home{% endBreadcrumbItem %}
  {% BreadcrumbItem %}Library{% endBreadcrumbItem %}
  {% BreadcrumbItem current=True %}Data{% endBreadcrumbItem %}
{% endBreadcrumb %}
"""
        expected = """
<nav aria-label="breadcrumb">
  <ol class="nj-breadcrumb">
    <li class="nj-breadcrumb__item"><a href="#" class="nj-link nj-link--sm nj-link--grayed">Home</a></li>
    <li class="nj-breadcrumb__item"><a href="#" class="nj-link nj-link--sm nj-link--grayed">Library</a></li>
    <li class="nj-breadcrumb__item" aria-current="page">Data</li>
  </ol>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_with_icon(self):
        template = """
{% load fluid_design %}
{% Breadcrumb %}
  {% BreadcrumbItem isicon=True %}
    <span aria-hidden="true" class="material-icons">home</span>
  {% endBreadcrumbItem %}
  {% BreadcrumbItem %}Library{% endBreadcrumbItem %}
  {% BreadcrumbItem current=True %}Data{% endBreadcrumbItem %}
{% endBreadcrumb %}
"""
        expected = """
<nav aria-label="breadcrumb">
  <ol class="nj-breadcrumb">
    <li class="nj-breadcrumb__item"><a href="#" class="nj-link nj-link--sm nj-link--grayed nj-link-icon"><span aria-hidden="true" class="material-icons">home</span></a></li>
    <li class="nj-breadcrumb__item"><a href="#" class="nj-link nj-link--sm nj-link--grayed">Library</a></li>
    <li class="nj-breadcrumb__item" aria-current="page">Data</li>
  </ol>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
