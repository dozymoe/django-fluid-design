# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
#-
from .base import compare_template, SimpleTestCase

class ToggleForm(forms.Form):
    toggle1 = forms.BooleanField(
            required=False,
            label="Label")


class ToggleTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Toggle form.toggle1 %}
"""
        expected = """
<div class="nj-toggle">
  <label for="id_toggle1">
   <input class="" id="id_toggle1" name="toggle1" role="switch" type="checkbox"/>
   <span class="nj-toggle__track">
   </span>
   <span>
    Label
   </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<form>
  {% Toggle form.toggle1 id="toggle1" %}
</form>
"""
        expected = """
<form>
  <div class="nj-toggle">
    <label for="toggle1">
      <input name="toggle1" type="checkbox" id="toggle1" role="switch" class="">
      <span class="nj-toggle__track"></span>
      <span>Label</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  {% Toggle form.toggle1 id="toggle2" %}
  {% Toggle form.toggle1 id="toggle3" size="lg" %}
</form>
"""
        expected = """
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  <div class="nj-toggle">
    <label for="toggle2">
      <input name="toggle1" class="" type="checkbox" id="toggle2" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Label</span>
    </label>
  </div>
  <div class="nj-toggle nj-toggle--lg">
    <label for="toggle3">
      <input name="toggle1" class="" type="checkbox" id="toggle3" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Label</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  {% Toggle form1.toggle1 label="Disabled" id="toggle4" disabled=True %}
  {% Toggle form2.toggle1 label="Checked disabled" id="toggle5" disabled=True %}
</form>
"""
        expected = """
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  <div class="nj-toggle nj-toggle--disabled">
    <label for="toggle4">
      <input name="toggle1" class="" type="checkbox" disabled id="toggle4" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Disabled</span>
    </label>
  </div>
  <div class="nj-toggle nj-toggle--disabled">
    <label for="toggle5">
      <input name="toggle1" class="" type="checkbox" checked disabled id="toggle5" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Checked disabled</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form1=ToggleForm(),
                form2=ToggleForm(data={'toggle1': True}))
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<form>
  {% Toggle form.toggle1 id="toggle6" label="Dark mode" darkmode=True %}
</form>
"""
        expected = """
<form>
<div class="nj-toggle" title="Dark mode">
  <label for="toggle6">
    <input name="toggle1" class="" type="checkbox" id="toggle6" role="switch">
    <span class="nj-toggle__track"></span>
    <svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="nj-toggle__icon">
      <path
        d="M9.53 16h-.48a8 8 0 01-7.4-8.47A7.94 7.94 0 019.52 0h.94l-.64.6a7.71 7.71 0 00-2.06 8 7.6 7.6 0 006.3 5.23l.87.1-.7.52A7.77 7.77 0 019.53 16zM8.71.74a7.31 7.31 0 00.38 14.54 7.06 7.06 0 004-.94 8.35 8.35 0 01-6-5.55A8.48 8.48 0 018.71.74z"/>
    </svg>
    <span class="nj-sr-only">Dark mode</span>
  </label>
</div>
</form>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  {% Toggle form.toggle1 id="toggle7" %}
  {% Toggle form.toggle1 id="toggle8" label="Enable sound" icon="volume_up" %}
</div>
"""
        expected = """
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  <div class="nj-toggle">
    <label for="toggle7">
      <input name="toggle1" class="" type="checkbox" id="toggle7" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Label</span>
    </label>
  </div>
  <div class="nj-toggle" title="Enable sound">
    <label for="toggle8">
      <input name="toggle1" class="" type="checkbox" id="toggle8" role="switch">
      <span class="nj-toggle__track"></span>
      <span aria-hidden="true" class="nj-toggle__icon material-icons">volume_up</span>
      <span class="nj-sr-only">Enable sound</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<form>
  {% Toggle form.toggle1 id="toggle1" %}
</form>
"""
        expected = """
<form>
  <div class="nj-toggle">
    <label for="toggle1">
      <input name="toggle1" class="" type="checkbox" id="toggle1" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Label</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  {% Toggle form.toggle1 id="toggle2" %}
  {% Toggle form.toggle1 id="toggle3" size="lg" %}
</form>
"""
        expected = """
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  <div class="nj-toggle">
    <label for="toggle2">
      <input name="toggle1" class="" type="checkbox" id="toggle2" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Label</span>
    </label>
  </div>
  <div class="nj-toggle nj-toggle--lg">
    <label for="toggle3">
      <input name="toggle1" class="" type="checkbox" id="toggle3" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Label</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  {% Toggle form.toggle1 id="toggle7" label="Off" %}
  {% Toggle form.toggle1 id="toggle8" icon="volume_up" label="Enable sound" %}
</form>
"""
        expected = """
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  <div class="nj-toggle">
    <label for="toggle7">
      <input name="toggle1" class="" type="checkbox" id="toggle7" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Off</span>
    </label>
  </div>
  <div class="nj-toggle" title="Enable sound">
    <label for="toggle8">
      <input name="toggle1" class="" type="checkbox" id="toggle8" role="switch">
      <span class="nj-toggle__track"></span>
      <span aria-hidden="true" class="nj-toggle__icon material-icons">volume_up</span>
      <span class="nj-sr-only">Enable sound</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  {% Toggle form1.toggle1 id="toggle4" label="Disabled" disabled=True %}
  {% Toggle form2.toggle1 id="toggle5" label="Checked disabled" disabled=True %}
</form>
"""
        expected = """
<form style="display: flex; align-items: center; gap: var(--nj-size-space-16)">
  <div class="nj-toggle nj-toggle--disabled">
    <label for="toggle4">
      <input name="toggle1" class="" type="checkbox" disabled id="toggle4" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Disabled</span>
  </label>
  </div>
  <div class="nj-toggle nj-toggle--disabled">
    <label for="toggle5">
      <input name="toggle1" class="" type="checkbox" checked disabled id="toggle5" role="switch">
      <span class="nj-toggle__track"></span>
      <span>Checked disabled</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form1=ToggleForm(),
                form2=ToggleForm(data={'toggle1': True}))
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
<form>
  {% Toggle form.toggle1 id="toggle6" darkmode=True label="Dark mode" %}
</form>
"""
        expected = """
<form>
  <div class="nj-toggle" title="Dark mode">
    <label for="toggle6">
      <input name="toggle1" class="" type="checkbox" id="toggle6" role="switch">
      <span class="nj-toggle__track"></span>
      <svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="nj-toggle__icon">
        <path
          d="M9.53 16h-.48a8 8 0 01-7.4-8.47A7.94 7.94 0 019.52 0h.94l-.64.6a7.71 7.71 0 00-2.06 8 7.6 7.6 0 006.3 5.23l.87.1-.7.52A7.77 7.77 0 019.53 16zM8.71.74a7.31 7.31 0 00.38 14.54 7.06 7.06 0 004-.94 8.35 8.35 0 01-6-5.55A8.48 8.48 0 018.71.74z"/>
      </svg>
      <span class="nj-sr-only">Dark mode</span>
    </label>
  </div>
</form>
"""
        rendered = compare_template(template, expected, form=ToggleForm())
        self.assertEqual(*rendered)
