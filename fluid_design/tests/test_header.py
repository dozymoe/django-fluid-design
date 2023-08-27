# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class HeaderTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Header %}{% endHeader %}
"""
        expected = """
<header class="nj-header">
  <div class="nj-header__group">
   <nav class="container">
    <div aria-expanded="false" aria-label="menu" class="nj-header__nav-burger">
     <button>
      <div>
      </div>
     </button>
    </div>
    <ul class="nj-header__nav nj-header__nav--panel">
    </ul>
   </nav>
  </div>
</header>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="height: 60vh; transform: translateZ(0); overflow: auto">
  {% Header fixed=True scroll="sm" expand="lg" logo_src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" logo_alt="ENGIE" logo_width=133 logosm_width=31 %}
    {% H_Menu active=True href="#" %}Accueil{% endH_Menu %}
    {% H_MenuTag href="#" color="green" %}News{% endH_MenuTag %}
    {% H_Menu href="#" %}Act with ENGIE{% endH_Menu %}
    {% H_Menu href="#" %}Group{% endH_Menu %}
    {% H_Menu href="#" %}
      Activities

      {% Slot 'submenu' %}
        {% Grid %}
          {% Row %}
            {% Col col="fill" %}
              {% H_Submenu label="Renouvelables" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biogaz" %}
                  Biogaz
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biomasse" %}
                  Biomasse
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydrogene-vert" %}
                  Hydrogène vert
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydroelectricite" %}
                  Hydroélectricité
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Solutions clients" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Thermique" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Centrales thermiques
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Nucléaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Gaz
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
          {% endRow %}
        {% endGrid %}
      {% endSlot %}
    {% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}

    {% Slot 'search' %}
      {% H_Search id="search-header" %}
    {% endSlot %}

    {% Slot 'head_first' %}
      <div>
        {% H_HeadLink href="#" %}EN{% endH_HeadLink %} /
        {% H_HeadLink href="#" active=True %}FR{% endH_HeadLink %}
      </div>
    {% endSlot %}
    {% Slot 'head_last' %}
      {% H_HeadLink href="" %}Espace client{% endH_HeadLink %}
    {% endSlot %}
  {% endHeader %}
</div>
"""
        expected = """
<div style="height: 60vh; transform: translateZ(0); overflow: auto"><header class="nj-header nj-header--fixed nj-header--scroll-sm nj-header--expand-lg">
  <div class="nj-header__group">
    <div class="nj-header__head">
      <div>
        <a href="#" class="nj-header__head-link">EN</a> /
        <a href="#" class="nj-header__head-link nj-header__head-link--active">FR</a>
      </div>
      <a href="#" class="nj-header__logo">
       <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="133" height="48">
      </a>
      <a href="" class="nj-header__head-link">Espace client</a>
    </div>
    <hr class="m-0">
    <nav class="container">
     <div class="nj-header__nav-burger" aria-label="menu" aria-expanded="false"><button><div></div></button></div>
     <div class="nj-header__nav-logo--reduced">
       <a href="#">
        <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="31" height="32">
       </a>
     </div>
     <ul class="nj-header__nav nj-header__nav--panel">
        <li class="nj-header__nav-item active"><a class="nj-header__nav-link" href="#">Accueil</a></li>
        <li class="nj-header__nav-item"><a class="nj-tag nj-tag--green" href="#">News</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Act with ENGIE</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Group</a></li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Activities <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
          <div class="nj-header__menu nj-header__nav--panel">
            <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i> Activities</a>
            <div class="container">
              <div class="row">
                <div class="col">
                  <ul class="nj-header__sub-nav">
                    <li>
                      <a href="#" class="nj-header__menu-title" aria-label="open" aria-expanded="false">Renouvelables <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                      <ul class="nj-header__nav--panel">
                        <li><a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Renouvelables</a></li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biogaz">Biogaz</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biomasse">Biomasse</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydrogene-vert">Hydrogène vert</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydroelectricite">Hydroélectricité</a>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a href="#" class="nj-header__menu-title" aria-label="open" aria-expanded="false">Solutions clients <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                    <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Solutions clients</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                    </li>
                  </ul>
                    </li></ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a class="nj-header__menu-title" href="#" aria-label="open" aria-expanded="false">Thermique <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                   <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Thermique</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Centrales thermiques</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Nucléaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Gaz</a>
                    </li>
                  </ul>
                  </li></ul>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
      </ul>
       <a class="nj-header__search-icon" data-toggle="collapse" data-target="#collapse-search-bar-header" aria-expanded="false" aria-controls="collapse-search-bar-header">
          <i class="material-icons nj-icon-material nj-icon-material--brand">search</i>
       </a>
       <form class="nj-header__search nj-collapse" id="search-header">
           <input class="nj-form-control nj-navbar__search-input" type="text" id="search-header-input" placeholder="Enter your query...">
           <button type="submit" class="nj-btn nj-navbar__search-button">Search</button>
           <a data-target="#collapse-search-bar-header" class="nj-header__close" aria-label="Close" data-toggle="collapse">
             <i class="material-icons nj-icon-material nj-icon-material--brand">close</i>
           </a>
       </form>
    </nav>
  </div>
</header></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="height: 60vh; transform: translateZ(0); overflow: auto">
  {% Header fixed=True logo_src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" logo_alt="ENGIE" logo_width=133 logosm_width=31 %}
    {% H_Menu active=True href="#" %}Accueil{% endH_Menu %}
    {% H_MenuTag href="#" color="green" %}News{% endH_MenuTag %}
    {% H_Menu href="#" %}Act with ENGIE{% endH_Menu %}
    {% H_Menu href="#" %}Group{% endH_Menu %}
    {% H_Menu href="#" %}
      Activities

      {% Slot 'submenu' %}
        {% Grid %}
          {% Row %}
            {% Col col="fill" %}
              {% H_Submenu label="Renouvelables" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biogaz" %}
                  Biogaz
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biomasse" %}
                  Biomasse
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydrogene-vert" %}
                  Hydrogène vert
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydroelectricite" %}
                  Hydroélectricité
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Solutions clients" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Thermique" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Centrales thermiques
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Nucléaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Gaz
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
          {% endRow %}
        {% endGrid %}
      {% endSlot %}
    {% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}

    {% Slot 'search' %}
      {% H_Search id="search-header" %}
    {% endSlot %}

    {% Slot 'head_first' %}
      <div>
        {% H_HeadLink href="#" %}EN{% endH_HeadLink %} /
        {% H_HeadLink href="#" active=True %}FR{% endH_HeadLink %}
      </div>
    {% endSlot %}
    {% Slot 'head_last' %}
      {% H_HeadLink href="" %}Espace client{% endH_HeadLink %}
    {% endSlot %}
  {% endHeader %}
</div>
"""
        expected = """
<div style="height: 60vh; transform: translateZ(0); overflow: auto"> <header class="nj-header nj-header--fixed">
  <div class="nj-header__group">
    <div class="nj-header__head">
      <div>
        <a href="#" class="nj-header__head-link">EN</a> /
        <a href="#" class="nj-header__head-link nj-header__head-link--active">FR</a>
      </div>
      <a href="#" class="nj-header__logo">
       <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="133" height="48">
      </a>
      <a href="" class="nj-header__head-link">Espace client</a>
    </div>
    <hr class="m-0">
    <nav class="container">
     <div class="nj-header__nav-burger" aria-expanded="false" aria-label="menu"><button><div></div></button></div>
     <div class="nj-header__nav-logo--reduced">
       <a href="#">
        <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="31" height="32">
       </a>
     </div>
     <ul class="nj-header__nav nj-header__nav--panel">
        <li class="nj-header__nav-item active"><a class="nj-header__nav-link" href="#">Accueil</a></li>
        <li class="nj-header__nav-item"><a class="nj-tag nj-tag--green" href="#">News</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Act with ENGIE</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Group</a></li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Activities <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
          <div class="nj-header__menu nj-header__nav--panel">
                  <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i> Activities</a>
            <div class="container">
              <div class="row">
                <div class="col">
                  <ul class="nj-header__sub-nav">
                    <li>
                      <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Renouvelables <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                      <ul class="nj-header__nav--panel">
                        <li><a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Renouvelables</a></li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biogaz">Biogaz</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biomasse">Biomasse</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydrogene-vert">Hydrogène vert</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydroelectricite">Hydroélectricité</a>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Solutions clients <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                    <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Solutions clients</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                    </li>
                  </ul>
                    </li></ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Thermique <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                   <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Thermique</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Centrales thermiques</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Nucléaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Gaz</a>
                    </li>
                  </ul>
                  </li></ul>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
      </ul>
       <a class="nj-header__search-icon" data-toggle="collapse" data-target="#collapse-search-bar-header" aria-expanded="false" aria-controls="collapse-search-bar-header"><i class="material-icons nj-icon-material nj-icon-material--brand">search</i></a>
       <form class="nj-header__search nj-collapse" id="search-header">
                 <input class="nj-form-control nj-navbar__search-input" type="text" id="search-header-input" placeholder="Enter your query...">
                 <button type="submit" class="nj-btn nj-navbar__search-button">Search</button>
                 <a data-target="#collapse-search-bar-header" class="nj-header__close" aria-label="Close" data-toggle="collapse">
                   <i class="material-icons nj-icon-material nj-icon-material--brand">close</i>
                 </a>
       </form>
    </nav>
  </div>
</header></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="height: 60vh; transform: translateZ(0); overflow: auto">
  {% Header size="sm" logo_src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" logo_alt="ENGIE" logo_width=133 logosm_width=31 %}
    {% H_Menu active=True href="#" %}Accueil{% endH_Menu %}
    {% H_MenuTag href="#" color="green" %}News{% endH_MenuTag %}
    {% H_Menu href="#" %}Act with ENGIE{% endH_Menu %}
    {% H_Menu href="#" %}Group{% endH_Menu %}
    {% H_Menu href="#" %}
      Activities

      {% Slot 'submenu' %}
        {% Grid %}
          {% Row %}
            {% Col col="fill" %}
              {% H_Submenu label="Renouvelables" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biogaz" %}
                  Biogaz
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biomasse" %}
                  Biomasse
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydrogene-vert" %}
                  Hydrogène vert
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydroelectricite" %}
                  Hydroélectricité
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Solutions clients" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Thermique" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Centrales thermiques
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Nucléaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Gaz
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
          {% endRow %}
        {% endGrid %}
      {% endSlot %}
    {% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}

    {% Slot 'search' %}
      {% H_Search id="search-header" %}
    {% endSlot %}

    {% Slot 'head_first' %}
      <div>
        {% H_HeadLink href="#" %}EN{% endH_HeadLink %} /
        {% H_HeadLink href="#" active=True %}FR{% endH_HeadLink %}
      </div>
    {% endSlot %}
    {% Slot 'head_last' %}
      {% H_HeadLink href="" %}Espace client{% endH_HeadLink %}
    {% endSlot %}
  {% endHeader %}
</div>
"""
        expected = """
<div style="height: 60vh; transform: translateZ(0); overflow: auto"> <header class="nj-header nj-header--sm">
  <div class="nj-header__group">
    <div class="nj-header__head">
      <div>
        <a href="#" class="nj-header__head-link">EN</a> /
        <a href="#" class="nj-header__head-link nj-header__head-link--active">FR</a>
      </div>
      <a href="#" class="nj-header__logo">
       <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="133" height="48">
      </a>
      <a href="" class="nj-header__head-link">Espace client</a>
    </div>
    <hr class="m-0">
    <nav class="container">
     <div class="nj-header__nav-burger" aria-expanded="false" aria-label="menu"><button><div></div></button></div>
     <div class="nj-header__nav-logo--reduced">
       <a href="#">
        <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="31" height="32">
       </a>
     </div>
     <ul class="nj-header__nav nj-header__nav--panel">
        <li class="nj-header__nav-item active"><a class="nj-header__nav-link" href="#">Accueil</a></li>
        <li class="nj-header__nav-item"><a class="nj-tag nj-tag--green" href="#">News</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Act with ENGIE</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Group</a></li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Activities <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
          <div class="nj-header__menu nj-header__nav--panel">
                  <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i> Activities</a>
            <div class="container">
              <div class="row">
                <div class="col">
                  <ul class="nj-header__sub-nav">
                    <li>
                      <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Renouvelables <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                      <ul class="nj-header__nav--panel">
                        <li><a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Renouvelables</a></li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biogaz">Biogaz</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biomasse">Biomasse</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydrogene-vert">Hydrogène vert</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydroelectricite">Hydroélectricité</a>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Solutions clients <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                    <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Solutions clients</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                    </li>
                  </ul>
                    </li></ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Thermique <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                   <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Thermique</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Centrales thermiques</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Nucléaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Gaz</a>
                    </li>
                  </ul>
                  </li></ul>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
      </ul>
       <a class="nj-header__search-icon" data-toggle="collapse" data-target="#collapse-search-bar-header" aria-expanded="false" aria-controls="collapse-search-bar-header"><i class="material-icons nj-icon-material nj-icon-material--brand">search</i></a>
       <form class="nj-header__search nj-collapse" id="search-header">
                 <input class="nj-form-control nj-navbar__search-input" type="text" id="search-header-input" placeholder="Enter your query...">
                 <button type="submit" class="nj-btn nj-navbar__search-button">Search</button>
                 <a data-target="#collapse-search-bar-header" class="nj-header__close" aria-label="Close" data-toggle="collapse">
                   <i class="material-icons nj-icon-material nj-icon-material--brand">close</i>
                 </a>
       </form>
    </nav>
  </div>
</header></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="height: 60vh; transform: translateZ(0); overflow: auto">
  {% Header fixed=True scroll="sm" logo_src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" logo_alt="ENGIE" logo_width=133 logosm_width=31 %}
    {% H_Menu active=True href="#" %}Accueil{% endH_Menu %}
    {% H_MenuTag href="#" color="green" %}News{% endH_MenuTag %}
    {% H_Menu href="#" %}Act with ENGIE{% endH_Menu %}
    {% H_Menu href="#" %}Group{% endH_Menu %}
    {% H_Menu href="#" %}
      Activities

      {% Slot 'submenu' %}
        {% Grid %}
          {% Row %}
            {% Col col="fill" %}
              {% H_Submenu label="Renouvelables" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biogaz" %}
                  Biogaz
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biomasse" %}
                  Biomasse
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydrogene-vert" %}
                  Hydrogène vert
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydroelectricite" %}
                  Hydroélectricité
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Solutions clients" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Thermique" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Centrales thermiques
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Nucléaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Gaz
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
          {% endRow %}
        {% endGrid %}
      {% endSlot %}
    {% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}

    {% Slot 'search' %}
      {% H_Search id="search-header" %}
    {% endSlot %}

    {% Slot 'head_first' %}
      <div>
        {% H_HeadLink href="#" %}EN{% endH_HeadLink %} /
        {% H_HeadLink href="#" active=True %}FR{% endH_HeadLink %}
      </div>
    {% endSlot %}
    {% Slot 'head_last' %}
      {% H_HeadLink href="" %}Espace client{% endH_HeadLink %}
    {% endSlot %}
  {% endHeader %}
</div>
"""
        expected = """
<div style="height: 60vh; transform: translateZ(0); overflow: auto"> <header class="nj-header nj-header--fixed nj-header--scroll-sm">
  <div class="nj-header__group">
    <div class="nj-header__head">
      <div>
        <a href="#" class="nj-header__head-link">EN</a> /
        <a href="#" class="nj-header__head-link nj-header__head-link--active">FR</a>
      </div>
      <a href="#" class="nj-header__logo">
       <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="133" height="48">
      </a>
      <a href="" class="nj-header__head-link">Espace client</a>
    </div>
    <hr class="m-0">
    <nav class="container">
     <div class="nj-header__nav-burger" aria-expanded="false" aria-label="menu"><button><div></div></button></div>
     <div class="nj-header__nav-logo--reduced">
       <a href="#">
        <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="31" height="32">
       </a>
     </div>
     <ul class="nj-header__nav nj-header__nav--panel">
        <li class="nj-header__nav-item active"><a class="nj-header__nav-link" href="#">Accueil</a></li>
        <li class="nj-header__nav-item"><a class="nj-tag nj-tag--green" href="#">News</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Act with ENGIE</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Group</a></li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Activities <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
          <div class="nj-header__menu nj-header__nav--panel">
                  <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i> Activities</a>
            <div class="container">
              <div class="row">
                <div class="col">
                  <ul class="nj-header__sub-nav">
                    <li>
                      <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Renouvelables <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                      <ul class="nj-header__nav--panel">
                        <li><a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Renouvelables</a></li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biogaz">Biogaz</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biomasse">Biomasse</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydrogene-vert">Hydrogène vert</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydroelectricite">Hydroélectricité</a>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Solutions clients <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                    <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Solutions clients</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                    </li>
                  </ul>
                    </li></ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a href="#" class="nj-header__menu-title" aria-expanded="false" aria-label="open">Thermique <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                   <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Thermique</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Centrales thermiques</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Nucléaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Gaz</a>
                    </li>
                  </ul>
                  </li></ul>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
      </ul>
       <a class="nj-header__search-icon" data-toggle="collapse" data-target="#collapse-search-bar-header" aria-expanded="false" aria-controls="collapse-search-bar-header"><i class="material-icons nj-icon-material nj-icon-material--brand">search</i></a>
       <form class="nj-header__search nj-collapse" id="search-header">
                 <input class="nj-form-control nj-navbar__search-input" type="text" id="search-header-input" placeholder="Enter your query...">
                 <button type="submit" class="nj-btn nj-navbar__search-button">Search</button>
                 <a data-target="#collapse-search-bar-header" class="nj-header__close" aria-label="Close" data-toggle="collapse">
                   <i class="material-icons nj-icon-material nj-icon-material--brand">close</i>
                 </a>
       </form>
    </nav>
  </div>
</header></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div style="height: 60vh; transform: translateZ(0); overflow: auto">
  {% Header fixed=True scroll="sm" expand="lg" logo_src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" logo_alt="ENGIE" logo_width=133 logosm_width=31 %}
    {% H_Menu active=True href="#" %}Accueil{% endH_Menu %}
    {% H_MenuTag href="#" color="green" %}News{% endH_MenuTag %}
    {% H_Menu href="#" %}Act with ENGIE{% endH_Menu %}
    {% H_Menu href="#" %}Group{% endH_Menu %}
    {% H_Menu href="#" %}
      Activities

      {% Slot 'submenu' %}
        {% Grid %}
          {% Row %}
            {% Col col="fill" %}
              {% H_Submenu label="Renouvelables" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biogaz" %}
                  Biogaz
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/biomasse" %}
                  Biomasse
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydrogene-vert" %}
                  Hydrogène vert
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/hydroelectricite" %}
                  Hydroélectricité
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Solutions clients" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Éolien
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Solaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Géothermie
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
            {% Col col="fill" %}
              {% H_Submenu label="Thermique" %}
                {% H_Link href="/activites/renouvelables/eolien" %}
                  Centrales thermiques
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/solaire" %}
                  Nucléaire
                {% endH_Link %}
                {% H_Link href="/activites/renouvelables/geothermie" %}
                  Gaz
                {% endH_Link %}
              {% endH_Submenu %}
            {% endCol %}
          {% endRow %}
        {% endGrid %}
      {% endSlot %}
    {% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}
    {% H_Menu href="#" %}Other item{% endH_Menu %}

    {% Slot 'search' %}
      {% H_Search id="search-header" %}
    {% endSlot %}

    {% Slot 'head_first' %}
      <div>
        {% H_HeadLink href="#" %}EN{% endH_HeadLink %} /
        {% H_HeadLink href="#" active=True %}FR{% endH_HeadLink %}
      </div>
    {% endSlot %}
    {% Slot 'head_last' %}
      {% H_HeadLink href="" %}Espace client{% endH_HeadLink %}
    {% endSlot %}
  {% endHeader %}
</div>
"""
        expected = """
<div style="height: 60vh; transform: translateZ(0); overflow: auto"><header class="nj-header nj-header--fixed nj-header--scroll-sm nj-header--expand-lg">
  <div class="nj-header__group">
    <div class="nj-header__head">
      <div>
        <a href="#" class="nj-header__head-link">EN</a> /
        <a href="#" class="nj-header__head-link nj-header__head-link--active">FR</a>
      </div>
      <a href="#" class="nj-header__logo">
       <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="133" height="48">
      </a>
      <a href="" class="nj-header__head-link">Espace client</a>
    </div>
    <hr class="m-0">
    <nav class="container">
     <div class="nj-header__nav-burger" aria-expanded="false" aria-label="menu"><button><div></div></button></div>
     <div class="nj-header__nav-logo--reduced">
       <a href="#">
        <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="31" height="32">
       </a>
     </div>
     <ul class="nj-header__nav nj-header__nav--panel">
        <li class="nj-header__nav-item active"><a class="nj-header__nav-link" href="#">Accueil</a></li>
        <li class="nj-header__nav-item"><a class="nj-tag nj-tag--green" href="#">News</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Act with ENGIE</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Group</a></li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Activities <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
          <div class="nj-header__menu nj-header__nav--panel">
                  <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i> Activities</a>
            <div class="container">
              <div class="row">
                <div class="col">
                  <ul class="nj-header__sub-nav">
                    <li>
                      <a aria-expanded="false" aria-label="open" class="nj-header__menu-title" href="#">Renouvelables <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                      <ul class="nj-header__nav--panel">
                        <li><a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Renouvelables</a></li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biogaz">Biogaz</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/biomasse">Biomasse</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydrogene-vert">Hydrogène vert</a>
                        </li>
                        <li>
                          <a class="nj-header__menu-link" href="/activites/renouvelables/hydroelectricite">Hydroélectricité</a>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a aria-expanded="false" aria-label="open" class="nj-header__menu-title" href="#">Solutions clients <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                    <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Solutions clients</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Éolien</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Solaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Géothermie</a>
                    </li>
                  </ul>
                    </li></ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                  <li>
                 <a aria-expanded="false" aria-label="open" class="nj-header__menu-title" href="#">Thermique <i class="nj-header__menu-arrow-right material-icons md-24">keyboard_arrow_right</i></a>
                  <ul class="nj-header__nav--panel">
                   <li>
                      <a class="nj-header__menu-return"><i class="nj-header__menu-arrow-left material-icons md-24">keyboard_arrow_left</i>Thermique</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/eolien">Centrales thermiques</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/solaire">Nucléaire</a>
                    </li>
                    <li>
                      <a class="nj-header__menu-link" href="/activites/renouvelables/geothermie">Gaz</a>
                    </li>
                  </ul>
                  </li></ul>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
        <li class="nj-header__nav-item"><a class="nj-header__nav-link" href="#">Other item</a></li>
      </ul>
       <a class="nj-header__search-icon" data-toggle="collapse" data-target="#collapse-search-bar-header" aria-expanded="false" aria-controls="collapse-search-bar-header"><i class="material-icons nj-icon-material nj-icon-material--brand">search</i></a>
       <form class="nj-header__search nj-collapse" id="search-header">
                 <input class="nj-form-control nj-navbar__search-input" type="text" id="search-header-input" placeholder="Enter your query...">
                 <button type="submit" class="nj-btn nj-navbar__search-button">Search</button>
                 <a data-target="#collapse-search-bar-header" class="nj-header__close" aria-label="Close" data-toggle="collapse">
                   <i class="material-icons nj-icon-material nj-icon-material--brand">close</i>
                 </a>
       </form>
    </nav>
  </div>
</header></div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Header expand="lg" logo_src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" logo_alt="ENGIE" logo_width=133 logosm_width=31 %}
  {% H_Menu active=True href="#" %}Accueil{% endH_Menu %}
  {% H_MenuTag href="#" color="teal" %}News{% endH_MenuTag %}
  {% H_Menu href="#" %}Act with ENGIE{% endH_Menu %}
  {% H_Menu href="#" %}Group{% endH_Menu %}
  {% H_Menu href="#" %}
    Activities

    {% Slot 'submenu' %}
      {% Grid %}
        {% Row %}
          {% Col col="fill" %}
            {% H_Submenu label="Renouvelables" %}
              {% H_Link href="/activites/renouvelables/eolien" %}
                Éolien
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/solaire" %}
                Solaire
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/geothermie" %}
                Géothermie
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/biogaz" %}
                Biogaz
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/biomasse" %}
                Biomasse
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/hydrogene-vert" %}
                Hydrogène vert
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/hydroelectricite" %}
                Hydroélectricité
              {% endH_Link %}
            {% endH_Submenu %}
          {% endCol %}
          {% Col col="fill" %}
            {% H_Submenu label="Solutions clients" %}
              {% H_Link href="/activites/renouvelables/eolien" %}
                Éolien
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/solaire" %}
                Solaire
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/geothermie" %}
                Géothermie
              {% endH_Link %}
            {% endH_Submenu %}
          {% endCol %}
          {% Col col="fill" %}
            {% H_Submenu label="Thermique" %}
              {% H_Link href="/activites/renouvelables/eolien" %}
                Centrales thermiques
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/solaire" %}
                Nucléaire
              {% endH_Link %}
              {% H_Link href="/activites/renouvelables/geothermie" %}
                Gaz
              {% endH_Link %}
            {% endH_Submenu %}
          {% endCol %}
        {% endRow %}
      {% endGrid %}
    {% endSlot %}
  {% endH_Menu %}
  {% H_Menu href="#" %}Other item{% endH_Menu %}
  {% H_Menu href="#" %}Other item{% endH_Menu %}

  {% Slot 'search' %}
    {% H_Search id="search-header" color="blue" %}
  {% endSlot %}

  {% Slot 'head_first' %}
    <div>
      {% H_HeadLink href="#" %}EN{% endH_HeadLink %} /
      {% H_HeadLink href="#" active=True %}FR{% endH_HeadLink %}
    </div>
  {% endSlot %}
  {% Slot 'head_last' %}
    {% H_HeadLink href="" %}Espace client{% endH_HeadLink %}
  {% endSlot %}
{% endHeader %}
"""
        expected = """
<header class="nj-header nj-header--expand-lg">
  <div class="nj-header__group">
    <div class="nj-header__head">
      <div>
        <a href="#" class="nj-header__head-link">EN</a> /
        <a href="#" class="nj-header__head-link nj-header__head-link--active"
          >FR</a
        >
      </div>
      <a href="#" class="nj-header__logo">
        <img
          src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg"
          alt="ENGIE"
          width="133"
          height="48"
        />
      </a>
      <a href="" class="nj-header__head-link">Espace client</a>
    </div>
    <hr class="m-0" />
    <nav class="container">
      <div
        class="nj-header__nav-burger"
        aria-label="menu"
        aria-expanded="false"
      >
        <button><div></div></button>
      </div>
      <div class="nj-header__nav-logo--reduced">
        <a href="#">
          <img
            src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg"
            alt="ENGIE"
            width="31"
            height="32"
          />
        </a>
      </div>
      <ul class="nj-header__nav nj-header__nav--panel">
        <li class="nj-header__nav-item active">
          <a class="nj-header__nav-link" href="#">Accueil</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-tag nj-tag--teal" href="#">News</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Act with ENGIE</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Group</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#"
            >Activities
            <i class="nj-header__menu-arrow-right material-icons md-24"
              >keyboard_arrow_right</i
            ></a
          >
          <div class="nj-header__menu nj-header__nav--panel">
                  <a class="nj-header__menu-return"
                    ><i class="nj-header__menu-arrow-left material-icons md-24"
                      >keyboard_arrow_left</i
                    >
                    Activities</a
                  >
            <div class="container">
              <div class="row">
                <div class="col">
                  <ul class="nj-header__sub-nav">
                    <li>
                      <a
                        href="#"
                        class="nj-header__menu-title"
                        aria-label="open"
                        aria-expanded="false"
                        >Renouvelables
                        <i
                          class="
                            nj-header__menu-arrow-right
                            material-icons
                            md-24
                          "
                          >keyboard_arrow_right</i
                        ></a
                      >
                      <ul class="nj-header__nav--panel">
                        <li>
                          <a class="nj-header__menu-return"
                            ><i
                              class="
                                nj-header__menu-arrow-left
                                material-icons
                                md-24
                              "
                              >keyboard_arrow_left</i
                            >Renouvelables</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/eolien"
                            >Éolien</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/solaire"
                            >Solaire</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/geothermie"
                            >Géothermie</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/biogaz"
                            >Biogaz</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/biomasse"
                            >Biomasse</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/hydrogene-vert"
                            >Hydrogène vert</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/hydroelectricite"
                            >Hydroélectricité</a
                          >
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                    <li>
                      <a
                        href="#"
                        class="nj-header__menu-title"
                        aria-label="open"
                        aria-expanded="false"
                        >Solutions clients
                        <i
                          class="
                            nj-header__menu-arrow-right
                            material-icons
                            md-24
                          "
                          >keyboard_arrow_right</i
                        ></a
                      >
                      <ul class="nj-header__nav--panel">
                        <li>
                          <a class="nj-header__menu-return"
                            ><i
                              class="
                                nj-header__menu-arrow-left
                                material-icons
                                md-24
                              "
                              >keyboard_arrow_left</i
                            >Solutions clients</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/eolien"
                            >Éolien</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/solaire"
                            >Solaire</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/geothermie"
                            >Géothermie</a
                          >
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
                <div class="col">
                  <ul class="nj-header__sub-nav">
                    <li>
                      <a
                        class="nj-header__menu-title"
                        href="#"
                        aria-label="open"
                        aria-expanded="false"
                      >
                        Thermique
                        <i
                          class="
                            nj-header__menu-arrow-right
                            material-icons
                            md-24
                          "
                          >keyboard_arrow_right</i
                        >
                      </a>
                      <ul class="nj-header__nav--panel">
                        <li>
                          <a class="nj-header__menu-return"
                            ><i
                              class="
                                nj-header__menu-arrow-left
                                material-icons
                                md-24
                              "
                              >keyboard_arrow_left</i
                            >Thermique</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/eolien"
                            >Centrales thermiques</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/solaire"
                            >Nucléaire</a
                          >
                        </li>
                        <li>
                          <a
                            class="nj-header__menu-link"
                            href="/activites/renouvelables/geothermie"
                            >Gaz</a
                          >
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Other item</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Other item</a>
        </li>
      </ul>
      <a
        class="nj-header__search-icon"
        data-toggle="collapse"
        data-target="#collapse-search-bar-header"
        aria-expanded="false"
        aria-controls="collapse-search-bar-header"
        ><i class="material-icons nj-icon-material nj-icon-material--blue">search</i></a
      >
      <form
        class="nj-header__search nj-collapse"
        id="search-header"
      >
        <input
          class="nj-form-control nj-navbar__search-input"
          type="text"
          id="search-header-input"
          placeholder="Enter your query..."
        />
        <button type="submit" class="nj-btn nj-navbar__search-button">
          Search
        </button>
        <a
          data-target="#collapse-search-bar-header"
          class="nj-header__close"
          aria-label="Close"
          data-toggle="collapse"
        >
          <i class="material-icons nj-icon-material nj-icon-material--blue">close</i>
        </a>
      </form>
    </nav>
  </div>
</header>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Header fixed=True scroll="sm" %}{% endHeader %}
"""
        expected = """
<header class="nj-header nj-header--fixed nj-header--scroll-sm">
  <div class="nj-header__group">
   <nav class="container">
    <div aria-expanded="false" aria-label="menu" class="nj-header__nav-burger">
     <button>
      <div>
      </div>
     </button>
    </div>
    <ul class="nj-header__nav nj-header__nav--panel">
    </ul>
   </nav>
  </div>
</header>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Header size="sm" expand="lg" logo_src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" logo_alt="ENGIE" logo_width=133 logosm_width=31 %}
  {% H_Menu active=True href="#" %}Accueil{% endH_Menu %}
  {% H_MenuTag href="#" color="teal" %}News{% endH_MenuTag %}
  {% H_Menu href="#" %}Act with ENGIE{% endH_Menu %}
  {% H_Menu href="#" %}Group{% endH_Menu %}
  {% H_Menu href="#" %}Activities{% endH_Menu %}
  {% H_Menu href="#" %}Other item{% endH_Menu %}
  {% H_Menu href="#" %}Other item{% endH_Menu %}

  {% Slot 'search' %}
    {% H_Search id="search-header" color="blue" %}
  {% endSlot %}

  {% Slot 'head_first' %}
    <div>
      {% H_HeadLink href="#" %}EN{% endH_HeadLink %} /
      {% H_HeadLink href="#" active=True %}FR{% endH_HeadLink %}
    </div>
  {% endSlot %}
  {% Slot 'head_last' %}
    {% H_HeadLink href="" %}Espace client{% endH_HeadLink %}
  {% endSlot %}
{% endHeader %}
"""
        expected = """
<header class="nj-header nj-header--sm nj-header--expand-lg">
  <div class="nj-header__group">
    <div class="nj-header__head">
      <div>
        <a href="#" class="nj-header__head-link">EN</a> /
        <a href="#" class="nj-header__head-link nj-header__head-link--active"
          >FR</a
        >
      </div>
      <a href="#" class="nj-header__logo">
        <img
          src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg"
          alt="ENGIE"
          width="133"
          height="48"
        />
      </a>
      <a href="" class="nj-header__head-link">Espace client</a>
    </div>
    <hr class="m-0" />
    <nav class="container">
      <div
        class="nj-header__nav-burger"
        aria-label="menu"
        aria-expanded="false"
      >
        <button><div></div></button>
      </div>
      <div class="nj-header__nav-logo--reduced">
        <a href="#">
          <img
            src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg"
            alt="ENGIE"
            width="31"
            height="32"
          />
        </a>
      </div>
      <ul class="nj-header__nav nj-header__nav--panel">
        <li class="nj-header__nav-item active">
          <a class="nj-header__nav-link" href="#">Accueil</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-tag nj-tag--teal" href="#">News</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Act with ENGIE</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Group</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#"
            >Activities
            </a
          >
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Other item</a>
        </li>
        <li class="nj-header__nav-item">
          <a class="nj-header__nav-link" href="#">Other item</a>
        </li>
      </ul>
      <a
        class="nj-header__search-icon"
        data-toggle="collapse"
        data-target="#collapse-search-bar-header"
        aria-expanded="false"
        aria-controls="collapse-search-bar-header"
        ><i class="material-icons nj-icon-material nj-icon-material--blue">search</i></a
      >
      <form
        class="nj-header__search nj-collapse"
        id="search-header"
      >
        <input
          class="nj-form-control nj-navbar__search-input"
          type="text"
          id="search-header-input"
          placeholder="Enter your query..."
        />
        <button type="submit" class="nj-btn nj-navbar__search-button">
          Search
        </button>
        <a
          data-target="#collapse-search-bar-header"
          class="nj-header__close"
          aria-label="Close"
          data-toggle="collapse"
        >
          <i class="material-icons nj-icon-material nj-icon-material--blue">close</i>
        </a>
      </form>
    </nav>
  </div>
</header>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
{% Header fixed=True %}
  {% Slot 'search' %}
    {% H_Search id="search-header" color="blue" %}
  {% endSlot %}
{% endHeader %}
"""
        expected = """
<header class="nj-header nj-header--fixed">
  <div class="nj-header__group">
  <nav class="container">
    <div aria-expanded="false" aria-label="menu" class="nj-header__nav-burger">
      <button>
        <div>
        </div>
      </button>
    </div>
    <ul class="nj-header__nav nj-header__nav--panel">
    </ul>
     <a class="nj-header__search-icon" data-toggle="collapse" data-target="#collapse-search-bar-header" aria-expanded="false" aria-controls="collapse-search-bar-header"><i class="material-icons nj-icon-material nj-icon-material--blue">search</i></a>
     <form class="nj-header__search nj-collapse" id="search-header">
       <input class="nj-form-control nj-navbar__search-input" type="text" id="search-header-input" placeholder="Enter your query...">
       <button type="submit" class="nj-btn nj-navbar__search-button">Search</button>
       <a data-target="#collapse-search-bar-header" class="nj-header__close" aria-label="Close" data-toggle="collapse">
         <i class="material-icons nj-icon-material nj-icon-material--blue">close</i>
       </a>
     </form>
  </nav>  
  </div>
</header>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
{% Header fixed=True %}{% endHeader %}
"""
        expected = """
<header class="nj-header nj-header--fixed">
  <div class="nj-header__group">
   <nav class="container">
    <div aria-expanded="false" aria-label="menu" class="nj-header__nav-burger">
     <button>
      <div>
      </div>
     </button>
    </div>
    <ul class="nj-header__nav nj-header__nav--panel">
    </ul>
   </nav>
  </div>
</header>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example11(self):
        template = """
{% load fluid_design %}
{% Header expand="lg" %}{% endHeader %}
"""
        expected = """
<header class="nj-header nj-header--expand-lg">
  <div class="nj-header__group">
   <nav class="container">
    <div aria-expanded="false" aria-label="menu" class="nj-header__nav-burger">
     <button>
      <div>
      </div>
     </button>
    </div>
    <ul class="nj-header__nav nj-header__nav--panel">
    </ul>
   </nav>
  </div>
</header>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
