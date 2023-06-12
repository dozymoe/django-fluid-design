# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class FabTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Fab %}
{% endFab %}
"""
        expected = """
<button class="nj-fab" type="button">
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Fab %}
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
{% endFab %}
"""
        expected = """
<button type="button" class="nj-fab">
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% Fab size="sm" %}
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
{% endFab %}
"""
        expected = """
<button type="button" class="nj-fab nj-fab--sm">
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% Fab disabled=True %}
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
{% endFab %}
"""
        expected = """
<button type="button" class="nj-fab disabled" disabled>
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-48); height: 450px; align-items: flex-start; justify-content: flex-end">
  {% Fab %}
    <span aria-hidden="true" class="material-icons">add</span>
    <span class="nj-sr-only">Add</span>

    {% Slot 'menu' %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">attachment</span>
        <span class="nj-sr-only">Add an attachment</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">add_a_photo</span>
        <span class="nj-sr-only">Add a photo</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">cloud_upload</span>
        <span class="nj-sr-only">Upload</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">create_new_folder</span>
        <span class="nj-sr-only">Create new folder</span>
      {% endFabItem %}
    {% endSlot %}
  {% endFab %}
  {% Fab placement="right" %}
    <span aria-hidden="true" class="material-icons">add</span>
    <span class="nj-sr-only">Add</span>

    {% Slot 'menu' %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">attachment</span>
        <span class="nj-sr-only">Add a photo</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">add_a_photo</span>
        <span class="nj-sr-only">Upload</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">cloud_upload</span>
        <span class="nj-sr-only">Create new folder</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">create_new_folder</span>
        <span class="nj-sr-only">Add</span>
      {% endFabItem %}
    {% endSlot %}
  {% endFab %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-48); height: 450px; align-items: flex-start; justify-content: flex-end">
  <div class="nj-fab-menu">
    <button type="button" class="nj-fab">
      <span aria-hidden="true" class="material-icons">add</span>
      <span class="nj-sr-only">Add</span>
    </button>
    <ul class="nj-fab__actions">
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">attachment</span>
          <span class="nj-sr-only">Add an attachment</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">add_a_photo</span>
          <span class="nj-sr-only">Add a photo</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">cloud_upload</span>
          <span class="nj-sr-only">Upload</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">create_new_folder</span>
          <span class="nj-sr-only">Create new folder</span>
        </button>
      </li>
    </ul>
  </div>
  <div class="nj-fab-menu" data-placement="right">
    <button type="button" class="nj-fab">
      <span aria-hidden="true" class="material-icons">add</span>
      <span class="nj-sr-only">Add</span>
    </button>
    <ul class="nj-fab__actions">
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">attachment</span>
          <span class="nj-sr-only">Add a photo</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">add_a_photo</span>
          <span class="nj-sr-only">Upload</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">cloud_upload</span>
          <span class="nj-sr-only">Create new folder</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">create_new_folder</span>
          <span class="nj-sr-only">Add</span>
        </button>
      </li>
    </ul>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Fab %}
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
{% endFab %}
"""
        expected = """
<button type="button" class="nj-fab">
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Fab disabled=True %}
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
{% endFab %}
"""
        expected = """
<button type="button" class="nj-fab disabled" disabled>
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Fab size="sm" %}
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
{% endFab %}
"""
        expected = """
<button type="button" class="nj-fab nj-fab--sm">
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-48); height: 450px; align-items: flex-start; justify-content: flex-end">
  {% Fab %}
    <span aria-hidden="true" class="material-icons">add</span>
    <span class="nj-sr-only">Add</span>

    {% Slot 'menu' %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">attachment</span>
        <span class="nj-sr-only">Add an attachment</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">add_a_photo</span>
        <span class="nj-sr-only">Add a photo</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">cloud_upload</span>
        <span class="nj-sr-only">Upload</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">create_new_folder</span>
        <span class="nj-sr-only">Create new folder</span>
      {% endFabItem %}
    {% endSlot %}
  {% endFab %}
  {% Fab placement="right" %}
    <span aria-hidden="true" class="material-icons">add</span>
    <span class="nj-sr-only">Add</span>

    {% Slot 'menu' %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">attachment</span>
        <span class="nj-sr-only">Add a photo</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">add_a_photo</span>
        <span class="nj-sr-only">Upload</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">cloud_upload</span>
        <span class="nj-sr-only">Create new folder</span>
      {% endFabItem %}
      {% FabItem %}
        <span aria-hidden="true" class="material-icons">create_new_folder</span>
        <span class="nj-sr-only">Add</span>
      {% endFabItem %}
    {% endSlot %}
  {% endFab %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: var(--nj-size-space-48); height: 450px; align-items: flex-start; justify-content: flex-end">
  <div class="nj-fab-menu">
    <button type="button" class="nj-fab">
      <span aria-hidden="true" class="material-icons">add</span>
      <span class="nj-sr-only">Add</span>
    </button>
    <ul class="nj-fab__actions">
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">attachment</span>
          <span class="nj-sr-only">Add an attachment</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">add_a_photo</span>
          <span class="nj-sr-only">Add a photo</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">cloud_upload</span>
          <span class="nj-sr-only">Upload</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">create_new_folder</span>
          <span class="nj-sr-only">Create new folder</span>
        </button>
      </li>
    </ul>
  </div>
  <div class="nj-fab-menu" data-placement="right">
    <button type="button" class="nj-fab">
      <span aria-hidden="true" class="material-icons">add</span>
      <span class="nj-sr-only">Add</span>
    </button>
    <ul class="nj-fab__actions">
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">attachment</span>
          <span class="nj-sr-only">Add a photo</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">add_a_photo</span>
          <span class="nj-sr-only">Upload</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">cloud_upload</span>
          <span class="nj-sr-only">Create new folder</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">create_new_folder</span>
          <span class="nj-sr-only">Add</span>
        </button>
      </li>
    </ul>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
{% Fab size="sm" placement="right" %}
  <span aria-hidden="true" class="material-icons">add</span>
  <span class="nj-sr-only">Add</span>

  {% Slot 'menu' %}
    {% FabItem %}
      <span aria-hidden="true" class="material-icons">attachment</span>
      <span class="nj-sr-only">Add an attachment</span>
    {% endFabItem %}
    {% FabItem %}
      <span aria-hidden="true" class="material-icons">add_a_photo</span>
      <span class="nj-sr-only">Add a photo</span>
    {% endFabItem %}
    {% FabItem %}
      <span aria-hidden="true" class="material-icons">cloud_upload</span>
      <span class="nj-sr-only">Upload</span>
    {% endFabItem %}
    {% FabItem %}
      <span aria-hidden="true" class="material-icons">create_new_folder</span>
      <span class="nj-sr-only">Create new folder</span>
    {% endFabItem %}
  {% endSlot %}
{% endFab %}
"""
        expected = """
<div class="nj-fab-menu" data-placement="right">
    <button type="button" class="nj-fab nj-fab--sm">
      <span aria-hidden="true" class="material-icons">add</span>
      <span class="nj-sr-only">Add</span>
    </button>
    <ul class="nj-fab__actions nj-fab__actions--sm">
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">attachment</span>
          <span class="nj-sr-only">Add an attachment</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">add_a_photo</span>
          <span class="nj-sr-only">Add a photo</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">cloud_upload</span>
          <span class="nj-sr-only">Upload</span>
        </button>
      </li>
      <li class="nj-fab__item">
        <button type="button" class="nj-fab nj-fab--light nj-fab--sm">
          <span aria-hidden="true" class="material-icons">create_new_folder</span>
          <span class="nj-sr-only">Create new folder</span>
        </button>
      </li>
    </ul>
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
