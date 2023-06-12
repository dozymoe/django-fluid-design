# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class IconButtonTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% IconButton %}{% endIconButton %}
"""
        expected = """
<button class="nj-icon-btn">
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% IconButton type="button" %}
  Some accessible label
  {% Slot 'icon' %}
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
      close
    </span>
  {% endSlot %}
{% endIconButton %}
{% IconButton type="button" disabled=True %}
  Some accessible label
  {% Slot 'icon' %}
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
      close
    </span>
  {% endSlot %}
{% endIconButton %}
"""
        expected = """
<button type="button" class="nj-icon-btn">
  <span class="nj-sr-only">Some accessible label</span>
  <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
</button>

<button type="button" class="nj-icon-btn" disabled>
  <span class="nj-sr-only">Some accessible label</span>
  <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% IconButton type="button" variant="secondary" %}
  {% Slot 'icon' %}
    <i class="nj-icon-btn__icon material-icons">close</i>
  {% endSlot %}
{% endIconButton %}
{% IconButton type="button" variant="secondary" disabled=True %}
  {% Slot 'icon' %}
    <i class="nj-icon-btn__icon material-icons">close</i>
  {% endSlot %}
{% endIconButton %}
"""
        expected = """
<button type="button" class="nj-icon-btn nj-icon-btn--secondary">
  <i class="nj-icon-btn__icon material-icons">close</i>
</button>

<button type="button" class="nj-icon-btn nj-icon-btn--secondary" disabled>
  <i class="nj-icon-btn__icon material-icons">close</i> 
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% IconButton type="button" variant="destructive" %}
  Some accessible label
  {% Slot 'icon' %}
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
      close
    </span>
  {% endSlot %}
{% endIconButton %}
{% IconButton type="button" variant="destructive" disabled=True %}
  Some accessible label
  {% Slot 'icon' %}
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
      close
    </span>
  {% endSlot %}
{% endIconButton %}
"""
        expected = """
<button type="button" class="nj-icon-btn nj-icon-btn--destructive">
  <span class="nj-sr-only">Some accessible label</span>
  <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
</button>

<button type="button" class="nj-icon-btn nj-icon-btn--destructive" disabled>
  <span class="nj-sr-only">Some accessible label</span>
  <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="background-color: var(--nj-color-palette-ultramarine-800); padding: var(--nj-size-space-16);">
  {% IconButton type="button" inversed=True %}
    Some accessible label
    {% Slot 'icon' %}
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        close
      </span>
    {% endSlot %}
  {% endIconButton %}
  {% IconButton type="button" inversed=True disabled=True %}
    Some accessible label
    {% Slot 'icon' %}
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        close
      </span>
    {% endSlot %}
  {% endIconButton %}
</div>
"""
        expected = """
<div style="background-color: var(--nj-color-palette-ultramarine-800); padding: var(--nj-size-space-16);">
  <button type="button" class="nj-icon-btn nj-icon-btn--inverse">
    <span class="nj-sr-only">Some accessible label</span>
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
  </button>
  
  <button type="button" class="nj-icon-btn nj-icon-btn--inverse" disabled>
    <span class="nj-sr-only">Some accessible label</span>
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
  </button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div class="mt-3 story-btn-row" style="display: flex; align-items: center; gap: 16px">
  {% IconButton type="button" size="sm" %}
    Some accessible label
    {% Slot 'icon' %}
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        close
      </span>
    {% endSlot %}
  {% endIconButton %}
  {% IconButton type="button" %}
    Some accessible label
    {% Slot 'icon' %}
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        close
      </span>
    {% endSlot %}
  {% endIconButton %}
  {% IconButton type="button" size="lg" %}
    Some accessible label
    {% Slot 'icon' %}
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        close
      </span>
    {% endSlot %}
  {% endIconButton %}
</div>
"""
        expected = """
<div class="mt-3 story-btn-row" style="display: flex; align-items: center; gap: 16px">
  <button type="button" class="nj-icon-btn nj-icon-btn--sm">
    <span class="nj-sr-only">Some accessible label</span>
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
  </button>

  <button type="button" class="nj-icon-btn">
    <span class="nj-sr-only">Some accessible label</span>
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
  </button>

  <button type="button" class="nj-icon-btn nj-icon-btn--lg">
    <span class="nj-sr-only">Some accessible label</span>
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
  </button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
