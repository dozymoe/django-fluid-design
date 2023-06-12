# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class BadgeTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Badge %}{% endBadge %}
"""
        expected = """
<p class="nj-badge"></p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; align-items: flex-start; flex-wrap: wrap; gap: 16px; padding: 24px;">
  <h4>Bold</h4>
  {% Badge %}7{% endBadge %}
  {% Badge %}75{% endBadge %}
  {% Badge %}75+{% endBadge %}
  <hr>
  <h4>Subtle</h4>
  {% Badge variant="subtle" %}7{% endBadge %}
  {% Badge variant="subtle" %}75{% endBadge %}
  {% Badge variant="subtle" %}75+{% endBadge %}
  <hr>
  <h4>Minimal</h4>
  {% Badge variant="minimal" %}7{% endBadge %}
  {% Badge variant="minimal" %}75{% endBadge %}
  {% Badge variant="minimal" %}75+{% endBadge %}
  <hr>
  <h4>Bold color variants</h4>
  {% Badge uppercase=True %}
    Information, in progress
  {% endBadge %}
  {% Badge uppercase=True style="danger" %}
    Danger
  {% endBadge %}
  {% Badge uppercase=True style="warning" %}
    Warning
  {% endBadge %}
  {% Badge uppercase=True style="success" %}
    Success
  {% endBadge %}
  {% Badge uppercase=True style="information" %}
    Information
  {% endBadge %}
  {% Badge uppercase=True style="discovery" %}
    Discovery
  {% endBadge %}
  <hr>
  <h4>Subtle color variants</h4>
  {% Badge uppercase=True variant="subtle" %}
    Information, in progress
  {% endBadge %}
  {% Badge uppercase=True variant="subtle" style="danger" %}
    Danger
  {% endBadge %}
  {% Badge uppercase=True variant="subtle" style="warning" %}
    Warning
  {% endBadge %}
  {% Badge uppercase=True variant="subtle" style="success" %}
    Success
  {% endBadge %}
  {% Badge uppercase=True variant="subtle" style="information" %}
    Information
  {% endBadge %}
  {% Badge uppercase=True variant="subtle" style="discovery" %}
    Discovery
  {% endBadge %}
  <hr>
  <h4>Minimal color variants</h4>
  {% Badge uppercase=True variant="minimal" %}
    Information, in progress
  {% endBadge %}
  {% Badge uppercase=True variant="minimal" style="danger" %}
    Danger
  {% endBadge %}
  {% Badge uppercase=True variant="minimal" style="warning" %}
    Warning
  {% endBadge %}
  {% Badge uppercase=True variant="minimal" style="success" %}
    Success
  {% endBadge %}
  {% Badge uppercase=True variant="minimal" style="information" %}
    Information
  {% endBadge %}
  {% Badge uppercase=True variant="minimal" style="discovery" %}
    Discovery
  {% endBadge %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; align-items: flex-start; flex-wrap: wrap; gap: 16px; padding: 24px;">
  <h4>Bold</h4>
  <p class="nj-badge">7</p>
  <p class="nj-badge">75</p>
  <p class="nj-badge">75+</p>
  <hr>
  <h4>Subtle</h4>
  <p class="nj-badge nj-badge--subtle">7</p>
  <p class="nj-badge nj-badge--subtle">75</p>
  <p class="nj-badge nj-badge--subtle">75+</p>
  <hr>
  <h4>Minimal</h4>
  <p class="nj-badge nj-badge--minimal">7</p>
  <p class="nj-badge nj-badge--minimal">75</p>
  <p class="nj-badge nj-badge--minimal">75+</p>
  <hr>
  <h4>Bold color variants</h4>
  <p class="nj-badge nj-badge--uppercase ">Information, in progress</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--danger">Danger</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--warning">Warning</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--success">Success</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--information">Information</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--discovery">Discovery</p>
  <hr>
  <h4>Subtle color variants</h4>
  <p class="nj-badge nj-badge--uppercase nj-badge--subtle">Information, in progress</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--subtle nj-badge--danger">Danger</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--subtle nj-badge--warning">Warning</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--subtle nj-badge--success">Success</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--subtle nj-badge--information">Information</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--subtle nj-badge--discovery">Discovery</p>
  <hr>
  <h4>Minimal color variants</h4>
  <p class="nj-badge nj-badge--uppercase nj-badge--minimal">Information, in progress</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--minimal nj-badge--danger">Danger</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--minimal nj-badge--warning">Warning</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--minimal nj-badge--success">Success</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--minimal nj-badge--information">Information</p>
  <p class="nj-badge nj-badge--uppercase nj-badge--minimal nj-badge--discovery">Discovery</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; align-items: flex-start; flex-wrap: wrap; gap: 16px; padding: 24px;">
  {% Badge size="lg" %}7{% endBadge %}
  {% Badge size="lg" %}75{% endBadge %}
  {% Badge size="lg" %}75+{% endBadge %}
  {% Badge size="lg" %}Information, in progress{% endBadge %}
  {% Badge size="lg" style="danger" %}Danger{% endBadge %}
  {% Badge size="lg" style="warning" %}Warning{% endBadge %}
  {% Badge size="lg" style="success" %}Success{% endBadge %}
  {% Badge size="lg" style="information" %}Information{% endBadge %}
  {% Badge size="lg" style="discovery" %}Discovery{% endBadge %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; align-items: flex-start; flex-wrap: wrap; gap: 16px; padding: 24px;">
  <p class="nj-badge nj-badge--lg">7</p>
  <p class="nj-badge nj-badge--lg">75</p>
  <p class="nj-badge nj-badge--lg">75+</p>
  <p class="nj-badge nj-badge--lg">Information, in progress</p>
  <p class="nj-badge nj-badge--lg nj-badge--danger">Danger</p>
  <p class="nj-badge nj-badge--lg nj-badge--warning">Warning</p>
  <p class="nj-badge nj-badge--lg nj-badge--success">Success</p>
  <p class="nj-badge nj-badge--lg nj-badge--information">Information</p>
  <p class="nj-badge nj-badge--lg nj-badge--discovery">Discovery</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; align-items: flex-start; flex-wrap: wrap; gap: 16px; padding: 24px;">
  {% Badge variant="subtle" %}Information, in progress{% endBadge %}
  {% Badge variant="subtle" style="danger" %}Danger{% endBadge %}
  {% Badge variant="subtle" style="warning" %}Warning{% endBadge %}
  {% Badge variant="subtle" style="success" %}Success{% endBadge %}
  {% Badge variant="subtle" style="information" %}Information{% endBadge %}
  {% Badge variant="subtle" style="discovery" %}Discovery{% endBadge %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; align-items: flex-start; flex-wrap: wrap; gap: 16px; padding: 24px;">
  <p class="nj-badge nj-badge--subtle">Information, in progress</p>
  <p class="nj-badge nj-badge--subtle nj-badge--danger">Danger</p>
  <p class="nj-badge nj-badge--subtle nj-badge--warning">Warning</p>
  <p class="nj-badge nj-badge--subtle nj-badge--success">Success</p>
  <p class="nj-badge nj-badge--subtle nj-badge--information">Information</p>
  <p class="nj-badge nj-badge--subtle nj-badge--discovery">Discovery</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; align-items: flex-start; flex-wrap: wrap; gap: 16px; padding: 24px;">
  {% Badge variant="minimal" %}Information, in progress{% endBadge %}
  {% Badge variant="minimal" style="danger" %}Danger{% endBadge %}
  {% Badge variant="minimal" style="warning" %}Warning{% endBadge %}
  {% Badge variant="minimal" style="success" %}Success{% endBadge %}
  {% Badge variant="minimal" style="information" %}Information{% endBadge %}
  {% Badge variant="minimal" style="discovery" %}Discovery{% endBadge %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; align-items: flex-start; flex-wrap: wrap; gap: 16px; padding: 24px;">
  <p class="nj-badge nj-badge--minimal">Information, in progress</p>
  <p class="nj-badge nj-badge--minimal nj-badge--danger">Danger</p>
  <p class="nj-badge nj-badge--minimal nj-badge--warning">Warning</p>
  <p class="nj-badge nj-badge--minimal nj-badge--success">Success</p>
  <p class="nj-badge nj-badge--minimal nj-badge--information">Information</p>
  <p class="nj-badge nj-badge--minimal nj-badge--discovery">Discovery</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Badge %}7{% endBadge %}
{% Badge %}75{% endBadge %}
{% Badge %}Neutral badge+{% endBadge %}
"""
        expected = """
<p class="nj-badge">7</p>
<p class="nj-badge">75</p>
<p class="nj-badge">Neutral badge+</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Badge size="lg" %}7{% endBadge %}
{% Badge size="lg" %}75{% endBadge %}
{% Badge size="lg" %}Neutral badge{% endBadge %}
"""
        expected = """
<p class="nj-badge nj-badge--lg">7</p>
<p class="nj-badge nj-badge--lg">75</p>
<p class="nj-badge nj-badge--lg">Neutral badge</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Badge %}Bold badge (default){% endBadge %}
{% Badge variant="subtle" %}Subtle badge{% endBadge %}
{% Badge variant="minimal" %}Minimal badge{% endBadge %}
"""
        expected = """
<p class="nj-badge">Bold badge (default)</p>
<p class="nj-badge nj-badge--subtle">Subtle badge</p>
<p class="nj-badge nj-badge--minimal">Minimal badge</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Badge %}Neutral badge{% endBadge %}
{% Badge style="information" %}Information badge{% endBadge %}
{% Badge style="discovery" %}Discovery badge{% endBadge %}
{% Badge style="success" %}Success badge{% endBadge %}
{% Badge style="warning" %}Warning badge{% endBadge %}
{% Badge style="danger" %}Danger badge{% endBadge %}
"""
        expected = """
<p class="nj-badge">Neutral badge</p>
<p class="nj-badge nj-badge--information">Information badge</p>
<p class="nj-badge nj-badge--discovery">Discovery badge</p>
<p class="nj-badge nj-badge--success">Success badge</p>
<p class="nj-badge nj-badge--warning">Warning badge</p>
<p class="nj-badge nj-badge--danger">Danger badge</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
