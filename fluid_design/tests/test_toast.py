# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ToastTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Toast %}{% endToast %}
"""
        expected = """
<div class="nj-toast">
  <div class="nj-toast__body">
   <div class="nj-toast__content">
   </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="display: flex; gap: 16px; flex-direction: column; margin-bottom: 48px; width: 360px;">
  {% Toast content_id="toast-1" btncolor="inverse" %}
    {% ToastText id="toast-1" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
  {% Toast content_id="toast-2" btncolor="inverse" %}
    {% ToastText id="toast-2" %}Rows successfully inserted{% endToastText %}

    {% Slot 'icon' %}
      {% Icon label="check" %}
    {% endSlot %}
  {% endToast %}
  {% Toast content_id="toast-3" btncolor="inverse" %}
    {% ToastTitle id="toast-3" %}Your table has been updated !{% endToastTitle %}
    {% ToastText %}Rows successfully inserted{% endToastText %}
  {% endToast %}
  {% Toast content_id="toast-4" btncolor="inverse" %}
    {% ToastTitle id="toast-4" %}Your table has been updated !{% endToastTitle %}
    {% ToastText %}Rows successfully inserted{% endToastText %}

    {% Slot 'icon' %}
      {% Icon label="check" %}
    {% endSlot %}
  {% endToast %}
</div>
"""
        expected = """
<div style="display: flex; gap: 16px; flex-direction: column; margin-bottom: 48px; width: 360px;">
  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-1">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-1">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>

  <div class="nj-toast">
    <div class="nj-toast__body">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-toast__icon">check</span>
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-2">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-2">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>

  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__title" id="toast-3">Your table has been updated !</p>
        <p class="nj-toast__text">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-3">
        <span class="nj-sr-only">Close notification</span>
       <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>

  <div class="nj-toast">
    <div class="nj-toast__body">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-toast__icon">check</span>
      <div class="nj-toast__content">
        <p class="nj-toast__title" id="toast-4">Your table has been updated !</p>
        <p class="nj-toast__text">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-4">
        <span class="nj-sr-only">Close notification</span>
       <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="width: 100%; padding: 48px; background-color: var(--nj-color-palette-ultramarine-800);">
  <div style="display: flex; gap: 16px; flex-direction: column; margin-bottom: 48px; width: 360px;">
    <p style="color: var(--nj-color-text-inverse);">Inverse toasts should be used on a darker surface</p>
    {% Toast content_id="toast-5" color="inverse" %}
      {% ToastText id="toast-5" %}Rows successfully inserted{% endToastText %}
    {% endToast %}
    {% Toast content_id="toast-6" color="inverse" %}
      {% ToastText id="toast-6" %}Rows successfully inserted{% endToastText %}

      {% Slot 'icon' %}
        {% Icon label="check" %}
      {% endSlot %}
    {% endToast %}
    {% Toast content_id="toast-7" color="inverse" %}
      {% ToastTitle id="toast-7" %}Your table has been updated !{% endToastTitle %}
      {% ToastText %}Rows successfully inserted{% endToastText %}
    {% endToast %}
    {% Toast content_id="toast-8" color="inverse" %}
      {% ToastTitle id="toast-8" %}Your table has been updated !{% endToastTitle %}
      {% ToastText %}Rows successfully inserted{% endToastText %}

      {% Slot 'icon' %}
        {% Icon label="check" %}
      {% endSlot %}
    {% endToast %}
  </div>
</div>
"""
        expected = """
<div style="width: 100%; padding: 48px; background-color: var(--nj-color-palette-ultramarine-800);">
  <div style="display: flex; gap: 16px; flex-direction: column; margin-bottom: 48px; width: 360px;">
    <p style="color: var(--nj-color-text-inverse);">Inverse toasts should be used on a darker surface</p>

    <div class="nj-toast nj-toast--inverse">
      <div class="nj-toast__body">
        <div class="nj-toast__content">
          <p class="nj-toast__text" id="toast-5">Rows successfully inserted</p>
        </div>
      </div>
      <div class="nj-toast__action">
        <button type="button" class="nj-icon-btn nj-icon-btn--lg" aria-describedby="toast-5">
          <span class="nj-sr-only">Close notification</span>
         <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
    </div>

    <div class="nj-toast nj-toast--inverse">
      <div class="nj-toast__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-toast__icon">check</span>
        <div class="nj-toast__content">
          <p class="nj-toast__text" id="toast-6">Rows successfully inserted</p>
        </div>
      </div>
      <div class="nj-toast__action">
        <button type="button" class="nj-icon-btn nj-icon-btn--lg" aria-describedby="toast-6">
          <span class="nj-sr-only">Close notification</span>
         <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
    </div>

    <div class="nj-toast nj-toast--inverse">
      <div class="nj-toast__body">
        <div class="nj-toast__content">
          <p class="nj-toast__title" id="toast-7">Your table has been updated !</p>
          <p class="nj-toast__text">Rows successfully inserted</p>
        </div>
      </div>
      <div class="nj-toast__action">
        <button type="button" class="nj-icon-btn nj-icon-btn--lg" aria-describedby="toast-7">
          <span class="nj-sr-only">Close notification</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
    </div>

    <div class="nj-toast nj-toast--inverse">
      <div class="nj-toast__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-toast__icon">check</span>
        <div class="nj-toast__content">
          <p class="nj-toast__title" id="toast-8">Your table has been updated !</p>
          <p class="nj-toast__text">Rows successfully inserted</p>
        </div>
      </div>
      <div class="nj-toast__action">
        <button type="button" class="nj-icon-btn nj-icon-btn--lg" aria-describedby="toast-8">
          <span class="nj-sr-only">Close notification</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="min-height: 70vh; max-height: 80vh; transform: translateZ(0); overflow: auto;">
<div class="nj-sr-only" aria-live="polite" aria-atomic="true">
  <p>3 notifications</p>
</div>
{% ToastContainer label="Notification area (3)" %}
  {% Toast content_id="toast-1" btncolor="inverse" %}
    {% ToastText id="toast-1" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
  {% Toast content_id="toast-2" btncolor="inverse" %}
    {% ToastText id="toast-2" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
  {% Toast content_id="toast-3" btncolor="inverse" %}
    {% ToastText id="toast-3" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
{% endToastContainer %}
</div>
"""
        expected = """
<div style="min-height: 70vh; max-height: 80vh; transform: translateZ(0); overflow: auto;">
<div class="nj-sr-only" aria-live="polite" aria-atomic="true">
  <p>3 notifications</p>
</div>

<div class="nj-toast__container" role="region" aria-label="Notification area (3)">
  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-1">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-1">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>

  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-2">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-2">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>

  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-3">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-3">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>
</div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="min-height: 70vh; max-height: 80vh; transform: translateZ(0); overflow: auto;">
<div class="nj-sr-only" aria-live="polite" aria-atomic="true">
  <p>3 notifications</p>
</div>
{% ToastContainer label="Notification area (3)" fullwidth=True %}
  {% Toast content_id="toast-5" btncolor="inverse" %}
    {% ToastText id="toast-5" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
  {% Toast content_id="toast-6" btncolor="inverse" %}
    {% ToastText id="toast-6" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
  {% Toast content_id="toast-7" btncolor="inverse" %}
    {% ToastText id="toast-7" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
{% endToastContainer %}
</div>
"""
        expected = """
<div style="min-height: 70vh; max-height: 80vh; transform: translateZ(0); overflow: auto;">

<div class="nj-sr-only" aria-live="polite" aria-atomic="true">
  <p>3 notifications</p>
</div>

<div class="nj-toast__container nj-toast__container--full-width" role="region" aria-label="Notification area (3)">
  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-5">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-5">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>

  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-6">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-6">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>

  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-7">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-7">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>
</div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Toast content_id="toast-1" gauge=5 btncolor="inverse" %}
  {% ToastText id="toast-1" %}Rows successfully inserted{% endToastText %}
{% endToast %}
"""
        expected = """
<div class="nj-toast">
  <div class="nj-toast__body">
    <div class="nj-toast__content">
      <p class="nj-toast__text" id="toast-1">Rows successfully inserted</p>
    </div>
  </div>
  <div class="nj-toast__action">
    <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-1">
      <span class="nj-sr-only">Close notification</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-toast__gauge">
    <div class="nj-toast__gauge-bar">
      <p class="nj-sr-only">The toast will be automatically closed in 5s</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<div style="display: flex; gap: 16px; flex-direction: column;">
  {% Toast content_id="toast-1" gauge=5 btncolor="inverse" %}
    {% ToastText id="toast-1" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
  {% Toast content_id="toast-5" gauge=5 color="inverse" btncolor="secondary" %}
    {% ToastText id="toast-5" %}Rows successfully inserted{% endToastText %}
  {% endToast %}
</div>
"""
        expected = """
<div style="display: flex; gap: 16px; flex-direction: column;">
  <div class="nj-toast">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-1">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-1">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-toast__gauge">
      <div class="nj-toast__gauge-bar">
        <p class="nj-sr-only">The toast will be automatically closed in 5s</p>
      </div>
    </div>
  </div>

  <div class="nj-toast nj-toast--inverse">
    <div class="nj-toast__body">
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-5">Rows successfully inserted</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary" aria-describedby="toast-5">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-toast__gauge">
      <div class="nj-toast__gauge-bar">
        <p class="nj-sr-only">The toast will be automatically closed in 5s</p>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Toast content_id="toast-3" gauge=5 btncolor="inverse" %}
  {% ToastTitle id="toast-3" %}Your table has been updated !{% endToastTitle %}
  {% ToastText %}Rows successfully inserted{% endToastText %}
{% endToast %}
"""
        expected = """
<div class="nj-toast">
  <div class="nj-toast__body">
    <div class="nj-toast__content">
      <p class="nj-toast__title" id="toast-3">Your table has been updated !</p>
      <p class="nj-toast__text">Rows successfully inserted</p>
    </div>
  </div>
  <div class="nj-toast__action">
    <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-3">
      <span class="nj-sr-only">Close notification</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-toast__gauge">
    <div class="nj-toast__gauge-bar">
      <p class="nj-sr-only">The toast will be automatically closed in 5s</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Toast content_id="toast-4" gauge=5 btncolor="inverse" %}
  {% ToastTitle id="toast-4" %}Your table has been updated !{% endToastTitle %}
  {% ToastText %}Rows successfully inserted{% endToastText %}

  {% Slot 'icon' %}
    {% Icon label="check" %}
  {% endSlot %}
{% endToast %}
"""
        expected = """
<div class="nj-toast">
  <div class="nj-toast__body">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-toast__icon">check</span>
    <div class="nj-toast__content">
      <p class="nj-toast__title" id="toast-4">Your table has been updated !</p>
      <p class="nj-toast__text">Rows successfully inserted</p>
    </div>
  </div>
  <div class="nj-toast__action">
    <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-4">
      <span class="nj-sr-only">Close notification</span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
    </button>
  </div>
  <div class="nj-toast__gauge">
    <div class="nj-toast__gauge-bar">
      <p class="nj-sr-only">The toast will be automatically closed in 5s</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
<div style="display: flex; gap: 16px; flex-direction: column;">
  {% Toast content_id="toast-4" gauge=10 btncolor="inverse" %}
    {% ToastText id="toast-4" %}10 sec gauge duration{% endToastText %}
  
    {% Slot 'icon' %}
      {% Icon label="check" %}
    {% endSlot %}
  {% endToast %}
  {% Toast content_id="toast-5" btncolor="inverse" %}
    {% ToastText id="toast-5" %}No gauge{% endToastText %}
  
    {% Slot 'icon' %}
      {% Icon label="check" %}
    {% endSlot %}
  {% endToast %}
</div>
"""
        expected = """
<div style="display: flex; gap: 16px; flex-direction: column;">
  <div class="nj-toast">
    <div class="nj-toast__body">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-toast__icon">check</span>
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-4">10 sec gauge duration</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-4">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
    <div class="nj-toast__gauge">
      <div class="nj-toast__gauge-bar" style="animation-duration: 10s;">
        <p class="nj-sr-only">The toast will be automatically closed in 10s</p>
      </div>
    </div>
  </div>

  <div class="nj-toast">
    <div class="nj-toast__body">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-toast__icon">check</span>
      <div class="nj-toast__content">
        <p class="nj-toast__text" id="toast-5">No gauge</p>
      </div>
    </div>
    <div class="nj-toast__action">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg nj-icon-btn--inverse" aria-describedby="toast-5">
        <span class="nj-sr-only">Close notification</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
      </button>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
{% Toast %}
  {% ToastText %}No close button{% endToastText %}

  {% Slot 'icon' %}
    {% Icon label="check" %}
  {% endSlot %}
{% endToast %}
"""
        expected = """
<div class="nj-toast">
    <div class="nj-toast__body">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-toast__icon">check</span>
      <div class="nj-toast__content">
        <p class="nj-toast__text">No close button</p>
      </div>
    </div>
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
