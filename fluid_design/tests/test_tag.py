# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TagTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Tag %}{% endTag %}
"""
        expected = """
<div class="nj-tag">
  <span class="nj-tag__text"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
  {% Tag inversed=True %}tag{% endTag %}
  {% Tag inversed=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag href="#" delete=True inversed=True %}XXX{% endTag %}
  {% Tag href="#" delete=True inversed=True %}
    XXX

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag disabled=True inversed=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
</div>
"""
        expected = """
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag">
      <span class="nj-tag__text">tag</span>
    </div>
    <div class="nj-tag">
      <span class="nj-tag__text">tag</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">tag</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
  <h5 style="margin: 0">SM:</h5>
  {% Tag size="sm" inversed=True %}tag{% endTag %}
  {% Tag size="sm" inversed=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag href="#" delete=True size="sm" inversed=True %}XXX{% endTag %}
  {% Tag href="#" delete=True size="sm" inversed=True %}
    XXX

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag disabled=True size="sm" inversed=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
</div>
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8); margin-top: var(--nj-size-space-24);">
  <h5 style="margin: 0">MD (Default):</h5>
  {% Tag inversed=True %}tag{% endTag %}
  {% Tag inversed=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag href="#" delete=True inversed=True %}XXX{% endTag %}
  {% Tag href="#" delete=True inversed=True %}
    XXX

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag disabled=True inversed=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
</div>
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8); margin-top: var(--nj-size-space-24);">
  <h5 style="margin: 0">LG:</h5>
  {% Tag size="lg" inversed=True %}tag{% endTag %}
  {% Tag size="lg" inversed=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag href="#" delete=True size="lg" inversed=True %}XXX{% endTag %}
  {% Tag href="#" delete=True size="lg" inversed=True %}
    XXX

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag disabled=True size="lg" inversed=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
</div>
"""
        expected = """
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <h5 style="margin: 0">SM:</h5>
    <div class="nj-tag nj-tag--sm">
      <span class="nj-tag__text">tag</span>
    </div>
    <div class="nj-tag nj-tag--sm">
      <span class="nj-tag__text">tag</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--sm">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--sm">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
       <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--sm nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">tag</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
</div>
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8); margin-top: var(--nj-size-space-24);">
    <h5 style="margin: 0">MD (Default):</h5>
    <div class="nj-tag">
      <span class="nj-tag__text">tag</span>
    </div>
    <div class="nj-tag">
      <span class="nj-tag__text">tag</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
       <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">tag</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
</div>
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8); margin-top: var(--nj-size-space-24);">
   <h5 style="margin: 0">LG:</h5>
   <div class="nj-tag nj-tag--lg">
      <span class="nj-tag__text">tag</span>
    </div>
    <div class="nj-tag nj-tag--lg">
      <span class="nj-tag__text">tag</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--lg">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--lg">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
       <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--lg nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">tag</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-24)">
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag inversed=True %}default{% endTag %}
    {% Tag inversed=True %}
      default

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag href="#" delete=True inversed=True %}default{% endTag %}
    {% Tag href="#" delete=True inversed=True %}
      default

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag disabled=True inversed=True %}
      default

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="brand" inversed=True %}brand{% endTag %}
    {% Tag style="brand" inversed=True %}
      brand

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="brand" href="#" delete=True inversed=True %}brand{% endTag %}
    {% Tag style="brand" href="#" delete=True inversed=True %}
      brand

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="brand" disabled=True inversed=True %}
      brand

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="grey" inversed=True %}grey{% endTag %}
    {% Tag style="grey" inversed=True %}
      grey

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="grey" href="#" delete=True inversed=True %}grey{% endTag %}
    {% Tag style="grey" href="#" delete=True inversed=True %}
      grey

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="grey" disabled=True inversed=True %}
      grey

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="teal" inversed=True %}teal{% endTag %}
    {% Tag style="teal" inversed=True %}
      teal

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="teal" href="#" delete=True inversed=True %}teal{% endTag %}
    {% Tag style="teal" href="#" delete=True inversed=True %}
      teal

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="teal" disabled=True inversed=True %}
      teal

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="pink" inversed=True %}pink{% endTag %}
    {% Tag style="pink" inversed=True %}
      pink

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="pink" href="#" delete=True inversed=True %}pink{% endTag %}
    {% Tag style="pink" href="#" delete=True inversed=True %}
      pink

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="pink" disabled=True inversed=True %}
      pink

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="orange" inversed=True %}orange{% endTag %}
    {% Tag style="orange" inversed=True %}
      orange

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="orange" href="#" delete=True inversed=True %}orange{% endTag %}
    {% Tag style="orange" href="#" delete=True inversed=True %}
      orange

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="orange" disabled=True inversed=True %}
      orange

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="red" inversed=True %}red{% endTag %}
    {% Tag style="red" inversed=True %}
      red

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="red" href="#" delete=True inversed=True %}red{% endTag %}
    {% Tag style="red" href="#" delete=True inversed=True %}
      red

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="red" disabled=True inversed=True %}
      red

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="green" inversed=True %}green{% endTag %}
    {% Tag style="green" inversed=True %}
      green

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="green" href="#" delete=True inversed=True %}green{% endTag %}
    {% Tag style="green" href="#" delete=True inversed=True %}
      green

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="green" disabled=True inversed=True %}
      green

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="ultramarine" inversed=True %}ultramarine{% endTag %}
    {% Tag style="ultramarine" inversed=True %}
      ultramarine

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="ultramarine" href="#" delete=True inversed=True %}ultramarine{% endTag %}
    {% Tag style="ultramarine" href="#" delete=True inversed=True %}
      ultramarine

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="ultramarine" disabled=True inversed=True %}
      ultramarine

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="yellow" inversed=True %}yellow{% endTag %}
    {% Tag style="yellow" inversed=True %}
      yellow

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="yellow" href="#" delete=True inversed=True %}yellow{% endTag %}
    {% Tag style="yellow" href="#" delete=True inversed=True %}
      yellow

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="yellow" disabled=True inversed=True %}
      yellow

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="purple" inversed=True %}purple{% endTag %}
    {% Tag style="purple" inversed=True %}
      purple

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="purple" href="#" delete=True inversed=True %}purple{% endTag %}
    {% Tag style="purple" href="#" delete=True inversed=True %}
      purple

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="purple" disabled=True inversed=True %}
      purple

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="blue" inversed=True %}blue{% endTag %}
    {% Tag style="blue" inversed=True %}
      blue

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="blue" href="#" delete=True inversed=True %}blue{% endTag %}
    {% Tag style="blue" href="#" delete=True inversed=True %}
      blue

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="blue" disabled=True inversed=True %}
      blue

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="lime" inversed=True %}lime{% endTag %}
    {% Tag style="lime" inversed=True %}
      lime

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="lime" href="#" delete=True inversed=True %}lime{% endTag %}
    {% Tag style="lime" href="#" delete=True inversed=True %}
      lime

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="lime" disabled=True inversed=True %}
      lime

      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-24)">
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag">
        <span class="nj-tag__text">default</span>
      </div>
      <div class="nj-tag">
        <span class="nj-tag__text">default</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag">
        <a href="#" class="nj-tag__link">default</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag default</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag">
        <a href="#" class="nj-tag__link">default</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag default</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">default</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--brand">
        <span class="nj-tag__text">brand</span>
      </div>
      <div class="nj-tag nj-tag--brand">
        <span class="nj-tag__text">brand</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--brand">
        <a href="#" class="nj-tag__link">brand</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag brand</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--brand">
        <a href="#" class="nj-tag__link">brand</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag brand</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--brand nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">brand</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--grey">
        <span class="nj-tag__text">grey</span>
      </div>
      <div class="nj-tag nj-tag--grey">
        <span class="nj-tag__text">grey</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--grey">
        <a href="#" class="nj-tag__link">grey</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag grey</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--grey">
        <a href="#" class="nj-tag__link">grey</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag grey</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--grey nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">grey</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--teal">
        <span class="nj-tag__text">teal</span>
      </div>
      <div class="nj-tag nj-tag--teal">
        <span class="nj-tag__text">teal</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--teal">
        <a href="#" class="nj-tag__link">teal</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag teal</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--teal">
        <a href="#" class="nj-tag__link">teal</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag teal</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--teal nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">teal</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--pink">
        <span class="nj-tag__text">pink</span>
      </div>
      <div class="nj-tag nj-tag--pink">
        <span class="nj-tag__text">pink</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--pink">
        <a href="#" class="nj-tag__link">pink</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag pink</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--pink">
        <a href="#" class="nj-tag__link">pink</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag pink</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--pink nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">pink</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--orange">
        <span class="nj-tag__text">orange</span>
      </div>
      <div class="nj-tag nj-tag--orange">
        <span class="nj-tag__text">orange</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--orange">
        <a href="#" class="nj-tag__link">orange</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag orange</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--orange">
        <a href="#" class="nj-tag__link">orange</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag orange</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--orange nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">orange</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--red">
        <span class="nj-tag__text">red</span>
      </div>
      <div class="nj-tag nj-tag--red">
        <span class="nj-tag__text">red</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--red">
        <a href="#" class="nj-tag__link">red</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag red</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--red">
        <a href="#" class="nj-tag__link">red</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag red</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--red nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">red</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--green">
        <span class="nj-tag__text">green</span>
      </div>
      <div class="nj-tag nj-tag--green">
        <span class="nj-tag__text">green</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--green">
        <a href="#" class="nj-tag__link">green</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag green</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--green">
        <a href="#" class="nj-tag__link">green</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag green</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--green nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">green</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--ultramarine">
        <span class="nj-tag__text">ultramarine</span>
      </div>
      <div class="nj-tag nj-tag--ultramarine">
        <span class="nj-tag__text">ultramarine</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--ultramarine">
        <a href="#" class="nj-tag__link">ultramarine</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag ultramarine</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--ultramarine">
        <a href="#" class="nj-tag__link">ultramarine</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag ultramarine</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--ultramarine nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">ultramarine</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--yellow">
        <span class="nj-tag__text">yellow</span>
      </div>
      <div class="nj-tag nj-tag--yellow">
        <span class="nj-tag__text">yellow</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--yellow">
        <a href="#" class="nj-tag__link">yellow</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag yellow</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--yellow">
        <a href="#" class="nj-tag__link">yellow</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag yellow</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--yellow nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">yellow</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--purple">
        <span class="nj-tag__text">purple</span>
      </div>
      <div class="nj-tag nj-tag--purple">
        <span class="nj-tag__text">purple</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--purple">
        <a href="#" class="nj-tag__link">purple</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag purple</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--purple">
        <a href="#" class="nj-tag__link">purple</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag purple</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--purple nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">purple</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--blue">
        <span class="nj-tag__text">blue</span>
      </div>
      <div class="nj-tag nj-tag--blue">
        <span class="nj-tag__text">blue</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--blue">
        <a href="#" class="nj-tag__link">blue</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag blue</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--blue">
        <a href="#" class="nj-tag__link">blue</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag blue</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--blue nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">blue</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
      <div class="nj-tag nj-tag--lime">
        <span class="nj-tag__text">lime</span>
      </div>
      <div class="nj-tag nj-tag--lime">
        <span class="nj-tag__text">lime</span>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
      <div class="nj-tag nj-tag--lime">
        <a href="#" class="nj-tag__link">lime</a>
        <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag lime</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--lime">
        <a href="#" class="nj-tag__link">lime</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
         <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm">
          <span class="nj-sr-only">Remove tag lime</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-tag nj-tag--lime nj-tag--disabled">
        <a role="link" aria-disabled="true" class="nj-tag__text">lime</a>
        <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
  {% Tag %}tag{% endTag %}
  {% Tag %}
    tag with icon

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag href="#" delete=True %}closable tag{% endTag %}
  {% Tag href="#" delete=True %}
    closable tag with icon

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag disabled=True %}
    disabled tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
</div>
"""
        expected = """
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
  <div class="nj-tag">
    <span class="nj-tag__text">tag</span>
  </div>
  <div class="nj-tag">
    <span class="nj-tag__text">tag with icon</span>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
  </div>
  <div class="nj-tag">
    <a href="#" class="nj-tag__link">closable tag</a>
    <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
      <span class="nj-sr-only">Remove tag closable tag</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-tag">
    <a href="#" class="nj-tag__link">closable tag with icon</a>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
      <span class="nj-sr-only">Remove tag closable tag with icon</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-tag nj-tag--disabled">
    <a role="link" aria-disabled="true" class="nj-tag__text">disabled tag</a>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
  <h5 style="margin: 0">SM:</h5>
  {% Tag size="sm" %}tag{% endTag %}
  {% Tag size="sm" %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag size="sm" href="#" delete=True %}XXX{% endTag %}
  {% Tag size="sm" href="#" delete=True %}
    XXX

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag size="sm" disabled=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
</div>
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8); margin-top: var(--nj-size-space-24);">
  <h5 style="margin: 0">MD (Default):</h5>
  {% Tag %}tag{% endTag %}
  {% Tag %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag href="#" delete=True %}XXX{% endTag %}
  {% Tag href="#" delete=True %}
    XXX

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag disabled=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
</div>
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8); margin-top: var(--nj-size-space-24);">
  <h5 style="margin: 0">LG:</h5>
  {% Tag size="lg" %}tag{% endTag %}
  {% Tag size="lg" %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag size="lg" href="#" delete=True %}XXX{% endTag %}
  {% Tag size="lg" href="#" delete=True %}
    XXX

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
  {% Tag size="lg" disabled=True %}
    tag

    {% Slot 'icon' class="material-icons" %}check{% endSlot %}
  {% endTag %}
</div>
"""
        expected = """
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
  <h5 style="margin: 0">SM:</h5>
  <div class="nj-tag nj-tag--sm">
    <span class="nj-tag__text">tag</span>
  </div>
  <div class="nj-tag nj-tag--sm">
    <span class="nj-tag__text">tag</span>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
  </div>
  <div class="nj-tag nj-tag--sm">
    <a href="#" class="nj-tag__link">XXX</a>
    <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
      <span class="nj-sr-only">Remove tag XXX</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-tag nj-tag--sm">
    <a href="#" class="nj-tag__link">XXX</a>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
      <span class="nj-sr-only">Remove tag XXX</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-tag nj-tag--sm nj-tag--disabled">
    <a role="link" aria-disabled="true" class="nj-tag__text">tag</a>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
  </div>
</div>
  
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8); margin-top: var(--nj-size-space-24);">
  <h5 style="margin: 0">MD (Default):</h5>
  <div class="nj-tag">
    <span class="nj-tag__text">tag</span>
  </div>
  <div class="nj-tag">
    <span class="nj-tag__text">tag</span>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
  </div>
  <div class="nj-tag">
    <a href="#" class="nj-tag__link">XXX</a>
    <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
      <span class="nj-sr-only">Remove tag XXX</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-tag">
    <a href="#" class="nj-tag__link">XXX</a>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
      <span class="nj-sr-only">Remove tag XXX</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-tag nj-tag--disabled">
    <a role="link" aria-disabled="true" class="nj-tag__text">tag</a>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
  </div>
</div>
  
<div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8); margin-top: var(--nj-size-space-24);">
  <h5 style="margin: 0">LG:</h5>
  <div class="nj-tag nj-tag--lg">
    <span class="nj-tag__text">tag</span>
  </div>
  <div class="nj-tag nj-tag--lg">
    <span class="nj-tag__text">tag</span>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
  </div>
  <div class="nj-tag nj-tag--lg">
    <a href="#" class="nj-tag__link">XXX</a>
    <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
      <span class="nj-sr-only">Remove tag XXX</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-tag nj-tag--lg">
    <a href="#" class="nj-tag__link">XXX</a>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
      <span class="nj-sr-only">Remove tag XXX</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-tag nj-tag--lg nj-tag--disabled">
    <a role="link" aria-disabled="true" class="nj-tag__text">tag</a>
    <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-24)">
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag %}tag{% endTag %}
    {% Tag %}
      tag
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag href="#" delete=True %}XXX{% endTag %}
    {% Tag href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag disabled=True %}
      tag
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="brand" %}brand{% endTag %}
    {% Tag style="brand" %}
      brand
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="brand" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="brand" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="brand" disabled=True %}
      brand
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="teal" %}teal{% endTag %}
    {% Tag style="teal" %}
      teal
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="teal" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="teal" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="teal" disabled=True %}
      teal
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="pink" %}pink{% endTag %}
    {% Tag style="pink" %}
      pink
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="pink" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="pink" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="pink" disabled=True %}
      pink
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="orange" %}orange{% endTag %}
    {% Tag style="orange" %}
      orange
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="orange" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="orange" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="orange" disabled=True %}
      orange
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="red" %}red{% endTag %}
    {% Tag style="red" %}
      red
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="red" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="red" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="red" disabled=True %}
      red
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="green" %}green{% endTag %}
    {% Tag style="green" %}
      green
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="green" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="green" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="green" disabled=True %}
      green
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="ultramarine" %}ultramarine{% endTag %}
    {% Tag style="ultramarine" %}
      ultramarine
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="ultramarine" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="ultramarine" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="ultramarine" disabled=True %}
      ultramarine
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="yellow" %}yellow{% endTag %}
    {% Tag style="yellow" %}
      yellow
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="yellow" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="yellow" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="yellow" disabled=True %}
      yellow
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="purple" %}purple{% endTag %}
    {% Tag style="purple" %}
      purple
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="purple" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="purple" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="purple" disabled=True %}
      purple
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="blue" %}blue{% endTag %}
    {% Tag style="blue" %}
      blue
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="blue" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="blue" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="blue" disabled=True %}
      blue
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    {% Tag style="lime" %}lime{% endTag %}
    {% Tag style="lime" %}
      lime
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="lime" href="#" delete=True %}XXX{% endTag %}
    {% Tag style="lime" href="#" delete=True %}
      XXX
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
    {% Tag style="lime" disabled=True %}
      lime
  
      {% Slot 'icon' class="material-icons" %}check{% endSlot %}
    {% endTag %}
  </div>
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-24)">
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag">
      <span class="nj-tag__text">tag</span>
    </div>
    <div class="nj-tag">
      <span class="nj-tag__text">tag</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary ">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">tag</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--brand">
      <span class="nj-tag__text">brand</span>
    </div>
    <div class="nj-tag nj-tag--brand">
      <span class="nj-tag__text">brand</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--brand">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--brand">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--brand nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">brand</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--teal">
      <span class="nj-tag__text">teal</span>
    </div>
    <div class="nj-tag nj-tag--teal">
      <span class="nj-tag__text">teal</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--teal">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--teal">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--teal nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">teal</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--pink">
      <span class="nj-tag__text">pink</span>
    </div>
    <div class="nj-tag nj-tag--pink">
      <span class="nj-tag__text">pink</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--pink">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--pink">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--pink nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">pink</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--orange">
      <span class="nj-tag__text">orange</span>
    </div>
    <div class="nj-tag nj-tag--orange">
      <span class="nj-tag__text">orange</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--orange">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--orange">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--orange nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">orange</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--red">
      <span class="nj-tag__text">red</span>
    </div>
    <div class="nj-tag nj-tag--red">
      <span class="nj-tag__text">red</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--red">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--red">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--red nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">red</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--green">
      <span class="nj-tag__text">green</span>
    </div>
    <div class="nj-tag nj-tag--green">
      <span class="nj-tag__text">green</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--green">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--green">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--green nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">green</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--ultramarine">
      <span class="nj-tag__text">ultramarine</span>
    </div>
    <div class="nj-tag nj-tag--ultramarine">
      <span class="nj-tag__text">ultramarine</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--ultramarine">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--ultramarine">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--ultramarine nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">ultramarine</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--yellow">
      <span class="nj-tag__text">yellow</span>
    </div>
    <div class="nj-tag nj-tag--yellow">
      <span class="nj-tag__text">yellow</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--yellow">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--yellow">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--yellow nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">yellow</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--purple">
      <span class="nj-tag__text">purple</span>
    </div>
    <div class="nj-tag nj-tag--purple">
      <span class="nj-tag__text">purple</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--purple">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--purple">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--purple nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">purple</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--blue">
      <span class="nj-tag__text">blue</span>
    </div>
    <div class="nj-tag nj-tag--blue">
      <span class="nj-tag__text">blue</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--blue">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--blue">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--blue nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">blue</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
  <div style="display: flex; align-items: center; flex-wrap: wrap; gap: var(--nj-size-space-8)">
    <div class="nj-tag nj-tag--lime">
      <span class="nj-tag__text">lime</span>
    </div>
    <div class="nj-tag nj-tag--lime">
      <span class="nj-tag__text">lime</span>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
    <div class="nj-tag nj-tag--lime">
      <a href="#" class="nj-tag__link">XXX</a>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--lime">
      <a href="#" class="nj-tag__link">XXX</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
      <button type="button" class="nj-tag__close nj-icon-btn nj-icon-btn--sm nj-icon-btn--secondary">
        <span class="nj-sr-only">Remove tag XXX</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-tag nj-tag--lime nj-tag--disabled">
      <a role="link" aria-disabled="true" class="nj-tag__text">lime</a>
      <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Tag disabled=True %}
  disabled tag

  {% Slot 'icon' class="material-icons" %}check{% endSlot %}
{% endTag %}
"""
        expected = """
<div class="nj-tag nj-tag--disabled">
  <a role="link" aria-disabled="true" class="nj-tag__text">disabled tag</a>
  <span aria-hidden="true" class="nj-tag__icon material-icons">check</span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
