# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class PaginationTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Pagination %}
"""
        expected = """
<nav class="" role="navigation">
  <ul class="nj-pagination">
   <li class="nj-pagination__item">
    <button class="nj-icon-btn nj-icon-btn--lg" type="button">
     <span class="nj-sr-only">
      Previous page
     </span>
     <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
      chevron_left
     </span>
    </button>
   </li>
   <li class="nj-pagination__item">
    <button class="nj-icon-btn nj-icon-btn--lg" type="button">
     <span class="nj-sr-only">
      Next page
     </span>
     <span aria-hidden="true" class="nj-icon-btn__icon material-icons">
      chevron_right
     </span>
    </button>
   </li>
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Pagination current=3 total=20 links=6 label="Page navigation example" %}
"""
        expected = """
<nav aria-label="Page navigation example" role="navigation" class="">
  <ul class="nj-pagination">
    <li class="nj-pagination__item">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg">
        <span class="nj-sr-only">Previous page</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">chevron_left</span>
      </button>
    </li>
    <li class="nj-pagination__item"><a class="nj-pagination__link" href="#" aria-label="Page 1">1</a></li>
    <li class="nj-pagination__item"><a class="nj-pagination__link" href="#" aria-label="Page 2">2</a></li>
    <li class="nj-pagination__item nj-pagination__item--active"><a class="nj-pagination__link" href="#" aria-current="true" aria-label="Page 3">3</a></li>
    <li class="nj-pagination__item"><a class="nj-pagination__link" href="#" aria-label="Page 4">4</a></li>
    <li class="nj-pagination__item">
      <span class="nj-pagination__more material-icons" aria-hidden="true">more_horiz</span>
      <span class="nj-sr-only">...</span>
    </li>
    <li class="nj-pagination__item"><a class="nj-pagination__link" href="#" aria-label="Page 20">20</a></li>
    <li class="nj-pagination__item">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg">
        <span class="nj-sr-only">Next page</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">chevron_right</span>
      </button>
    </li>
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% Pagination current=3 total=20 links=6 label="Page navigation example" %}
"""
        expected = """
<nav aria-label="Page navigation example" role="navigation" class="">
  <ul class="nj-pagination">
    <li class="nj-pagination__item">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg">
        <span class="nj-sr-only">Previous page</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">chevron_left</span>
      </button>
    </li>
    <li class="nj-pagination__item"><a class="nj-pagination__link" href="#" aria-label="Page 1">1</a></li>
    <li class="nj-pagination__item"><a class="nj-pagination__link" href="#" aria-label="Page 2">2</a></li>
    <li class="nj-pagination__item nj-pagination__item--active"><a class="nj-pagination__link" href="#" aria-current="true" aria-label="Page 3">3</a></li>
    <li class="nj-pagination__item"><a class="nj-pagination__link" href="#" aria-label="Page 4">4</a></li>
    <li class="nj-pagination__item">
      <span aria-hidden="true" class="nj-pagination__more material-icons">more_horiz</span>
      <span class="nj-sr-only">...</span>
    </li>
    <li class="nj-pagination__item"><a class="nj-pagination__link" href="#" aria-label="Page 20">20</a></li>
    <li class="nj-pagination__item">
      <button type="button" class="nj-icon-btn nj-icon-btn--lg">
        <span class="nj-sr-only">Next page</span>
        <span aria-hidden="true" class="nj-icon-btn__icon material-icons">chevron_right</span>
      </button>
    </li>
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
