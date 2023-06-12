# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class CheckboxSetTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% CheckboxSet form1.choice %}
"""
        expected = """
<fieldset class="nj-checkbox-group">
  <legend class="nj-checkbox-group__legend">Choice label</legend>
  <div class="nj-checkbox">
    <label for="id_choice-1">
      <input id="id_choice-1" name="choice" type="checkbox" value="val1"
        checked/>
      Wonderful choice
    </label>
  </div>
  <div class="nj-checkbox">
    <label for="id_choice-2">
      <input id="id_choice-2" name="choice" type="checkbox" value="val2"/>
      Neutral choice
    </label>
  </div>
  <div class="nj-checkbox">
    <label for="id_choice-3">
      <input id="id_choice-3" name="choice" type="checkbox" value="val3"/>
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
  {% CheckboxSet form1.choice id="id_choice1" %}
</form>
<form>
  {% CheckboxSet form2.choice id="id_choice2" %}
</form>
"""
        expected = """
<form>
  <fieldset class="nj-checkbox-group">
    <legend class="nj-checkbox-group__legend">Choice label</legend>
    <div class="nj-checkbox">
      <label for="id_choice1-1">
        <input id="id_choice1-1" name="choice" type="checkbox" value="val1" checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-checkbox">
      <label for="id_choice1-2">
        <input id="id_choice1-2" name="choice" type="checkbox" value="val2">
        Neutral choice
      </label>
    </div>
    <div class="nj-checkbox">
      <label for="id_choice1-3">
        <input id="id_choice1-3" name="choice" type="checkbox" value="val3">
        Bad choice
      </label>
    </div>
  </fieldset>
</form>
<form>
  <fieldset class="nj-checkbox-group">
    <legend class="nj-checkbox-group__legend">Choice label</legend>
    <div class="nj-checkbox">
      <label for="id_choice2-1">
        <input id="id_choice2-1" name="choice" type="checkbox" value="val1"
          checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-checkbox">
      <label for="id_choice2-2">
        <input id="id_choice2-2" name="choice" type="checkbox" value="val2">
        Neutral choice
      </label>
    </div>
    <div class="nj-checkbox">
      <label for="id_choice2-3">
        <input id="id_choice2-3" name="choice" type="checkbox" value="val3" checked>
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
  {% CheckboxSet form1.choice id="id_choice1" exclude="val2;val3" %}
</form>
<form>
  {% CheckboxSet form2.choice id="id_choice2" exclude="val2;val3" style="display: flex; flex-direction: column; gap: var(--nj-size-space-8);" %}
</form>
"""
        expected = """
<form>
  <fieldset class="nj-checkbox-group">
    <legend class="nj-checkbox-group__legend">Choice label</legend>
    <div class="nj-checkbox">
      <label for="id_choice1-1">
        <input name="choice" value="val1" type="checkbox" id="id_choice1-1" checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-checkbox nj-checkbox--disabled">
      <label for="id_choice1-2">
        <input name="choice" value="val2" type="checkbox" id="id_choice1-2" disabled>
        Neutral choice
      </label>
    </div>
    <div class="nj-checkbox nj-checkbox--disabled">
      <label for="id_choice1-3">
        <input name="choice" value="val3" type="checkbox" id="id_choice1-3" disabled>
        Bad choice
      </label>
    </div>
  </div>
</form>
<form>
  <fieldset class="nj-checkbox-group"
      style="display: flex; flex-direction: column; gap: var(--nj-size-space-8);">
    <legend class="nj-checkbox-group__legend">Choice label</legend>
    <div class="nj-checkbox">
      <label for="id_choice2-1">
        <input name="choice" value="val1" type="checkbox" id="id_choice2-1" checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-checkbox nj-checkbox--disabled">
      <label for="id_choice2-2">
        <input name="choice" value="val2" type="checkbox" disabled id="id_choice2-2">
        Neutral choice
      </label>
    </div>
    <div class="nj-checkbox nj-checkbox--disabled">
      <label for="id_choice2-3">
        <input name="choice" value="val3" type="checkbox" checked disabled id="id_choice2-3">
        Bad choice
      </label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<form>
  {% CheckboxSet form1.choice id="id_choice1" inline=True exclude="val3" %}
</form>
<form>
  {% CheckboxSet form2.choice id="id_choice2" inline=True exclude="val3" %}
</form>
"""
        expected = """
<form>
  <fieldset class="nj-checkbox-group">
    <legend class="nj-checkbox-group__legend">Choice label</legend>
    <div class="nj-checkbox nj-checkbox--inline">
      <label for="id_choice1-1">
        <input name="choice" value="val1" type="checkbox" id="id_choice1-1"
          checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-checkbox nj-checkbox--inline">
      <label for="id_choice1-2">
        <input name="choice" value="val2" type="checkbox" id="id_choice1-2">
        Neutral choice
      </label>
    </div>
    <div class="nj-checkbox nj-checkbox--inline nj-checkbox--disabled">
      <label for="id_choice1-3">
        <input name="choice" value="val3" type="checkbox" id="id_choice1-3" disabled>
        Bad choice
      </label>
    </div>
  </fieldset>
</form>
<form>
  <fieldset class="nj-checkbox-group">
    <legend class="nj-checkbox-group__legend">Choice label</legend>
    <div class="nj-checkbox nj-checkbox--inline">
      <label for="id_choice2-1">
        <input name="choice" value="val1" type="checkbox" id="id_choice2-1"
          checked>
        Wonderful choice
      </label>
    </div>
    <div class="nj-checkbox nj-checkbox--inline">
      <label for="id_choice2-2">
        <input name="choice" value="val2" type="checkbox" id="id_choice2-2">
        Neutral choice
      </label>
    </div>
    <div class="nj-checkbox nj-checkbox--inline nj-checkbox--disabled">
      <label for="id_choice2-3">
        <input name="choice" value="val3" type="checkbox" id="id_choice2-3" disabled checked>
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
  {% CheckboxSet form1.choice_missing id="id_choice" %}
</form>
"""
        expected = """
<form>
  <fieldset class="nj-checkbox-group">
    <legend class="nj-checkbox-group__legend">
      Choice missing
      <span id="id_choice-errors" class="nj-checkbox__error">
        This field is required.
      </span>
    </legend>
    <div class="nj-checkbox">
      <label for="id_choice-1">
        <input name="choice_missing" value="val1" type="checkbox"
            id="id_choice-1" aria-invalid="true"
            aria-describedby="id_choice-errors">
        Value One
      </label>
    </div>
    <div class="nj-checkbox">
      <label for="id_choice-2">
        <input name="choice_missing" value="val2" type="checkbox"
            id="id_choice-2" aria-invalid="true"
            aria-describedby="id_choice-errors">
        Value Two
      </label>
    </div>
  </fieldset>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
