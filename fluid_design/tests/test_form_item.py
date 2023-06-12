# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class FormItemTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% TextInput form1.text %}
"""
        expected = """
<div class="nj-form-item nj-form-item--static">
  <div class="nj-form-item__field-wrapper">
    <input name="text" value="a text" type="text" required id="id_text"
        class="nj-form-item__field">
    <label for="id_text" class="nj-form-item__label">
      Text
      <span class="nj-form-item__required-asterisk">*</span>
    </label>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 24px; padding: 20px; width: 350px; margin: 0 auto">
  {% TextInput form1.text_empty floating=True id="exampleFloatingFirstName" %}
  {% TextInput form1.text_empty floating=True size="xl" id="exampleFloatingFirstNameXl" %}
  {% TextInput form1.text_empty floating=True size="lg" id="exampleFloatingFirstNameLg" %}
  {% TextInput form1.text_empty floating=True size="sm" id="exampleFloatingFirstNameSm" %}
  {% PasswordInput form1.text_empty floating=True id="examplePassword" %}
  {% TextInputIcon form1.text_empty floating=True id="exampleFloatingFirstNameIcon" %}
    {% Slot 'icon' class="material-icons" %}
      info_outline
    {% endSlot %}
  {% endTextInputIcon %}
  {% TextInput form1.number_help floating=True id="exampleFloatingFirstNameInfo" %}
  {% TextInput form1.text_missing floating=True id="exampleFloatingFirstNameError" %}
  {% TextInput form1.text floating=True id="exampleFloatingRequired" %}
  {% TextInput form1.text_empty floating=True readonly=True id="exampleFloatingReadOnly" %}
  {% TextInputIcon form1.number_help floating=True disabled=True id="exampleFloatingDisabled" %}
    {% Slot 'icon' class="material-icons" %}
      info_outline
    {% endSlot %}
  {% endTextInputIcon %}
</form>
"""
        expected = """
  <form style="display: flex; flex-direction: column; gap: 24px; padding: 20px; width: 350px; margin: 0 auto">
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleFloatingFirstName" placeholder="">
        <label for="exampleFloatingFirstName" class="nj-form-item__label">Text empty</label>
      </div>
    </div>
    <div class="nj-form-item nj-form-item--xl">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleFloatingFirstNameXl" placeholder="">
        <label for="exampleFloatingFirstNameXl" class="nj-form-item__label">Text empty</label>
      </div>
    </div>
    <div class="nj-form-item nj-form-item--lg">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleFloatingFirstNameLg" placeholder="">
        <label for="exampleFloatingFirstNameLg" class="nj-form-item__label">Text empty</label>
      </div>
    </div>
    <div class="nj-form-item nj-form-item--sm">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleFloatingFirstNameSm" placeholder="">
        <label for="exampleFloatingFirstNameSm" class="nj-form-item__label">Text empty</label>
      </div>
    </div>
    <div class="nj-form-item nj-form-item--password">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="password" class="nj-form-item__field" id="examplePassword" placeholder="">
        <label for="examplePassword" class="nj-form-item__label">Text empty</label>
        <button type="button" aria-pressed="false" class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
          <span class="nj-sr-only" data-password-button-label-show="Show password" data-password-button-label-hide="Hide password"></span>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
        </button>
        <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true" data-password-notice-is-visible="Password is visible" data-password-notice-is-hidden="Password is hidden"></p>
      </div>
    </div>
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleFloatingFirstNameIcon" placeholder="">
        <label for="exampleFloatingFirstNameIcon" class="nj-form-item__label">Text empty</label>
        <span aria-hidden="true" class="nj-form-item__icon material-icons">info_outline</span>
      </div>
    </div>
     <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input name="number_help" value="1" type="number" class="nj-form-item__field" id="exampleFloatingFirstNameInfo" placeholder="" aria-describedby="exampleFloatingFirstNameInfo-hint" aria-controls="exampleFloatingFirstNameInfo-hint">
        <label for="exampleFloatingFirstNameInfo" class="nj-form-item__label">Number input label</label>
      </div>
      <p id="exampleFloatingFirstNameInfo-hint" class="nj-form-item__subscript">
        Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
      </p>
    </div>
     <div class="nj-form-item nj-form-item--error">
      <div class="nj-form-item__field-wrapper">
        <input name="text_missing" type="text" class="nj-form-item__field" id="exampleFloatingFirstNameError" placeholder="" aria-describedby="exampleFloatingFirstNameError-error" aria-controls="exampleFloatingFirstNameError-error" aria-invalid="true" required>
        <label for="exampleFloatingFirstNameError" class="nj-form-item__label">Text missing<span class="nj-form-item__required-asterisk">*</span></label>
      </div>
      <p id="exampleFloatingFirstNameError-error" class="nj-form-item__subscript">
        <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">warning</span>
        This field is required.
      </p>
    </div>
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input name="text" value="a text" type="text" class="nj-form-item__field" id="exampleFloatingRequired" placeholder="" required>
        <label for="exampleFloatingRequired" class="nj-form-item__label">Text<span class="nj-form-item__required-asterisk">*</span></label>
      </div>
    </div>
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleFloatingReadOnly" placeholder="" readonly>
        <label for="exampleFloatingReadOnly" class="nj-form-item__label">Text empty</label>
      </div>
    </div>
    <div class="nj-form-item nj-form-item--disabled">
      <div class="nj-form-item__field-wrapper">
        <input name="number_help" value="1"  type="number" class="nj-form-item__field" id="exampleFloatingDisabled" placeholder="" disabled aria-describedby="exampleFloatingDisabled-hint" aria-controls="exampleFloatingDisabled-hint">
        <label for="exampleFloatingDisabled" class="nj-form-item__label">Number input label</label>
        <span aria-hidden="true" class="nj-form-item__icon material-icons">info_outline</span>
      </div>
      <p id="exampleFloatingDisabled-hint" class="nj-form-item__subscript">
        Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
      </p>
    </div>
  </form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 24px; padding: 20px; width: 350px; margin: 0 auto">
  {% TextInput form1.text_empty floating=True id="exampleFloatingFirstName" %}
  {% TextInput form1.text_empty floating=True size="xl" id="exampleFloatingFirstNameXl" %}
  {% TextInput form1.text_empty floating=True size="lg" id="exampleFloatingFirstNameLg" %}
  {% TextInput form1.text_empty floating=True size="sm" id="exampleFloatingFirstNameSm" %}
  {% PasswordInput form1.text_empty floating=True id="examplePassword" %}
  {% TextInputIcon form1.text_empty floating=True id="exampleFloatingFirstNameIcon" %}
    {% Slot 'icon' class="material-icons" %}
      info_outline
    {% endSlot %}
  {% endTextInputIcon %}
  {% TextInput form1.number_help floating=True id="exampleFloatingFirstNameInfo" %}
  {% TextInput form1.text_missing floating=True id="exampleFloatingFirstNameError" %}
  {% TextInput form1.text floating=True id="exampleFloatingRequired" %}
  {% TextInput form1.text_empty floating=True readonly=True id="exampleFloatingReadOnly" %}
  {% TextInputIcon form1.number_help floating=True disabled=True id="exampleFloatingDisabled" %}
    {% Slot 'icon' class="material-icons" %}
      info_outline
    {% endSlot %}
  {% endTextInputIcon %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px; padding: 20px">
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticFirstName" placeholder="First name">
      <label for="exampleInputStaticFirstName" class="nj-form-item__label">Firstname</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--xl">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticFirstNameXl" placeholder="First name xl">
      <label for="exampleInputStaticFirstNameXl" class="nj-form-item__label">Firstname xl</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--lg">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticFirstNameLg" placeholder="First name lg">
      <label for="exampleInputStaticFirstNameLg" class="nj-form-item__label">Firstname lg</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--sm">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticFirstNameSm" placeholder="First name sm">
      <label for="exampleInputStaticFirstNameSm" class="nj-form-item__label">Firstname sm</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--password">
    <div class="nj-form-item__field-wrapper">
      <input type="password" class="nj-form-item__field" id="examplePasswordStatic" placeholder="password">
      <label for="examplePasswordStatic" class="nj-form-item__label">Password</label>
      <button type="button" aria-pressed="false" class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
        <span class="nj-sr-only" data-password-button-label-show="Show password" data-password-button-label-hide="Hide password"></span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
      </button>
      <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true" data-password-notice-is-visible="Password is visible" data-password-notice-is-hidden="Password is hidden"></p>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticIcon" placeholder="sm">
      <label for="exampleInputStaticIcon" class="nj-form-item__label">Firstname sm</label>
      <i class="nj-form-item__icon material-icons">info_outline</i>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticFirstNameInfo" placeholder="default" aria-describedby="static-firstname-hint">
      <label for="exampleInputStaticFirstNameInfo" class="nj-form-item__label">Firstname</label>
    </div>
    <p id="static-firstname-hint" class="nj-form-item__subscript">Information</p>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--error">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticFirstNameError" placeholder="default" aria-describedby="static-firstname-error" aria-invalid="true">
      <label for="exampleInputStaticFirstNameError" class="nj-form-item__label">Firstname</label>
    </div>
    <p id="static-firstname-error" class="nj-form-item__subscript">
     <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">warning</span>
     Error
     </p>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticRequired" placeholder="First name" required>
      <label for="exampleInputStaticRequired" class="nj-form-item__label">Firstname<span class="nj-form-item__required-asterisk">*</span></label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticReadOnly" placeholder="default" value="readonly" readonly>
      <label for="exampleInputStaticReadOnly" class="nj-form-item__label">Firstname read only</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--disabled">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputStaticDisabled" placeholder="default" value="disabled" disabled aria-describedby="static-firstname-disabled">
      <label for="exampleInputStaticDisabled" class="nj-form-item__label">Firstname disabled</label>
      <i class="nj-form-item__icon material-icons">info_outline</i>
    </div>
    <p id="static-firstname-disabled" class="nj-form-item__subscript">Information</p>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px; padding: 20px">
  <div class="nj-form-item nj-form-item--textarea nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <textarea class="nj-form-item__field" id="exampleTextAreaStatic" placeholder="Comment"></textarea>
      <label for="exampleTextAreaStatic" class="nj-form-item__label">Firstname</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea class="nj-form-item__field" id="exampleTextAreaFloat" placeholder=" "></textarea>
      <label for="exampleTextAreaFloat" class="nj-form-item__label">Firstname</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea class="nj-form-item__field" id="exampleTextAreaFloatInfo" placeholder=" " aria-describedby="textarea-hint"></textarea>
      <label for="exampleTextAreaFloatInfo" class="nj-form-item__label">Firstname</label>
    </div>
    <p id="textarea-hint" class="nj-form-item__subscript">Information</p>
  </div>
  <div class="nj-form-item nj-form-item--textarea nj-form-item--error">
    <div class="nj-form-item__field-wrapper">
      <textarea class="nj-form-item__field" id="exampleTextAreaFloatError" placeholder=" " aria-describedby="textarea-error" aria-invalid="true"></textarea>
      <label for="exampleTextAreaFloatError" class="nj-form-item__label">Firstname</label>
    </div>
    <p id="textarea-error" class="nj-form-item__subscript">
     <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">warning</span>
     Error
    </p>
  </div
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleFloatingInput" placeholder="default">
      <label for="exampleFloatingInput" class="nj-form-item__label">Floating</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleStaticInput" placeholder="Static text field example">
      <label for="exampleStaticInput" class="nj-form-item__label">Static</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputFirstName" placeholder="default">
      <label for="exampleInputFirstName" class="nj-form-item__label">Firstname</label>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputLastName" placeholder="default">
      <label for="exampleInputLastName" class="nj-form-item__label">Lastname</label>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputEmail" placeholder="default" required>
      <label for="exampleInputEmail" class="nj-form-item__label">Email</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--password">
    <div class="nj-form-item__field-wrapper">
      <input type="password" class="nj-form-item__field" id="examplePassword" placeholder=" " required>
      <label for="examplePassword" class="nj-form-item__label">Password</label>
      <button type="button" aria-pressed="false" class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
        <span class="sr-only" data-password-button-label-show="Show password" data-password-button-label-hide="Hide password"></span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
      </button>
      <p class="sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true" data-password-notice-is-visible="Password is visible" data-password-notice-is-hidden="Password is hidden"></p>
    </div>
    <div class="nj-form-item__subscript">Must be x character long</div>
  </div>
  <div class="nj-form-item nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea class="nj-form-item__field" id="exampleTextAreaFloat" placeholder="Comment"></textarea>
      <label for="exampleTextAreaFloat" class="nj-form-item__label">Comment</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputFirstName" placeholder="default">
      <label for="exampleInputFirstName" class="nj-form-item__label">Firstname</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputLastName" placeholder="default">
      <label for="exampleInputLastName" class="nj-form-item__label">Lastname</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputEmail" placeholder="default" required>
      <label for="exampleInputEmail" class="nj-form-item__label">Email</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--password">
    <div class="nj-form-item__field-wrapper">
      <input type="password" class="nj-form-item__field" id="examplePassword" placeholder=" " required>
      <label for="examplePassword" class="nj-form-item__label">Password</label>
      <button type="button" aria-pressed="false" class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
        <span class="sr-only" data-password-button-label-show="Show password" data-password-button-label-hide="Hide password"></span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
      </button>
      <p class="sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true" data-password-notice-is-visible="Password is visible" data-password-notice-is-hidden="Password is hidden"></p>
    </div>
    <div class="nj-form-item__subscript">Must be x character long</div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea class="nj-form-item__field" id="exampleTextAreaFloatStatic" placeholder="Comment"></textarea>
      <label for="exampleTextAreaFloatStatic" class="nj-form-item__label">Comment</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputRequired" placeholder="default" required>
      <label for="exampleInputRequired" class="nj-form-item__label">Required</label>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputReadOnly" placeholder="default" value="readonly value" readonly>
      <label for="exampleInputReadOnly" class="nj-form-item__label">Read only</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--disabled">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputDisabled" placeholder="default" value="disabled value" disabled>
      <label for="exampleInputDisabled" class="nj-form-item__label">Disabled</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item nj-form-item--error">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleFloatingFirstNameError" placeholder=" " aria-describedby="floating-firstname-error" aria-invalid="true" required>
      <label for="exampleFloatingFirstNameError" class="nj-form-item__label">Firstname<span class="nj-form-item__required-asterisk">*</span></label>
    </div>
    <p id="floating-firstname-error" class="nj-form-item__subscript">
      <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">warning</span>
      Error
    </p>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; gap: 24px;">
  <div class="nj-form-item nj-form-item--sm">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleSmFloatingInputsm" placeholder="default">
      <label for="exampleSmFloatingInputsm" class="nj-form-item__label">Sm</label>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleFloatingInputmd" placeholder="default">
      <label for="exampleFloatingInputmd" class="nj-form-item__label">Default</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--lg">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleLgFloatingInputlg" placeholder="default">
      <label for="exampleLgFloatingInputlg" class="nj-form-item__label">Lg</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--xl">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleXlFloatingInputxl" placeholder="default">
      <label for="exampleXlFloatingInputxl" class="nj-form-item__label">Xl</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example11(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputWithInfo" placeholder="default">
      <label for="exampleInputWithInfo" class="nj-form-item__label">Example with information</label>
    </div>
    <div class="nj-form-item__subscript">Information line</div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example12(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputFirstNameSm" placeholder="sm">
      <label for="exampleInputFirstNameSm" class="nj-form-item__label">Firstname sm</label>
      <span aria-hidden="true" class="nj-form-item__icon material-icons">info_outline</span>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input type="text" class="nj-form-item__field" id="exampleInputFirstNameSm" placeholder="sm">
      <label for="exampleInputFirstNameSm" class="nj-form-item__label">Firstname sm</label>
      <span aria-hidden="true" class="nj-form-item__icon material-icons">check</span>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example13(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form>
  <div class="nj-form-item nj-form-item--input-number">
    <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-default">
      <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
        <span class="nj-sr-only">- Decrement</span>
      </button>
  
      <input
        type="number"
        inputmode="numeric"
        class="nj-form-item__field"
        id="input-number-default"
        value="0"
        min="-100"
        max="100"
      >
      <label for="input-number-default" class="nj-form-item__label">Amount</label>
  
      <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button">
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
        <span class="nj-sr-only">+ Increment</span>
      </button>
  
      <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example14(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item nj-form-item--password">
    <div class="nj-form-item__field-wrapper">
      <input type="password" class="nj-form-item__field" id="examplePassword" placeholder=" " required>
      <label for="examplePassword" class="nj-form-item__label">Password</label>
      <button type="button" aria-pressed="false"
              class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
        <span class="sr-only" data-password-button-label-show="Show password"
              data-password-button-label-hide="Hide password"></span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
      </button>
      <p class="sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true"
         data-password-notice-is-visible="Password is visible"
         data-password-notice-is-hidden="Password is hidden"></p>
    </div>
    <div class="nj-form-item__subscript">Must be x character long</div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example15(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea class="nj-form-item__field" id="exampleTextArea" placeholder="Comment"></textarea>
     <label for="exampleTextArea" class="nj-form-item__label">Comment</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example16(self):
        template = """
{% load fluid_design %}
"""
        expected = """
<form class="row">
  <div class="col-md-7">
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input type="text" class="nj-form-item__field" id="exampleColumnSizing1" placeholder="default">
        <label for="exampleColumnSizing1" class="nj-form-item__label">City</label>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input type="text" class="nj-form-item__field" id="exampleColumnSizing2" placeholder="default">
        <label for="exampleColumnSizing2" class="nj-form-item__label">State</label>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input type="text" class="nj-form-item__field" id="exampleColumnSizing3" placeholder="default">
        <label for="exampleColumnSizing3" class="nj-form-item__label">Zip</label>
      </div>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
