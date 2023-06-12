# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class CollapseTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Collapse id="test" %}
{% endCollapse %}
"""
        expected = """
<div class="nj-collapse" id="test">
  <div class="nj-card nj-card__body">
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div>
  {% CollapseBtn mode="anchor" target="#collapseExample" %}
    Link with href
  {% endCollapseBtn %}
  {% CollapseBtn target="#collapseExample" %}
    Button with data-target
  {% endCollapseBtn %}
</div>
{% Collapse id="collapseExample" %}
  Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
  richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes
  anderson cred nesciunt sapiente ea proident.
{% endCollapse %}
"""
        expected = """
<div>
  <a class="nj-btn" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    Link with href
  </a>
  <button class="nj-btn" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Button with data-target
  </button>
</div>
<div class="nj-collapse" id="collapseExample">
  <div class="nj-card nj-card__body">
    Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
  richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes
  anderson cred nesciunt sapiente ea proident.
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<p>
  {% CollapseBtn mode="anchor" target="#multiCollapseExample1" %}
    Toggle first element
  {% endCollapseBtn %}
  {% CollapseBtn target="#multiCollapseExample2" %}
    Toggle second element
  {% endCollapseBtn %}
  {% CollapseBtn target=".multi-collapse" controls="multiCollapseExample1 multiCollapseExample2" %}
    Toggle both elements
  {% endCollapseBtn %}
</p>
{% Row %}
  {% Col col="fill" %}
    {% Collapse id="multiCollapseExample1" class="multi-collapse" %}
      Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
      richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes
      anderson cred nesciunt sapiente ea proident.
    {% endCollapse %}
  {% endCol %}
  {% Col col="fill" %}
    {% Collapse id="multiCollapseExample2" class="multi-collapse" %}
      Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
      richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes
      anderson cred nesciunt sapiente ea proident.
    {% endCollapse %}
  {% endCol %}
{% endRow %}
"""
        expected = """
<p>
  <a class="nj-btn" data-toggle="collapse" href="#multiCollapseExample1" role="button" aria-expanded="false" aria-controls="multiCollapseExample1">Toggle first element</a>
  <button class="nj-btn" type="button" data-toggle="collapse" data-target="#multiCollapseExample2" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
  <button class="nj-btn" type="button" data-toggle="collapse" data-target=".multi-collapse" aria-expanded="false" aria-controls="multiCollapseExample1 multiCollapseExample2">Toggle both elements</button>
</p>
<div class="row">
  <div class="col">
    <div class="nj-collapse multi-collapse" id="multiCollapseExample1">
      <div class="nj-card nj-card__body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
      richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes
      anderson cred nesciunt sapiente ea proident.
      </div>
    </div>
  </div>
  <div class="col">
    <div class="nj-collapse multi-collapse" id="multiCollapseExample2">
      <div class="nj-card nj-card__body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
      richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes
      anderson cred nesciunt sapiente ea proident.
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
