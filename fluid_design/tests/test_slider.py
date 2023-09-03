# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
#-
from .base import compare_template, SimpleTestCase

class SliderForm(forms.Form):
    slider = forms.IntegerField(
            required=False,
            label="Slider label")
    slider_disabled = forms.IntegerField(
            required=False,
            label="Slider Disabled",
            validators=[MaxValueValidator(100), MinValueValidator(1)])


class SliderTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Slider form1.number %}
"""
        expected = """
<div class="nj-slider">
  <label class="" for="id_number">
   Number
  </label>
  <input class="" id="id_number" name="number" type="range" value="0"/>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<form>
  {% Slider form.slider id="formControlSlider" min="0" max=10 step=".1" %}
  {% Slider form.slider_disabled min=1 max=100 id="formControlSlider2" disabled=True %}
</form>
"""
        expected = """
<form>
  <div class="nj-slider">
    <label for="formControlSlider" class="">Slider label</label>
    <input name="slider" min="0" type="range" value="2" max="10" step=".1" id="formControlSlider" class="">
  </div>
  <div class="nj-slider nj-slider--disabled">
    <label for="formControlSlider2" class="">Slider Disabled</label>
    <input name="slider_disabled" min="1" max="100" type="range" value="25" id="formControlSlider2" disabled class="">
  </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected,
                form=SliderForm(data={'slider': 2, 'slider_disabled': 25}))
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<form>
  {% Slider form.slider id="formControlSlider3" min=15 tooltip=True %}
  {% Slider form.slider id="formControlSlider4" min=1 max=100 tooltip=True %}
</form>
"""
        expected = """
<form>
  <div class="nj-slider" data-tooltip="true">
    <label for="formControlSlider3" class="">Slider label</label>
    <input name="slider" min="15" type="range" value="25" id="formControlSlider3" class="">
  </div>
  <div class="nj-slider" data-tooltip="true">
    <label for="formControlSlider4" class="">Slider label</label>
    <input name="slider" min="1" max="100" type="range" value="25" id="formControlSlider4" class="">
  </div>
</form>
"""
        rendered = compare_template(template, expected,
                form=SliderForm(data={'slider': 25}))
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<form>
  {% Slider form.slider id="formControlSlider" min="0" max=10 step=".1" %}
</form>
"""
        expected = """
<form>
  <div class="nj-slider">
    <label for="formControlSlider" class="">Slider label</label>
    <input name="slider" min="0" type="range" value="2" max="10" step=".1" id="formControlSlider" class="">
  </div>
</form>
"""
        rendered = compare_template(template, expected,
                form=SliderForm(data={'slider': 2}))
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<form>
  {% Row %}
    {% Col md=4 %}
      {% Slider form.slider id="formControlSlider3" min=15 max=100 tooltip=True %}
    {% endCol %}
    {% Col md=8 %}
      {% Slider form.slider id="formControlSlider4" min=1 max=100 tooltip=True %}
    {% endCol %}
  {% endRow %}
</form>
"""
        expected = """
<form>
  <div class="row">
    <div class="col-md-4">
      <div class="nj-slider" data-tooltip="true">
        <label for="formControlSlider3" class="">Slider label</label>
        <input name="slider" min="15" max="100" type="range" value="25" id="formControlSlider3" class="">
      </div>
    </div>
    <div class="col-md-8">
      <div class="nj-slider" data-tooltip="true">
        <label for="formControlSlider4" class="">Slider label</label>
        <input name="slider" min="1" max="100" type="range" value="25" id="formControlSlider4" class="">
      </div>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected,
                form=SliderForm(data={'slider': 25}))
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<form>
  {% Slider form.slider_disabled min=1 max=100 id="formControlSlider2" disabled=True %}
</form>
"""
        expected = """
<form>
  <div class="nj-slider nj-slider--disabled">
    <label for="formControlSlider2" class="">Slider Disabled</label>
    <input name="slider_disabled" min="1" max="100" type="range" value="25" id="formControlSlider2" disabled class="">
  </div>
</form>
"""
        rendered = compare_template(template, expected,
                form=SliderForm(data={'slider_disabled': 25}))
        self.assertEqual(*rendered)
