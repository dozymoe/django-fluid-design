# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class LinkTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Link %}{% endLink %}
"""
        expected = """
<a class="nj-link"></a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Link href="#" %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
  <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" icon_before=True %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" icon_before=True %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
<div style="width:200px">
  {% Link href="#" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.
  {% endLink %}
  <br><br><br>
  {% Link href="#" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" icon_before=True %}
    <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span>

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
</div>
"""
        expected = """
<a href="#" class="nj-link nj-link-icon"><span>Here is a text link</span><span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link-icon">Here is a text link <span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Here is a text link</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link-icon"><span aria-hidden="true" class="material-icons">add</span>Here is a text link</a>
<br><br>
<div style="width:200px">
  <a href="#" class="nj-link">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.</a><br><br><br>
  <a href="#" class="nj-link nj-link-icon">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt <span aria-hidden="true"
    class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span></a><br><br>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="width:200px">
  {% Link href="#" style="bold" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.
  {% endLink %}
  <br><br><br>
  {% Link href="#" style="bold" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="bold" icon_before=True %}
    <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span>

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
</div>
<br><br>
{% Link href="#" style="bold" %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
  <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="bold" %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="bold" icon_before=True %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="bold" icon_before=True %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
"""
        expected = """
<div style="width:200px">
  <a href="#" class="nj-link nj-link--bold">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.</a><br><br><br>
  <a href="#" class="nj-link nj-link--bold nj-link-icon">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt <span aria-hidden="true"
    class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link--bold nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span></a><br><br>
</div>
<br><br>
<a href="#" class="nj-link nj-link--bold nj-link-icon"><span>Here is a text link</span><span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link--bold nj-link-icon">Here is a text link <span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link--bold nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Here is a text link</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link--bold nj-link-icon"><span aria-hidden="true" class="material-icons">add</span>Here is a text link</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% Link href="#" size="sm" %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
  <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" size="sm" %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" size="sm" icon_before=True %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" size="sm" icon_before=True %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
<div style="width:200px">
  {% Link href="#" size="sm" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.
  {% endLink %}
  <br><br><br>
  {% Link href="#" size="sm" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" size="sm" icon_before=True %}
    <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span>

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
</div>
"""
        expected = """
<a href="#" class="nj-link nj-link--sm nj-link-icon"><span>Here is a text link</span><span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link--sm nj-link-icon">Here is a text link <span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Here is a text link</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span>Here is a text link</a>
 <br><br>
<div style="width:200px">
  <a href="#" class="nj-link nj-link--sm">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.</a><br><br><br>
  <a href="#" class="nj-link nj-link--sm nj-link-icon">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt <span aria-hidden="true"
    class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span></a><br><br>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% Link href="#" style="contextual" size="sm" %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
  <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="contextual" size="sm" %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="contextual" size="sm" icon_before=True %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="contextual" size="sm" icon_before=True %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
<div style="width:200px">
  {% Link href="#" style="contextual" size="sm" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.
  {% endLink %}
  <br><br><br>
  {% Link href="#" style="contextual" size="sm" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="contextual" size="sm" icon_before=True %}
    <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span>

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
</div>
"""
        expected = """
<a href="#" class="nj-link nj-link--contextual nj-link--sm nj-link-icon"><span>Here is a text link</span><span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link--contextual nj-link--sm nj-link-icon">Here is a text link <span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link--contextual nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Here is a text link</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link--contextual nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span>Here is a text link</a>
<br><br>
<div style="width:200px">
  <a href="#" class="nj-link nj-link--contextual nj-link--sm">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.</a><br><br><br>
  <a href="#" class="nj-link nj-link--contextual nj-link--sm nj-link-icon">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt <span aria-hidden="true"
    class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link--contextual nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span></a><br><br>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Link href="#" style="grayed" size="sm" %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
  <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="grayed" size="sm" %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">chevron_right</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="grayed" size="sm" icon_before=True %}
  <span>Here is a text link</span>

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
{% Link href="#" style="grayed" size="sm" icon_before=True %}
  Here is a text link

  {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">add</span>
  {% endSlot %}
{% endLink %}
<br><br>
<div style="width:200px">
  {% Link href="#" style="grayed" size="sm" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.
  {% endLink %}
  <br><br><br>
  {% Link href="#" style="grayed" size="sm" %}
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="grayed" size="sm" icon_before=True %}
    <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span>

    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
</div>
"""
        expected = """
<a href="#" class="nj-link nj-link--grayed nj-link--sm nj-link-icon"><span>Here is a text link</span><span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link--grayed nj-link--sm nj-link-icon">Here is a text link <span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link--grayed nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Here is a text link</span></a><br><br>
<a href="#" class="nj-link nj-link-icon--before nj-link--grayed nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span>Here is a text link</a>
<br><br>
<div style="width:200px">
  <a href="#" class="nj-link nj-link--grayed nj-link--sm">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.</a><br><br><br>
  <a href="#" class="nj-link nj-link--grayed nj-link--sm nj-link-icon">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt <span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link--grayed nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span></a><br><br>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<div style="padding: var(--nj-size-space-16); background: var(--nj-color-palette-blue-200)">
  {% Link href="#" style="high-contrast" size="sm" %}
    <span>Here is a text link</span>
  
    {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="high-contrast" size="sm" %}
    Here is a text link
  
    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="high-contrast" size="sm" icon_before=True %}
    <span>Here is a text link</span>
  
    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="high-contrast" size="sm" icon_before=True %}
    Here is a text link
  
    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  <div style="width:200px">
    {% Link href="#" style="high-contrast" size="sm" %}
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.
    {% endLink %}
    <br><br><br>
    {% Link href="#" style="high-contrast" size="sm" %}
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt
  
      {% Slot 'icon' %}
        <span aria-hidden="true" class="material-icons">chevron_right</span>
      {% endSlot %}
    {% endLink %}
    <br><br>
    {% Link href="#" style="high-contrast" size="sm" icon_before=True %}
      <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span>
  
      {% Slot 'icon' %}
        <span aria-hidden="true" class="material-icons">add</span>
      {% endSlot %}
    {% endLink %}
    <br><br>
  </div>
</div>
"""
        expected = """
<div style="padding: var(--nj-size-space-16); background: var(--nj-color-palette-blue-200)">
  <a href="#" class="nj-link nj-link--high-contrast nj-link--sm nj-link-icon"><span>Here is a text link</span><span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link--high-contrast nj-link--sm nj-link-icon">Here is a text link <span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link--high-contrast nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Here is a text link</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link--high-contrast nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span>Here is a text link</a>
  <br><br>
  <div style="width:200px">
    <a href="#" class="nj-link nj-link--high-contrast nj-link--sm">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.</a><br><br><br>
    <a href="#" class="nj-link nj-link--high-contrast nj-link--sm nj-link-icon">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt <span aria-hidden="true"
      class="material-icons">chevron_right</span></a><br><br>
    <a href="#" class="nj-link nj-link-icon--before nj-link--high-contrast nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span></a><br><br>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
<div style="padding: var(--nj-size-space-16); background: var(--nj-color-palette-ultramarine-800)">
  {% Link href="#" style="inverse" size="sm" %}
    <span>Here is a text link</span>
  
    {% Slot 'icon' %}
    <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="inverse" size="sm" %}
    Here is a text link
  
    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">chevron_right</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="inverse" size="sm" icon_before=True %}
    <span>Here is a text link</span>
  
    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  {% Link href="#" style="inverse" size="sm" icon_before=True %}
    Here is a text link
  
    {% Slot 'icon' %}
      <span aria-hidden="true" class="material-icons">add</span>
    {% endSlot %}
  {% endLink %}
  <br><br>
  <div style="width:200px">
    {% Link href="#" style="inverse" size="sm" %}
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.
    {% endLink %}
    <br><br><br>
    {% Link href="#" style="inverse" size="sm" %}
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt
  
      {% Slot 'icon' %}
        <span aria-hidden="true" class="material-icons">chevron_right</span>
      {% endSlot %}
    {% endLink %}
    <br><br>
    {% Link href="#" style="inverse" size="sm" icon_before=True %}
      <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span>
  
      {% Slot 'icon' %}
        <span aria-hidden="true" class="material-icons">add</span>
      {% endSlot %}
    {% endLink %}
    <br><br>
  </div>
</div>
"""
        expected = """
<div style="padding: var(--nj-size-space-16); background: var(--nj-color-palette-ultramarine-800)">
  <a href="#" class="nj-link nj-link--inverse nj-link--sm nj-link-icon"><span>Here is a text link</span><span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link--inverse nj-link--sm nj-link-icon">Here is a text link <span aria-hidden="true" class="material-icons">chevron_right</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link--inverse nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Here is a text link</span></a><br><br>
  <a href="#" class="nj-link nj-link-icon--before nj-link--inverse nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span>Here is a text link</a>
  <br><br>
  <div style="width:200px">
    <a href="#" class="nj-link nj-link--inverse nj-link--sm">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt.</a><br><br><br>
    <a href="#" class="nj-link nj-link--inverse nj-link--sm nj-link-icon">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt <span aria-hidden="true"
      class="material-icons">chevron_right</span></a><br><br>
    <a href="#" class="nj-link nj-link-icon--before nj-link--inverse nj-link--sm nj-link-icon"><span aria-hidden="true" class="material-icons">add</span><span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, incidunt</span></a><br><br>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Link href="#" external=True %}
  External link
{% endLink %}
"""
        expected = """
<a href="#" target="_blank" class="nj-link nj-link-icon">
  External link
  <span class="nj-sr-only">&nbsp;(open in new tab)</span>
  <span aria-hidden="true" class="material-icons">open_in_new</span>
</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
