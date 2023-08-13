# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ProgressTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Progress %}
"""
        expected = """
<div class="nj-progress">
  <div aria-valuemax="100" aria-valuemin="0" aria-valuenow="0" class="nj-progress__bar" role="progressbar">
   <span class="nj-sr-only">
    0%
   </span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 24px;">
  {% Progress label="Label of progressbar" %}
  {% Progress current=25 label="Label of progressbar" %}
  {% Progress current=50 label="Label of progressbar" %}
  {% Progress current=75 label="Label of progressbar" %}
  {% Progress current=100 label="Label of progressbar" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 24px;">
<div class="nj-progress">
  <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
    <span class="nj-sr-only">0%</span>
  </div>
</div>
<div class="nj-progress">
  <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
    <span class="nj-sr-only">25%</span>
  </div>
</div>
<div class="nj-progress">
  <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
    <span class="nj-sr-only">50%</span>
  </div>
</div>
<div class="nj-progress">
  <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
    <span class="nj-sr-only">75%</span>
  </div>
</div>
<div class="nj-progress">
  <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
    <span class="nj-sr-only">100%</span>
  </div>
</div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 24px;">
  {% Progress current=25 label="Label of progressbar" text="25%" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 24px;">
<div class="nj-progress">
  <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
    <span class="nj-sr-only">25%</span>
  </div>
  <div aria-hidden="true" class="nj-progress__text">25%</div>
</div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% Progress current=25 label="Label of progressbar" %}
"""
        expected = """
<div class="nj-progress">
  <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
    <span class="nj-sr-only">25%</span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 24px;">
  {% Progress label="Label of progressbar" %}
  {% Progress current=25 label="Label of progressbar" %}
  {% Progress current=50 label="Label of progressbar" %}
  {% Progress current=75 label="Label of progressbar" %}
  {% Progress current=100 label="Label of progressbar" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 24px;">
    <div class="nj-progress">
      <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
        <span class="nj-sr-only">0%</span>
      </div>
    </div>
    <div class="nj-progress">
      <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
        <span class="nj-sr-only">25%</span>
      </div>
    </div>
    <div class="nj-progress">
      <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
        <span class="nj-sr-only">50%</span>
      </div>
    </div>
    <div class="nj-progress">
      <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
        <span class="nj-sr-only">75%</span>
      </div>
    </div>
    <div class="nj-progress">
      <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
        <span class="nj-sr-only">100%</span>
      </div>
    </div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 24px;">
  {% Progress current=25 label="Label of progressbar" text="25%" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 24px;">
  <div class="nj-progress">
    <div class="nj-progress__bar" role="progressbar" aria-label="Label of progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
      <span class="nj-sr-only">25%</span>
    </div>
    <div aria-hidden="true" class="nj-progress__text">25%</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
