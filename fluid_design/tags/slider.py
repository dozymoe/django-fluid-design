"""
Slider
======

See: https://www.engie.design/fluid-design-system/components/slider/

A slider allows the user to slide a knob along a straight track to control or to
change a variable. Sliders can have icons on both ends of the bar, for example
when you want to change the brightness of your screen.
"""
from .base import FormNode
from .base_widgets import CustomRangeInput

class Slider(FormNode):
    """Slider component
    """
    NODE_PROPS = ('tooltip',)
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'wrapper')
    "Prepare xxx_class and xxx_props values."
    widget_class = CustomRangeInput

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('disabled'), context):
            values['wrapper_class'].append('nj-slider--disabled')
        if self.eval(self.kwargs.get('tooltip'), context):
            values['wrapper_props'].append(('data-tooltip', 'true'))


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<div class="nj-slider {wrapper_class}" {wrapper_props}>
  {tmpl_label}
  {tmpl_element}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''
        if self.bound_field.field.required or\
                self.eval(self.kwargs.get('required'), context):
            tmpl = """
<label for="{id}" class="{label_class}" {label_props}>
  {label}{label_suffix}
  <span class="nj-form-item__required-asterisk">*</span>
</label>
"""
        else:
            tmpl = """
<label for="{id}" class="{label_class}" {label_props}>
  {label}{label_suffix}
</label>
"""
        return self.format(tmpl, values)


components = {
    'Slider': Slider,
}
