# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class NavbarTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Navbar id="example" %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow">
 <button class="nj-navbar__toggler" data-target="#example" data-toggle="collapse" type="button">
  <span class="nj-navbar__toggler-icon material-icons">menu</span>
 </button>
 <div class="nj-navbar--collapse nj-collapse" id="example">
  <ul class="nj-navbar__nav">
  </ul>
 </div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Navbar id="navbarExample" href="#" logo_src="static/media/logo-engie.0ee922c2.svg#logo-engie" expand="xl" %}
  {% N_Menu href="#" active=True %}Nav item active{% endN_Menu %}
  {% N_Menu href="#" disabled=True %}Nav item disabled{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" icon=True %}
    {% Icon label="network_check" class="md--primary" %}
  {% endN_Menu %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow nj-navbar--expand-xl">
  <a class="nj-navbar__brand" href="#"><svg class="nj-navbar__logo" aria-label="home"><use href="static/media/logo-engie.0ee922c2.svg#logo-engie" /></svg></a>
  <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample">
    <span class="nj-navbar__toggler-icon material-icons">menu</span>
  </button>
  <div class="nj-navbar--collapse nj-collapse" id="navbarExample">
    <ul class="nj-navbar__nav">
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Nav item active</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link disabled" href="#">Nav item disabled</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link nj-navbar__nav-link--icon" href="#"><span class="material-icons nj-icon-material md--primary" aria-hidden="true">network_check</span></a></li>
    </ul>
  </div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% Navbar id="navbarExample" expand=True href="#" logo_src="static/media/logo-engie.0ee922c2.svg#logo-engie" %}
  {% N_MenuSearch target="collapse-search-bar-example" color="primary" %}
  {% Slot 'after' %}
    {% N_Search id="collapse-search-bar-example" color="primary" %}
  {% endSlot %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow nj-navbar--expand">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="static/media/logo-engie.0ee922c2.svg#logo-engie" /></svg></a>
  <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample">
    <span class="nj-navbar__toggler-icon material-icons">menu</span>
  </button>
  <div class="nj-navbar--collapse nj-collapse" id="navbarExample">
    <ul class="nj-navbar__nav">
      <li class="nj-navbar__nav-item">
        <a class="nj-navbar__nav-link nj-navbar__nav-link--icon" data-toggle="collapse" href="#collapse-search-bar-example" aria-expanded="false" aria-controls="collapse-search-bar-example">
          <span class="material-icons nj-icon-material nj-icon-material--primary" aria-hidden="true">search</span>
        </a>
      </li>
    </ul>
    <form class="nj-navbar__search nj-collapse" id="collapse-search-bar-example">
      <input class="nj-form-control nj-navbar__search-input" type="text" id="collapse-search-bar-example-input" placeholder="Enter your query...">
      <button type="submit" class="nj-btn nj-navbar__search-button">Search</button>
      <a href="#" class="nj-navbar__nav-link nj-navbar__nav-link--icon nj-collapse-inline__close" aria-label="Close"
        data-dismiss="#collapse-search-bar-example">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--primary">close</span>
      </a>
    </form>
  </div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="background:url('https://assets.design.digital.engie.com/image/bg-home.jpg');" class="pb-6">
  {% Navbar id="navbarExample03" href="#" logo_src="static/media/logo-engie.0ee922c2.svg#logo-engie" expand="xl" transparent=True %}
    {% N_Menu href="#" active=True %}Nav item{% endN_Menu %}
    {% N_Menu href="#" %}Nav item{% endN_Menu %}
    {% N_Menu href="#" %}Nav item{% endN_Menu %}
    {% N_Menu href="#" icon=True %}
      {% Icon label="network_check" color="white" %}
    {% endN_Menu %}
  {% endNavbar %}
</div>
"""
        expected = """
<div style="background:url('https://assets.design.digital.engie.com/image/bg-home.jpg');" class="pb-6">
  <nav class="nj-navbar nj-navbar--transparent nj-navbar--expand-xl">
    <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="static/media/logo-engie.0ee922c2.svg#logo-engie" /></svg></a>
    <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample03">
      <span class="nj-navbar__toggler-icon material-icons">menu</span>
    </button>
    <div class="nj-navbar--collapse nj-collapse" id="navbarExample03">
      <ul class="nj-navbar__nav">
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link nj-navbar__nav-link--icon" href="#"><span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--white">network_check</span></a></li>
      </ul>
    </div>
  </nav>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% Navbar id="navbarExampleSmall" href="#" expand="xl" size="sm" logo_src="static/media/logo-engie.0ee922c2.svg#logo-engie" %}
    {% N_Menu href="#" active=True %}Nav item{% endN_Menu %}
    {% N_Menu href="#" %}Nav item{% endN_Menu %}
    {% N_Menu href="#" %}Nav item{% endN_Menu %}
    {% N_Menu href="#" %}Nav item{% endN_Menu %}
    {% N_Menu href="#" icon=True %}
      {% Icon label="network_check" color="primary" %}
    {% endN_Menu %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--sm nj-navbar--shadow nj-navbar--expand-xl">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="static/media/logo-engie.0ee922c2.svg#logo-engie" /></svg></a>
  <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExampleSmall">
    <span class="nj-navbar__toggler-icon material-icons">menu</span>
  </button>
  <div class="nj-navbar--collapse nj-collapse" id="navbarExampleSmall">
    <ul class="nj-navbar__nav">
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link nj-navbar__nav-link--icon" href="#"><span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--primary">network_check</span></a></li>
    </ul>
  </div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Navbar id="navbarExample04" href="#" logo_src="static/media/logo-engie.0ee922c2.svg#logo-engie" expand="xl" %}
  {% N_Menu href="#" active=True %}Nav link{% endN_Menu %}
  {% N_Menu href="#" %}Nav link{% endN_Menu %}
  {% N_Menu href="#" %}Nav link{% endN_Menu %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow nj-navbar--expand-xl">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="static/media/logo-engie.0ee922c2.svg#logo-engie" /></svg></a>
  <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample04">
    <span class="nj-navbar__toggler-icon material-icons">menu</span>
  </button>
  <div class="nj-navbar--collapse nj-collapse" id="navbarExample04">
    <ul class="nj-navbar__nav">
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Nav link</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav link</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav link</a></li>
    </ul>
  </div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Navbar mode="simple" expand=True href="#" logo_src="static/media/logo-engie.0ee922c2.svg#logo-engie" %}
  {% N_Menu href="#" active=True %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow nj-navbar--expand">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="static/media/logo-engie.0ee922c2.svg#logo-engie" /></svg></a>
  <ul class="nj-navbar__nav">
    <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Nav item</a></li>
    <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
    <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
    <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Navbar id="navbarExample" href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" expand="xl" %}
  {% N_Menu href="#" active=True %}Active nav item{% endN_Menu %}
  {% N_Menu href="#" disabled=True %}Disabled nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" icon=True %}
    {% Icon label="network_check" color="brand" %}
    <span class="nj-sr-only">Nav item</span>
  {% endN_Menu %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow nj-navbar--expand-xl">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
  <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample">
    <span class="nj-navbar__toggler-icon material-icons">menu</span>
  </button>
  <div class="nj-navbar--collapse nj-collapse" id="navbarExample">
    <ul class="nj-navbar__nav">
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Active nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link disabled" href="#">Disabled nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
      <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link nj-navbar__nav-link--icon" href="#"><span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--brand">network_check</span><span class="nj-sr-only">Nav item</span></a></li>
    </ul>
  </div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Navbar mode="simple" href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
  <ul class="nj-navbar__nav">
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
{% Navbar id="navbarExample" href="#" expand=True logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
  {% N_MenuSearch target="collapse-search-bar-example" color="blue-corporate" %}
  {% Slot 'after' %}
    {% N_Search id="collapse-search-bar-example" color="blue-corporate" %}
  {% endSlot %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow nj-navbar--expand">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
  <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample">
    <span class="nj-navbar__toggler-icon material-icons">menu</span>
  </button>
  <div class="nj-navbar--collapse nj-collapse" id="navbarExample">
    <ul class="nj-navbar__nav">
      <li class="nj-navbar__nav-item">
        <a class="nj-navbar__nav-link nj-navbar__nav-link--icon" data-toggle="collapse" href="#collapse-search-bar-example" aria-expanded="false" aria-controls="collapse-search-bar-example">
          <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--blue-corporate">search</span>
        </a>
      </li>
    </ul>
    <form class="nj-navbar__search nj-collapse" id="collapse-search-bar-example">
      <input class="nj-form-control nj-navbar__search-input" type="text" id="collapse-search-bar-example-input" placeholder="Enter your query...">
      <button type="submit" class="nj-btn nj-navbar__search-button">Search</button>
      <a href="#" class="nj-navbar__nav-link nj-navbar__nav-link--icon nj-collapse-inline__close" aria-label="Close"
        data-dismiss="#collapse-search-bar-example">
        <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--blue-corporate">close</span>
      </a>
    </form>
  </div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
<div style="background:url('/assets/img/bg-home-dark.jpg');" class="pb-6">
  {% Navbar id="navbarExample03" transparent=True class="mb-3" expand="xl" href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
    {% N_Menu href="#" active=True %}Active nav item{% endN_Menu %}
    {% N_Menu href="#" %}Nav item{% endN_Menu %}
    {% N_Menu href="#" %}Nav item{% endN_Menu %}
    {% N_Menu href="#" icon=True %}
      {% Icon label="network_check" color="white" %}
    {% endN_Menu %}
  {% endNavbar %}
</div>
"""
        expected = """
<div style="background:url('/assets/img/bg-home-dark.jpg');" class="pb-6">
    <nav class="nj-navbar mb-3 nj-navbar--transparent nj-navbar--expand-xl">
      <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
      <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample03">
        <span class="nj-navbar__toggler-icon material-icons">menu</span>
      </button>
      <div class="nj-navbar--collapse nj-collapse" id="navbarExample03">
        <ul class="nj-navbar__nav">
          <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Active nav item</a></li>
          <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
          <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
          <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link nj-navbar__nav-link--icon" href="#"><span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--white">network_check</span></a></li>
        </ul>
      </div>
    </nav>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example11(self):
        template = """
{% load fluid_design %}
{% Navbar id="navbarExampleSmall" size="sm" expand="xl" href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
  {% N_Menu href="#" active=True %}Active nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" icon=True %}
    {% Icon label="network_check" color="blue-corporate" %}
  {% endN_Menu %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--sm nj-navbar--shadow nj-navbar--expand-xl">
    <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
    <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExampleSmall">
      <span class="nj-navbar__toggler-icon material-icons">menu</span>
    </button>
    <div class="nj-navbar--collapse nj-collapse" id="navbarExampleSmall">
      <ul class="nj-navbar__nav">
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Active nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link nj-navbar__nav-link--icon" href="#"><span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--blue-corporate">network_check</span></a></li>
      </ul>
    </div>
  </nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example12(self):
        template = """
{% load fluid_design %}
{% Navbar id="navbarExample04" class="mb-3" expand="xl" href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
  {% N_Menu href="#" active=True %}Active nav link{% endN_Menu %}
  {% N_Menu href="#" %}Nav link{% endN_Menu %}
  {% N_Menu href="#" %}Nav link{% endN_Menu %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar mb-3 nj-navbar--shadow nj-navbar--expand-xl">
      <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
      <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample04">
        <span class="nj-navbar__toggler-icon material-icons">menu</span>
      </button>
      <div class="nj-navbar--collapse nj-collapse" id="navbarExample04">
        <ul class="nj-navbar__nav">
          <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Active nav link</a></li>
          <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav link</a></li>
          <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav link</a></li>
        </ul>
      </div>
  </nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example13(self):
        template = """
{% load fluid_design %}
{% Navbar mode="simple" class="fixed-top" href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar fixed-top nj-navbar--shadow">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
  <ul class="nj-navbar__nav">
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example14(self):
        template = """
{% load fluid_design %}
{% Navbar mode="simple" class="fixed-bottom" href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar fixed-bottom nj-navbar--shadow">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
  <ul class="nj-navbar__nav">
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example15(self):
        template = """
{% load fluid_design %}
{% Navbar mode="simple" class="sticky-top" href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar sticky-top nj-navbar--shadow">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
  <ul class="nj-navbar__nav">
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example16(self):
        template = """
{% load fluid_design %}
{% Navbar mode="simple" expand=True href="#" logo_src="/assets/brand/logo-engie.svg#logo-engie" %}
  {% N_Menu href="#" active=True %}Active nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
  {% N_Menu href="#" %}Nav item{% endN_Menu %}
{% endNavbar %}
"""
        expected = """
<nav class="nj-navbar nj-navbar--shadow nj-navbar--expand">
  <a class="nj-navbar__brand" href="#"><svg aria-label="home" class="nj-navbar__logo"><use href="/assets/brand/logo-engie.svg#logo-engie" /></svg></a>
  <ul class="nj-navbar__nav">
    <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Active nav item</a></li>
    <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
    <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
    <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
