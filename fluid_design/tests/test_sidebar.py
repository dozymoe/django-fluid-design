# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class SidebarTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Sidebar id="test" %}
{% endSidebar %}
"""
        expected = """
<div class="nj-sidebar" data-close-on-interact-out="true" id="test">
  <nav class="nj-sidebar__navigation">
   <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
   </ul>
  </nav>
  <ul class="nj-sidebar__collapse nj-list-group nj-list-group--sm nj-list-group--no-border">
   <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--no-border">
    <button aria-pressed="false" data-target="#test" data-toggle="sidebar">
     <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-sidebar__fold-btn">
      chevron_left
     </span>
     <span class="nj-list-group__item-content">
      Close
     </span>
    </button>
   </li>
  </ul>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="min-height: 80vh; max-height: 100vh; transform: translateZ(0); overflow: auto;">
  {% Sidebar id="sidebarExample" logo_src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" logosm_src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" logo_alt="ENGIE - back to home" logo_width="100px" logosm_width="auto" %}
    {% S_Menu arrow=True current=True %}
      Dashboard

      {% Slot 'icon' %}{% Icon label='dashboard' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu badge=7 %}
      Alerts

      {% Slot 'icon' %}{% Icon label='report_problem' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Signals

      {% Slot 'icon' %}{% Icon label='show_chart' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Simulation

      {% Slot 'icon' %}{% Icon label='online_prediction' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Events

      {% Slot 'icon' %}{% Icon label='event' %}{% endSlot %}
    {% endS_Menu %}

    {% Slot 'footer' %}
      {% S_Menu %}
        Settings

        {% Slot 'icon' %}{% Icon label="settings" %}{% endSlot %}
      {% endS_Menu %}
      {% S_Menu %}
        Profile

        {% Slot 'icon' %}{% Icon label="account_circle" %}{% endSlot %}
      {% endS_Menu %}
      {% S_Menu %}
        Logout

        {% Slot 'icon' %}{% Icon label="power_settings_new" %}{% endSlot %}
      {% endS_Menu %}
    {% endSlot %}
  {% endSidebar %}
  <div class="nj-sidebar-content" style="padding: var(--nj-size-space-16);">
    <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
  </div>
</div>
"""
        expected = """
<div style="min-height: 80vh; max-height: 100vh; transform: translateZ(0); overflow: auto;">
  <div class="nj-sidebar" id="sidebarExample" data-close-on-interact-out="true">
    <a class="nj-sidebar__brand" href="#" title="ENGIE - back to home">
      <img class="nj-sidebar__logo" src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" alt="ENGIE - back to home" width="100px" height="">
      <img class="nj-sidebar__logo--folded" src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" alt="ENGIE - back to home" width="auto" height="36">
    </a>

    <nav class="nj-sidebar__navigation">
      <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border active" aria-current="true">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">dashboard</span>
            <span class="nj-list-group__item-content">Dashboard</span>
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">report_problem</span>
            <span class="nj-list-group__item-content">Alerts</span>
            <p class="nj-badge nj-list-group__item-right-content">7</p>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">show_chart</span>
            <span class="nj-list-group__item-content">Signals</span>
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">online_prediction</span>
            <span class="nj-list-group__item-content">Simulation</span>
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">event</span>
            <span class="nj-list-group__item-content">Events</span>
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
          </a>
        </li>
      </ul>
    </nav>

    <nav class="nj-sidebar__navigation nj-sidebar__navigation--footer">
      <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
        <div class="nj-sidebar__divider"></div>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">settings</span>
            <span class="nj-list-group__item-content">Settings</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">account_circle</span>
            <span class="nj-list-group__item-content">Profile</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">power_settings_new</span>
            <span class="nj-list-group__item-content">Logout</span>
          </a>
        </li>
      </ul>
    </nav>

    <ul class="nj-sidebar__collapse nj-list-group nj-list-group--sm nj-list-group--no-border">
      <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--no-border">
        <button data-toggle="sidebar" data-target="#sidebarExample" aria-pressed="false">
          <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-sidebar__fold-btn">chevron_left</span>
          <span class="nj-list-group__item-content">Close</span>
        </button>
      </li>
    </ul>
  </div>

  <div class="nj-sidebar-content" style="padding: var(--nj-size-space-16);">
    <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="min-height: 80vh; max-height: 100vh; transform: translateZ(0); overflow: auto;">
  {% Sidebar id="sidebarExampleFolded" folded=True logo_src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" logosm_src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" logo_alt="ENGIE - back to home" logo_width="100px" logosm_width="auto" %}
    {% S_Menu arrow=True current=True %}
      Dashboard

      {% Slot 'icon' %}{% Icon label='dashboard' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu badge=7 %}
      Alerts

      {% Slot 'icon' %}{% Icon label='report_problem' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Signals

      {% Slot 'icon' %}{% Icon label='show_chart' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Simulation

      {% Slot 'icon' %}{% Icon label='online_prediction' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Events

      {% Slot 'icon' %}{% Icon label='event' %}{% endSlot %}
    {% endS_Menu %}

    {% Slot 'footer' %}
      {% S_Menu %}
        Settings

        {% Slot 'icon' %}{% Icon label="settings" %}{% endSlot %}
      {% endS_Menu %}
      {% S_Menu %}
        Profile

        {% Slot 'icon' %}{% Icon label="account_circle" %}{% endSlot %}
      {% endS_Menu %}
      {% S_Menu %}
        Logout

        {% Slot 'icon' %}{% Icon label="power_settings_new" %}{% endSlot %}
      {% endS_Menu %}
    {% endSlot %}
  {% endSidebar %}
  <div class="nj-sidebar-content" style="padding: var(--nj-size-space-16);">
    <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
    <p>For a folded sidebar, add the <code>.nj-sidebar--folded</code> modifier.</p>
  </div>
</div>
"""
        expected = """
<div style="min-height: 80vh; max-height: 100vh; transform: translateZ(0); overflow: auto;">
  <div class="nj-sidebar nj-sidebar--folded" id="sidebarExampleFolded" data-close-on-interact-out="true">
    <a class="nj-sidebar__brand" href="#" title="ENGIE - back to home">
      <img class="nj-sidebar__logo" src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" alt="ENGIE - back to home" width="100px" height="">
      <img class="nj-sidebar__logo--folded" src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" alt="ENGIE - back to home" width="auto" height="36">
    </a>

    <nav class="nj-sidebar__navigation">
      <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border active" aria-current="true">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">dashboard</span>
            <span class="nj-list-group__item-content">Dashboard</span>
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">report_problem</span>
            <span class="nj-list-group__item-content">Alerts</span>
            <p class="nj-badge nj-list-group__item-right-content">7</p>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">show_chart</span>
            <span class="nj-list-group__item-content">Signals</span>
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">online_prediction</span>
            <span class="nj-list-group__item-content">Simulation</span>
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">event</span>
            <span class="nj-list-group__item-content">Events</span>
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
          </a>
        </li>
      </ul>
    </nav>

    <nav class="nj-sidebar__navigation nj-sidebar__navigation--footer">
      <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
        <div class="nj-sidebar__divider"></div>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">settings</span>
            <span class="nj-list-group__item-content">Settings</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">account_circle</span>
            <span class="nj-list-group__item-content">Profile</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">power_settings_new</span>
            <span class="nj-list-group__item-content">Logout</span>
          </a>
        </li>
      </ul>
    </nav>

    <ul class="nj-sidebar__collapse nj-list-group nj-list-group--sm nj-list-group--no-border">
      <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--no-border">
        <button data-toggle="sidebar" data-target="#sidebarExampleFolded" aria-pressed="false">
          <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-sidebar__fold-btn">chevron_left</span>
          <span class="nj-list-group__item-content">Close</span>
        </button>
      </li>
    </ul>
  </div>

  <div class="nj-sidebar-content" style="padding: var(--nj-size-space-16);">
    <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
    <p>For a folded sidebar, add the <code>.nj-sidebar--folded</code> modifier.</p>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="min-height: 80vh; max-height: 100vh; transform: translateZ(0); overflow: auto;">
  {% Sidebar id="sidebarExampleNoPush" logo_src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" logosm_src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" logo_alt="ENGIE - back to home" logo_width="100px" logosm_width="auto" %}
    {% S_Menu arrow=True current=True %}
      Dashboard

      {% Slot 'icon' %}{% Icon label='dashboard' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu badge=7 %}
      Alerts

      {% Slot 'icon' %}{% Icon label='report_problem' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Signals

      {% Slot 'icon' %}{% Icon label='show_chart' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Simulation

      {% Slot 'icon' %}{% Icon label='online_prediction' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Events

      {% Slot 'icon' %}{% Icon label='event' %}{% endSlot %}
    {% endS_Menu %}

    {% Slot 'footer' %}
      {% S_Menu %}
        Settings

        {% Slot 'icon' %}{% Icon label="settings" %}{% endSlot %}
      {% endS_Menu %}
      {% S_Menu %}
        Profile

        {% Slot 'icon' %}{% Icon label="account_circle" %}{% endSlot %}
      {% endS_Menu %}
      {% S_Menu %}
        Logout

        {% Slot 'icon' %}{% Icon label="power_settings_new" %}{% endSlot %}
      {% endS_Menu %}
    {% endSlot %}
  {% endSidebar %}
  <div class="nj-sidebar-content nj-sidebar-content--nopush" style="padding: var(--nj-size-space-16);">
    <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
    <p>To have the sidebar go over the content, add the <code>.nj-sidebar-content--nopush</code> modifier.</p>
  </div>
</div>
"""
        expected = """
<div style="min-height: 80vh; max-height: 100vh; transform: translateZ(0); overflow: auto;">
    <div class="nj-sidebar" id="sidebarExampleNoPush" data-close-on-interact-out="true">
      <a class="nj-sidebar__brand" href="#" title="ENGIE - back to home">
        <img class="nj-sidebar__logo" src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" alt="ENGIE - back to home" width="100px" height="">
        <img class="nj-sidebar__logo--folded" src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" alt="ENGIE - back to home" width="auto" height="36">
      </a>

      <nav class="nj-sidebar__navigation">
        <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border active" aria-current="true">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">dashboard</span>
              <span class="nj-list-group__item-content">Dashboard</span>
              <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">report_problem</span>
              <span class="nj-list-group__item-content">Alerts</span>
              <p class="nj-badge nj-list-group__item-right-content">7</p>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">show_chart</span>
              <span class="nj-list-group__item-content">Signals</span>
              <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">online_prediction</span>
              <span class="nj-list-group__item-content">Simulation</span>
              <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">event</span>
              <span class="nj-list-group__item-content">Events</span>
              <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
            </a>
          </li>
        </ul>
      </nav>

      <nav class="nj-sidebar__navigation nj-sidebar__navigation--footer">
        <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
          <div class="nj-sidebar__divider"></div>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">settings</span>
              <span class="nj-list-group__item-content">Settings</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">account_circle</span>
              <span class="nj-list-group__item-content">Profile</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">power_settings_new</span>
              <span class="nj-list-group__item-content">Logout</span>
            </a>
          </li>
        </ul>
      </nav>

      <ul class="nj-sidebar__collapse nj-list-group nj-list-group--sm nj-list-group--no-border">
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--no-border">
          <button data-toggle="sidebar" data-target="#sidebarExampleNoPush" aria-pressed="false">
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-sidebar__fold-btn">chevron_left</span>
            <span class="nj-list-group__item-content">Close</span>
          </button>
        </li>
      </ul>
    </div>

    <div class="nj-sidebar-content nj-sidebar-content--nopush" style="padding: var(--nj-size-space-16);">
      <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
      <p>To have the sidebar go over the content, add the <code>.nj-sidebar-content--nopush</code> modifier.</p>
    </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="min-height: 80vh; max-height: 100vh; transform: translateZ(0); overflow: auto;">
  {% Sidebar id="sidebarExampleNoMotion" nomotion=True logo_src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" logosm_src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" logo_alt="ENGIE - back to home" logo_width="100px" logosm_width="auto" %}
    {% S_Menu arrow=True current=True %}
      Dashboard

      {% Slot 'icon' %}{% Icon label='dashboard' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu badge=7 %}
      Alerts

      {% Slot 'icon' %}{% Icon label='report_problem' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Signals

      {% Slot 'icon' %}{% Icon label='show_chart' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Simulation

      {% Slot 'icon' %}{% Icon label='online_prediction' %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu arrow=True %}
      Events

      {% Slot 'icon' %}{% Icon label='event' %}{% endSlot %}
    {% endS_Menu %}

    {% Slot 'footer' %}
      {% S_Menu %}
        Settings

        {% Slot 'icon' %}{% Icon label="settings" %}{% endSlot %}
      {% endS_Menu %}
      {% S_Menu %}
        Profile

        {% Slot 'icon' %}{% Icon label="account_circle" %}{% endSlot %}
      {% endS_Menu %}
      {% S_Menu %}
        Logout

        {% Slot 'icon' %}{% Icon label="power_settings_new" %}{% endSlot %}
      {% endS_Menu %}
    {% endSlot %}
  {% endSidebar %}
  <div class="nj-sidebar-content" style="padding: var(--nj-size-space-16);">
    <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
    <p>For a reduced motion sidebar, add the <code>.nj-sidebar--no-motion</code> modifier.</p>
  </div>
</div>
"""
        expected = """
<div style="min-height: 80vh; max-height: 100vh; transform: translateZ(0); overflow: auto;">
    <div class="nj-sidebar nj-sidebar--no-motion" id="sidebarExampleNoMotion" data-close-on-interact-out="true">
      <a class="nj-sidebar__brand" href="#" title="ENGIE - back to home">
        <img class="nj-sidebar__logo" src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" alt="ENGIE - back to home" width="100px" height="">
        <img class="nj-sidebar__logo--folded" src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" alt="ENGIE - back to home" width="auto" height="36">
      </a>

      <nav class="nj-sidebar__navigation">
        <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border active" aria-current="true">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">dashboard</span>
              <span class="nj-list-group__item-content">Dashboard</span>
              <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">report_problem</span>
              <span class="nj-list-group__item-content">Alerts</span>
              <p class="nj-badge nj-list-group__item-right-content">7</p>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">show_chart</span>
              <span class="nj-list-group__item-content">Signals</span>
              <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">online_prediction</span>
              <span class="nj-list-group__item-content">Simulation</span>
              <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">event</span>
              <span class="nj-list-group__item-content">Events</span>
              <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-list-group__item-right-content">chevron_right</span>
            </a>
          </li>
        </ul>
      </nav>

      <nav class="nj-sidebar__navigation nj-sidebar__navigation--footer">
        <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
          <div class="nj-sidebar__divider"></div>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">settings</span>
              <span class="nj-list-group__item-content">Settings</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">account_circle</span>
              <span class="nj-list-group__item-content">Profile</span>
            </a>
          </li>
          <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
            <a href="#">
              <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">power_settings_new</span>
              <span class="nj-list-group__item-content">Logout</span>
            </a>
          </li>
        </ul>
      </nav>

      <ul class="nj-sidebar__collapse nj-list-group nj-list-group--sm nj-list-group--no-border">
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--no-border">
          <button data-toggle="sidebar" data-target="#sidebarExampleNoMotion" aria-pressed="false">
            <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-sidebar__fold-btn">chevron_left</span>
            <span class="nj-list-group__item-content">Close</span>
          </button>
        </li>
      </ul>
    </div>

    <div class="nj-sidebar-content" style="padding: var(--nj-size-space-16);">
      <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
      <p>For a reduced motion sidebar, add the <code>.nj-sidebar--no-motion</code> modifier.</p>
    </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Sidebar id="sidebarExample" logo_src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" logosm_src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" logo_alt="ENGIE - back to home" logo_width="100px" logosm_width="auto" %}
  {% S_Menu current=True %}
    Dashboard

    {% Slot 'icon' %}{% Icon label='dashboard' %}{% endSlot %}
  {% endS_Menu %}
  {% S_Menu badge=7 %}
    Alerts

    {% Slot 'icon' %}{% Icon label='report_problem' %}{% endSlot %}
  {% endS_Menu %}
  {% S_Menu %}
    Signals

    {% Slot 'icon' %}{% Icon label='show_chart' %}{% endSlot %}
  {% endS_Menu %}
  {% S_Menu %}
    Simulation

    {% Slot 'icon' %}{% Icon label='online_prediction' %}{% endSlot %}
  {% endS_Menu %}
  {% S_Menu %}
    Events

    {% Slot 'icon' %}{% Icon label='event' %}{% endSlot %}
  {% endS_Menu %}

  {% Slot 'footer' %}
    {% S_Menu %}
      Settings

      {% Slot 'icon' %}{% Icon label="settings" %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu %}
      Profile

      {% Slot 'icon' %}{% Icon label="account_circle" %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu %}
      Logout

      {% Slot 'icon' %}{% Icon label="power_settings_new" %}{% endSlot %}
    {% endS_Menu %}
  {% endSlot %}
{% endSidebar %}
<div class="nj-sidebar-content" style="padding: var(--nj-size-space-16);">
  <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
</div>
"""
        expected = """
  <div class="nj-sidebar" id="sidebarExample" data-close-on-interact-out="true">
    <a class="nj-sidebar__brand" href="#" title="ENGIE - back to home">
      <img class="nj-sidebar__logo" src="https://design.digital.engie.com/assets/brand/logo-engie-blue.svg" alt="ENGIE - back to home" width="100px" height="">
      <img class="nj-sidebar__logo--folded" src="https://design.digital.engie.com/assets/brand/logo-engie-small-blue.svg" alt="ENGIE - back to home" width="auto" height="36">
    </a>

    <nav class="nj-sidebar__navigation">
      <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border active" aria-current="true">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">dashboard</span>
            <span class="nj-list-group__item-content">Dashboard</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">report_problem</span>
            <span class="nj-list-group__item-content">Alerts</span>
            <p class="nj-badge nj-list-group__item-right-content">7</p>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">show_chart</span>
            <span class="nj-list-group__item-content">Signals</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">online_prediction</span>
            <span class="nj-list-group__item-content">Simulation</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">event</span>
            <span class="nj-list-group__item-content">Events</span>
          </a>
        </li>
      </ul>
    </nav>

    <nav class="nj-sidebar__navigation nj-sidebar__navigation--footer">
      <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
        <div class="nj-sidebar__divider"></div>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">settings</span>
            <span class="nj-list-group__item-content">Settings</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">account_circle</span>
            <span class="nj-list-group__item-content">Profile</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">power_settings_new</span>
            <span class="nj-list-group__item-content">Logout</span>
          </a>
        </li>
      </ul>
    </nav>

    <ul class="nj-sidebar__collapse nj-list-group nj-list-group--sm nj-list-group--no-border">
      <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--no-border">
        <button data-toggle="sidebar" data-target="#sidebarExample" aria-pressed="false">
          <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-sidebar__fold-btn">chevron_left</span>
          <span class="nj-list-group__item-content">Close</span>
        </button>
      </li>
    </ul>
  </div>

  <div class="nj-sidebar-content" style="padding: var(--nj-size-space-16);">
    <h3>This div has the <code>.nj-sidebar-content</code> class. It's mandatory to have the right behavior with a fixed sidebar.</h3>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus amet debitis, esse est expedita harum magnam nesciunt nulla officia quam, quis quos soluta ut voluptas? Fugit libero minima perspiciatis.</p>
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
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

{% Sidebar id="sidebarExample" class="nj-sidebar--custom-height" %}
  {% S_Menu current=True %}
    Dashboard

    {% Slot 'icon' %}{% Icon label='dashboard' %}{% endSlot %}
  {% endS_Menu %}
  {% S_Menu badge=7 %}
    Alerts

    {% Slot 'icon' %}{% Icon label='report_problem' %}{% endSlot %}
  {% endS_Menu %}
  {% S_Menu %}
    Signals

    {% Slot 'icon' %}{% Icon label='show_chart' %}{% endSlot %}
  {% endS_Menu %}
  {% S_Menu %}
    Simulation

    {% Slot 'icon' %}{% Icon label='online_prediction' %}{% endSlot %}
  {% endS_Menu %}
  {% S_Menu %}
    Events

    {% Slot 'icon' %}{% Icon label='event' %}{% endSlot %}
  {% endS_Menu %}

  {% Slot 'footer' %}
    {% S_Menu %}
      Settings

      {% Slot 'icon' %}{% Icon label="settings" %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu %}
      Profile

      {% Slot 'icon' %}{% Icon label="account_circle" %}{% endSlot %}
    {% endS_Menu %}
    {% S_Menu %}
      Logout

      {% Slot 'icon' %}{% Icon label="power_settings_new" %}{% endSlot %}
    {% endS_Menu %}
  {% endSlot %}
{% endSidebar %}
<div class="nj-sidebar-content" style="padding: var(--nj-size-space-16); height: 2000px;">
  <!-- Your content goes here -->
</div>
"""
        expected = """
  <nav class="nj-navbar nj-navbar--shadow nj-navbar--expand-xl">
    <a class="nj-navbar__brand" href="#">
      <svg class="nj-navbar__logo" aria-label="home">
        <use href="/assets/brand/logo-engie.svg#logo-engie"/>
      </svg>
    </a>
    <button class="nj-navbar__toggler" type="button" data-toggle="collapse" data-target="#navbarExample">
      <span class="nj-navbar__toggler-icon material-icons">menu</span>
    </button>
    <div class="nj-navbar--collapse nj-collapse" id="navbarExample">
      <ul class="nj-navbar__nav">
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link active" href="#">Active nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link disabled" href="#">Disabled nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link" href="#">Nav item</a></li>
        <li class="nj-navbar__nav-item"><a class="nj-navbar__nav-link nj-navbar__nav-link--icon" href="#"><span
              aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--brand">network_check</span><span
              class="nj-sr-only">Nav item</span></a></li>
      </ul>
    </div>
  </nav>

  <div class="nj-sidebar nj-sidebar--custom-height" id="sidebarExample" data-close-on-interact-out="true">

    <nav class="nj-sidebar__navigation">
      <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border active" aria-current="true">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">dashboard</span>
            <span class="nj-list-group__item-content">Dashboard</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">report_problem</span>
            <span class="nj-list-group__item-content">Alerts</span>
            <p class="nj-badge nj-list-group__item-right-content">7</p>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">show_chart</span>
            <span class="nj-list-group__item-content">Signals</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">online_prediction</span>
            <span class="nj-list-group__item-content">Simulation</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">event</span>
            <span class="nj-list-group__item-content">Events</span>
          </a>
        </li>
      </ul>
    </nav>

    <nav class="nj-sidebar__navigation nj-sidebar__navigation--footer">
      <ul class="nj-list-group nj-list-group--sm nj-list-group--no-border nj-list-group--spaced-items">
        <div class="nj-sidebar__divider"></div>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">settings</span>
            <span class="nj-list-group__item-content">Settings</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">account_circle</span>
            <span class="nj-list-group__item-content">Profile</span>
          </a>
        </li>
        <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--right-border">
          <a href="#">
            <span aria-hidden="true" class="material-icons nj-icon-material nj-list-group__item-icon">power_settings_new</span>
            <span class="nj-list-group__item-content">Logout</span>
          </a>
        </li>
      </ul>
    </nav>

    <ul class="nj-sidebar__collapse nj-list-group nj-list-group--sm nj-list-group--no-border">
      <li class="nj-list-group__item nj-list-group__item--clickable nj-list-group__item--no-border">
        <button data-toggle="sidebar" data-target="#sidebarExample" aria-pressed="false">
          <span aria-hidden="true" class="material-icons nj-list-group__item-icon nj-sidebar__fold-btn">chevron_left</span>
          <span class="nj-list-group__item-content">Close</span>
        </button>
      </li>
    </ul>
  </div>

  <div class="nj-sidebar-content" style="padding: var(--nj-size-space-16); height: 2000px;">
    <!-- Your content goes here -->
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
