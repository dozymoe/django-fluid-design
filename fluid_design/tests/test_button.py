# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ButtonTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Button %}{% endButton %}
"""
        expected = """
<button class="nj-btn">
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_primary(self):
        template = """
{% load fluid_design %}
{% Button type="button" %}Bold{% endButton %}
{% Button type="button" variant="subtle" %}Subtle{% endButton %}
{% Button type="button" variant="minimal" %}Minimal{% endButton %}
"""
        expected = """
<button type="button" class="nj-btn">Bold</button>
<button type="button" class="nj-btn nj-btn--subtle">Subtle</button>
<button type="button" class="nj-btn nj-btn--minimal">Minimal</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_secondary(self):
        template = """
{% load fluid_design %}
{% Button type="button" color="secondary" %}Bold{% endButton %}
{% Button type="button" color="secondary" variant="subtle" %}
  Subtle
{% endButton %}
{% Button type="button" color="secondary" variant="minimal" %}
  Minimal
{% endButton %}
"""
        expected = """
<button type="button" class="nj-btn nj-btn--secondary">Bold</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--secondary">Subtle</button>
<button type="button" class="nj-btn nj-btn--minimal nj-btn--secondary">Minimal</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_destructive(self):
        template = """
{% load fluid_design %}
{% Button type="button" color="destructive" %}Bold{% endButton %}
{% Button type="button" color="destructive" variant="subtle" %}
  Subtle
{% endButton %}
{% Button type="button" color="destructive" variant="minimal" %}
  Minimal
{% endButton %}
"""
        expected = """
<button type="button" class="nj-btn nj-btn--destructive">Bold</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive">Subtle</button>
<button type="button" class="nj-btn nj-btn--minimal nj-btn--destructive">Minimal</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_inverse(self):
        template = """
{% load fluid_design %}
{% Button type="button" color="inverse" %}Bold{% endButton %}
{% Button type="button" color="inverse" variant="subtle" %}
  Subtle
{% endButton %}
{% Button type="button" color="inverse" variant="minimal" %}
  Minimal
{% endButton %}
"""
        expected = """
<button type="button" class="nj-btn nj-btn--inverse">Bold</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--inverse">Subtle</button>
<button type="button" class="nj-btn nj-btn--minimal nj-btn--inverse">Minimal</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_size_variations(self):
        template = """
{% load fluid_design %}
{% Button type="button" size="xs" %}Button XS{% endButton %}
{% Button type="button" size="sm" %}Button SM{% endButton %}
{% Button type="button" %}Button normal{% endButton %}
{% Button type="button" size="lg" %}Button LG{% endButton %}
"""
        expected = """
<button type="button" class="nj-btn nj-btn--xs">Button XS</button>
<button type="button" class="nj-btn nj-btn--sm">Button SM</button>
<button type="button" class="nj-btn">Button normal</button>
<button type="button" class="nj-btn nj-btn--lg ">Button LG</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_tags(self):
        template = """
{% load fluid_design %}
{% Button astag="a" href="#" role="button" %}Link{% endButton %}
{% Button type="submit" %}Button{% endButton %}
{% Button astag="input" type="button" value="Input" %}{% endButton %}
{% Button astag="input" type="submit" value="Submit" %}{% endButton %}
{% Button astag="input" type="reset" value="Reset" %}{% endButton %}
"""
        expected = """
<a class="nj-btn" href="#" role="button">Link</a>
<button class="nj-btn" type="submit">Button</button>
<input class="nj-btn" type="button" value="Input">
<input class="nj-btn" type="submit" value="Submit">
<input class="nj-btn" type="reset" value="Reset">
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_with_text_icon(self):
        template = """
{% load fluid_design %}
<div class="my-3 story-btn-row">
  {% Button type="button" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" variant="subtle" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" variant="minimal" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
</div>
<div class="my-3 story-btn-row">
  {% Button type="button" color="secondary" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" color="secondary" variant="subtle" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" color="secondary" variant="minimal" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
</div>
<div class="my-3 story-btn-row">
  {% Button type="button" color="destructive" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" color="destructive" variant="subtle" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" color="destructive" variant="minimal" %}
    Button
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
</div>
<div class="my-3" style="background-color: var(--nj-color-palette-ultramarine-800)">
  <div class="p-2 story-btn-row">
    {% Button type="button" color="inverse" %}
      Button
      {% Slot 'icon' %}
        <span aria-hidden="true"
            class="nj-btn__icon nj-btn__icon--before material-icons">
          get_app
        </span>
      {% endSlot %}
    {% endButton %}
    {% Button type="button" color="inverse" variant="subtle" %}
      Button
      {% Slot 'icon' %}
        <span aria-hidden="true"
            class="nj-btn__icon nj-btn__icon--before material-icons">
          get_app
        </span>
      {% endSlot %}
    {% endButton %}
    {% Button type="button" color="inverse" variant="minimal" %}
      Button
      {% Slot 'icon' %}
        <span aria-hidden="true"
            class="nj-btn__icon nj-btn__icon--before material-icons">
          get_app
        </span>
      {% endSlot %}
    {% endButton %}
  </div>
</div>
"""
        expected = """
<div class="my-3 story-btn-row">
  <button type="button" class="nj-btn">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
  <button type="button" class="nj-btn nj-btn--subtle">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
  <button type="button" class="nj-btn nj-btn--minimal">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
</div>
<div class="my-3 story-btn-row">
  <button type="button" class="nj-btn nj-btn--secondary">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
  <button type="button" class="nj-btn nj-btn--subtle nj-btn--secondary">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
  <button type="button" class="nj-btn nj-btn--minimal nj-btn--secondary">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
</div>
<div class="my-3 story-btn-row">
  <button type="button" class="nj-btn nj-btn--destructive">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
  <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
  <button type="button" class="nj-btn nj-btn--minimal nj-btn--destructive">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    Button
  </button>
</div>
<div class="my-3" style="background-color: var(--nj-color-palette-ultramarine-800)">
  <div class="p-2 story-btn-row">
    <button type="button" class="nj-btn nj-btn--inverse">
      <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
      Button
    </button>
    <button type="button" class="nj-btn nj-btn--subtle nj-btn--inverse">
      <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
      Button
    </button>
    <button type="button" class="nj-btn nj-btn--minimal nj-btn--inverse">
      <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
      Button
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_only_icon(self):
        template = """
{% load fluid_design %}
<div class="my-3 story-btn-row">
  {% Button type="button" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" variant="subtle" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" variant="minimal" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
</div>
<div class="my-3 story-btn-row">
  {% Button type="button" color="secondary" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" color="secondary" variant="subtle" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" color="secondary" variant="minimal" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
</div>
<div class="my-3 story-btn-row">
  {% Button type="button" color="destructive" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" color="destructive" variant="subtle" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
  {% Button type="button" color="destructive" variant="minimal" %}
    {% Slot 'icon' %}
      <span aria-hidden="true"
          class="nj-btn__icon nj-btn__icon--before material-icons">
        get_app
      </span>
    {% endSlot %}
  {% endButton %}
</div>
<div class="my-3" style="background-color: var(--nj-color-palette-ultramarine-800)">
  <div class="p-2 story-btn-row">
    {% Button type="button" color="inverse" %}
      {% Slot 'icon' %}
        <span aria-hidden="true"
            class="nj-btn__icon nj-btn__icon--before material-icons">
          get_app
        </span>
      {% endSlot %}
    {% endButton %}
    {% Button type="button" color="inverse" variant="subtle" %}
      {% Slot 'icon' %}
        <span aria-hidden="true"
            class="nj-btn__icon nj-btn__icon--before material-icons">
          get_app
        </span>
      {% endSlot %}
    {% endButton %}
    {% Button type="button" color="inverse" variant="minimal" %}
      {% Slot 'icon' %}
        <span aria-hidden="true"
            class="nj-btn__icon nj-btn__icon--before material-icons">
          get_app
        </span>
      {% endSlot %}
    {% endButton %}
  </div>
</div>
"""
        expected = """
<div class="my-3 story-btn-row">
  <button type="button" class="nj-btn">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
  <button type="button" class="nj-btn nj-btn--subtle">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
  <button type="button" class="nj-btn nj-btn--minimal">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
</div>
<div class="my-3 story-btn-row">
  <button type="button" class="nj-btn nj-btn--secondary">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
  <button type="button" class="nj-btn nj-btn--subtle nj-btn--secondary">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
  <button type="button" class="nj-btn nj-btn--minimal nj-btn--secondary">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
</div>
<div class="my-3 story-btn-row">
  <button type="button" class="nj-btn nj-btn--destructive">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
  <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
  <button type="button" class="nj-btn nj-btn--minimal nj-btn--destructive">
    <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
  </button>
</div>
<div class="my-3" style="background-color: var(--nj-color-palette-ultramarine-800)">
  <div class="p-2 story-btn-row">
    <button type="button" class="nj-btn nj-btn--inverse">
      <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    </button>
    <button type="button" class="nj-btn nj-btn--subtle nj-btn--inverse">
      <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    </button>
    <button type="button" class="nj-btn nj-btn--minimal nj-btn--inverse">
      <span aria-hidden="true" class="nj-btn__icon nj-btn__icon--before material-icons">get_app</span>
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
