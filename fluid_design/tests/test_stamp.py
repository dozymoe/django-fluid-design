# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class StampTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Stamp id="nj-stamp" %}
"""
        expected = """
<svg class="nj-stamp" xmlns="http://www.w3.org/2000/svg">
  <defs>
   <mask height="100%" id="nj-stamp-mask" width="100%" x="0" y="0">
    <circle class="nj-stamp__overlay" cx="85" cy="85" r="85">
    </circle>
    <text class="nj-stamp__text" transform="translate(85)" y="67">
     <tspan text-anchor="middle" x="0">
     </tspan>
    </text>
   </mask>
  </defs>
  <circle cx="85" cy="85" fill="#fff" mask="url(#nj-stamp-mask)" r="85">
  </circle>
</svg>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="display: flex; justify-content: center; align-items: center; background:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg) 0 0 no-repeat;width: 500px;height: 250px;background-size: cover;">
  {% Stamp id="nj-stamp" label="#Act With ENGIE" gradient="#0af #23d2b5" %}
</div>
"""
        expected = """
<div style="display: flex; justify-content: center; align-items: center; background:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg) 0 0 no-repeat;width: 500px;height: 250px;background-size: cover;">
<svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp">
  <defs>
     <linearGradient id="nj-stamp-gradient" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#0af"/>
      <stop offset="100%" stop-color="#23d2b5"/>
    </linearGradient>
    <mask id="nj-stamp-mask" x="0" y="0" width="100%" height="100%">
      <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
      <text class="nj-stamp__text" y="67" transform="translate(85)">
        <tspan x="0" text-anchor="middle">#Act</tspan>
        <tspan x="0" text-anchor="middle" dy="28">With</tspan>
        <tspan x="0" text-anchor="middle" dy="28">ENGIE</tspan>
      </text>
    </mask>
  </defs>
  <circle cx="85" cy="85" r="85" fill="url(#nj-stamp-gradient)" mask="url(#nj-stamp-mask)"/>
</svg>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: flex; justify-content: center; align-items: center; background:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg) 0 0 no-repeat;width: 500px;height: 250px;background-size: cover;">
  {% Stamp label="#Act With ENGIE" id="nj-stamp" %}
</div>
"""
        expected = """
<div style="display: flex; justify-content: center; align-items: center; background:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg) 0 0 no-repeat;width: 500px;height: 250px;background-size: cover;">
<svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp">
  <defs>
    <mask id="nj-stamp-mask" x="0" y="0" width="100%" height="100%">
      <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
      <text class="nj-stamp__text" y="67" transform="translate(85)">
        <tspan x="0" text-anchor="middle">#Act</tspan>
        <tspan x="0" text-anchor="middle" dy="28">With</tspan>
        <tspan x="0" text-anchor="middle" dy="28">ENGIE</tspan>
      </text>
    </mask>
  </defs>
  <circle cx="85" cy="85" r="85" fill="#fff" mask="url(#nj-stamp-mask)"/>
</svg>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="display: flex; justify-content: center; align-items: center; background-color: var(--nj-color-background-brand); width: 500px;height: 250px;">
  {% Stamp label="#Act With ENGIE" gradient="#0af #23d2b5" shadow=True id="nj-stamp" %}
</div>
"""
        expected = """
<div style="display: flex; justify-content: center; align-items: center; background-color: var(--nj-color-background-brand); width: 500px;height: 250px;">
  <svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp nj-stamp--shadow">
  <defs>
     <linearGradient id="nj-stamp-gradient" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#0af"/>
      <stop offset="100%" stop-color="#23d2b5"/>
    </linearGradient>
    <mask id="nj-stamp-mask" x="0" y="0" width="100%" height="100%">
      <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
      <text class="nj-stamp__text" y="67" transform="translate(85)">
        <tspan x="0" text-anchor="middle">#Act</tspan>
        <tspan x="0" text-anchor="middle" dy="28">With</tspan>
        <tspan x="0" text-anchor="middle" dy="28">ENGIE</tspan>
      </text>
    </mask>
  </defs>
  <circle cx="85" cy="85" r="85" fill="url(#nj-stamp-gradient)" mask="url(#nj-stamp-mask)"/>
</svg>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% Stamp label="#Act With ENGIE" gradient="#0af #23d2b5" id="nj-stamp" %}
"""
        expected = """
<svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp">
  <defs>
     <linearGradient id="nj-stamp-gradient" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#0af"/>
      <stop offset="100%" stop-color="#23d2b5"/>
    </linearGradient>
    <mask id="nj-stamp-mask" x="0" y="0" width="100%" height="100%">
      <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
      <text class="nj-stamp__text" y="67" transform="translate(85)">
        <tspan x="0" text-anchor="middle">#Act</tspan>
        <tspan x="0" text-anchor="middle" dy="28">With</tspan>
        <tspan x="0" text-anchor="middle" dy="28">ENGIE</tspan>
      </text>
    </mask>
  </defs>
  <circle cx="85" cy="85" r="85" fill="url(#nj-stamp-gradient)" mask="url(#nj-stamp-mask)"/>
</svg>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Stamp label="#Act With ENGIE" gradient="#0af #23d2b5" id="nj-stamp" %}
"""
        expected = """
  <svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp">
    <defs>
       <linearGradient id="nj-stamp-gradient" x1="0" x2="1" y1="0" y2="1">
        <stop offset="0%" stop-color="#0af"/>
        <stop offset="100%" stop-color="#23d2b5"/>
      </linearGradient>
      <mask id="nj-stamp-mask" x="0" y="0" width="100%" height="100%">
        <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
        <text class="nj-stamp__text" y="67" transform="translate(85)">
          <tspan x="0" text-anchor="middle">#Act</tspan>
          <tspan x="0" text-anchor="middle" dy="28">With</tspan>
          <tspan x="0" text-anchor="middle" dy="28">ENGIE</tspan>
        </text>
      </mask>
    </defs>
    <circle cx="85" cy="85" r="85" fill="url(#nj-stamp-gradient)" mask="url(#nj-stamp-mask)"/>
  </svg>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Stamp label="#Act With ENGIE*" gradient="#0af #23d2b5" id="nj-stamp" %}
"""
        expected = """
<svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp">
  <defs>
      <linearGradient id="nj-stamp-gradient" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#0af"/>
      <stop offset="100%" stop-color="#23d2b5"/>
    </linearGradient>
    <mask id="nj-stamp-mask" x="0" y="0" width="100%" height="100%">
      <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
      <text class="nj-stamp__text" y="67" transform="translate(85)">
        <tspan x="0" text-anchor="middle">#Act</tspan>
        <tspan x="0" text-anchor="middle" dy="28">With</tspan>
        <tspan x="0" text-anchor="middle" dy="28">ENGIE*</tspan>
      </text>
    </mask>
  </defs>
  <circle cx="85" cy="85" r="85" fill="url(#nj-stamp-gradient)" mask="url(#nj-stamp-mask)"/>
</svg>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
<div>
  {% Stamp label="#Act With ENGIE" id="nj-stamp" %}
</div>
"""
        expected = """
<div>
  <svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp">
    <defs>
      <mask id="nj-stamp-mask" x="0" y="0" width="100%" height="100%">
        <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
        <text class="nj-stamp__text" y="67" transform="translate(85)">
          <tspan x="0" text-anchor="middle">#Act</tspan>
          <tspan x="0" text-anchor="middle" dy="28">With</tspan>
          <tspan x="0" text-anchor="middle" dy="28">ENGIE</tspan>
        </text>
      </mask>
    </defs>
    <circle cx="85" cy="85" r="85" fill="#fff" mask="url(#nj-stamp-mask)"/>
  </svg>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
<div>
  {% Stamp label="#Act With ENGIE" gradient="#0af #23d2b5" id="nj-stamp" shadow=True %}
</div>
"""
        expected = """
<div>
  <svg xmlns="http://www.w3.org/2000/svg" class="nj-stamp nj-stamp--shadow">
    <defs>
       <linearGradient id="nj-stamp-gradient" x1="0" x2="1" y1="0" y2="1">
        <stop offset="0%" stop-color="#0af"/>
        <stop offset="100%" stop-color="#23d2b5"/>
      </linearGradient>
      <mask id="nj-stamp-mask" x="0" y="0" width="100%" height="100%">
        <circle class="nj-stamp__overlay" cx="85" cy="85" r="85"/>
        <text class="nj-stamp__text" y="67" transform="translate(85)">
          <tspan x="0" text-anchor="middle">#Act</tspan>
          <tspan x="0" text-anchor="middle" dy="28">With</tspan>
          <tspan x="0" text-anchor="middle" dy="28">ENGIE</tspan>
        </text>
      </mask>
    </defs>
    <circle cx="85" cy="85" r="85" fill="url(#nj-stamp-gradient)" mask="url(#nj-stamp-mask)"/>
  </svg>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
