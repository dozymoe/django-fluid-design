"""
Button
======

See: https://www.engie.design/fluid-design-system/components/button/

Buttons allow users to interact with the product and trigger actions. They can
be of different sizes, colors and status.
In terms of accessibility, be mindful of people using assistive technologies:
don’t use links instead of buttons to trigger actions.
"""

from .base import Node

class Button(Node):
    """Button component
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."
    NODE_PROPS = ('disabled', 'variant', 'style', 'size')
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."
    POSSIBLE_VARIANTS = ('subtle', 'minimal')
    "Possible values for variant argument."
    POSSIBLE_STYLES = ('secondary', 'destructive', 'inverse')
    "Possible values for style argument."
    POSSIBLE_SIZES = ('xs', 'sm', 'lg')
    "Possible values for size argument."

    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        if self.eval(self.kwargs.get('disabled'), context):
            values['props'].append(('disabled', ''))

        variant = self.eval(self.kwargs.get('variant'), context)
        if variant in self.POSSIBLE_VARIANTS:
            values['class'].append(f'nj-btn--{variant}')

        style = self.eval(self.kwargs.get('style'), context)
        if style in self.POSSIBLE_STYLES:
            values['class'].append(f'nj-btn--{style}')

        size = self.eval(self.kwargs.get('size'), context)
        if size in self.POSSIBLE_SIZES:
            values['class'].append(f'nj-btn--{size}')


    def render_default(self, values, context):
        """Html output of the component
        """
        template = """
<{astag} class="nj-btn {class}" {props}>
  {slot_icon}
  {child}
</{astag}>
"""
        return self.format(template, values, context)


components = {
    'Button': Button,
}
