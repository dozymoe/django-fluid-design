"""
Form
====

See: https://www.engie.design/fluid-design-system/components/form/

Forms are used to send and collect data.
"""
from django.forms.widgets import (PasswordInput as PasswordWidget,
        Textarea as TextareaWidget)
from django.utils.translation import gettext as _
#-
from .base import FormNode

class TextInput(FormNode):
    """Form text item component
    """
    NODE_PROPS = ('floating', 'size', 'disabled')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'help', 'wrapper')
    "Prepare xxx_class and xxx_props values."
    POSSIBLE_SIZES = ('sm', 'lg', 'xl')
    "Possible values for size argument."

    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if not self.eval(self.kwargs.get('floating'), context):
            values['wrapper_class'].append('nj-form-item--static')

        size = self.eval(self.kwargs.get('size'), context)
        if size in self.POSSIBLE_SIZES:
            values['wrapper_class'].append(f'nj-form-item--{size}')

        if self.eval(self.kwargs.get('disabled'), context):
            values['wrapper_class'].append('nj-form-item--disabled')


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].append('nj-form-item__field')

        if self.eval(self.kwargs.get('floating'), context):
            props['placeholder'] = ''


    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--error {wrapper_class}" {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item {wrapper_class}" {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


class PasswordInput(TextInput):
    """Form password item component
    """
    widget_class = PasswordWidget

    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        super().prepare(values, context)

        values['txt_hide'] = _("Hide password")
        values['txt_show'] = _("Show password")
        values['txt_hidden'] = _("Password is hidden")
        values['txt_visible'] = _("Password is visible")


    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--error nj-form-item--password {wrapper_class}"
    {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    <button type="button" aria-pressed="false"
        class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
      <span class="nj-sr-only" data-password-button-label-show="{txt_show}"
          data-password-button-label-hide="{txt_hide}"></span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        visibility
      </span>
    </button>
    <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite"
        aria-atomic="true" data-password-notice-is-visible="{txt_visible}"
        data-password-notice-is-hidden="{txt_hidden}"></p>
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item nj-form-item--password {wrapper_class}"
    {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    <button type="button" aria-pressed="false"
        class="nj-form-item__password-button nj-icon-btn nj-icon-btn--lg nj-icon-btn--secondary">
      <span class="nj-sr-only" data-password-button-label-show="{txt_show}"
          data-password-button-label-hide="{txt_hide}"></span>
      <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
        visibility
      </span>
    </button>
    <p class="nj-sr-only nj-form-item__password-notice" aria-live="polite"
        aria-atomic="true" data-password-notice-is-visible="{txt_visible}"
        data-password-notice-is-hidden="{txt_hidden}"></p>
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


class TextInputIcon(TextInput):
    """Form text item component with icon
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."

    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--error {wrapper_class}" {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {slot_icon}
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item {wrapper_class}" {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {slot_icon}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<span class="nj-form-item__icon {class}" aria-hidden="true" {props}>
  {child}
</span>
"""
        return tmpl.format(**values)


class Textarea(TextInput):
    """Form textarea item component
    """
    widget_class = TextareaWidget

    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--textarea nj-form-item--error {wrapper_class}"
    {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {slot_icon}
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item nj-form-item--textarea {wrapper_class}"
    {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {slot_icon}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


class NumberInput(TextInput):
    """Form number item component
    """
    def render_default(self, values, context):
        """Html output of the component
        """
        if self.bound_field.errors:
            template = """
<div class="nj-form-item nj-form-item--textarea nj-form-item--error {wrapper_class}"
    {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {slot_icon}
  </div>
  {tmpl_help}
  {tmpl_errors}
</div>
"""
        else:
            template = """
<div class="nj-form-item nj-form-item--textarea {wrapper_class}"
    {wrapper_props}>
  <div class="nj-form-item__field-wrapper">
    {tmpl_element}
    {tmpl_label}
    {slot_icon}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


components = {
    'NumberInput': NumberInput,
    'PasswordInput': PasswordInput,
    'TextInput': TextInput,
    'TextInputIcon': TextInputIcon,
    'Textarea': Textarea,
}
