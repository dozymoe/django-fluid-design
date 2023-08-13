# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ModalTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Modal id="modal" %}{% endModal %}
"""
        expected = """
<div aria-labelledby="modal-title" class="nj-modal fade" id="modal"
   role="alertDialog">
  <div class="nj-modal__dialog" role="document">
   <div class="nj-modal__content">
    <div class="nj-modal__header">
     <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg"
       data-dismiss="modal">
      <span class="nj-sr-only">
       Close
      </span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
       close
      </span>
     </button>
    </div>
    <div class="nj-modal__body">
    </div>
   </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModal" %}
  Info modal
{% endModalBtn %}
{% ModalBtn type="button" variant="subtle" color="destructive" modal="#exampleModalDanger" %}
  Danger modal
{% endModalBtn %}
{% ModalBtn type="button" modal="#exampleModalAppendTo" %}
  Modal Append to Body
{% endModalBtn %}

{% Modal id="exampleModal" %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
{% endModal %}

{% Modal id="exampleModalDanger" %}
  {% Slot 'title' %}Delete the file?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" color="destructive" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" color="destructive" %}Delete{% endButton %}
  {% endSlot %}
{% endModal %}

{% Modal id="exampleModalAppendTo" append_to="body" %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModal">
  Info modal
</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-toggle="modal" data-target="#exampleModalDanger">
  Danger modal
</button>
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalAppendTo">
  Modal Append to Body
</button>

<div class="nj-modal fade" id="exampleModal" role="alertDialog" aria-labelledby="exampleModal-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModal-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade" id="exampleModalDanger" role="alertDialog" aria-labelledby="exampleModalDanger-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalDanger-title">
          Delete the file?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn nj-btn--destructive">Delete</button>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade" id="exampleModalAppendTo" role="alertDialog" data-appendTo="body" aria-labelledby="exampleModalAppendTo-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalAppendTo-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalCentered" %}
  Info modal
{% endModalBtn %}
{% ModalBtn type="button" variant="subtle" color="destructive" modal="#exampleModalCenteredDanger" %}
  Danger modal
{% endModalBtn %}

{% Modal id="exampleModalCentered" vcenter=True %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
{% endModal %}

{% Modal id="exampleModalCenteredDanger" vcenter=True %}
  {% Slot 'title' %}Delete the file?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" color="destructive" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" color="destructive" %}Delete{% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalCentered">
  Info modal
</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-toggle="modal" data-target="#exampleModalCenteredDanger">
  Danger modal
</button>

<div class="nj-modal fade nj-modal--vertical-centered" id="exampleModalCentered" role="alertDialog" aria-labelledby="exampleModalCentered-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalCentered-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade nj-modal--vertical-centered" id="exampleModalCenteredDanger" role="alertDialog" aria-labelledby="exampleModalCenteredDanger-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalCenteredDanger-title">
          Delete the file?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn nj-btn--destructive">Delete</button>
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
{% ModalBtn type="button" modal="#exampleModalCheckbox" %}
  Info modal
{% endModalBtn %}
{% ModalBtn type="button" modal="#exampleModalCheckboxDanger" variant="subtle" color="destructive" %}
  Info modal
{% endModalBtn %}

{% Modal id="exampleModalCheckbox" %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    <div class="d-flex w-100 justify-content-between align-items-center">
      <div class="nj-checkbox">
        <label for="checkbox-1">
          <input type="checkbox" id="checkbox-1"> Don't show me again
        </label>
      </div>
      <div class="d-flex">
        {% ModalCloseBtn type="button" variant="subtle" %}
          Cancel
        {% endModalCloseBtn %}
        {% Button type="button" class="ml-1" %}Confirm{% endButton %}
      </div>
    </div>
  {% endSlot %}
{% endModal %}

{% Modal id="exampleModalCheckboxDanger" %}
  {% Slot 'title' %}Delete the file?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    <div class="d-flex w-100 justify-content-between align-items-center">
      <div class="nj-checkbox">
        <label for="checkbox-2">
          <input type="checkbox" id="checkbox-2"> Don't show me again
        </label>
      </div>
      <div class="d-flex">
        {% ModalCloseBtn type="button" variant="subtle" color="destructive" %}
          Cancel
        {% endModalCloseBtn %}
        {% Button type="button" class="ml-1" color="destructive" %}Delete{% endButton %}
      </div>
    </div>
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalCheckbox">
  Info modal
</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-toggle="modal" data-target="#exampleModalCheckboxDanger">
  Info modal
</button>

<div class="nj-modal fade" id="exampleModalCheckbox" role="alertDialog" aria-labelledby="exampleModalCheckbox-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalCheckbox-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <div class="d-flex w-100 justify-content-between align-items-center">
          <div class="nj-checkbox">
            <label for="checkbox-1">
              <input type="checkbox" id="checkbox-1"> Don't show me again
            </label>
          </div>
          <div class="d-flex">
            <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
            <button type="button" class="nj-btn ml-1">Confirm</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade" id="exampleModalCheckboxDanger" role="alertDialog" aria-labelledby="exampleModalCheckboxDanger-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalCheckboxDanger-title">
          Delete the file?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <div class="d-flex w-100 justify-content-between align-items-center">
          <div class="nj-checkbox">
            <label for="checkbox-2">
              <input type="checkbox" id="checkbox-2"> Don't show me again
            </label>
          </div>
          <div class="d-flex">
            <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-dismiss="modal">Cancel</button>
            <button type="button" class="nj-btn ml-1 nj-btn--destructive">Delete</button>
          </div>
        </div>
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
{% ModalBtn type="button" modal="#exampleModalIcon" %}
  Info modal
{% endModalBtn %}
{% ModalBtn type="button" variant="subtle" color="destructive" modal="#exampleModalIconDanger" %}
  Info modal
{% endModalBtn %}

{% Modal id="exampleModalIcon" %}
  {% Slot 'title' %}
    Confirm these settings?
  {% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}

  {% Slot 'icon' %}
    {% Icon label="info" color="brand" %}
  {% endSlot %}
{% endModal %}

{% Modal id="exampleModalIconDanger" %}
  {% Slot 'title' %}
    Delete the file?
  {% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" color="destructive" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" color="destructive" %}Delete{% endButton %}
  {% endSlot %}

  {% Slot 'icon' %}
    {% Icon label="info" color="red" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalIcon">
  Info modal
</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-toggle="modal" data-target="#exampleModalIconDanger">
  Info modal
</button>

<div class="nj-modal fade" id="exampleModalIcon" role="alertDialog" aria-labelledby="exampleModalIcon-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalIcon-title">
          <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--brand">info</span>Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade" id="exampleModalIconDanger" role="alertDialog" aria-labelledby="exampleModalIconDanger-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalIconDanger-title">
          <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--red">info</span>Delete the file?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn nj-btn--destructive">Delete</button>
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
{% ModalBtn type="button" modal="#exampleModalSizeSmall" %}
  Small modal
{% endModalBtn %}
{% ModalBtn type="button" modal="#exampleModalSizeDefault" %}
  Default modal
{% endModalBtn %}

{% Modal id="exampleModalSizeSmall" size="sm" %}
  {% Slot 'title' %}Small modal{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Submit{% endButton %}
  {% endSlot %}
{% endModal %}

{% Modal id="exampleModalSizeDefault" %}
  {% Slot 'title' %}Default modal{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Submit{% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalSizeSmall">
  Small modal
</button>
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalSizeDefault">
  Default modal
</button>

<div class="nj-modal fade" id="exampleModalSizeSmall" role="alertDialog" aria-labelledby="exampleModalSizeSmall-title">
  <div class="nj-modal__dialog nj-modal--sm" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalSizeSmall-title">Small modal</h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Submit</button>
      </div>
    </div>
  </div>
</div>
<div class="nj-modal fade" id="exampleModalSizeDefault" role="alertDialog" aria-labelledby="exampleModalSizeDefault-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalSizeDefault-title">Default modal</h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Submit</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateSuccess" %}
  Success information modal
{% endModalBtn %}
{% Modal id="exampleModalStateSuccess" mode="information" fcenter=True role="dialog" %}
  {% Slot 'title' %}
    Success modal
  {% endSlot %}

  <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>

  {% Slot 'footer' %}
    {% Button type="button" %}Next{% endButton %}
  {% endSlot %}

  {% Slot 'icon' %}
    {% Icon label="check_circle" color="green" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalStateSuccess">
  Success information modal
</button>
<div class="nj-modal fade nj-modal--information" id="exampleModalStateSuccess" role="dialog" aria-labelledby="exampleModalStateSuccess-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-modal__icon nj-icon-material--xxl nj-icon-material--green">check_circle</span>
        <h1 class="nj-modal__title" id="exampleModalStateSuccess-title">
          Success modal
        </h1>
        <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
      <div class="nj-modal__footer nj-modal__footer--centered">
        <button type="button" class="nj-btn">Next</button>
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
{% ModalBtn type="button" modal="#exampleModalStateError" color="destructive" %}
  Error information modal
{% endModalBtn %}
{% Modal mode="information" id="exampleModalStateError" fcenter=True %}
  {% Slot 'title' %}Failure modal{% endSlot %}

  <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>

  {% Slot 'footer' %}
    {% Button type="button" %}Retry{% endButton %}
  {% endSlot %}

  {% Slot 'icon' %}
    {% Icon label="report_problem" color="red" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn nj-btn--destructive" data-toggle="modal" data-target="#exampleModalStateError">
  Error information modal
</button>
<div class="nj-modal fade nj-modal--information" id="exampleModalStateError" role="alertDialog" aria-labelledby="exampleModalStateError-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-modal__icon nj-icon-material--xxl nj-icon-material--red">report_problem</span>
        <h1 class="nj-modal__title" id="exampleModalStateError-title">
          Failure modal
        </h1>
        <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
      <div class="nj-modal__footer nj-modal__footer--centered">
        <button type="button" class="nj-btn">Retry</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateWarning" %}
  Warning information modal
{% endModalBtn %}
{% Modal mode="information" id="exampleModalStateWarning" fcenter=True %}
  {% Slot 'title' %}Warning modal{% endSlot %}

  <p class="text-center">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
  {% Slot 'icon' %}
    {% Icon label="info" color="orange" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalStateWarning">
  Warning information modal
</button>
<div class="nj-modal fade nj-modal--information" id="exampleModalStateWarning" role="alertDialog" aria-labelledby="exampleModalStateWarning-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-modal__icon nj-icon-material--xxl nj-icon-material--orange">info</span>
        <h1 class="nj-modal__title" id="exampleModalStateWarning-title">
          Warning modal
        </h1>
        <p class="text-center">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
      <div class="nj-modal__footer nj-modal__footer--centered">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateInfo" %}
  Information modal
{% endModalBtn %}
{% Modal mode="information" id="exampleModalStateInfo" fcenter=True %}
  {% Slot 'title' %}Warning modal{% endSlot %}

  <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
  {% Slot 'icon' %}
    {% Icon label="info" color="brand" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalStateInfo">
  Information modal
</button>
<div class="nj-modal fade nj-modal--information" id="exampleModalStateInfo" role="alertDialog" aria-labelledby="exampleModalStateInfo-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-modal__icon nj-icon-material--xxl nj-icon-material--brand">info</span>
        <h1 class="nj-modal__title" id="exampleModalStateInfo-title">
          Warning modal
        </h1>
        <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
      <div class="nj-modal__footer nj-modal__footer--centered">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateLoading" %}
  Waiting information modal
{% endModalBtn %}
{% Modal mode="spinner" id="exampleModalStateLoading" role="dialog" %}
  {% Slot 'title' %}Waiting modal{% endSlot %}

  <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalStateLoading">
  Waiting information modal
</button>
<div class="nj-modal fade nj-modal--information" id="exampleModalStateLoading" role="dialog" aria-labelledby="exampleModalStateLoading-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__body">
        <div class="nj-spinner nj-spinner--md nj-modal__loading-spinner" role="status">
          <span class="nj-sr-only">Loading...</span>
        </div>
        <h1 class="nj-modal__title" id="exampleModalStateLoading-title">
          Waiting modal
        </h1>
        <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example11(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModal" %}
  Basic confirmation modal
{% endModalBtn %}
{% Modal id="exampleModal" %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModal">
  Basic confirmation modal
</button>

<div class="nj-modal fade" id="exampleModal" role="alertDialog" aria-labelledby="exampleModal-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModal-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example12(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModal" %}
  Confirmation modal
{% endModalBtn %}
{% ModalBtn type="button" modal="#exampleModalDanger" variant="subtle" color="destructive" %}
  Destructive modal
{% endModalBtn %}
{% ModalBtn type="button" modal="#exampleModalAppendTo" %}
  Modal Append to Body
{% endModalBtn %}
{% Modal id="exampleModal" %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
{% endModal  %}
{% Modal id="exampleModalDanger" %}
  {% Slot 'title' %}Delete the file?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" color="destructive" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" color="destructive" %}Delete{% endButton %}
  {% endSlot %}
{% endModal  %}
{% Modal id="exampleModalAppendTo" append_to="body" %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
{% endModal  %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModal">
  Confirmation modal
</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-toggle="modal" data-target="#exampleModalDanger">
  Destructive modal
</button>
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalAppendTo">
  Modal Append to Body
</button>

<div class="nj-modal fade" id="exampleModal" role="alertDialog" aria-labelledby="exampleModal-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModal-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade" id="exampleModalDanger" role="alertDialog" aria-labelledby="exampleModalDanger-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalDanger-title">
          Delete the file?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn nj-btn--destructive">Delete</button>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade" id="exampleModalAppendTo" role="alertDialog" data-appendTo="body" aria-labelledby="exampleModalAppendTo-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalAppendTo-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example13(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateInfo" %}
  Default information modal
{% endModalBtn %}
{% Modal id="exampleModalStateInfo" mode="information" fcenter=True %}
  {% Slot 'title' %}Information modal{% endSlot %}

  <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
  {% Slot 'icon' %}
    {% Icon label="info" color="brand" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalStateInfo">
  Default information modal
</button>
  
<div class="nj-modal fade nj-modal--information" id="exampleModalStateInfo" role="alertDialog" aria-labelledby="exampleModalStateInfo-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-modal__icon nj-icon-material--xxl nj-icon-material--brand">info</span>
        <h1 class="nj-modal__title" id="exampleModalStateInfo-title">
          Information modal
        </h1>
        <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
      <div class="nj-modal__footer nj-modal__footer--centered">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example14(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateSuccess" %}
  Success information modal
{% endModalBtn %}
{% Modal id="exampleModalStateSuccess" mode="information" role="dialog" fcenter=True %}
  {% Slot 'title' %}Success modal{% endSlot %}

  <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>

  {% Slot 'footer' %}
    {% Button type="button" %}Next{% endButton %}
  {% endSlot %}
  {% Slot 'icon' %}
    {% Icon label="check_circle" color="green" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalStateSuccess">
  Success information modal
</button>
<div class="nj-modal fade nj-modal--information" id="exampleModalStateSuccess" role="dialog" aria-labelledby="exampleModalStateSuccess-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-modal__icon nj-icon-material--xxl nj-icon-material--green">check_circle</span>
        <h1 class="nj-modal__title" id="exampleModalStateSuccess-title">
          Success modal
        </h1>
        <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
      <div class="nj-modal__footer nj-modal__footer--centered">
        <button type="button" class="nj-btn">Next</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example15(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateWarning" color="secondary" %}
  Warning information modal
{% endModalBtn %}
{% Modal id="exampleModalStateWarning" mode="information" fcenter=True %}
  {% Slot 'title' %}Warning modal{% endSlot %}

  <p class="text-center">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
  {% Slot 'icon' %}
    {% Icon label="info" color="orange" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn nj-btn--secondary" data-toggle="modal" data-target="#exampleModalStateWarning">
  Warning information modal
</button>
<div class="nj-modal fade nj-modal--information" id="exampleModalStateWarning" role="alertDialog" aria-labelledby="exampleModalStateWarning-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-modal__icon  nj-icon-material--xxl nj-icon-material--orange">info</span>
        <h1 class="nj-modal__title" id="exampleModalStateWarning-title">
          Warning modal
        </h1>
        <p class="text-center">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
      <div class="nj-modal__footer nj-modal__footer--centered">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example16(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateError" color="destructive" %}
  Error information modal
{% endModalBtn %}
{% Modal id="exampleModalStateError" mode="information" fcenter=True %}
  {% Slot 'title' %}Failure modal{% endSlot %}

  <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>

  {% Slot 'footer' %}
    {% Button type="button" %}Retry{% endButton %}
  {% endSlot %}
  {% Slot 'icon' %}
    {% Icon label="report_problem" color="red" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn nj-btn--destructive" data-toggle="modal" data-target="#exampleModalStateError">
  Error information modal
</button>
<div class="nj-modal fade nj-modal--information" id="exampleModalStateError" role="alertDialog" aria-labelledby="exampleModalStateError-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-modal__icon nj-icon-material--xxl nj-icon-material--red">report_problem</span>
        <h1 class="nj-modal__title" id="exampleModalStateError-title">
          Failure modal
        </h1>
        <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
      </div>
      <div class="nj-modal__footer nj-modal__footer--centered">
        <button type="button" class="nj-btn">Retry</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example17(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalStateLoading" %}
  Waiting information modal
{% endModalBtn %}
{% Modal id="exampleModalStateLoading" mode="spinner" role="dialog" %}
  {% Slot 'title' %}Waiting modal{% endSlot %}

  <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalStateLoading">
    Waiting information modal
  </button>
  <div class="nj-modal fade nj-modal--information" id="exampleModalStateLoading" role="dialog" aria-labelledby="exampleModalStateLoading-title">
    <div class="nj-modal__dialog" role="document">
      <div class="nj-modal__content">
        <div class="nj-modal__body">
          <div class="nj-spinner nj-spinner--md nj-modal__loading-spinner" role="status">
            <span class="nj-sr-only">Loading...</span>
          </div>
          <h1 class="nj-modal__title" id="exampleModalStateLoading-title">
            Waiting modal
          </h1>
          <p class="nj-modal__description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet</p>
        </div>
      </div>
    </div>
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example18(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalSizeSmall" %}
  Small modal
{% endModalBtn %}
{% ModalBtn type="button" modal="#exampleModalSizeDefault" %}
  Default modal
{% endModalBtn %}
{% Modal id="exampleModalSizeSmall" size="sm" %}
  {% Slot 'title' %}Small modal{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Submit{% endButton %}
  {% endSlot %}
{% endModal %}
{% Modal id="exampleModalSizeDefault" %}
  {% Slot 'title' %}Default modal{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Submit{% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalSizeSmall">
  Small modal
</button>
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalSizeDefault">
  Default modal
</button>

<div class="nj-modal fade" id="exampleModalSizeSmall" role="alertDialog" aria-labelledby="exampleModalSizeSmall-title">
  <div class="nj-modal__dialog nj-modal--sm" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalSizeSmall-title">Small modal</h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Submit</button>
      </div>
    </div>
  </div>
</div>
<div class="nj-modal fade" id="exampleModalSizeDefault" role="alertDialog" aria-labelledby="exampleModalSizeDefault-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalSizeDefault-title">Default modal</h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Submit</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example19(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalCentered" %}
  Centered modal
{% endModalBtn %}
{% ModalBtn type="button" modal="#exampleModalCenteredDanger" variant="subtle" color="destructive" %}
  Centered danger modal
{% endModalBtn %}
{% Modal id="exampleModalCentered" vcenter=True %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
{% endModal %}
{% Modal id="exampleModalCenteredDanger" vcenter=True %}
  {% Slot 'title' %}Delete the file?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" color="destructive" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" color="destructive" %}Delete{% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalCentered">
  Centered modal
</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-toggle="modal" data-target="#exampleModalCenteredDanger">
  Centered danger modal
</button>

<div class="nj-modal fade nj-modal--vertical-centered" id="exampleModalCentered" role="alertDialog" aria-labelledby="exampleModalCentered-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalCentered-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade nj-modal--vertical-centered" id="exampleModalCenteredDanger" role="alertDialog" aria-labelledby="exampleModalCenteredDanger-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalCenteredDanger-title">
          Delete the file?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn nj-btn--destructive">Delete</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example20(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalIcon" %}
  Info modal
{% endModalBtn %}
{% ModalBtn type="button" variant="subtle" color="destructive" modal="#exampleModalIconDanger" %}
  Info modal
{% endModalBtn %}
{% Modal id="exampleModalIcon" %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" %}Confirm{% endButton %}
  {% endSlot %}
  {% Slot 'icon' %}
    {% Icon label="info" color="brand" %}
  {% endSlot %}
{% endModal %}
{% Modal id="exampleModalIconDanger" %}
  {% Slot 'title' %}Delete the file?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    {% ModalCloseBtn type="button" variant="subtle" color="destructive" %}
      Cancel
    {% endModalCloseBtn %}
    {% Button type="button" color="destructive" %}Delete{% endButton %}
  {% endSlot %}
  {% Slot 'icon' %}
    {% Icon label="info" color="red" %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalIcon">
  Info modal
</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-toggle="modal" data-target="#exampleModalIconDanger">
  Info modal
</button>

<div class="nj-modal fade" id="exampleModalIcon" role="alertDialog" aria-labelledby="exampleModalIcon-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalIcon-title">
          <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--brand">info</span>Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn">Confirm</button>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade" id="exampleModalIconDanger" role="alertDialog" aria-labelledby="exampleModalIconDanger-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalIconDanger-title">
          <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--red">info</span>Delete the file?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-dismiss="modal">Cancel</button>
        <button type="button" class="nj-btn nj-btn--destructive">Delete</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example21(self):
        template = """
{% load fluid_design %}
{% ModalBtn type="button" modal="#exampleModalCheckbox" %}
  Confirmation modal with checkbox
{% endModalBtn %}
{% ModalBtn type="button" modal="#exampleModalCheckboxDanger" variant="subtle" color="destructive" %}
  Danger modal with checkbox
{% endModalBtn %}
{% Modal id="exampleModalCheckbox" %}
  {% Slot 'title' %}Confirm these settings?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    <div class="d-flex w-100 justify-content-between align-items-center">
      <div class="nj-checkbox">
        <label for="checkbox-1">
          <input type="checkbox" id="checkbox-1"> Don't show me again
        </label>
      </div>
      <div class="d-flex">
        {% ModalCloseBtn type="button" variant="subtle" %}
          Cancel
        {% endModalCloseBtn %}
        {% Button type="button" class="ml-1" %}Confirm{% endButton %}
      </div>
    </div>
  {% endSlot %}
{% endModal %}

{% Modal id="exampleModalCheckboxDanger" %}
  {% Slot 'title' %}Delete the file?{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>

  {% Slot 'footer' %}
    <div class="d-flex w-100 justify-content-between align-items-center">
      <div class="nj-checkbox">
        <label for="checkbox-2">
          <input type="checkbox" id="checkbox-2"> Don't show me again
        </label>
      </div>
      <div class="d-flex">
        {% ModalCloseBtn type="button" variant="subtle" color="destructive" %}
          Cancel
        {% endModalCloseBtn %}
        {% Button type="button" color="destructive" class="ml-1" %}
          Delete
        {% endButton %}
      </div>
    </div>
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button type="button" class="nj-btn" data-toggle="modal" data-target="#exampleModalCheckbox">
  Confirmation modal with checkbox
</button>
<button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-toggle="modal" data-target="#exampleModalCheckboxDanger">
  Danger modal with checkbox
</button>

<div class="nj-modal fade" id="exampleModalCheckbox" role="alertDialog" aria-labelledby="exampleModalCheckbox-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalCheckbox-title">
          Confirm these settings?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <div class="d-flex w-100 justify-content-between align-items-center">
          <div class="nj-checkbox">
            <label for="checkbox-1">
              <input type="checkbox" id="checkbox-1"> Don't show me again
            </label>
          </div>
          <div class="d-flex">
            <button type="button" class="nj-btn nj-btn--subtle" data-dismiss="modal">Cancel</button>
            <button type="button" class="nj-btn ml-1">Confirm</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="nj-modal fade" id="exampleModalCheckboxDanger" role="alertDialog" aria-labelledby="exampleModalCheckboxDanger-title">
  <div class="nj-modal__dialog" role="document">
    <div class="nj-modal__content">
      <div class="nj-modal__header">
        <h1 class="nj-modal__title" id="exampleModalCheckboxDanger-title">
          Delete the file?
        </h1>
        <button type="button" class="nj-icon-btn nj-modal__close nj-icon-btn--lg" data-dismiss="modal">
          <span class="nj-sr-only">Close</span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">close</span>
        </button>
      </div>
      <div class="nj-modal__body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.</p>
      </div>
      <div class="nj-modal__footer">
        <div class="d-flex w-100 justify-content-between align-items-center">
          <div class="nj-checkbox">
            <label for="checkbox-2">
              <input type="checkbox" id="checkbox-2"> Don't show me again
            </label>
          </div>
          <div class="d-flex">
            <button type="button" class="nj-btn nj-btn--subtle nj-btn--destructive" data-dismiss="modal">Cancel</button>
            <button type="button" class="nj-btn ml-1 nj-btn--destructive">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
