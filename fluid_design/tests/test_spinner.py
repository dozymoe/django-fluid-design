# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class SpinnerTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Spinner %}
"""
        expected = """
<div aria-atomic="true" aria-live="polite" class="nj-spinner">
  <p class="nj-sr-only">
   Loading...
  </p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Spinner %}
{% Spinner size="md" %}
{% Spinner size="sm" %}
{% Spinner size="xs" %}
{% Spinner size="xxs" %}
"""
        expected = """
<div aria-live="polite" aria-atomic="true" class="nj-spinner">
  <p class="nj-sr-only">Loading...</p>
</div>

<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--md">
  <p class="nj-sr-only">Loading...</p>
</div>

<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--sm">
  <p class="nj-sr-only">Loading...</p>
</div>

<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--xs">
  <p class="nj-sr-only">Loading...</p>
</div>

<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--xxs">
  <p class="nj-sr-only">Loading...</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: inline-block; padding: var(--nj-size-space-8);
           margin-bottom: var(--nj-size-space-8);  margin-right: var(--nj-size-space-16);
           background: var(--nj-color-palette-ultramarine-800)">
  {% Spinner color="inverse" %}
</div>
{% Spinner color="grey" %}
"""
        expected = """
<div style="display: inline-block; padding: var(--nj-size-space-8);
           margin-bottom: var(--nj-size-space-8);  margin-right: var(--nj-size-space-16);
           background: var(--nj-color-palette-ultramarine-800)">
  <div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--inverse">
    <p class="nj-sr-only">Loading...</p>
  </div>
</div>
  <div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--grey">
    <p class="nj-sr-only">Loading...</p>
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% Button type="button" style="margin-right: var(--nj-size-space-16)" %}
  Submit
  {% Spinner astag="span" color="inverse" size="xs" class="ml-1" %}
{% endButton %}
{% Button type="button" disabled=True %}
  Submit
  {% Spinner astag="span" color="inverse" size="xs" class="ml-1" %}
{% endButton %}
"""
        expected = """
<button type="button" class="nj-btn" style="margin-right: var(--nj-size-space-16)">
  Submit
  <span aria-live="polite" aria-atomic="true" class="nj-spinner ml-1 nj-spinner--inverse nj-spinner--xs">
    <span class="nj-sr-only">Loading...</span>
  </span>
</button>
<button type="button" class="nj-btn" disabled>
  Submit
  <span aria-live="polite" aria-atomic="true" class="nj-spinner ml-1 nj-spinner--inverse nj-spinner--xs">
    <span class="nj-sr-only">Loading...</span>
  </span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% Spinner %}
"""
        expected = """
<div aria-live="polite" aria-atomic="true" class="nj-spinner">
  <p class="nj-sr-only">Loading...</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div style="display: inline-block; padding: var(--nj-size-space-16); background: var(--nj-color-palette-ultramarine-800); margin-right: var(--nj-size-space-32);">
  {% Spinner color="inverse" %}
</div>
{% Spinner color="grey" %}
"""
        expected = """
<div style="display: inline-block; padding: var(--nj-size-space-16); background: var(--nj-color-palette-ultramarine-800); margin-right: var(--nj-size-space-32);">
  <div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--inverse">
    <p class="nj-sr-only">Loading...</p>
  </div>
</div>
  
<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--grey">
  <p class="nj-sr-only">Loading...</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Spinner %}
{% Spinner size="md" %}
{% Spinner size="sm" %}
{% Spinner size="xs" %}
{% Spinner size="xxs" %}
"""
        expected = """
<div aria-live="polite" aria-atomic="true" class="nj-spinner">
  <p class="nj-sr-only">Loading...</p>
</div>

<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--md">
  <p class="nj-sr-only">Loading...</p>
</div>

<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--sm">
  <p class="nj-sr-only">Loading...</p>
</div>

<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--xs">
  <p class="nj-sr-only">Loading...</p>
</div>

<div aria-live="polite" aria-atomic="true" class="nj-spinner nj-spinner--xxs">
  <p class="nj-sr-only">Loading...</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Button type="button" class="mr-3" %}
  Submit
  {% Spinner astag="span" color="inverse" size="xs" class="ml-1" %}
{% endButton %}
{% Button type="button" disabled=True %}
  Submit
  {% Spinner astag="span" size="xs" class="ml-1" %}
{% endButton %}
"""
        expected = """
<button type="button" class="nj-btn mr-3">
  Submit
  <span aria-live="polite" aria-atomic="true" class="nj-spinner ml-1 nj-spinner--inverse nj-spinner--xs">
    <span class="nj-sr-only">Loading...</span>
  </span>
</button>
<button type="button" class="nj-btn" disabled>
  Submit
  <span aria-live="polite" aria-atomic="true" class="nj-spinner ml-1 nj-spinner--xs">
    <span class="nj-sr-only">Loading...</span>
  </span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
