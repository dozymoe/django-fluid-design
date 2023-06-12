# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class GridTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Grid %}{% endGrid %}
"""
        expected = """
<div class="container"></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  <example>
	{% Grid %}
      {% Row %}
        {% Col sm="fill" %}One of three columns{% endCol %}
        {% Col sm="fill" %}One of three columns{% endCol %}
        {% Col sm="fill" %}One of three columns{% endCol %}
      {% endRow %}
    {% endGrid %}
  </example>
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
  <example>
    <div class="container">
      <div class="row">
        <div class="col-sm">
          One of three columns
        </div>
        <div class="col-sm">
          One of three columns
        </div>
        <div class="col-sm">
          One of three columns
        </div>
      </div>
    </div>
  </example>
</div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Grid %}
    {% Row %}
      {% Col col="fill" %}1 of 2{% endCol %}
      {% Col col="fill" %}2 of 2{% endCol %}
    {% endRow %}
    {% Row %}
      {% Col col="fill" %}1 of 3{% endCol %}
      {% Col col="fill" %}2 of 3{% endCol %}
      {% Col col="fill" %}3 of 3{% endCol %}
    {% endRow %}
  {% endGrid %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="container">
  <div class="row">
    <div class="col">
      1 of 2
    </div>
    <div class="col">
      2 of 2
    </div>
  </div>
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col">
      2 of 3
    </div>
    <div class="col">
      3 of 3
    </div>
  </div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Grid %}
    {% Row %}
      {% Col col="fill" %}1 of 3{% endCol %}
      {% Col col=6 %}2 of 3 (wider){% endCol %}
      {% Col col="fill" %}3 of 3{% endCol %}
    {% endRow %}
    {% Row %}
      {% Col col="fill" %}1 of 3{% endCol %}
      {% Col col=5 %}2 of 3 (wider){% endCol %}
      {% Col col="fill" %}3 of 3{% endCol %}
    {% endRow %}
  {% endGrid %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="container">
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col-6">
      2 of 3 (wider)
    </div>
    <div class="col">
      3 of 3
    </div>
  </div>
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col-5">
      2 of 3 (wider)
    </div>
    <div class="col">
      3 of 3
    </div>
  </div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Grid %}
    {% Row align_md="center" %}
      {% Col col="fill" lg=2 %}1 of 3{% endCol %}
      {% Col md="shrink" %}Variable width content{% endCol %}
      {% Col col="fill" lg=2 %}3 of 3{% endCol %}
    {% endRow %}
    {% Row %}
      {% Col col="fill" %}1 of 3{% endCol %}
      {% Col md="shrink" %}Variable width content{% endCol %}
      {% Col col="fill" lg=2 %}3 of 3{% endCol %}
    {% endRow %}
  {% endGrid %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="container">
  <div class="row justify-content-md-center">
    <div class="col col-lg-2">
      1 of 3
    </div>
    <div class="col-md-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>
  </div>
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col-md-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>
  </div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row %}
    {% Col col="fill" %}col{% endCol %}
    {% Col col="fill" %}col{% endCol %}
    {% Col class="w-100" %}{% endCol %}
    {% Col col="fill" %}col{% endCol %}
    {% Col col="fill" %}col{% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row">
  <div class="col">col</div>
  <div class="col">col</div>
  <div class="w-100"></div>
  <div class="col">col</div>
  <div class="col">col</div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row %}
    {% Col col="fill" %}col{% endCol %}
    {% Col col="fill" %}col{% endCol %}
    {% Col col="fill" %}col{% endCol %}
    {% Col col="fill" %}col{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col col=8 %}col-8{% endCol %}
    {% Col col=4 %}col-4{% endCol %}
  {% endRow %}
  <p>Stacked to horizontal</p>
  {% Row %}
    {% Col sm=8 %}col-sm-8{% endCol %}
    {% Col sm=4 %}col-sm-4{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col sm="fill" %}col-sm{% endCol %}
    {% Col sm="fill" %}col-sm{% endCol %}
    {% Col sm="fill" %}col-sm{% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row">
  <div class="col">col</div>
  <div class="col">col</div>
  <div class="col">col</div>
  <div class="col">col</div>
</div>
<div class="row">
  <div class="col-8">col-8</div>
  <div class="col-4">col-4</div>
</div>
<p>Stacked to horizontal</p>
<div class="row">
  <div class="col-sm-8">col-sm-8</div>
  <div class="col-sm-4">col-sm-4</div>
</div>
<div class="row">
  <div class="col-sm">col-sm</div>
  <div class="col-sm">col-sm</div>
  <div class="col-sm">col-sm</div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row %}
    {% Col col=12 md=8 %}.col-12 .col-md-8{% endCol %}
    {% Col col=6 md=4 %}.col-6 .col-md-4{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col col=6 md=4 %}.col-6 .col-md-4{% endCol %}
    {% Col col=6 md=4 %}.col-6 .col-md-4{% endCol %}
    {% Col col=6 md=4 %}.col-6 .col-md-4{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col col=6 %}.col-6{% endCol %}
    {% Col col=6 %}.col-6{% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row">
  <div class="col-12 col-md-8">.col-12 .col-md-8</div>
  <div class="col-6 col-md-4">.col-6 .col-md-4</div>
</div>
<div class="row">
  <div class="col-6 col-md-4">.col-6 .col-md-4</div>
  <div class="col-6 col-md-4">.col-6 .col-md-4</div>
  <div class="col-6 col-md-4">.col-6 .col-md-4</div>
</div>
<div class="row">
  <div class="col-6">.col-6</div>
  <div class="col-6">.col-6</div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row njd-example-row-flex-cols"><div class="njd-example">
  {% Grid %}
    {% Row valign_col="start" %}
      {% Col col="fill" %}One of three columns{% endCol %}
      {% Col col="fill" %}One of three columns{% endCol %}
      {% Col col="fill" %}One of three columns{% endCol %}
    {% endRow %}
    {% Row valign_col="center" %}
      {% Col col="fill" %}One of three columns{% endCol %}
      {% Col col="fill" %}One of three columns{% endCol %}
      {% Col col="fill" %}One of three columns{% endCol %}
    {% endRow %}
    {% Row valign_col="end" %}
      {% Col col="fill" %}One of three columns{% endCol %}
      {% Col col="fill" %}One of three columns{% endCol %}
      {% Col col="fill" %}One of three columns{% endCol %}
    {% endRow %}
  {% endGrid %}
</div></div>
"""
        expected = """
<div class="njd-example-row njd-example-row-flex-cols"><div class="njd-example">
<div class="container">
  <div class="row align-items-start">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
  <div class="row align-items-center">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
  <div class="row align-items-end">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Grid %}
    {% Row align_col="start" %}
      {% Col col=4 %}One of two columns{% endCol %}
      {% Col col=4 %}One of two columns{% endCol %}
    {% endRow %}
    {% Row align_col="center" %}
      {% Col col=4 %}One of two columns{% endCol %}
      {% Col col=4 %}One of two columns{% endCol %}
    {% endRow %}
    {% Row align_col="end" %}
      {% Col col=4 %}One of two columns{% endCol %}
      {% Col col=4 %}One of two columns{% endCol %}
    {% endRow %}
    {% Row align_col="around" %}
      {% Col col=4 %}One of two columns{% endCol %}
      {% Col col=4 %}One of two columns{% endCol %}
    {% endRow %}
    {% Row align_col="between" %}
      {% Col col=4 %}One of two columns{% endCol %}
      {% Col col=4 %}One of two columns{% endCol %}
    {% endRow %}
  {% endGrid %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="container">
  <div class="row justify-content-start">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
  <div class="row justify-content-center">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
  <div class="row justify-content-end">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
  <div class="row justify-content-around">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
  <div class="row justify-content-between">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row gutter=False %}
    {% Col col=12 sm=6 md=8 %}.col-12 .col-sm-6 .col-md-8{% endCol %}
    {% Col col=6 md=4 %}.col-6 .col-md-4{% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row no-gutters">
  <div class="col-12 col-sm-6 col-md-8">.col-12 .col-sm-6 .col-md-8</div>
  <div class="col-6 col-md-4">.col-6 .col-md-4</div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example11(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row %}
    {% Col col=9 %}.col-9{% endCol %}
    {% Col col=4 %}
      .col-4<br>Since 9 + 4 = 13 &gt; 12, this 4-column-wide div gets wrapped
      onto a new line as one contiguous unit.
    {% endCol %}
    {% Col col=6 %}
      .col-6<br>Subsequent columns continue along the new line.
    {% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row">
  <div class="col-9">.col-9</div>
  <div class="col-4">
      .col-4<br>Since 9 + 4 = 13 &gt; 12, this 4-column-wide div gets wrapped
      onto a new line as one contiguous unit.
  </div>
  <div class="col-6">.col-6<br>Subsequent columns continue along the new line.</div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example12(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row %}
    {% Col col=6 sm=3 %}.col-6 .col-sm-3{% endCol %}
    {% Col col=6 sm=3 %}.col-6 .col-sm-3{% endCol %}
    {% Col class="w-100" %}{% endCol %}
    {% Col col=6 sm=3 %}.col-6 .col-sm-3{% endCol %}
    {% Col col=6 sm=3 %}.col-6 .col-sm-3{% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row">
  <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
  <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>

  <div class="w-100"></div>

  <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
  <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example13(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Grid %}
    {% Row %}
      {% Col col="fill" %}First, but unordered{% endCol %}
      {% Col col="fill" order=12 %}Second, but last{% endCol %}
      {% Col col="fill" order=1 %}Third, but first{% endCol %}
    {% endRow %}
  {% endGrid %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="container">
  <div class="row">
    <div class="col">
      First, but unordered
    </div>
    <div class="col order-12">
      Second, but last
    </div>
    <div class="col order-1">
      Third, but first
    </div>
  </div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example14(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row %}
    {% Col md=4 %}.col-md-4{% endCol %}
    {% Col md=4 offset_md=4 %}.col-md-4 .offset-md-4{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col md=3 offset_md=3 %}.col-md-3 .offset-md-3{% endCol %}
    {% Col md=3 offset_md=3 %}.col-md-3 .offset-md-3{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col md=6 offset_md=3 %}.col-md-6 .offset-md-3{% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row">
  <div class="col-md-4">.col-md-4</div>
  <div class="col-md-4 offset-md-4">.col-md-4 .offset-md-4</div>
</div>
<div class="row">
  <div class="col-md-3 offset-md-3">.col-md-3 .offset-md-3</div>
  <div class="col-md-3 offset-md-3">.col-md-3 .offset-md-3</div>
</div>
<div class="row">
  <div class="col-md-6 offset-md-3">.col-md-6 .offset-md-3</div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example15(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row %}
    {% Col md=4 %}.col-md-4{% endCol %}
    {% Col md=4 ml_col="auto" %}.col-md-4 .ml-auto{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col md=3 ml_md="auto" %}.col-md-3 .ml-md-auto{% endCol %}
    {% Col md=3 ml_md="auto" %}.col-md-3 .ml-md-auto{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col col="shrink" mr_col="auto" %}.col-auto .mr-auto{% endCol %}
    {% Col col="shrink" %}.col-auto{% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row">
  <div class="col-md-4">.col-md-4</div>
  <div class="ml-auto col-md-4">.col-md-4 .ml-auto</div>
</div>
<div class="row">
  <div class="col-md-3 ml-md-auto">.col-md-3 .ml-md-auto</div>
  <div class="col-md-3 ml-md-auto">.col-md-3 .ml-md-auto</div>
</div>
<div class="row">
  <div class="col-auto mr-auto">.col-auto .mr-auto</div>
  <div class="col-auto">.col-auto</div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example16(self):
        template = """
{% load fluid_design %}
<div class="njd-example-row"><div class="njd-example">
  {% Row %}
    {% Col sm=9 %}
      Level 1: .col-sm-9

      {% Row %}
        {% Col col=8 sm=6 %}
          Level 2: .col-8 .col-sm-6
        {% endCol %}
        {% Col col=4 sm=6 %}
          Level 2: .col-4 .col-sm-6
        {% endCol %}
      {% endRow %}
    {% endCol %}
  {% endRow %}
</div></div>
"""
        expected = """
<div class="njd-example-row"><div class="njd-example">
<div class="row">
  <div class="col-sm-9">
    Level 1: .col-sm-9
    <div class="row">
      <div class="col-8 col-sm-6">
        Level 2: .col-8 .col-sm-6
      </div>
      <div class="col-4 col-sm-6">
        Level 2: .col-4 .col-sm-6
      </div>
    </div>
  </div>
</div></div></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
