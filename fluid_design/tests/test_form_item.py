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
<form style="display: flex; flex-direction: column; gap: 24px; padding: 20px">
  {% TextInput form1.text_empty placeholder="First name" id="exampleInputStaticFirstName" %}
  {% TextInput form1.text_empty size="xl" placeholder="First name xl" id="exampleInputStaticFirstNameXl" %}
  {% TextInput form1.text_empty size="lg" placeholder="First name lg" id="exampleInputStaticFirstNameLg" %}
  {% TextInput form1.text_empty size="sm" placeholder="First name sm" id="exampleInputStaticFirstNameSm" %}
  {% PasswordInput form1.text_empty placeholder="password" id="examplePasswordStatic" %}
  {% TextInputIcon form1.text_empty placeholder="sm" id="exampleInputStaticIcon" %}
    {% Slot 'icon' class="material-icons" %}
      info_outline
    {% endSlot %}
  {% endTextInputIcon %}
  {% TextInput form1.number_help placeholder="default" id="exampleInputStaticFirstNameInfo" %}
  {% TextInput form1.text_missing placeholder="default" id="exampleInputStaticFirstNameError" %}
  {% TextInput form1.text placeholder="First name" id="exampleInputStaticRequired" %}
  {% TextInput form1.text_empty placeholder="default" readonly=True id="exampleInputStaticReadOnly" %}
  {% TextInputIcon form1.number_help disabled=True placeholder="default" id="exampleInputStaticDisabled" %}
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
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputStaticFirstName" placeholder="First name">
      <label for="exampleInputStaticFirstName" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--xl">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputStaticFirstNameXl" placeholder="First name xl">
      <label for="exampleInputStaticFirstNameXl" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--lg">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputStaticFirstNameLg" placeholder="First name lg">
      <label for="exampleInputStaticFirstNameLg" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--sm">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputStaticFirstNameSm" placeholder="First name sm">
      <label for="exampleInputStaticFirstNameSm" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--password nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="password" class="nj-form-item__field" id="examplePasswordStatic" placeholder="password">
      <label for="examplePasswordStatic" class="nj-form-item__label">Text empty</label>
      <button type="button" aria-pressed="false" class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
        <span class="nj-sr-only" data-password-button-label-show="Show password" data-password-button-label-hide="Hide password"></span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
      </button>
      <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true" data-password-notice-is-visible="Password is visible" data-password-notice-is-hidden="Password is hidden"></p>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputStaticIcon" placeholder="sm">
      <label for="exampleInputStaticIcon" class="nj-form-item__label">Text empty</label>
      <span aria-hidden="true" class="nj-form-item__icon material-icons">info_outline</span>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="number_help" value="1" type="number" class="nj-form-item__field" id="exampleInputStaticFirstNameInfo" placeholder="default"
          aria-describedby="exampleInputStaticFirstNameInfo-hint"
          aria-controls="exampleInputStaticFirstNameInfo-hint">
      <label for="exampleInputStaticFirstNameInfo" class="nj-form-item__label">Number input label</label>
    </div>
    <p id="exampleInputStaticFirstNameInfo-hint" class="nj-form-item__subscript">
      Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
    </p>
  </div>
  <div class="nj-form-item nj-form-item--error nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text_missing" type="text" required class="nj-form-item__field" id="exampleInputStaticFirstNameError" placeholder="default" aria-invalid="true"
          aria-describedby="exampleInputStaticFirstNameError-error"
          aria-controls="exampleInputStaticFirstNameError-error">
      <label for="exampleInputStaticFirstNameError" class="nj-form-item__label">
        Text missing
        <span class="nj-form-item__required-asterisk">*</span>
      </label>
    </div>
    <p id="exampleInputStaticFirstNameError-error" class="nj-form-item__subscript">
     <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">warning</span>
     This field is required.
     </p>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text" value="a text" type="text" class="nj-form-item__field" id="exampleInputStaticRequired" placeholder="First name" required>
      <label for="exampleInputStaticRequired" class="nj-form-item__label">Text<span class="nj-form-item__required-asterisk">*</span></label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputStaticReadOnly" placeholder="default" readonly>
      <label for="exampleInputStaticReadOnly" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static nj-form-item--disabled">
    <div class="nj-form-item__field-wrapper">
      <input name="number_help" type="number" class="nj-form-item__field" id="exampleInputStaticDisabled" placeholder="default" value="1" disabled
          aria-describedby="exampleInputStaticDisabled-hint"
          aria-controls="exampleInputStaticDisabled-hint">
      <label for="exampleInputStaticDisabled" class="nj-form-item__label">Number input label</label>
      <span aria-hidden="true" class="nj-form-item__icon material-icons">info_outline</span>
    </div>
    <p id="exampleInputStaticDisabled-hint" class="nj-form-item__subscript">
      Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
    </p>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 24px; padding: 20px">
  {% Textarea form1.text_empty placeholder="Comment" id="exampleTextAreaStatic" %}
  {% Textarea form1.text_empty floating=True id="exampleTextAreaFloat" %}
  {% Textarea form1.text_help floating=True id="exampleTextAreaFloatInfo" %}
  {% Textarea form1.text_missing floating=True id="exampleTextAreaFloatError" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px; padding: 20px">
  <div class="nj-form-item nj-form-item--textarea nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <textarea name="text_empty" cols="40" rows="10" class="nj-form-item__field" id="exampleTextAreaStatic" placeholder="Comment">
</textarea>
      <label for="exampleTextAreaStatic" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea name="text_empty" cols="40" rows="10" class="nj-form-item__field" id="exampleTextAreaFloat" placeholder="">
</textarea>
      <label for="exampleTextAreaFloat" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea name="text_help" cols="40" rows="10" class="nj-form-item__field" id="exampleTextAreaFloatInfo" placeholder=""
          aria-describedby="exampleTextAreaFloatInfo-hint"
          aria-controls="exampleTextAreaFloatInfo-hint">
</textarea>
      <label for="exampleTextAreaFloatInfo" class="nj-form-item__label">Text help</label>
    </div>
    <p id="exampleTextAreaFloatInfo-hint" class="nj-form-item__subscript">
      Must be x character long
    </p>
  </div>
  <div class="nj-form-item nj-form-item--textarea nj-form-item--error">
    <div class="nj-form-item__field-wrapper">
      <textarea name="text_missing" cols="40" rows="10" required class="nj-form-item__field" id="exampleTextAreaFloatError" placeholder="" aria-invalid="true"
          aria-describedby="exampleTextAreaFloatError-error"
          aria-controls="exampleTextAreaFloatError-error">
</textarea>
      <label for="exampleTextAreaFloatError" class="nj-form-item__label">
        Text missing
        <span class="nj-form-item__required-asterisk">*</span>
      </label>
    </div>
    <p id="exampleTextAreaFloatError-error" class="nj-form-item__subscript">
     <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">warning</span>
     This field is required.
    </p>
  </div
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<form>
  {% TextInput form1.text_empty floating=True id="exampleFloatingInput" %}
</form>
"""
        expected = """
<form>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleFloatingInput" placeholder="">
      <label for="exampleFloatingInput" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<form>
  {% TextInput form1.text_empty label="Static" placeholder="Static text field example" id="exampleStaticInput" %}
</form>
"""
        expected = """
<form>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleStaticInput" placeholder="Static text field example">
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
<form style="display: flex; flex-direction: column; gap: 24px;">
  {% TextInput form1.text_empty floating=True id="exampleInputFirstName" %}
  {% TextInput form1.text_empty floating=True id="exampleInputLastName" %}
  {% TextInput form1.text floating=True id="exampleInputEmail" %}
  {% PasswordInput form1.text_help floating=True id="examplePassword" %}
  {% Textarea form1.text_empty floating=True id="exampleTextAreaFloat" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputFirstName" placeholder="">
      <label for="exampleInputFirstName" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputLastName" placeholder="">
      <label for="exampleInputLastName" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text" value="a text" type="text" class="nj-form-item__field" id="exampleInputEmail" placeholder="" required>
      <label for="exampleInputEmail" class="nj-form-item__label">
        Text
        <span class="nj-form-item__required-asterisk">*</span>
      </label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--password">
    <div class="nj-form-item__field-wrapper">
      <input name="text_help" type="password" class="nj-form-item__field" id="examplePassword" placeholder=""
          aria-describedby="examplePassword-hint"
          aria-controls="examplePassword-hint">
      <label for="examplePassword" class="nj-form-item__label">Text help</label>
      <button type="button" aria-pressed="false" class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
        <span class="nj-sr-only" data-password-button-label-show="Show password" data-password-button-label-hide="Hide password"></span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
      </button>
      <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true" data-password-notice-is-visible="Password is visible" data-password-notice-is-hidden="Password is hidden"></p>
    </div>
    <p id="examplePassword-hint" class="nj-form-item__subscript">Must be x character long</p>
  </div>
  <div class="nj-form-item nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea name="text_empty" cols="40" rows="10" class="nj-form-item__field" id="exampleTextAreaFloat" placeholder="">
</textarea>
      <label for="exampleTextAreaFloat" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 24px;">
  {% TextInput form1.text_empty placeholder="default" id="exampleInputFirstName" %}
  {% TextInput form1.text_empty placeholder="default" id="exampleInputLastName" %}
  {% TextInput form1.text placeholder="default" id="exampleInputEmail" %}
  {% PasswordInput form1.text_help id="examplePassword" %}
  {% Textarea form1.text_empty placeholder="Comment" id="exampleTextAreaFloatStatic" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputFirstName" placeholder="default">
      <label for="exampleInputFirstName" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputLastName" placeholder="default">
      <label for="exampleInputLastName" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text" value="a text" type="text" class="nj-form-item__field" id="exampleInputEmail" placeholder="default" required>
      <label for="exampleInputEmail" class="nj-form-item__label">
        Text
        <span class="nj-form-item__required-asterisk">*</span>
      </label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--password nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <input name="text_help" type="password" class="nj-form-item__field" id="examplePassword"
          aria-describedby="examplePassword-hint"
          aria-controls="examplePassword-hint">
      <label for="examplePassword" class="nj-form-item__label">Text help</label>
      <button type="button" aria-pressed="false" class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
        <span class="nj-sr-only" data-password-button-label-show="Show password" data-password-button-label-hide="Hide password"></span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
      </button>
      <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true" data-password-notice-is-visible="Password is visible" data-password-notice-is-hidden="Password is hidden"></p>
    </div>
    <p id="examplePassword-hint" class="nj-form-item__subscript">Must be x character long</p>
  </div>
  <div class="nj-form-item nj-form-item--textarea nj-form-item--static">
    <div class="nj-form-item__field-wrapper">
      <textarea name="text_empty" cols="40" rows="10" class="nj-form-item__field" id="exampleTextAreaFloatStatic" placeholder="Comment">
</textarea>
      <label for="exampleTextAreaFloatStatic" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 24px;">
  {% TextInput form1.text floating=True id="exampleInputRequired" %}
  {% TextInput form1.text_empty floating=True readonly=True id="exampleInputReadOnly" %}
  {% TextInput form1.text_empty floating=True disabled=True id="exampleInputDisabled" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text" value="a text" type="text" class="nj-form-item__field" id="exampleInputRequired" placeholder="" required>
      <label for="exampleInputRequired" class="nj-form-item__label">
        Text
        <span class="nj-form-item__required-asterisk">*</span>
      </label>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputReadOnly" placeholder="" readonly>
      <label for="exampleInputReadOnly" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--disabled">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputDisabled" placeholder="" disabled>
      <label for="exampleInputDisabled" class="nj-form-item__label">Text empty</label>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 24px;">
  {% TextInput form1.text_missing floating=True id="exampleFloatingFirstNameError" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item nj-form-item--error">
    <div class="nj-form-item__field-wrapper">
      <input name="text_missing" type="text" class="nj-form-item__field"
          id="exampleFloatingFirstNameError" placeholder=""
          aria-describedby="exampleFloatingFirstNameError-error"
          aria-controls="exampleFloatingFirstNameError-error"
          aria-invalid="true" required>
      <label for="exampleFloatingFirstNameError" class="nj-form-item__label">Text missing<span class="nj-form-item__required-asterisk">*</span></label>
    </div>
    <p id="exampleFloatingFirstNameError-error" class="nj-form-item__subscript">
      <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">warning</span>
      This field is required.
    </p>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
<form style="display: flex; gap: 24px;">
  {% TextInput form1.text_empty floating=True size="sm" label="Sm" id="exampleSmFloatingInputsm" %}
  {% TextInput form1.text_empty floating=True label="Default" id="exampleFloatingInputmd" %}
  {% TextInput form1.text_empty floating=True size="lg" label="Lg" id="exampleLgFloatingInputlg" %}
  {% TextInput form1.text_empty floating=True size="xl" label="Xl" id="exampleXlFloatingInputxl" %}
</form>
"""
        expected = """
<form style="display: flex; gap: 24px;">
  <div class="nj-form-item nj-form-item--sm">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleSmFloatingInputsm" placeholder="">
      <label for="exampleSmFloatingInputsm" class="nj-form-item__label">Sm</label>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleFloatingInputmd" placeholder="">
      <label for="exampleFloatingInputmd" class="nj-form-item__label">Default</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--lg">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleLgFloatingInputlg" placeholder="">
      <label for="exampleLgFloatingInputlg" class="nj-form-item__label">Lg</label>
    </div>
  </div>
  <div class="nj-form-item nj-form-item--xl">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleXlFloatingInputxl" placeholder="">
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
<form style="display: flex; flex-direction: column; gap: 24px;">
  {% TextInput form1.text_help floating=True label="Example with information" id="exampleInputWithInfo" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text_help" type="text" class="nj-form-item__field" id="exampleInputWithInfo" placeholder=""
          aria-describedby="exampleInputWithInfo-hint"
          aria-controls="exampleInputWithInfo-hint">
      <label for="exampleInputWithInfo" class="nj-form-item__label">Example with information</label>
    </div>
    <p id="exampleInputWithInfo-hint" class="nj-form-item__subscript">
      Must be x character long
    </p>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example12(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 24px;">
  {% TextInputIcon form1.text_empty floating=True label="Firstname sm" id="exampleInputFirstNameSm" %}
    {% Slot 'icon' class="material-icons" %}
      info_outline
    {% endSlot %}
  {% endTextInputIcon %}
  {% TextInputIcon form1.text_empty floating=True label="Firstname sm" id="exampleInputFirstNameSm" %}
    {% Slot 'icon' class="material-icons" %}
      check
    {% endSlot %}
  {% endTextInputIcon %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputFirstNameSm" placeholder="">
      <label for="exampleInputFirstNameSm" class="nj-form-item__label">Firstname sm</label>
      <span aria-hidden="true" class="nj-form-item__icon material-icons">info_outline</span>
    </div>
  </div>
  <div class="nj-form-item">
    <div class="nj-form-item__field-wrapper">
      <input name="text_empty" type="text" class="nj-form-item__field" id="exampleInputFirstNameSm" placeholder="">
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
<form>
  {% NumberInput form1.number id="input-number-default" label="Amount" max="100" min="-100" %}
</form>
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
        name="number"
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
<form style="display: flex; flex-direction: column; gap: 24px;">
  {% PasswordInput form1.text_help floating=True required=True id="examplePassword" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item nj-form-item--password">
    <div class="nj-form-item__field-wrapper">
      <input name="text_help" type="password" class="nj-form-item__field" id="examplePassword" placeholder="" required
          aria-describedby="examplePassword-hint"
          aria-controls="examplePassword-hint">
      <label for="examplePassword" class="nj-form-item__label">
        Text help
        <span class="nj-form-item__required-asterisk">*</span>
      </label>
      <button type="button" aria-pressed="false"
              class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
        <span class="nj-sr-only" data-password-button-label-show="Show password"
              data-password-button-label-hide="Hide password"></span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">visibility</span>
      </button>
      <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite" aria-atomic="true"
         data-password-notice-is-visible="Password is visible"
         data-password-notice-is-hidden="Password is hidden"></p>
    </div>
    <p id="examplePassword-hint" class="nj-form-item__subscript">
      Must be x character long
    </p>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example15(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 24px;">
  {% Textarea form1.text_empty floating=True label="Comment" id="exampleTextArea" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 24px;">
  <div class="nj-form-item nj-form-item--textarea">
    <div class="nj-form-item__field-wrapper">
      <textarea name="text_empty" cols="40" rows="10" class="nj-form-item__field" id="exampleTextArea" placeholder="">
</textarea>
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
{% Row astag="form" %}
  {% Col md=7 %}
    {% TextInput form1.text_empty floating=True id="exampleColumnSizing1" %}
  {% endCol %}
  {% Col col="fill" %}
    {% TextInput form1.text_empty floating=True id="exampleColumnSizing2" %}
  {% endCol %}
  {% Col col="fill" %}
    {% TextInput form1.text_empty floating=True id="exampleColumnSizing3" %}
  {% endCol %}
{% endRow %}
"""
        expected = """
<form class="row">
  <div class="col-md-7">
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleColumnSizing1" placeholder="">
        <label for="exampleColumnSizing1" class="nj-form-item__label">Text empty</label>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleColumnSizing2" placeholder="">
        <label for="exampleColumnSizing2" class="nj-form-item__label">Text empty</label>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="nj-form-item">
      <div class="nj-form-item__field-wrapper">
        <input name="text_empty" type="text" class="nj-form-item__field" id="exampleColumnSizing3" placeholder="">
        <label for="exampleColumnSizing3" class="nj-form-item__label">Text empty</label>
      </div>
    </div>
  </div>
</form>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example17(self):
        template = """
{% load fluid_design %}
<form style="display: flex; flex-direction: column; gap: 4px; padding: 20px; width: 350px; margin: 0 auto">
  <h2>With <code>min</code> and <code>max</code> attributes</h2>
  {% NumberInput form1.number label="Amount" id="input-number-default" min="-10" max="10" %}
  <h2>With <code>step</code> and <code>max</code> attributes</h2>
  {% NumberInput form1.number label="Amount" id="input-number-static" step="0.3" max="3" static=True %}
  <h2>With hint and error</h2>
  <div style="display: flex; flex-direction: column; gap: 16px;">
    {% NumberInput form1.number_help label="Amount" id="input-number-hint"%}
    {% NumberInput form1.number_invalid label="Amount" id="input-number-error"%}
  </div>
  <h2>With <code>disabled</code> and <code>readonly</code> attributes</h2>
  <div style="display: flex; flex-direction: column; gap: 16px;">
    {% NumberInput form1.number label="Amount" id="input-number-disabled" static=True disabled=True %}
    {% NumberInput form1.number label="Amount" id="input-number-readonly" readonly=True %}
  </div>
  <h2>With different sizes</h2>
  <div style="display: flex; flex-direction: column; gap: 16px;">
    {% NumberInput form1.number label="Amount" id="input-number-size-sm" size="sm" %}
    {% NumberInput form1.number label="Amount" id="input-number-size-lg" size="lg" %}
    {% NumberInput form1.number label="Amount" id="input-number-size-xl" size="xl" static=True %}
  </div>
  <h2>With custom live zone format</h2>
    {% NumberInput form1.number label="Adults" min="1" id="input-number-custom-live-zone" static=True format="{x} adults" %}
</form>
"""
        expected = """
<form style="display: flex; flex-direction: column; gap: 4px; padding: 20px; width: 350px; margin: 0 auto">
  <h2>With <code>min</code> and <code>max</code> attributes</h2>
  <div class="nj-form-item nj-form-item--input-number">
    <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-default">
      <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
        <span class="nj-sr-only">- Decrement</span>
      </button>

      <input
        name="number"
        type="number"
        inputmode="numeric"
        class="nj-form-item__field"
        id="input-number-default"
        value="0"
        min="-10"
        max="10"
      >
      <label for="input-number-default" class="nj-form-item__label">Amount</label>

      <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button">
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
        <span class="nj-sr-only">+ Increment</span>
      </button>

      <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
    </div>
  </div>

  <h2>With <code>step</code> and <code>max</code> attributes</h2>
  <div class="nj-form-item nj-form-item--input-number nj-form-item--static">
    <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-static">
      <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
        <span class="nj-sr-only">- Decrement</span>
      </button>

      <input
        name="number"
        type="number"
        inputmode="numeric"
        class="nj-form-item__field"
        id="input-number-static"
        value="0"
        step="0.3"
        max="3"
      >
      <label for="input-number-static" class="nj-form-item__label">Amount</label>

      <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button">
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
        <span class="nj-sr-only">+ Increment</span>
      </button>

      <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
    </div>
  </div>

  <h2>With hint and error</h2>
  <div style="display: flex; flex-direction: column; gap: 16px;">
    <div class="nj-form-item nj-form-item--input-number">
      <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-hint input-number-hint-hint">
        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
          <span class="nj-sr-only">- Decrement</span>
        </button>

        <input
          name="number_help"
          type="number"
          inputmode="numeric"
          class="nj-form-item__field"
          id="input-number-hint"
          aria-controls="input-number-hint-hint"
          aria-describedby="input-number-hint-hint"
          value="1"
        >
        <label for="input-number-hint" class="nj-form-item__label">Amount</label>

        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
          <span class="nj-sr-only">+ Increment</span>
        </button>

        <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
      </div>

      <p id="input-number-hint-hint" class="nj-form-item__subscript">
        Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
      </p>
    </div>

    <div class="nj-form-item nj-form-item--error nj-form-item--input-number">
      <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-error input-number-error-error">
        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
          <span class="nj-sr-only">- Decrement</span>
        </button>

        <input
          name="number_invalid"
          value="a"
          type="number"
          inputmode="numeric"
          class="nj-form-item__field"
          id="input-number-error"
          aria-describedby="input-number-error-error"
          aria-controls="input-number-error-error"
          aria-invalid="true"
        >
        <label for="input-number-error" class="nj-form-item__label">Amount</label>

        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
          <span class="nj-sr-only">+ Increment</span>
        </button>

        <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
      </div>

      <p id="input-number-error-error" class="nj-form-item__subscript">
        <span aria-hidden="true" class="nj-form-item__subscript-icon material-icons">warning</span>
        Enter a whole number.
      </p>
    </div>
  </div>

  <h2>With <code>disabled</code> and <code>readonly</code> attributes</h2>
  <div style="display: flex; flex-direction: column; gap: 16px;">
    <div class="nj-form-item nj-form-item--input-number nj-form-item--static nj-form-item--disabled">
      <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-disabled">
        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button" disabled>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
          <span class="nj-sr-only">- Decrement</span>
        </button>

        <input
          name="number"
          type="number"
          inputmode="numeric"
          class="nj-form-item__field"
          id="input-number-disabled"
          value="0"
          disabled
        >
        <label for="input-number-disabled" class="nj-form-item__label">Amount</label>

        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button" disabled>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
          <span class="nj-sr-only">+ Increment</span>
        </button>

        <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
      </div>
    </div>

    <div class="nj-form-item nj-form-item--input-number">
      <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-readonly">
        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button" disabled>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
          <span class="nj-sr-only">- Decrement</span>
        </button>

        <input
          name="number"
          type="number"
          inputmode="numeric"
          class="nj-form-item__field"
          id="input-number-readonly"
          value="0"
          readonly
        >
        <label for="input-number-readonly" class="nj-form-item__label">Amount</label>

        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button" disabled>
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
          <span class="nj-sr-only">+ Increment</span>
        </button>

        <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
      </div>
    </div>
  </div>

  <h2>With different sizes</h2>
  <div style="display: flex; flex-direction: column; gap: 16px;">
    <div class="nj-form-item nj-form-item--input-number nj-form-item--sm">
      <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-size-sm">
        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
          <span class="nj-sr-only">- Decrement</span>
        </button>

        <input
          name="number"
          type="number"
          inputmode="numeric"
          class="nj-form-item__field"
          id="input-number-size-sm"
          value="0"
        >
        <label for="input-number-size-sm" class="nj-form-item__label">Amount</label>

        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
          <span class="nj-sr-only">+ Increment</span>
        </button>

        <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
      </div>
    </div>

    <div class="nj-form-item nj-form-item--input-number nj-form-item--lg">
      <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-size-lg">
        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
          <span class="nj-sr-only">- Decrement</span>
        </button>

        <input
          name="number"
          type="number"
          inputmode="numeric"
          class="nj-form-item__field"
          id="input-number-size-lg"
          value="0"
        >
        <label for="input-number-size-lg" class="nj-form-item__label">Amount</label>

        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
          <span class="nj-sr-only">+ Increment</span>
        </button>

        <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
      </div>
    </div>

    <div class="nj-form-item nj-form-item--input-number nj-form-item--static nj-form-item--xl">
      <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-size-xl">
        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
          <span class="nj-sr-only">- Decrement</span>
        </button>

        <input
          name="number"
          type="number"
          inputmode="numeric"
          class="nj-form-item__field"
          id="input-number-size-xl"
          value="0"
        >
        <label for="input-number-size-xl" class="nj-form-item__label">Amount</label>

        <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__increment-button" type="button">
          <span aria-hidden="true" class="nj-icon-btn__icon material-icons">add</span>
          <span class="nj-sr-only">+ Increment</span>
        </button>

        <div aria-live="polite" aria-atomic="true" class="nj-sr-only"></div>
      </div>
    </div>
  </div>

  <h2>With custom live zone format</h2>
  <div class="nj-form-item nj-form-item--input-number nj-form-item--static" data-live-zone-format="{x} adults">
    <div class="nj-form-item__field-wrapper" role="group" aria-labelledby="input-number-custom-live-zone">
      <button class="nj-icon-btn nj-icon-btn--secondary nj-form-item__decrement-button" type="button">
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">remove</span>
        <span class="nj-sr-only">- Decrement</span>
      </button>

      <input
        name="number"
        type="number"
        inputmode="numeric"
        class="nj-form-item__field"
        id="input-number-custom-live-zone"
        value="0"
        min="1"
      >
      <label for="input-number-custom-live-zone" class="nj-form-item__label">Adults</label>

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
