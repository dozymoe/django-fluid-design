# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class AutocompleteTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Autocomplete form1.text %}
"""
        expected = """
<p hidden id="id_text-autocomplete-instructions">
  Use the UP / DOWN arrows to navigate within the suggestion list. Press Enter to select an option. On touch devices, use swipe to navigate and double tap to select an option
</p>
<div class="nj-form-item nj-form-item--autocomplete">
  <div class="nj-form-item__field-wrapper">
    <input aria-autocomplete="list" aria-controls="id_text-list" aria-describedby="id_text-autocomplete-instructions" aria-expanded="false" autocomplete="off" class="nj-form-item__field" id="id_text" name="text" required role="combobox" type="text" value="a text"/>
    <label class="nj-form-item__label" for="id_text">
      Text
      <span class="nj-form-item__required-asterisk">*</span>
    </label>
    <ul aria-label="Countries suggestions" class="nj-form-item__list nj-list-group nj-list-group--no-border nj-list-group--sm" hidden="" id="id_text-list" role="listbox" tabindex="-1">
      <li aria-selected="false" class="nj-list-group__item nj-list-group__item--clickable" role="option" tabindex="-1">
      </li>
    </ul>
    <span aria-hidden="true" class="nj-form-item__icon material-icons">
      keyboard_arrow_down
    </span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
