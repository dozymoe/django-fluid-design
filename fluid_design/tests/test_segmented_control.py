# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class SegmentedControlTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% SegmentedControl %}
{% endSegmentedControl %}
"""
        expected = """
<div class="nj-segmented-control" role="group">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% SegmentedControl label="View" value="Item 1" %}
  {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 2{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 4{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 5{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}
    Item 6

    {% Slot 'icon' %}
      {% Icon label="av_timer" %}
    {% endSlot %}
  {% endSegmentedControlBtn %}
  {% SegmentedControlBtn disabled=True  %}Item 7{% endSegmentedControlBtn %}
{% endSegmentedControl %}
"""
        expected = """
<div class="nj-segmented-control" role="group" aria-label="View" data-value="Item 1">
  <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 1">Item 1</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2">Item 2</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4">Item 4</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 5">Item 5</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 6">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">av_timer</span>
    <span>Item 6</span>
  </button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" disabled data-value="Item 7">Item 7</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-24); align-items: flex-start">
  <h5 style="margin: 0">SM:</h5>
  {% SegmentedControl label="View" value="Item 5" size="sm" %}
    {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 2{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 4{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 5{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}
      Item 6
  
      {% Slot 'icon' %}
        {% Icon label="av_timer" %}
      {% endSlot %}
    {% endSegmentedControlBtn %}
    {% SegmentedControlBtn disabled=True  %}Item 7{% endSegmentedControlBtn %}
  {% endSegmentedControl %}
  <h5 style="margin: 0">MD (Default):</h5>
  {% SegmentedControl label="View" value="Item 5" %}
    {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 2{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 4{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 5{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}
      Item 6
  
      {% Slot 'icon' %}
        {% Icon label="av_timer" %}
      {% endSlot %}
    {% endSegmentedControlBtn %}
    {% SegmentedControlBtn disabled=True  %}Item 7{% endSegmentedControlBtn %}
  {% endSegmentedControl %}
  <h5 style="margin: 0">LG:</h5>
  {% SegmentedControl label="View" value="Item 5" size="lg" %}
    {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 2{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 4{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 5{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}
      Item 6
  
      {% Slot 'icon' %}
        {% Icon label="av_timer" %}
      {% endSlot %}
    {% endSegmentedControlBtn %}
    {% SegmentedControlBtn disabled=True  %}Item 7{% endSegmentedControlBtn %}
  {% endSegmentedControl %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-24); align-items: flex-start">
  <h5 style="margin: 0">SM:</h5>
  <div class="nj-segmented-control nj-segmented-control--sm" role="group" aria-label="View" data-value="Item 5">
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 1">Item 1</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2">Item 2</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4">Item 4</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 5">Item 5</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 6">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">av_timer</span>
      <span>Item 6</span>
    </button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" disabled data-value="Item 7">Item 7</button>
  </div>
  <h5 style="margin: 0">MD (Default):</h5>
  <div class="nj-segmented-control" role="group" aria-label="View" data-value="Item 5">
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 1">Item 1</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2">Item 2</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4">Item 4</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 5">Item 5</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 6">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">av_timer</span>
      <span>Item 6</span>
    </button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" disabled data-value="Item 7">Item 7</button>
  </div>
  <h5 style="margin: 0">LG:</h5>
  <div class="nj-segmented-control nj-segmented-control--lg" role="group" aria-label="View" data-value="Item 5">
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 1">Item 1</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2">Item 2</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4">Item 4</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 5">Item 5</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 6">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">av_timer</span>
      <span>Item 6</span>
    </button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" disabled data-value="Item 7">Item 7</button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% SegmentedControl mode="compact" label="View" value="Item 1" %}
  {% SegmentedControlBtn value="Item 1" %}
    Align to left

    {% Slot 'icon' %}{% Icon label="format_align_left" %}{% endSlot %}
  {% endSegmentedControlBtn %}
  {% SegmentedControlBtn value="Item 2" %}
    Center

    {% Slot 'icon' %}{% Icon label="format_align_center" %}{% endSlot %}
  {% endSegmentedControlBtn %}
  {% SegmentedControlBtn value="Item 3" %}
    Align to right

    {% Slot 'icon' %}{% Icon label="format_align_right" %}{% endSlot %}
  {% endSegmentedControlBtn %}
  {% SegmentedControlBtn value="Item 4" disabled=True %}
    Justify

    {% Slot 'icon' %}{% Icon label="format_align_justify" %}{% endSlot %}
  {% endSegmentedControlBtn %}
{% endSegmentedControl %}
"""
        expected = """
<div class="nj-segmented-control" role="group" aria-label="View" data-value="Item 1">
  <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 1" title="Align to left">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">format_align_left</span>
    <span class="nj-sr-only">Align to left</span>
  </button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2" title="Center">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">format_align_center</span>
    <span class="nj-sr-only">Center</span>
  </button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3" title="Align to right">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">format_align_right</span>
    <span class="nj-sr-only">Align to right</span>
  </button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4" disabled title="Justify">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">format_align_justify</span>
    <span class="nj-sr-only">Justify</span>
  </button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% SegmentedControl label="View" value="Item 1" %}
  {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 2{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 4{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 5{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}
    Item 6

    {% Slot 'icon' %}
      {% Icon label="av_timer" %}
    {% endSlot %}
  {% endSegmentedControlBtn %}
  {% SegmentedControlBtn disabled=True  %}Item 7{% endSegmentedControlBtn %}
{% endSegmentedControl %}
"""
        expected = """
<div class="nj-segmented-control" role="group" aria-label="View" data-value="Item 1">
  <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 1">Item 1</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2">Item 2</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4">Item 4</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 5">Item 5</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 6">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">av_timer</span>
    <span>Item 6</span>
  </button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" disabled data-value="Item 7">Item 7</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% SegmentedControl label="View" value="Item 1" %}
  {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
  {% SegmentedControlBtn disabled=True %}Item 2{% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
{% endSegmentedControl %}
"""
        expected = """
<div class="nj-segmented-control" role="group" aria-label="View" data-value="Item 1">
  <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 1">Item 1</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2" disabled>Item 2</button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-24); align-items: flex-start">
  <h5 style="margin: 0">Small:</h5>
  {% SegmentedControl label="View" value="Item 5" size="sm" %}
    {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 2{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 4{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 5{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}
      Item 6
  
      {% Slot 'icon' %}
        {% Icon label="av_timer" %}
      {% endSlot %}
    {% endSegmentedControlBtn %}
    {% SegmentedControlBtn disabled=True  %}Item 7{% endSegmentedControlBtn %}
  {% endSegmentedControl %}
  <h5 style="margin: 0">Medium (Default):</h5>
  {% SegmentedControl label="View" value="Item 5" %}
    {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 2{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 4{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 5{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}
      Item 6
  
      {% Slot 'icon' %}
        {% Icon label="av_timer" %}
      {% endSlot %}
    {% endSegmentedControlBtn %}
    {% SegmentedControlBtn disabled=True  %}Item 7{% endSegmentedControlBtn %}
  {% endSegmentedControl %}
  <h5 style="margin: 0">Large:</h5>
  {% SegmentedControl label="View" value="Item 5" size="lg" %}
    {% SegmentedControlBtn %}Item 1{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 2{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 3{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 4{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}Item 5{% endSegmentedControlBtn %}
    {% SegmentedControlBtn %}
      Item 6
  
      {% Slot 'icon' %}
        {% Icon label="av_timer" %}
      {% endSlot %}
    {% endSegmentedControlBtn %}
    {% SegmentedControlBtn disabled=True  %}Item 7{% endSegmentedControlBtn %}
  {% endSegmentedControl %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-24); align-items: flex-start">
  <h5 style="margin: 0">Small:</h5>
  <div class="nj-segmented-control nj-segmented-control--sm" role="group" aria-label="View" data-value="Item 5">
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 1">Item 1</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2">Item 2</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4">Item 4</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 5">Item 5</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 6">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">av_timer</span>
      <span>Item 6</span>
    </button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" disabled data-value="Item 7">Item 7</button>
  </div>
  <h5 style="margin: 0">Medium (Default):</h5>
  <div class="nj-segmented-control" role="group" aria-label="View" data-value="Item 5">
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 1">Item 1</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2">Item 2</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4">Item 4</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 5">Item 5</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 6">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">av_timer</span>
      <span>Item 6</span>
    </button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" disabled data-value="Item 7">Item 7</button>
  </div>
  <h5 style="margin: 0">Large:</h5>
  <div class="nj-segmented-control nj-segmented-control--lg" role="group" aria-label="View" data-value="Item 5">
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 1">Item 1</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2">Item 2</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3">Item 3</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4">Item 4</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 5">Item 5</button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 6">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">av_timer</span>
      <span>Item 6</span>
    </button>
    <button class="nj-segmented-control-btn" type="button" aria-pressed="false" disabled data-value="Item 7">Item 7</button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% SegmentedControl mode="compact" label="View" value="Item 1" %}
  {% SegmentedControlBtn %}
    Item 1

    {% Slot 'icon' %}{% Icon label="format_align_left" %}{% endSlot %}
  {% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}
    Item 2

    {% Slot 'icon' %}{% Icon label="format_align_center" %}{% endSlot %}
  {% endSegmentedControlBtn %}
  {% SegmentedControlBtn %}
    Item 3

    {% Slot 'icon' %}{% Icon label="format_align_right" %}{% endSlot %}
  {% endSegmentedControlBtn %}
  {% SegmentedControlBtn disabled=True %}
    Item 4

    {% Slot 'icon' %}{% Icon label="format_align_justify" %}{% endSlot %}
  {% endSegmentedControlBtn %}
{% endSegmentedControl %}
"""
        expected = """
<div class="nj-segmented-control" role="group" aria-label="View" data-value="Item 1">
  <button class="nj-segmented-control-btn" type="button" aria-pressed="true" data-value="Item 1" title="Item 1">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">format_align_left</span>
    <span class="nj-sr-only">Item 1</span>
  </button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 2" title="Item 2">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">format_align_center</span>
    <span class="nj-sr-only">Item 2</span>
  </button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 3" title="Item 3">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">format_align_right</span>
    <span class="nj-sr-only">Item 3</span>
  </button>
  <button class="nj-segmented-control-btn" type="button" aria-pressed="false" data-value="Item 4" disabled title="Item 4">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-segmented-control-btn__icon">format_align_justify</span>
    <span class="nj-sr-only">Item 4</span>
  </button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
