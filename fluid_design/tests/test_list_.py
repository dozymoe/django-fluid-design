# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ListTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li %}
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item">
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li %}
    Default item with icon and right content

    {% Slot 'icon_first' %}
      {% Icon label="navigation" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
    {% Slot 'icon_last' %}
      {% Icon label="chevron_right" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}

  {% Li active=True %}
     Active item with icon and right content

    {% Slot 'icon_first' %}
      {% Icon label="check" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
    {% Slot 'icon_last' %}
      {% Icon label="chevron_right" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}

  {% Li border=True %}
    Default item with icon and badge as right content

    {% Slot 'icon_first' %}
      {% Icon label="list" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
    {% Slot 'icon_last' %}
      {% Badge style="information" label="7" %}
    {% endSlot %}
  {% endLi %}

  {% Li active=True border=True %}
    Active item with icon and right content, border on the right

    {% Slot 'icon_first' %}
      {% Icon label="tag_faces" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
    {% Slot 'icon_last' %}
      {% Icon label="chevron_right" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">navigation</span>
      <span class="nj-sr-only">Icon text alternative</span>
      <span class="nj-list-group__item-content">Default item with icon and right content</span>
      <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
      <span class="nj-sr-only">Icon text alternative</span>
  </li>
  <li class="nj-list-group__item active" aria-current="true">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">check</span>
      <span class="nj-sr-only">Icon text alternative</span>
      <span class="nj-list-group__item-content">Active item with icon and right content</span>
      <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
      <span class="nj-sr-only">Icon text alternative</span>
  </li>
  <li class="nj-list-group__item nj-list-group__item--right-border">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">list</span>
      <span class="nj-sr-only">Icon text alternative</span>
      <span class="nj-list-group__item-content">Default item with icon and badge as right content</span>
      <p class="nj-badge nj-list-group__item-right-content nj-badge--information">7</p>
  </li>
  <li class="nj-list-group__item nj-list-group__item--right-border active" aria-current="true">
      <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">tag_faces</span>
      <span class="nj-sr-only">Icon text alternative</span>
      <span class="nj-list-group__item-content">Active item with icon and right content, border on the right</span>
      <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
      <span class="nj-sr-only">Icon text alternative</span>
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% List size="sm" %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group nj-list-group--sm">
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li click=True active=True %}
    <button>Lorem ipsum dolor sit amet</button>
  {% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item nj-list-group__item--clickable active" aria-current="true">
      <button>Lorem ipsum dolor sit amet</button>
  </li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li click=True border=True active=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True border=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True border=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True border=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border active" aria-current="true">
    <a href="#">Lorem ipsum dolor sit amet</a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
    <a href="#">Lorem ipsum dolor sit amet</a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
    <a href="#">Lorem ipsum dolor sit amet</a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
    <a href="#">Lorem ipsum dolor sit amet</a>
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li disabled=True %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item disabled">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% List border=False %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group nj-list-group--no-border">
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li click=True active=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True %}
    <button>Lorem ipsum dolor sit amet</button>
  {% endLi %}
  {% Li click=True %}
    <button>
      {% Icon label="music_note" %}
      <span class="nj-sr-only">Icon text alternative</span>
      Lorem ipsum dolor sit amet
    </button>
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item nj-list-group__item--clickable active" aria-current="true">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable">
    <button>
      Lorem ipsum dolor sit amet
    </button>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable">
    <button>
      <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">music_note</span>
      <span class="nj-sr-only">Icon text alternative</span>
      Lorem ipsum dolor sit amet
    </button>
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li %}
    Lorem ipsum dolor sit amet

    {% Slot 'icon_first' %}
      {% Icon label="tag_faces" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
  {% Li active=True %}
    Lorem ipsum dolor sit amet

    {% Slot 'icon_first' %}
      {% Icon label="music_note" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
  {% Li %}
    Lorem ipsum dolor sit amet

    {% Slot 'icon_first' %}
      {% Icon label="flash_on" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">tag_faces</span>
    <span class="nj-sr-only">Icon text alternative</span>
    Lorem ipsum dolor sit amet
  </li>
  <li class="nj-list-group__item active" aria-current="true">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">music_note</span>
    <span class="nj-sr-only">Icon text alternative</span>
    Lorem ipsum dolor sit amet
  </li>
  <li class="nj-list-group__item">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">flash_on</span>
    <span class="nj-sr-only">Icon text alternative</span>
    Lorem ipsum dolor sit amet
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li %}
    List item with a badge on the right

    {% Slot 'icon_last' %}
      {% Badge style="information" label="14" %}
    {% endSlot %}
  {% endLi %}
  {% Li %}
    List item with an icon on the right

    {% Slot 'icon_last' %}
      {% Icon label="chevron_right" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
  {% Li active=True %}
    List item with a tag on the right

    {% Slot 'icon_last' %}
      {% Tag size="sm" %}Small tag{% endTag %}
    {% endSlot %}
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item">
    <span class="nj-list-group__item-content">
      List item with a badge on the right
    </span>
    <p class="nj-badge nj-list-group__item-right-content nj-badge--information">14</p>
  </li>
  <li class="nj-list-group__item">
    <span class="nj-list-group__item-content">
      List item with an icon on the right
    </span>
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
    <span class="nj-sr-only">Icon text alternative</span>
  </li>
  <li class="nj-list-group__item active" aria-current="true">
    <span class="nj-list-group__item-content">
      List item with a tag on the right
    </span>
    <div class="nj-tag nj-list-group__item-right-content nj-tag--sm">
      <span class="nj-tag__text">Small tag</span>
    </div>
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example11(self):
        template = """
{% load fluid_design %}
{% List border=False size="sm" spaced=True %}
  {% Li click=True %}
    <button>
      List item with a badge on the right
    </button>

    {% Slot 'icon_first' %}
      {% Icon label="dashboard" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
    {% Slot 'icon_last' %}
      {% Badge style="information" label="14" %}
    {% endSlot %}
  {% endLi %}
  {% Li click=True %}
    <button>
      List item with an icon on the right
    </button>

    {% Slot 'icon_first' %}
      {% Icon label="tag_faces" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
    {% Slot 'icon_last' %}
      {% Icon label="chevron_right" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
  {% Li click=True active=True %}
    <button>
      List item with an icon on the right
    </button>

    {% Slot 'icon_first' %}
      {% Icon label="flash_on" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
    {% Slot 'icon_last' %}
      {% Tag size="sm" %}Tag{% endTag %}
    {% endSlot %}
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group nj-list-group--no-border nj-list-group--sm nj-list-group--spaced-items">
  <li class="nj-list-group__item nj-list-group__item--clickable">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">dashboard</span>
    <span class="nj-sr-only">Icon text alternative</span>
    <span class="nj-list-group__item-content">
      <button>
        List item with a badge on the right
      </button>
    </span>
    <p class="nj-badge nj-list-group__item-right-content nj-badge--information">14</p>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">tag_faces</span>
    <span class="nj-sr-only">Icon text alternative</span>
    <span class="nj-list-group__item-content">
      <button>
        List item with an icon on the right
      </button>
    </span>
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
    <span class="nj-sr-only">Icon text alternative</span>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable active" aria-current="true">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">flash_on</span>
    <span class="nj-sr-only">Icon text alternative</span>
    <span class="nj-list-group__item-content">
      <button>
        List item with an icon on the right
      </button>
    </span>
    <div class="nj-tag nj-list-group__item-right-content nj-tag--sm">
      <span class="nj-tag__text">Tag</span>
    </div>
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example12(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example13(self):
        template = """
{% load fluid_design %}
{% List size="sm" %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group nj-list-group--sm">
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example14(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li active=True %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item active" aria-current="true">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example15(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li click=True border=True active=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True border=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True border=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True border=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border active"
      aria-current="true">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example16(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li disabled=True %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item disabled">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example17(self):
        template = """
{% load fluid_design %}
{% List border=False %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
  {% Li %}Lorem ipsum dolor sit amet{% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group nj-list-group--no-border">
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
  <li class="nj-list-group__item">Lorem ipsum dolor sit amet</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example18(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li click=True active=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
  {% Li click=True %}
    <a href="#">Lorem ipsum dolor sit amet</a>
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item nj-list-group__item--clickable active"
      aria-current="true">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
  <li class="nj-list-group__item nj-list-group__item--clickable">
    <a href="#">
      Lorem ipsum dolor sit amet
    </a>
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example19(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li %}
    Lorem ipsum dolor sit amet

    {% Slot 'icon_first' %}
      {% Icon label="tag_faces" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
  {% Li active=True %}
    Lorem ipsum dolor sit amet

    {% Slot 'icon_first' %}
      {% Icon label="music_note" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
  {% Li %}
    Lorem ipsum dolor sit amet

    {% Slot 'icon_first' %}
      {% Icon label="flash_on" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">tag_faces</span>
    <span class="nj-sr-only">Icon text alternative</span>
    Lorem ipsum dolor sit amet
  </li>
  <li class="nj-list-group__item active" aria-current="true">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">music_note</span>
    <span class="nj-sr-only">Icon text alternative</span>
    Lorem ipsum dolor sit amet
  </li>
  <li class="nj-list-group__item">
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">flash_on</span>
    <span class="nj-sr-only">Icon text alternative</span>
    Lorem ipsum dolor sit amet
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example20(self):
        template = """
{% load fluid_design %}
{% List %}
  {% Li %}
    List item with a badge on the right

    {% Slot 'icon_last' %}
      {% Badge style="information" label="14" %}
    {% endSlot %}
  {% endLi %}
  {% Li %}
    List item with an icon on the right

    {% Slot 'icon_last' %}
      {% Icon label="chevron_right" %}
      <span class="nj-sr-only">Icon text alternative</span>
    {% endSlot %}
  {% endLi %}
  {% Li active=True %}
    List item with a tag on the right

    {% Slot 'icon_last' %}
      {% Tag size="sm" %}Small tag {% endTag %}
    {% endSlot %}
  {% endLi %}
{% endList %}
"""
        expected = """
<ul class="nj-list-group">
  <li class="nj-list-group__item">
    <span class="nj-list-group__item-content">
      List item with a badge on the right
    </span>
    <p class="nj-badge nj-list-group__item-right-content nj-badge--information">14</p>
  </li>
  <li class="nj-list-group__item">
    <span class="nj-list-group__item-content">
      List item with an icon on the right
    </span>
    <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
    <span class="nj-sr-only">Icon text alternative</span>
  </li>
  <li class="nj-list-group__item active" aria-current="true">
    <span class="nj-list-group__item-content">
      List item with a tag on the right
    </span>
    <div class="nj-tag nj-list-group__item-right-content nj-tag--sm">
      <span class="nj-tag__text">Small tag</span>
    </div>
  </li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
