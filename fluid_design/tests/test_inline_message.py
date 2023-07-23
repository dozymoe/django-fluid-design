# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class InlineMessageTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
"""
        expected = """
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  {% Message style="error" %}
    {% Slot 'title' %}Title <b>error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="info" %}
    {% Slot 'title' %}Title <b>info</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="success" %}
    {% Slot 'title' %}Title <b>success</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="warning" %}
    {% Slot 'title' %}Title <b>warning</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="fatal-error" %}
    {% Slot 'title' %}Title <b>fatal error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--inverse">remediation
    action</a>
  {% endMessage %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
<div class="nj-inline-message">
  <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--error" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>error</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
  </div>
</div>
<div class="nj-inline-message nj-inline-message--info">
  <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--info" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>info</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
  </div>
</div>
<div class="nj-inline-message nj-inline-message--success">
  <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--success" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>success</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
  </div>
</div>
<div class="nj-inline-message nj-inline-message--warning">
  <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--warning" aria-hidden="true">
    <div class="nj-status-indicator__svg"></div>
  </div>
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>warning</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
  </div>
</div>
<div class="nj-inline-message nj-inline-message--fatal-error">
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>fatal error</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--inverse">remediation
    action</a></p>
  </div>
</div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  {% Message style="error" icon=False %}
    {% Slot 'title' %}Title <b>error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="info" icon=False %}
    {% Slot 'title' %}Title <b>info</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="success" icon=False %}
    {% Slot 'title' %}Title <b>success</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="warning" icon=False %}
    {% Slot 'title' %}Title <b>warning</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="fatal-error" %}
    {% Slot 'title' %}Title <b>fatal error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--inverse">remediation
    action</a>
  {% endMessage %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
<div class="nj-inline-message">
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>error</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
  </div>
</div>
<div class="nj-inline-message nj-inline-message--info">
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>info</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
  </div>
</div>
<div class="nj-inline-message nj-inline-message--success">
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>success</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
  </div>
</div>
<div class="nj-inline-message nj-inline-message--warning">
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>warning</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
  </div>
</div>
<div class="nj-inline-message nj-inline-message--fatal-error">
  <div class="nj-inline-message__content">
     <h4 class="nj-inline-message__title">Title <b>fatal error</b> Message</h4>
     <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--inverse">remediation
    action</a></p>
  </div>
</div>
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  {% Message style="error" close=True %}
    {% Slot 'title' %}Title <b>error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="info" close=True %}
    {% Slot 'title' %}Title <b>info</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="success" close=True %}
    {% Slot 'title' %}Title <b>success</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="warning" close=True %}
    {% Slot 'title' %}Title <b>warning</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="fatal-error" close=True %}
    {% Slot 'title' %}Title <b>fatal error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--inverse">remediation
    action</a>
  {% endMessage %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  <div class="nj-inline-message">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--error" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
       <h4 class="nj-inline-message__title">Title <b>error</b> Message</h4>
       <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn">
        <span class="nj-sr-only">Hide message</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-inline-message nj-inline-message--info">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--info" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
       <h4 class="nj-inline-message__title">Title <b>info</b> Message</h4>
       <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn">
        <span class="nj-sr-only">Hide message</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-inline-message nj-inline-message--success">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--success" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
       <h4 class="nj-inline-message__title">Title <b>success</b> Message</h4>
       <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn">
        <span class="nj-sr-only">Hide message</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-inline-message nj-inline-message--warning">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--warning" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
       <h4 class="nj-inline-message__title">Title <b>warning</b> Message</h4>
       <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn">
        <span class="nj-sr-only">Hide message</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-inline-message nj-inline-message--fatal-error">
    <div class="nj-inline-message__content">
       <h4 class="nj-inline-message__title">Title <b>fatal error</b> Message</h4>
       <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--inverse">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn nj-icon-btn--inverse">
        <span class="nj-sr-only">Hide message</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  {% Message style="error" %}
    {% Slot 'title' %}Title <b>error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="info" %}
    {% Slot 'title' %}Title <b>info</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="success" %}
    {% Slot 'title' %}Title <b>success</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="warning" %}
    {% Slot 'title' %}Title <b>warning</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="fatal-error" %}
    {% Slot 'title' %}Title <b>fatal error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--inverse">remediation
    action</a>
  {% endMessage %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  <div class="nj-inline-message">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--error" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>error</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
  </div>
  <div class="nj-inline-message nj-inline-message--info">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--info" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>info</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
  </div>
  <div class="nj-inline-message nj-inline-message--success">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--success" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>success</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
  </div>
  <div class="nj-inline-message nj-inline-message--warning">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--warning" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>warning</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
  </div>
  <div class="nj-inline-message nj-inline-message--fatal-error">
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>fatal error</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--inverse">remediation
    action</a></p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  {% Message style="error" icon=False %}
    {% Slot 'title' %}Title <b>error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="info" icon=False %}
    {% Slot 'title' %}Title <b>info</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="success" icon=False %}
    {% Slot 'title' %}Title <b>success</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="warning" icon=False %}
    {% Slot 'title' %}Title <b>warning</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="fatal-error" %}
    {% Slot 'title' %}Title <b>fatal error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--inverse">remediation
    action</a>
  {% endMessage %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  <div class="nj-inline-message">
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>error</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
  </div>
  <div class="nj-inline-message nj-inline-message--info">
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>info</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
  </div>
  <div class="nj-inline-message nj-inline-message--success">
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>success</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
  </div>
  <div class="nj-inline-message nj-inline-message--warning">
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>warning</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
  </div>
  <div class="nj-inline-message nj-inline-message--fatal-error">
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>fatal error</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--inverse">remediation
    action</a></p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  {% Message style="error" close=True %}
    {% Slot 'title' %}Title <b>error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="info" close=True %}
    {% Slot 'title' %}Title <b>info</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="success" close=True %}
    {% Slot 'title' %}Title <b>success</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="warning" close=True %}
    {% Slot 'title' %}Title <b>warning</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a>
  {% endMessage %}
  {% Message style="fatal-error" close=True %}
    {% Slot 'title' %}Title <b>fatal error</b> Message{% endSlot %}
  
    Message description or <a class="nj-link nj-link--inverse">remediation
    action</a>
  {% endMessage %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; flex-wrap: wrap; gap: 24px;">
  <div class="nj-inline-message">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--error" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>error</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn">
      <span class="nj-sr-only">Hide message</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-inline-message nj-inline-message--info">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--info" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>info</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn">
      <span class="nj-sr-only">Hide message</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-inline-message nj-inline-message--success">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--success" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>success</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn">
      <span class="nj-sr-only">Hide message</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-inline-message nj-inline-message--warning">
    <div class="nj-inline-message__status nj-status-indicator nj-status-indicator--warning" aria-hidden="true">
      <div class="nj-status-indicator__svg"></div>
    </div>
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>warning</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--high-contrast">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn">
      <span class="nj-sr-only">Hide message</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-inline-message nj-inline-message--fatal-error">
    <div class="nj-inline-message__content">
      <h4 class="nj-inline-message__title">Title <b>fatal error</b> Message</h4>
      <p class="nj-inline-message__body">Message description or <a class="nj-link nj-link--inverse">remediation
    action</a></p>
    </div>
    <button class="nj-inline-message__close nj-icon-btn nj-icon-btn--inverse">
      <span class="nj-sr-only">Hide message</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
