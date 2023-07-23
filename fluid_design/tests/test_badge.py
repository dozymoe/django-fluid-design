# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class BadgeTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Badge %}
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
  {% Badge label="7" %}
  {% Badge label="75" %}
  {% Badge label="75+" %}
  <hr>
  <h4>Subtle</h4>
  {% Badge variant="subtle" label="7" %}
  {% Badge variant="subtle" label="75" %}
  {% Badge variant="subtle" label="75+" %}
  <hr>
  <h4>Minimal</h4>
  {% Badge variant="minimal" label="7" %}
  {% Badge variant="minimal" label="75" %}
  {% Badge variant="minimal" label="75+" %}
  <hr>
  <h4>Bold color variants</h4>
  {% Badge uppercase=True label="Information, in progress" %}
  {% Badge uppercase=True style="danger" label="Danger" %}
  {% Badge uppercase=True style="warning" label="Warning" %}
  {% Badge uppercase=True style="success" label="Success" %}
  {% Badge uppercase=True style="information" label="Information" %}
  {% Badge uppercase=True style="discovery" label="Discovery" %}
  <hr>
  <h4>Subtle color variants</h4>
  {% Badge uppercase=True variant="subtle" label="Information, in progress" %}
  {% Badge uppercase=True variant="subtle" style="danger" label="Danger" %}
  {% Badge uppercase=True variant="subtle" style="warning" label="Warning" %}
  {% Badge uppercase=True variant="subtle" style="success" label="Success" %}
  {% Badge uppercase=True variant="subtle" style="information" label="Information" %}
  {% Badge uppercase=True variant="subtle" style="discovery" label="Discovery" %}
  <hr>
  <h4>Minimal color variants</h4>
  {% Badge uppercase=True variant="minimal" label="Information, in progress" %}
  {% Badge uppercase=True variant="minimal" style="danger" label="Danger" %}
  {% Badge uppercase=True variant="minimal" style="warning" label="Warning" %}
  {% Badge uppercase=True variant="minimal" style="success" label="Success" %}
  {% Badge uppercase=True variant="minimal" style="information" label="Information" %}
  {% Badge uppercase=True variant="minimal" style="discovery" label="Discovery" %}
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
  {% Badge size="lg" label="7" %}
  {% Badge size="lg" label="75" %}
  {% Badge size="lg" label="75+" %}
  {% Badge size="lg" label="Information, in progress" %}
  {% Badge size="lg" style="danger" label="Danger" %}
  {% Badge size="lg" style="warning" label="Warning" %}
  {% Badge size="lg" style="success" label="Success" %}
  {% Badge size="lg" style="information" label="Information" %}
  {% Badge size="lg" style="discovery" label="Discovery" %}
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
  {% Badge variant="subtle" label="Information, in progress" %}
  {% Badge variant="subtle" style="danger" label="Danger" %}
  {% Badge variant="subtle" style="warning" label="Warning" %}
  {% Badge variant="subtle" style="success" label="Success" %}
  {% Badge variant="subtle" style="information" label="Information" %}
  {% Badge variant="subtle" style="discovery" label="Discovery" %}
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
  {% Badge variant="minimal" label="Information, in progress" %}
  {% Badge variant="minimal" style="danger" label="Danger" %}
  {% Badge variant="minimal" style="warning" label="Warning" %}
  {% Badge variant="minimal" style="success" label="Success" %}
  {% Badge variant="minimal" style="information" label="Information" %}
  {% Badge variant="minimal" style="discovery" label="Discovery" %}
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
{% Badge label="7" %}
{% Badge label="75" %}
{% Badge label="Neutral badge+" %}
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
{% Badge size="lg" label="7" %}
{% Badge size="lg" label="75" %}
{% Badge size="lg" label="Neutral badge" %}
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
{% Badge label="Bold badge (default)" %}
{% Badge variant="subtle" label="Subtle badge" %}
{% Badge variant="minimal" label="Minimal badge" %}
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
{% Badge label="Neutral badge" %}
{% Badge style="information" label="Information badge" %}
{% Badge style="discovery" label="Discovery badge" %}
{% Badge style="success" label="Success badge" %}
{% Badge style="warning" label="Warning badge" %}
{% Badge style="danger" label="Danger badge" %}
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
