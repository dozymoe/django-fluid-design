# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class StatusIndicatorTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% StatusIndicator %}
"""
        expected = """
<div class="nj-status-indicator">
  <div class="nj-status-indicator__svg"></div>
  <p class="nj-status-indicator__text">Online</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  {% StatusIndicator status="offline" %}
  {% StatusIndicator status="online" %}
  {% StatusIndicator status="away" %}
  {% StatusIndicator status="do-not-disturb" %}
  {% StatusIndicator status="busy" %}
  {% StatusIndicator status="unknown" %}
  {% StatusIndicator status="error" %}
  {% StatusIndicator status="success" %}
  {% StatusIndicator status="warning" %}
  {% StatusIndicator status="in-progress" %}
  {% StatusIndicator status="info" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  <div class="nj-status-indicator nj-status-indicator--offline">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Offline</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--online">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Online</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--away">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Away</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--do-not-disturb">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Do not disturb</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--busy">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Busy</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--unknown">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Unknown</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--error">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Error</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--success">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Success</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--warning">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Warning</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--in-progress">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">In progress</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--info">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Info</p>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  {% StatusIndicator size="sm" %}
  {% StatusIndicator %}
  {% StatusIndicator size="lg" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  <div class="nj-status-indicator nj-status-indicator--sm">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Online</p>
  </div>
  <div class="nj-status-indicator">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Online</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--lg">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Online</p>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  {% StatusIndicator nolabel=True status="offline" %}
  {% StatusIndicator nolabel=True status="online" %}
  {% StatusIndicator nolabel=True status="away" %}
  {% StatusIndicator nolabel=True status="do-not-disturb" %}
  {% StatusIndicator nolabel=True status="busy" %}
  {% StatusIndicator nolabel=True status="unknown" %}
  {% StatusIndicator nolabel=True status="error" %}
  {% StatusIndicator nolabel=True status="success" %}
  {% StatusIndicator nolabel=True status="warning" %}
  {% StatusIndicator nolabel=True status="in-progress" %}
  {% StatusIndicator nolabel=True status="info" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  <div class="nj-status-indicator nj-status-indicator--offline" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--online" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--away" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--do-not-disturb" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--busy" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--unknown" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--error" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--success" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--warning" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--in-progress" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--info" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  {% StatusIndicator status="offline" %}
  {% StatusIndicator status="online" %}
  {% StatusIndicator status="away" %}
  {% StatusIndicator status="do-not-disturb" %}
  {% StatusIndicator status="busy" %}
  {% StatusIndicator status="unknown" %}
  {% StatusIndicator status="error" %}
  {% StatusIndicator status="success" %}
  {% StatusIndicator status="warning" %}
  {% StatusIndicator status="in-progress" %}
  {% StatusIndicator status="info" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  <div class="nj-status-indicator nj-status-indicator--offline">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Offline</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--online">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Online</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--away">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Away</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--do-not-disturb">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Do not disturb</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--busy">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Busy</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--unknown">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Unknown</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--error">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Error</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--success">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Success</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--warning">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Warning</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--in-progress">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">In progress</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--info">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Info</p>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  {% StatusIndicator size="sm" %}
  {% StatusIndicator %}
  {% StatusIndicator size="lg" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  <div class="nj-status-indicator nj-status-indicator--sm">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Online</p>
  </div>
  <div class="nj-status-indicator">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Online</p>
  </div>
  <div class="nj-status-indicator nj-status-indicator--lg">
    <div class="nj-status-indicator__svg"></div>
    <p class="nj-status-indicator__text">Online</p>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  {% StatusIndicator nolabel=True status="offline" %}
  {% StatusIndicator nolabel=True status="online" %}
  {% StatusIndicator nolabel=True status="away" %}
  {% StatusIndicator nolabel=True status="do-not-disturb" %}
  {% StatusIndicator nolabel=True status="busy" %}
  {% StatusIndicator nolabel=True status="unknown" %}
  {% StatusIndicator nolabel=True status="error" %}
  {% StatusIndicator nolabel=True status="success" %}
  {% StatusIndicator nolabel=True status="warning" %}
  {% StatusIndicator nolabel=True status="in-progress" %}
  {% StatusIndicator nolabel=True status="info" %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 56px;">
  <div class="nj-status-indicator nj-status-indicator--offline" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--online" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--away" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--do-not-disturb" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--busy" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--unknown" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--error" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--success" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--warning" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--in-progress" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-status-indicator nj-status-indicator--info" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
