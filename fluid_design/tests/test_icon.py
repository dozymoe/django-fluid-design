# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class IconTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Icon %}
"""
        expected = """
<span aria-hidden="true" class="material-icons nj-icon-material"></span>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<h2>1. Basic usage</h2>
<p>Simply use the <code>`material-icons`</code> class.</p>
<p>
  {% Icon label="dashboard" %}
</p>

<h3>1.1 With text</h3>
<p>
  When using the icon in a p tag, you can pass the
  <code>`nj-icon-material-text`</code> class to the <code>`p`</code> element to
  <b>align and space the icon correctly</b>.
</p>
<p class="nj-icon-material-text">
  Example with text
  {% Icon label="dashboard" %}
</p>
"""
        expected = """
<h2>1. Basic usage</h2>
<p>Simply use the <code>`material-icons`</code> class.</p>
<p>
  <span aria-hidden="true" class="material-icons nj-icon-material">dashboard</span>
</p>

<h3>1.1 With text</h3>
<p>When using the icon in a p tag, you can pass the <code>`nj-icon-material-text`</code> class to the <code>`p`</code> element to <b>align and space the icon correctly</b>.</p>
<p class="nj-icon-material-text">Example with text<span aria-hidden="true" class="material-icons nj-icon-material">dashboard</span></p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<h2>2. Working with colors</h2>
<h3>2.1 Default inherit behaviour</h3>
<p>By default, icons inherit the color of their wrapping element:</p>
<p class="nj-icon-material-text" style="color: var(--nj-color-text-brand-primary);">
  Passing brand color through wrapping p tag
  {% Icon label="dashboard" %}
</p>

<hr>
<h3>2.2 Icon colors directly on the icon</h3>

<p>To use additional colors directly on the icon, you can use the color modifiers: <code>`nj-icon-material--{color}`</code> </p>
<p class="nj-icon-material-text">
  <code>nj-icon-material--primary</code> (grey-800):
  {% Icon style="primary" label="dashboard" %}
</p>
<p style="font-size: var(--nj-size-font-deci);">(this should be used with primary text which is grey 1000 so the icon doesn't drag too much attention)</p>
  <p class="nj-icon-material-text">
  <code>nj-icon-material--secondary</code> (grey-600):
  {% Icon style="secondary" label="dashboard" %}
</p>
<p class="nj-icon-material-text" style="background-color: var(--nj-color-background-high-contrast); color: var(--nj-color-text-inverse); padding: 4px;">
  <code>nj-icon-material--inverse</code> (grey-0):
  {% Icon style="inverse" label="dashboard" %}
</p>

<h4>2.2.1 Icon colors</h4>

<p class="nj-icon-material-text">
  Inherit
  {% Icon label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Grey
  {% Icon color="grey" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Brand
  {% Icon color="brand" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Teal
  {% Icon color="teal" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Pink
  {% Icon color="pink" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Orange
  {% Icon color="orange" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Red
  {% Icon color="red" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Green
  {% Icon color="green" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Ultramarine
  {% Icon color="ultramarine" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Yellow
  {% Icon color="yellow" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Purple
  {% Icon color="purple" label="ev_station" %}
</p>

{% Icon label="ev_station" %}
{% Icon color="grey" label="ev_station" %}
{% Icon color="brand" label="ev_station" %}
{% Icon color="teal" label="ev_station" %}
{% Icon color="pink" label="ev_station" %}
{% Icon color="orange" label="ev_station" %}
{% Icon color="red" label="ev_station" %}
{% Icon color="green" label="ev_station" %}
{% Icon color="ultramarine" label="ev_station" %}
{% Icon color="yellow" label="ev_station" %}
{% Icon color="purple" label="ev_station" %}
"""
        expected = """
<h2>2. Working with colors</h2>
<h3>2.1 Default inherit behaviour</h3>
<p>By default, icons inherit the color of their wrapping element:</p>
<p class="nj-icon-material-text" style="color: var(--nj-color-text-brand-primary);">
  Passing brand color through wrapping p tag
  <span aria-hidden="true" class="material-icons nj-icon-material">dashboard</span>
</p>

<hr>
<h3>2.2 Icon colors directly on the icon</h3>

<p>To use additional colors directly on the icon, you can use the color modifiers: <code>`nj-icon-material--{color}`</code> </p>
<p class="nj-icon-material-text">
  <code>nj-icon-material--primary</code> (grey-800):
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--primary">dashboard</span>
</p>
<p style="font-size: var(--nj-size-font-deci);">(this should be used with primary text which is grey 1000 so the icon doesn't drag too much attention)</p>
  <p class="nj-icon-material-text">
  <code>nj-icon-material--secondary</code> (grey-600):
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--secondary">dashboard</span>
</p>
<p class="nj-icon-material-text" style="background-color: var(--nj-color-background-high-contrast); color: var(--nj-color-text-inverse); padding: 4px;">
  <code>nj-icon-material--inverse</code> (grey-0):
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--inverse">dashboard</span>
</p>

<h4>2.2.1 Icon colors</h4>

<p class="nj-icon-material-text">
  Inherit
  <span aria-hidden="true" class="material-icons nj-icon-material">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Grey
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--grey">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Brand
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--brand">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Teal
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--teal">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Pink
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--pink">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Orange
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--orange">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Red
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--red">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Green
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--green">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Ultramarine
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--ultramarine">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Yellow
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--yellow">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Purple
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--purple">ev_station</span>
</p>

<span aria-hidden="true" class="material-icons nj-icon-material">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--grey">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--brand">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--teal">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--pink">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--orange">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--red">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--green">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--ultramarine">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--yellow">ev_station</span>
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--purple">ev_station</span>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<h2>3. Working with sizes</h2>
<p>
  For additional sizes, you can use the size modifiers:
  <code>`nj-icon-material--{size}`</code>
</p>
<p class="nj-icon-material-text">
  Small --sm
  {% Icon size="sm" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Medium (default)
  {% Icon label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Large --lg
  {% Icon size="lg" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  Extra large --xl
  {% Icon size="xl" label="ev_station" %}
</p>
<p class="nj-icon-material-text">
  2 Extra large --xxl
  {% Icon size="xxl" label="ev_station" %}
</p>
"""
        expected = """
<h2>3. Working with sizes</h2>
<p>For additional sizes, you can use the size modifiers: <code>`nj-icon-material--{size}`</code> </p>
<p class="nj-icon-material-text">
  Small --sm
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--sm">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Medium (default)
  <span aria-hidden="true" class="material-icons nj-icon-material">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Large --lg
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--lg">ev_station</span>
</p>
<p class="nj-icon-material-text">
  Extra large --xl
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--xl">ev_station</span>
</p>
<p class="nj-icon-material-text">
  2 Extra large --xxl
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--xxl">ev_station</span>
</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% Icon label="dashboard" %}
"""
        expected = """
<span aria-hidden="true" class="material-icons nj-icon-material">dashboard</span>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<p class="nj-icon-material-text">
  Example with text
  {% Icon label="dashboard" %}
</p>
"""
        expected = """
<p class="nj-icon-material-text">
  Example with text
  <span aria-hidden="true" class="material-icons nj-icon-material">dashboard</span>
</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<p class="nj-icon-material-text" style="color: var(--nj-color-text-brand-primary);">
  Passing brand color through wrapping p tag
  {% Icon label="dashboard" %}
</p>
"""
        expected = """
<p class="nj-icon-material-text" style="color: var(--nj-color-text-brand-primary);">
  Passing brand color through wrapping p tag
  <span aria-hidden="true" class="material-icons nj-icon-material">dashboard</span>
</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Icon color="grey" label="ev_station" %}
{% Icon color="brand" label="ev_station" %}
{% Icon color="teal" label="ev_station" %}
{% Icon color="pink" label="ev_station" %}
{% Icon color="orange" label="ev_station" %}
{% Icon color="red" label="ev_station" %}
{% Icon color="green" label="ev_station" %}
{% Icon color="ultramarine" label="ev_station" %}
{% Icon color="yellow" label="ev_station" %}
{% Icon color="purple" label="ev_station" %}
{% Icon color="lime" label="ev_station" %}
"""
        expected = """
<span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--grey">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--brand">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--teal">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--pink">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--orange">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--red">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--green">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--ultramarine">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--yellow">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--purple">ev_station</span>
  <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--lime">ev_station</span>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
<p class="nj-icon-material-text">
    Small --sm
    {% Icon size="sm" label="ev_station" %}
  </p>
  <p class="nj-icon-material-text">
    Medium (default)
    {% Icon label="ev_station" %}
  </p>
  <p class="nj-icon-material-text">
    Large --lg
    {% Icon size="lg" label="ev_station" %}
  </p>
  <p class="nj-icon-material-text">
    Extra large --xl
    {% Icon size="xl" label="ev_station" %}
  </p>
  <p class="nj-icon-material-text">
    2 Extra large --xxl
    {% Icon size="xxl" label="ev_station" %}
  </p>
"""
        expected = """
<p class="nj-icon-material-text">
    Small --sm
    <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--sm">ev_station</span>
  </p>
  <p class="nj-icon-material-text">
    Medium (default)
    <span aria-hidden="true" class="material-icons nj-icon-material">ev_station</span>
  </p>
  <p class="nj-icon-material-text">
    Large --lg
    <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--lg">ev_station</span>
  </p>
  <p class="nj-icon-material-text">
    Extra large --xl
    <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--xl">ev_station</span>
  </p>
  <p class="nj-icon-material-text">
    2 Extra large --xxl
    <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--xxl">ev_station</span>
  </p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
