# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class RadioSetTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% RadioSet form1.choice %}
"""
        expected = """
<fieldset class="nj-radio-group">
  <legend class="nj-radio-group__legend">
    Choice label
  </legend>
  <div class="nj-radio">
    <label for="id_choice-1">
      <input name="choice" value="val1" type="radio" id="id_choice-1" checked>
      Wonderful choice
    </label>
  </div>
  <div class="nj-radio">
    <label for="id_choice-2">
      <input name="choice" value="val2" type="radio" id="id_choice-2">
      Neutral choice
    </label>
  </div>
  <div class="nj-radio">
    <label for="id_choice-3">
      <input name="choice" value="val3" type="radio" id="id_choice-3">
      Bad choice
    </label>
  </div>
</fieldset>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<form>
  {% RadioSet form1.choice %}
</form>
"""
        expected = """
<form>
  <fieldset class="nj-radio-group">
    <legend class="nj-radio-group__legend">Choice label</legend>
    <div class="nj-radio">
      <label for="id_choice-1">
        <input name="choice" value="val1" type="radio" id="id_choice-1" checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-radio">
      <label for="id_choice-2">
        <input name="choice" value="val2" type="radio" id="id_choice-2">
        Neutral choice
      </label>
    </div>
    <div class="nj-radio">
      <label for="id_choice-3">
        <input name="choice" value="val3" type="radio" id="id_choice-3">
        Bad choice
      </label>
    </div>
  </fieldset>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<form>
  {% RadioSet form1.choice exclude="val2;val3" %}
</form>
"""
        expected = """
<form>
  <fieldset class="nj-radio-group">
    <legend class="nj-radio-group__legend">Choice label</legend>
    <div class="nj-radio">
      <label for="id_choice-1">
        <input name="choice" value="val1" type="radio" id="id_choice-1" checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-radio nj-radio--disabled">
      <label for="id_choice-2">
        <input name="choice" value="val2" type="radio" id="id_choice-2" disabled>
        Neutral choice
      </label>
    </div>
    <div class="nj-radio nj-radio--disabled">
      <label for="id_choice-3">
        <input name="choice" value="val3" type="radio" id="id_choice-3" disabled>
        Bad choice
      </label>
    </div>
  </fieldset>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<form>
  {% RadioSet form1.choice exclude="val3" inline=True %}
</form>
"""
        expected = """
<form>
  <fieldset class="nj-radio-group nj-radio-group--row">
    <legend class="nj-radio-group__legend">Choice label</legend>
    <div class="nj-radio">
      <label for="id_choice-1">
        <input name="choice" value="val1" type="radio" id="id_choice-1" checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-radio">
      <label for="id_choice-2">
        <input name="choice" value="val2" type="radio" id="id_choice-2">
        Neutral choice
      </label>
    </div>
    <div class="nj-radio nj-radio--disabled">
      <label for="id_choice-3">
        <input name="choice" value="val3" type="radio" id="id_choice-3" disabled>
        Bad choice
      </label>
    </div>
  </fieldset>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<form>
  {% RadioSet form1.choice_missing inline=True %}
</form>
"""
        expected = """
<form>
  <fieldset class="nj-radio-group has-danger nj-radio-group--row">
    <legend class="nj-radio-group__legend">
      Choice missing
      <span id="id_choice_missing-errors" class="nj-radio-group__error">
        This field is required.
      </span>
    </legend>
    <div class="nj-radio">
      <label for="id_choice_missing-1">
        <input name="choice_missing" value="val1" type="radio"
            id="id_choice_missing-1" aria-invalid="true"
            aria-describedby="id_choice_missing-errors">
        Value One
      </label>
    </div>
    <div class="nj-radio">
      <label for="id_choice_missing-2">
        <input name="choice_missing" value="val2" type="radio"
            id="id_choice_missing-2" aria-invalid="true"
            aria-describedby="id_choice_missing-errors">
        Value Two
      </label>
    </div>
  </fieldset>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
