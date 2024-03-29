"""
Pagination
==========

See: https://www.engie.design/fluid-design-system/components/pagination/

Pagination helps users to navigate through multiple pages.
"""
from django.utils.translation import gettext as _
#-
from .base import Node

class Pagination(Node):
    """Pagination component
    """
    NODE_PROPS = ('links', 'current', 'total')
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates
        """
        values['txt_previous'] = _("Previous page")
        values['txt_next'] = _("Next page")

        if values['label']:
            values['props'].append(('aria-label', values['label']))

        values['current'] = self.eval(self.kwargs.get('current', 1), context)
        values['total'] = self.eval(self.kwargs.get('total', 0), context)

        links_count = max(self.eval(self.kwargs.get('links', 7), context), 1)
        values['show_first_last'] = links_count >= 6

        first_num = 1
        last_num = values['total']
        distance = links_count - 1
        if values['show_first_last']:
            first_num += 1
            last_num -= 1
            distance -= 2

        left_distance = right_distance = int(distance / 2)
        if distance % 2:
            left_distance += 1
        start_num = max(first_num, values['current'] - left_distance)
        right_distance += left_distance - (values['current'] - start_num)
        end_num = min(values['current'] + right_distance, last_num)
        values['numbers'] = list(range(start_num, end_num + 1))
        if values['numbers']:
            if start_num != first_num:
                values['numbers'][0] = None
            if end_num != last_num:
                values['numbers'][-1] = None


    def render_default(self, values, context):
        """Html output of the component
        """
        if values['show_first_last']:
            template = """
<nav role="navigation" class="{class}" {props}>
  <ul class="nj-pagination">
    {tmpl_previous}
    {tmpl_first}
    {tmpl_numbers}
    {tmpl_last}
    {tmpl_next}
  </ul>
</nav>
"""
        else:
            template = """
<nav role="navigation" class="{class}" {props}>
  <ul class="nj-pagination">
    {tmpl_previous}
    {tmpl_numbers}
    {tmpl_next}
  </ul>
</nav>
"""
        return self.format(template, values, context)


    def render_tmpl_previous(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<li class="nj-pagination__item">
  <button type="button" class="nj-icon-btn nj-icon-btn--lg">
    <span class="nj-sr-only">{txt_previous}</span>
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
      chevron_left
    </span>
  </button>
</li>
"""
        return self.format(template, values)


    def render_tmpl_next(self, values, context):
        """Dynamically render a part of the component's template
        """
        template = """
<li class="nj-pagination__item">
  <button type="button" class="nj-icon-btn nj-icon-btn--lg">
    <span class="nj-sr-only">{txt_next}</span>
    <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
      chevron_right
    </span>
  </button>
</li>
"""
        return self.format(template, values)


    def render_tmpl_first(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['total'] < 1:
            return ''
        template = """
<li class="nj-pagination__item">
  <a class="nj-pagination__link" href="#" aria-label="Page 1">1</a>
</li>
"""
        return self.format(template, values, context)


    def render_tmpl_last(self, values, context):
        """Dynamically render a part of the component's template
        """
        if values['total'] < 2:
            return ''
        template = """
<li class="nj-pagination__item">
  <a class="nj-pagination__link" href="#" aria-label="Page {total}">{total}</a>
</li>
"""
        return self.format(template, values)


    def render_tmpl_numbers(self, values, context):
        """Dynamically render a part of the component's template
        """
        tpl_item = """
<li class="nj-pagination__item">
  <a class="nj-pagination__link" href="#" aria-label="Page {num}">{num}</a>
</li>
"""
        tpl_item_active = """
<li class="nj-pagination__item nj-pagination__item--active">
  <a class="nj-pagination__link" href="#" aria-current="true"
      aria-label="Page {num}">
    {num}
  </a>
</li>
"""
        tpl_item_more = """
<li class="nj-pagination__item">
  <span class="nj-pagination__more material-icons" aria-hidden="true">
    more_horiz
  </span>
  <span class="nj-sr-only">...</span>
</li>
"""
        items = []
        for num in values['numbers']:
            if num is None:
                items.append(tpl_item_more)
            elif num == values['current']:
                items.append(tpl_item_active.format(num=num))
            else:
                items.append(tpl_item.format(num=num))
        return '\n'.join(items)


components = {
    'Pagination': Pagination,
}
