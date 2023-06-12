# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class FooterTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Footer %}
{% endFooter %}
"""
        expected = """
<footer class="nj-footer" role="contentinfo">
  <div class="container">
    <ul class="nj-footer__links">
    </ul>
  </div>
</footer>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Footer %}
  {% FooterLink href="#" %}Plan du site{% endFooterLink %}
  {% FooterLink href="#" %}Rejoignez-nous{% endFooterLink %}
  {% FooterLink href="#" %}Mentions légales{% endFooterLink %}
  {% FooterLink href="#" %}Données personnelles{% endFooterLink %}
  {% FooterLink href="#" %}Médiation{% endFooterLink %}

  {% Slot 'social' %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/facebook.svg"
          alt="Facebook" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/twitter.svg"
          alt="Twitter" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/linkedin.svg"
          alt="Linkedin" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/instagram.svg"
          alt="Instagram" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/youtube.svg"
          alt="Youtube" class="nj-footer__social-icon">
    {% endFooterSocial %}
  {% endSlot %}

  {% Slot 'banner' %}
    <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg"
        alt="ENGIE" width="134px" height="48px" class="nj-footer__logo">
    <p>L'énergie est notre avenir, économisons-la.</p>
  {% endSlot %}
{% endFooter %}
"""
        expected = """
<footer class="nj-footer" role="contentinfo">
  <div class="container">
    <div class="nj-footer__baseline">
      <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="134px" height="48px" class="nj-footer__logo">
      <p>L'énergie est notre avenir, économisons-la.</p>
    </div>
    <hr>
    <ul class="nj-footer__links">
      <li><a href="#" class="nj-link nj-link--contextual">Plan du site</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Rejoignez-nous</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Mentions légales</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Données personnelles</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Médiation</a></li>
    </ul>
    <ul class="nj-footer__social">
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/facebook.svg" alt="Facebook" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/twitter.svg" alt="Twitter" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/linkedin.svg" alt="Linkedin" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/instagram.svg" alt="Instagram" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/youtube.svg" alt="Youtube" class="nj-footer__social-icon"></a></li>
    </ul>
  </div>
</footer>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% Footer %}
  {% FooterLink href="#" %}Plan du site{% endFooterLink %}
  {% FooterLink href="#" %}Rejoignez-nous{% endFooterLink %}
  {% FooterLink href="#" %}Mentions légales{% endFooterLink %}
  {% FooterLink href="#" %}Données personnelles{% endFooterLink %}
  {% FooterLink href="#" %}Médiation{% endFooterLink %}

  {% Slot 'menu' %}
    {% FooterMenu label="Title 1" %}
      {% FooterLink href="#" %}Link 1{% endFooterLink %}
      {% FooterLink href="#" %}Link 2{% endFooterLink %}
      {% FooterLink href="#" %}Link 3{% endFooterLink %}
    {% endFooterMenu %}
    {% FooterMenu label="Title 2" %}
      {% FooterLink href="#" %}Link 1{% endFooterLink %}
      {% FooterLink href="#" %}Link 2{% endFooterLink %}
      {% FooterLink href="#" %}Link 3{% endFooterLink %}
    {% endFooterMenu %}
    {% FooterMenu label="Title 3" %}
      {% FooterLink href="#" %}Link 1{% endFooterLink %}
      {% FooterLink href="#" %}Link 2{% endFooterLink %}
      {% FooterLink href="#" %}Link 3{% endFooterLink %}
    {% endFooterMenu %}
  {% endSlot %}

  {% Slot 'social' %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/facebook.svg"
          alt="Facebook" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/twitter.svg"
          alt="Twitter" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/linkedin.svg"
          alt="Linkedin" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/instagram.svg"
          alt="Instagram" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/youtube.svg"
          alt="Youtube" class="nj-footer__social-icon">
    {% endFooterSocial %}
  {% endSlot %}

  {% Slot 'banner' %}
    <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg"
        alt="ENGIE" width="134px" height="48px" class="nj-footer__logo">
    <p>L'énergie est notre avenir, économisons-la.</p>
  {% endSlot %}
{% endFooter %}
"""
        expected = """
<footer class="nj-footer" role="contentinfo">
  <div class="container">
    <div class="nj-footer__baseline">
      <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="134px" height="48px" class="nj-footer__logo">
      <p>L'énergie est notre avenir, économisons-la.</p>
    </div>
    <hr>
    <div class="nj-footer__menu">
      <div class="nj-footer__menu-section">
        <h2 class="nj-footer__links-list-title">Title 1</h2>
        <ul class="nj-footer__links-list">
          <li><a href="#" class="nj-link nj-link--contextual">Link 1</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 2</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 3</a></li>
        </ul>
      </div>
      <div class="nj-footer__menu-section">
        <h2 class="nj-footer__links-list-title">Title 2</h2>
        <ul class="nj-footer__links-list">
          <li><a href="#" class="nj-link nj-link--contextual">Link 1</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 2</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 3</a></li>
        </ul>
      </div>
      <div class="nj-footer__menu-section">
        <h2 class="nj-footer__links-list-title">Title 3</h2>
        <ul class="nj-footer__links-list">
          <li><a href="#" class="nj-link nj-link--contextual">Link 1</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 2</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 3</a></li>
        </ul>
      </div>
    </div>
    <hr>
    <ul class="nj-footer__links">
      <li><a href="#" class="nj-link nj-link--contextual">Plan du site</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Rejoignez-nous</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Mentions légales</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Données personnelles</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Médiation</a></li>
    </ul>
    <ul class="nj-footer__social">
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/facebook.svg" alt="Facebook" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/twitter.svg" alt="Twitter" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/linkedin.svg" alt="Linkedin" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/instagram.svg" alt="Instagram" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/youtube.svg" alt="Youtube" class="nj-footer__social-icon"></a></li>
    </ul>
  </div>
</footer>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
{% Footer %}
  {% FooterLink href="#" %}Plan du site{% endFooterLink %}
  {% FooterLink href="#" %}Rejoignez-nous{% endFooterLink %}
  {% FooterLink href="#" %}Mentions légales{% endFooterLink %}
  {% FooterLink href="#" %}Données personnelles{% endFooterLink %}
  {% FooterLink href="#" %}Médiation{% endFooterLink %}

  {% Slot 'social' %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/facebook.svg"
          alt="Facebook" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/twitter.svg"
          alt="Twitter" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/linkedin.svg"
          alt="Linkedin" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/instagram.svg"
          alt="Instagram" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/youtube.svg"
          alt="Youtube" class="nj-footer__social-icon">
    {% endFooterSocial %}
  {% endSlot %}

  {% Slot 'banner' %}
    <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg"
        alt="ENGIE" width="134px" height="48px" class="nj-footer__logo">
    <p>L'énergie est notre avenir, économisons-la.</p>
  {% endSlot %}
{% endFooter %}
"""
        expected = """
<footer class="nj-footer" role="contentinfo">
    <div class="container">
      <div class="nj-footer__baseline">
        <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="134px" height="48px" class="nj-footer__logo">
        <p>L'énergie est notre avenir, économisons-la.</p>
      </div>
      <hr>
      <ul class="nj-footer__links">
        <li><a href="#" class="nj-link nj-link--contextual">Plan du site</a></li>
        <li><a href="#" class="nj-link nj-link--contextual">Rejoignez-nous</a></li>
        <li><a href="#" class="nj-link nj-link--contextual">Mentions légales</a></li>
        <li><a href="#" class="nj-link nj-link--contextual">Données personnelles</a></li>
        <li><a href="#" class="nj-link nj-link--contextual">Médiation</a></li>
      </ul>
      <ul class="nj-footer__social">
        <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/facebook.svg" alt="Facebook" class="nj-footer__social-icon"></a></li>
        <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/twitter.svg" alt="Twitter" class="nj-footer__social-icon"></a></li>
        <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/linkedin.svg" alt="Linkedin" class="nj-footer__social-icon"></a></li>
        <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/instagram.svg" alt="Instagram" class="nj-footer__social-icon"></a></li>
        <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/youtube.svg" alt="Youtube" class="nj-footer__social-icon"></a></li>
      </ul>
    </div>
  </footer>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% Footer %}
  {% FooterLink href="#" %}Plan du site{% endFooterLink %}
  {% FooterLink href="#" %}Rejoignez-nous{% endFooterLink %}
  {% FooterLink href="#" %}Mentions légales{% endFooterLink %}
  {% FooterLink href="#" %}Données personnelles{% endFooterLink %}
  {% FooterLink href="#" %}Médiation{% endFooterLink %}

  {% Slot 'menu' %}
    {% FooterMenu label="Title 1" %}
      {% FooterLink href="#" %}Link 1{% endFooterLink %}
      {% FooterLink href="#" %}Link 2{% endFooterLink %}
      {% FooterLink href="#" %}Link 3{% endFooterLink %}
    {% endFooterMenu %}
    {% FooterMenu label="Title 2" %}
      {% FooterLink href="#" %}Link 1{% endFooterLink %}
      {% FooterLink href="#" %}Link 2{% endFooterLink %}
      {% FooterLink href="#" %}Link 3{% endFooterLink %}
    {% endFooterMenu %}
    {% FooterMenu label="Title 3" %}
      {% FooterLink href="#" %}Link 1{% endFooterLink %}
      {% FooterLink href="#" %}Link 2{% endFooterLink %}
      {% FooterLink href="#" %}Link 3{% endFooterLink %}
    {% endFooterMenu %}
  {% endSlot %}

  {% Slot 'social' %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/facebook.svg"
          alt="Facebook" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/twitter.svg"
          alt="Twitter" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/linkedin.svg"
          alt="Linkedin" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/instagram.svg"
          alt="Instagram" class="nj-footer__social-icon">
    {% endFooterSocial %}
    {% FooterSocial href="#" %}
      <img src="https://assets.design.digital.engie.com/icons/social/youtube.svg"
          alt="Youtube" class="nj-footer__social-icon">
    {% endFooterSocial %}
  {% endSlot %}

  {% Slot 'banner' %}
    <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg"
        alt="ENGIE" width="134px" height="48px" class="nj-footer__logo">
    <p>L'énergie est notre avenir, économisons-la.</p>
  {% endSlot %}
{% endFooter %}
"""
        expected = """
<footer class="nj-footer" role="contentinfo">
  <div class="container">
    <div class="nj-footer__baseline">
      <img src="https://assets.design.digital.engie.com/brand/logo-engie-blue.svg" alt="ENGIE" width="134px" height="48px" class="nj-footer__logo">
      <p>L'énergie est notre avenir, économisons-la.</p>
    </div>
    <hr>
    <div class="nj-footer__menu">
      <div class="nj-footer__menu-section">
        <h2 class="nj-footer__links-list-title">Title 1</h2>
        <ul class="nj-footer__links-list">
          <li><a href="#" class="nj-link nj-link--contextual">Link 1</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 2</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 3</a></li>
        </ul>
      </div>
      <div class="nj-footer__menu-section">
        <h2 class="nj-footer__links-list-title">Title 2</h2>
        <ul class="nj-footer__links-list">
          <li><a href="#" class="nj-link nj-link--contextual">Link 1</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 2</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 3</a></li>
        </ul>
      </div>
      <div class="nj-footer__menu-section">
        <h2 class="nj-footer__links-list-title">Title 3</h2>
        <ul class="nj-footer__links-list">
          <li><a href="#" class="nj-link nj-link--contextual">Link 1</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 2</a></li>
          <li><a href="#" class="nj-link nj-link--contextual">Link 3</a></li>
        </ul>
      </div>
    </div>
    <hr>
    <ul class="nj-footer__links">
      <li><a href="#" class="nj-link nj-link--contextual">Plan du site</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Rejoignez-nous</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Mentions légales</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Données personnelles</a></li>
      <li><a href="#" class="nj-link nj-link--contextual">Médiation</a></li>
    </ul>
    <ul class="nj-footer__social">
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/facebook.svg" alt="Facebook" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/twitter.svg" alt="Twitter" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/linkedin.svg" alt="Linkedin" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/instagram.svg" alt="Instagram" class="nj-footer__social-icon"></a></li>
      <li><a href="#" class="nj-footer__social-link"><img src="https://assets.design.digital.engie.com/icons/social/youtube.svg" alt="Youtube" class="nj-footer__social-icon"></a></li>
    </ul>
  </div>
</footer>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
