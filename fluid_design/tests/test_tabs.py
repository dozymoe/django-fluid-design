# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TabsTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Tab %}{% endTab %}
"""
        expected = """
<div class="nj-tab">
  <div aria-label="Tab system label" class="nj-tab__items" role="tablist">
  </div>
  <div style="padding-top: var(--nj-size-space-16);">
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Tab %}
  {% Slot 'buttons' %}
    {% T_Btn label="Item 1" id="tab-item-1" target_id="tab-content-1" %}
    {% T_Btn label="Item 2" active=True id="tab-item-2" target_id="tab-content-2" %}
    {% T_Btn label="Item 3" disabled=True id="tab-item-3" target_id="tab-content-3" %}
    {% T_Btn label="Item 4" id="tab-item-4" target_id="tab-content-4" %}
    {% T_Btn label="Item 5" id="tab-item-5" target_id="tab-content-5" %}
    {% T_Btn label="Item 6" disabled=True id="tab-item-6" target_id="tab-content-5" %}
  {% endSlot %}
  {% T_Panel id="tab-content-1" trigger_id="tab-item-1" %}
    <p>My Item 1 content</p>
  {% endT_Panel %}
  {% T_Panel active=True id="tab-content-2" trigger_id="tab-item-2" %}
    <p>My Item 2 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-3" trigger_id="tab-item-3" %}
    <p>My Item 3 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-4" trigger_id="tab-item-4" %}
    <p>My Item 4 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-5" trigger_id="tab-item-5" %}
    <p>My Item 5 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-6" trigger_id="tab-item-6" %}
    <p>My Item 6 content</p>
  {% endT_Panel %}
{% endTab %}
"""
        expected = """
<div class="nj-tab">
 <div class="nj-tab__items" role="tablist" aria-label="Tab system label">
   <button class="nj-tab__item" id="tab-item-1" role="tab" aria-selected="false" tabindex="-1" aria-controls="tab-content-1">Item 1</button>
   <button class="nj-tab__item nj-tab__item--active"  id="tab-item-2" role="tab" aria-selected="true" tabindex="0" aria-controls="tab-content-2">Item 2</button>
   <button class="nj-tab__item"  id="tab-item-3" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-3" disabled>Item 3</button>
   <button class="nj-tab__item"  id="tab-item-4" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-4">Item 4</button>
   <button class="nj-tab__item"  id="tab-item-5" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-5">Item 5</button>
   <button class="nj-tab__item"  id="tab-item-6" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-5" disabled>Item 6</button>
 </div>
 <div style="padding-top: var(--nj-size-space-16);">
   <div class="nj-tab__content" id="tab-content-1" role="tabpanel" tabindex="0" aria-labelledby="tab-item-1">
     <p>My Item 1 content</p>
   </div>
   <div class="nj-tab__content nj-tab__content--active" id="tab-content-2" role="tabpanel" tabindex="0" aria-labelledby="tab-item-2">
     <p>My Item 2 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-3" role="tabpanel" tabindex="0" aria-labelledby="tab-item-3">
     <p>My Item 3 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-4" role="tabpanel" tabindex="0" aria-labelledby="tab-item-4">
     <p>My Item 4 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-5" role="tabpanel" tabindex="0" aria-labelledby="tab-item-5">
     <p>My Item 5 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-6" role="tabpanel" tabindex="0" aria-labelledby="tab-item-6">
     <p>My Item 6 content</p>
   </div>
 </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% Tab style="compact" %}
  {% Slot 'buttons' %}
    {% T_Btn label="Item 1" active=True id="tab-item-1" target_id="tab-content-1" %}
    {% T_Btn label="Item 2" disabled=True id="tab-item-2" target_id="tab-content-2" %}
    {% T_Btn label="Item 3" id="tab-item-3" target_id="tab-content-3" %}
    {% T_Btn label="Item 4" id="tab-item-4" target_id="tab-content-4" %}
    {% T_Btn label="Item 5" id="tab-item-5" target_id="tab-content-5" %}
    {% T_Btn label="Item 6" disabled=True id="tab-item-6" target_id="tab-content-5" %}
  {% endSlot %}
  {% T_Panel active=True id="tab-content-1" trigger_id="tab-item-1" %}
    <p>My Item 1 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-2" trigger_id="tab-item-2" %}
    <p>My Item 2 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-3" trigger_id="tab-item-3" %}
    <p>My Item 3 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-4" trigger_id="tab-item-4" %}
    <p>My Item 4 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-5" trigger_id="tab-item-5" %}
    <p>My Item 5 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-6" trigger_id="tab-item-6" %}
    <p>My Item 6 content</p>
  {% endT_Panel %}
{% endTab %}
"""
        expected = """
<div class="nj-tab nj-tab--compact">
 <div class="nj-tab__items" role="tablist" aria-label="Tab system label">
  <button class="nj-tab__item nj-tab__item--active" id="tab-item-1" role="tab" aria-selected="true" tabindex="0" aria-controls="tab-content-1">Item 1</button>
  <button class="nj-tab__item"  id="tab-item-2" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-2" disabled>Item 2</button>
  <button class="nj-tab__item"  id="tab-item-3" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-3">Item 3</button>
  <button class="nj-tab__item"  id="tab-item-4" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-4">Item 4</button>
  <button class="nj-tab__item"  id="tab-item-5" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-5">Item 5</button>
  <button class="nj-tab__item"  id="tab-item-6" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-5" disabled>Item 6</button>
 </div>
 <div style="padding-top: var(--nj-size-space-16);">
   <div class="nj-tab__content nj-tab__content--active" id="tab-content-1" role="tabpanel" tabindex="0" aria-labelledby="tab-item-1">
     <p>My Item 1 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-2" role="tabpanel" tabindex="0" aria-labelledby="tab-item-2">
     <p>My Item 2 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-3" role="tabpanel" tabindex="0" aria-labelledby="tab-item-3">
     <p>My Item 3 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-4" role="tabpanel" tabindex="0" aria-labelledby="tab-item-4">
     <p>My Item 4 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-5" role="tabpanel" tabindex="0" aria-labelledby="tab-item-5">
     <p>My Item 5 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-6" role="tabpanel" tabindex="0" aria-labelledby="tab-item-6">
     <p>My Item 6 content</p>
   </div>
 </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% Tab style="spacious" %}
  {% Slot 'buttons' %}
    {% T_Btn label="Item 1" active=True id="tab-item-1" target_id="tab-content-1" %}
    {% T_Btn label="Item 2" disabled=True id="tab-item-2" target_id="tab-content-2" %}
    {% T_Btn label="Item 3" id="tab-item-3" target_id="tab-content-3" %}
    {% T_Btn label="Item 4" disabled=True id="tab-item-4" target_id="tab-content-4" %}
    {% T_Btn label="Item 5" id="tab-item-5" target_id="tab-content-5" %}
    {% T_Btn label="Item 6" id="tab-item-6" target_id="tab-content-5" %}
  {% endSlot %}
  {% T_Panel active=True id="tab-content-1" trigger_id="tab-item-1" %}
    <p>My Item 1 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-2" trigger_id="tab-item-2" %}
    <p>My Item 2 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-3" trigger_id="tab-item-3" %}
    <p>My Item 3 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-4" trigger_id="tab-item-4" %}
    <p>My Item 4 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-5" trigger_id="tab-item-5" %}
    <p>My Item 5 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-6" trigger_id="tab-item-6" %}
    <p>My Item 6 content</p>
  {% endT_Panel %}
{% endTab %}
"""
        expected = """
<div class="nj-tab nj-tab--spacious">
 <div class="nj-tab__items" role="tablist" aria-label="Tab system label">
  <button class="nj-tab__item nj-tab__item--active" id="tab-item-1" role="tab" aria-selected="true" tabindex="0" aria-controls="tab-content-1">Item 1</button>
  <button class="nj-tab__item"  id="tab-item-2" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-2" disabled>Item 2</button>
  <button class="nj-tab__item"  id="tab-item-3" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-3">Item 3</button>
  <button class="nj-tab__item"  id="tab-item-4" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-4" disabled>Item 4</button>
  <button class="nj-tab__item"  id="tab-item-5" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-5">Item 5</button>
  <button class="nj-tab__item"  id="tab-item-6" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-5">Item 6</button>
 </div>
 <div style="padding-top: var(--nj-size-space-16);">
   <div class="nj-tab__content nj-tab__content--active" id="tab-content-1" role="tabpanel" tabindex="0" aria-labelledby="tab-item-1">
     <p>My Item 1 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-2" role="tabpanel" tabindex="0" aria-labelledby="tab-item-2">
     <p>My Item 2 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-3" role="tabpanel" tabindex="0" aria-labelledby="tab-item-3">
     <p>My Item 3 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-4" role="tabpanel" tabindex="0" aria-labelledby="tab-item-4">
     <p>My Item 4 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-5" role="tabpanel" tabindex="0" aria-labelledby="tab-item-5">
     <p>My Item 5 content</p>
   </div>
   <div class="nj-tab__content" id="tab-content-6" role="tabpanel" tabindex="0" aria-labelledby="tab-item-6">
     <p>My Item 6 content</p>
   </div>
 </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% Tab style="stretched" %}
  {% Slot 'buttons' %}
    {% T_Btn label="Item 1" active=True id="tab-item-1" target_id="tab-content-1" %}
    {% T_Btn label="Item 2" disabled=True id="tab-item-2" target_id="tab-content-2" %}
    {% T_Btn label="Item 3" id="tab-item-3" target_id="tab-content-3" %}
    {% T_Btn label="Item 4" id="tab-item-4" target_id="tab-content-4" %}
    {% T_Btn label="Item 5" id="tab-item-5" target_id="tab-content-5" %}
    {% T_Btn label="Item 6" id="tab-item-6" target_id="tab-content-5" %}
  {% endSlot %}
  {% T_Panel active=True id="tab-content-1" trigger_id="tab-item-1" %}
    <p>My Item 1 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-2" trigger_id="tab-item-2" %}
    <p>My Item 2 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-3" trigger_id="tab-item-3" %}
    <p>My Item 3 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-4" trigger_id="tab-item-4" %}
    <p>My Item 4 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-5" trigger_id="tab-item-5" %}
    <p>My Item 5 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-6" trigger_id="tab-item-6" %}
    <p>My Item 6 content</p>
  {% endT_Panel %}
{% endTab %}
"""
        expected = """
<div class="nj-tab nj-tab--stretched">
  <div class="nj-tab__items" role="tablist" aria-label="Tab system label">
   <button class="nj-tab__item nj-tab__item--active" id="tab-item-1" role="tab" aria-selected="true" tabindex="0" aria-controls="tab-content-1">Item 1</button>
   <button class="nj-tab__item"  id="tab-item-2" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-2" disabled>Item 2</button>
   <button class="nj-tab__item"  id="tab-item-3" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-3">Item 3</button>
   <button class="nj-tab__item"  id="tab-item-4" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-4">Item 4</button>
   <button class="nj-tab__item"  id="tab-item-5" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-5">Item 5</button>
   <button class="nj-tab__item"  id="tab-item-6" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-5">Item 6</button>
  </div>
  <div style="padding-top: var(--nj-size-space-16);">
    <div class="nj-tab__content nj-tab__content--active" id="tab-content-1" role="tabpanel" tabindex="0" aria-labelledby="tab-item-1">
      <p>My Item 1 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-2" role="tabpanel" tabindex="0" aria-labelledby="tab-item-2">
      <p>My Item 2 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-3" role="tabpanel" tabindex="0" aria-labelledby="tab-item-3">
      <p>My Item 3 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-4" role="tabpanel" tabindex="0" aria-labelledby="tab-item-4">
      <p>My Item 4 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-5" role="tabpanel" tabindex="0" aria-labelledby="tab-item-5">
      <p>My Item 5 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-6" role="tabpanel" tabindex="0" aria-labelledby="tab-item-6">
      <p>My Item 6 content</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Tab %}
  {% Slot 'buttons' %}
    {% T_Btn label="Item 1" id="tab-item-1" target_id="tab-content-1" %}
    {% T_Btn label="Item 2" active=True id="tab-item-2" target_id="tab-content-2" %}
    {% T_Btn label="Item 3" disabled=True id="tab-item-3" target_id="tab-content-3" %}
    {% T_Btn label="Item 4" id="tab-item-4" target_id="tab-content-4" %}
  {% endSlot %}
  {% T_Panel id="tab-content-1" trigger_id="tab-item-1" %}
    <p>My Item 1 content</p>
  {% endT_Panel %}
  {% T_Panel active=True id="tab-content-2" trigger_id="tab-item-2" %}
    <p>My Item 2 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-3" trigger_id="tab-item-3" %}
    <p>My Item 3 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-4" trigger_id="tab-item-4" %}
    <p>My Item 4 content</p>
  {% endT_Panel %}
{% endTab %}
"""
        expected = """
<div class="nj-tab">
  <div class="nj-tab__items" role="tablist" aria-label="Tab system label">
    <button class="nj-tab__item" id="tab-item-1" role="tab" aria-selected="false" tabindex="-1" aria-controls="tab-content-1">Item 1</button>
    <button class="nj-tab__item nj-tab__item--active"  id="tab-item-2" role="tab" aria-selected="true" tabindex="0" aria-controls="tab-content-2">Item 2</button>
    <button class="nj-tab__item"  id="tab-item-3" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-3" disabled>Item 3</button>
    <button class="nj-tab__item"  id="tab-item-4" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-4">Item 4</button>
  </div>
  <div style="padding-top: var(--nj-size-space-16);">
    <div class="nj-tab__content" id="tab-content-1" role="tabpanel" tabindex="0" aria-labelledby="tab-item-1">
      <p>My Item 1 content</p>
    </div>
    <div class="nj-tab__content nj-tab__content--active" id="tab-content-2" role="tabpanel" tabindex="0" aria-labelledby="tab-item-2">
      <p>My Item 2 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-3" role="tabpanel" tabindex="0" aria-labelledby="tab-item-3">
      <p>My Item 3 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-4" role="tabpanel" tabindex="0" aria-labelledby="tab-item-4">
      <p>My Item 4 content</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Tab style="compact" %}
  {% Slot 'buttons' %}
    {% T_Btn label="Item 1" active=True id="tab-item-1" target_id="tab-content-1" %}
    {% T_Btn label="Item 2" id="tab-item-2" target_id="tab-content-2" %}
    {% T_Btn label="Item 3" id="tab-item-3" target_id="tab-content-3" %}
    {% T_Btn label="Item 4" id="tab-item-4" target_id="tab-content-4" %}
  {% endSlot %}
  {% T_Panel active=True id="tab-content-1" trigger_id="tab-item-1" %}
    <p>My Item 1 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-2" trigger_id="tab-item-2" %}
    <p>My Item 2 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-3" trigger_id="tab-item-3" %}
    <p>My Item 3 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-4" trigger_id="tab-item-4" %}
    <p>My Item 4 content</p>
  {% endT_Panel %}
{% endTab %}
"""
        expected = """
<div class="nj-tab nj-tab--compact">
  <div class="nj-tab__items" role="tablist" aria-label="Tab system label">
    <button class="nj-tab__item nj-tab__item--active" id="tab-item-1" role="tab" aria-selected="true" tabindex="0" aria-controls="tab-content-1">Item 1</button>
    <button class="nj-tab__item"  id="tab-item-2" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-2">Item 2</button>
    <button class="nj-tab__item"  id="tab-item-3" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-3">Item 3</button>
    <button class="nj-tab__item"  id="tab-item-4" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-4">Item 4</button>
  </div>
  <div style="padding-top: var(--nj-size-space-16);">
    <div class="nj-tab__content nj-tab__content--active" id="tab-content-1" role="tabpanel" tabindex="0" aria-labelledby="tab-item-1">
      <p>My Item 1 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-2" role="tabpanel" tabindex="0" aria-labelledby="tab-item-2">
      <p>My Item 2 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-3" role="tabpanel" tabindex="0" aria-labelledby="tab-item-3">
      <p>My Item 3 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-4" role="tabpanel" tabindex="0" aria-labelledby="tab-item-4">
      <p>My Item 4 content</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Tab style="spacious" %}
  {% Slot 'buttons' %}
    {% T_Btn label="Item 1" active=True id="tab-item-1" target_id="tab-content-1" %}
    {% T_Btn label="Item 2" disabled=True id="tab-item-2" target_id="tab-content-2" %}
    {% T_Btn label="Item 3" id="tab-item-3" target_id="tab-content-3" %}
    {% T_Btn label="Item 4" disabled=True id="tab-item-4" target_id="tab-content-4" %}
  {% endSlot %}
  {% T_Panel active=True id="tab-content-1" trigger_id="tab-item-1" %}
    <p>My Item 1 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-2" trigger_id="tab-item-2" %}
    <p>My Item 2 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-3" trigger_id="tab-item-3" %}
    <p>My Item 3 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-4" trigger_id="tab-item-4" %}
    <p>My Item 4 content</p>
  {% endT_Panel %}
{% endTab %}
"""
        expected = """
<div class="nj-tab nj-tab--spacious">
  <div class="nj-tab__items" role="tablist" aria-label="Tab system label">
    <button class="nj-tab__item nj-tab__item--active" id="tab-item-1" role="tab" aria-selected="true" tabindex="0" aria-controls="tab-content-1">Item 1</button>
    <button class="nj-tab__item"  id="tab-item-2" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-2" disabled>Item 2</button>
    <button class="nj-tab__item"  id="tab-item-3" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-3">Item 3</button>
    <button class="nj-tab__item"  id="tab-item-4" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-4" disabled>Item 4</button>
  </div>
  <div style="padding-top: var(--nj-size-space-16);">
    <div class="nj-tab__content nj-tab__content--active" id="tab-content-1" role="tabpanel" tabindex="0" aria-labelledby="tab-item-1">
      <p>My Item 1 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-2" role="tabpanel" tabindex="0" aria-labelledby="tab-item-2">
      <p>My Item 2 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-3" role="tabpanel" tabindex="0" aria-labelledby="tab-item-3">
      <p>My Item 3 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-4" role="tabpanel" tabindex="0" aria-labelledby="tab-item-4">
      <p>My Item 4 content</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Tab style="stretched" %}
  {% Slot 'buttons' %}
    {% T_Btn label="Item 1" active=True id="tab-item-1" target_id="tab-content-1" %}
    {% T_Btn label="Item 2" disabled=True id="tab-item-2" target_id="tab-content-2" %}
    {% T_Btn label="Item 3" id="tab-item-3" target_id="tab-content-3" %}
    {% T_Btn label="Item 4" id="tab-item-4" target_id="tab-content-4" %}
  {% endSlot %}
  {% T_Panel active=True id="tab-content-1" trigger_id="tab-item-1" %}
    <p>My Item 1 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-2" trigger_id="tab-item-2" %}
    <p>My Item 2 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-3" trigger_id="tab-item-3" %}
    <p>My Item 3 content</p>
  {% endT_Panel %}
  {% T_Panel id="tab-content-4" trigger_id="tab-item-4" %}
    <p>My Item 4 content</p>
  {% endT_Panel %}
{% endTab %}
"""
        expected = """
<div class="nj-tab nj-tab--stretched">
  <div class="nj-tab__items" role="tablist" aria-label="Tab system label">
    <button class="nj-tab__item nj-tab__item--active" id="tab-item-1" role="tab" aria-selected="true" tabindex="0" aria-controls="tab-content-1">Item 1</button>
    <button class="nj-tab__item"  id="tab-item-2" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-2" disabled>Item 2</button>
    <button class="nj-tab__item"  id="tab-item-3" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-3">Item 3</button>
    <button class="nj-tab__item"  id="tab-item-4" role="tab" aria-selected="false" tabindex="-1"  aria-controls="tab-content-4">Item 4</button>
  </div>
  <div style="padding-top: var(--nj-size-space-16);">
    <div class="nj-tab__content nj-tab__content--active" id="tab-content-1" role="tabpanel" tabindex="0" aria-labelledby="tab-item-1">
      <p>My Item 1 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-2" role="tabpanel" tabindex="0" aria-labelledby="tab-item-2">
      <p>My Item 2 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-3" role="tabpanel" tabindex="0" aria-labelledby="tab-item-3">
      <p>My Item 3 content</p>
    </div>
    <div class="nj-tab__content" id="tab-content-4" role="tabpanel" tabindex="0" aria-labelledby="tab-item-4">
      <p>My Item 4 content</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
