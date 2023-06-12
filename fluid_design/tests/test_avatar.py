# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class AvatarTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% AvatarList %}
  {% Avatar %}{% endAvatar %}
{% endAvatarList %}
"""
        expected = """
<div class="nj-avatar-list">
  <div class="nj-avatar nj-avatar--default-icon">
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; padding: 24px;">
  {% AvatarList %}
    {% Avatar size="sm" %}User profile{% endAvatar %}
    {% Avatar size="sm" %}User profile{% endAvatar %}
    {% Avatar size="sm" %}User profile{% endAvatar %}
    {% Avatar size="sm" %}User profile{% endAvatar %}
    {% AvatarMore count=4 size="sm" clickable=True %}
  {% endAvatarList %}
  {% AvatarList %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% AvatarMore count=4 clickable=True %}
  {% endAvatarList %}
  {% AvatarList %}
    {% Avatar size="lg" %}User profile{% endAvatar %}
    {% Avatar size="lg" %}User profile{% endAvatar %}
    {% Avatar size="lg" %}User profile{% endAvatar %}
    {% Avatar size="lg" %}User profile{% endAvatar %}
    {% AvatarMore count=4 size="lg" clickable=True %}
  {% endAvatarList %}
  {% AvatarList %}
    {% Avatar size="xl" %}User profile{% endAvatar %}
    {% Avatar size="xl" %}User profile{% endAvatar %}
    {% Avatar size="xl" %}User profile{% endAvatar %}
    {% Avatar size="xl" %}User profile{% endAvatar %}
    {% AvatarMore count=4 size="xl" clickable=True %}
  {% endAvatarList %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; padding: 24px;">
<div class="nj-avatar-list">
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
  </div>
  <button class="nj-avatar nj-avatar--remaining-count nj-avatar--sm nj-avatar--clickable">
    <span aria-hidden="true">+4</span>
    <span class="nj-sr-only">Show 4 more user profiles</span>
  </button>
</div>
<div class="nj-avatar-list">
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <button class="nj-avatar nj-avatar--remaining-count nj-avatar--clickable">
    <span aria-hidden="true">+4</span>
    <span class="nj-sr-only">Show 4 more user profiles</span>
  </button>
</div>
<div class="nj-avatar-list">
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
  </div>
  <button class="nj-avatar nj-avatar--remaining-count nj-avatar--lg nj-avatar--clickable">
    <span aria-hidden="true">+4</span>
    <span class="nj-sr-only">Show 4 more user profiles</span>
  </button>
</div>
<div class="nj-avatar-list">
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
  </div>
  <button class="nj-avatar nj-avatar--remaining-count nj-avatar--xl nj-avatar--clickable">
    <span aria-hidden="true">+4</span>
    <span class="nj-sr-only">Show 4 more user profiles</span>
  </button>
</div>
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; padding: 24px;">
  {% AvatarList variant="compact" %}
    {% Avatar size="sm" %}User profile{% endAvatar %}
    {% Avatar size="sm" %}User profile{% endAvatar %}
    {% Avatar size="sm" %}User profile{% endAvatar %}
    {% Avatar size="sm" %}User profile{% endAvatar %}
    {% AvatarMore count=4 size="sm" clickable=True %}
  {% endAvatarList %}
  {% AvatarList variant="compact" %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% AvatarMore count=4 clickable=True %}
  {% endAvatarList %}
  {% AvatarList variant="compact" %}
    {% Avatar size="lg" %}User profile{% endAvatar %}
    {% Avatar size="lg" %}User profile{% endAvatar %}
    {% Avatar size="lg" %}User profile{% endAvatar %}
    {% Avatar size="lg" %}User profile{% endAvatar %}
    {% AvatarMore count=4 size="lg" clickable=True %}
  {% endAvatarList %}
  {% AvatarList variant="compact" %}
    {% Avatar size="xl" %}User profile{% endAvatar %}
    {% Avatar size="xl" %}User profile{% endAvatar %}
    {% Avatar size="xl" %}User profile{% endAvatar %}
    {% Avatar size="xl" %}User profile{% endAvatar %}
    {% AvatarMore count=4 size="xl" clickable=True %}
  {% endAvatarList %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; padding: 24px;">
<div class="nj-avatar-list nj-avatar-list--compact">
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
  </div>
  <button class="nj-avatar nj-avatar--remaining-count nj-avatar--sm nj-avatar--clickable">
    <span aria-hidden="true">+4</span>
    <span class="nj-sr-only">Show 4 more user profiles</span>
  </button>
</div>
<div class="nj-avatar-list nj-avatar-list--compact">
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <button class="nj-avatar nj-avatar--remaining-count nj-avatar--clickable">
    <span aria-hidden="true">+4</span>
    <span class="nj-sr-only">Show 4 more user profiles</span>
  </button>
</div>
<div class="nj-avatar-list nj-avatar-list--compact">
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
  </div>
  <button class="nj-avatar nj-avatar--remaining-count nj-avatar--lg nj-avatar--clickable">
    <span aria-hidden="true">+4</span>
    <span class="nj-sr-only">Show 4 more user profiles</span>
  </button>
</div>
<div class="nj-avatar-list nj-avatar-list--compact">
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
  </div>
  <button class="nj-avatar nj-avatar--remaining-count nj-avatar--xl nj-avatar--clickable">
    <span aria-hidden="true">+4</span>
    <span class="nj-sr-only">Show 4 more user profiles</span>
  </button>
</div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  {% Avatar %}User profile{% endAvatar %}
  {% Avatar initial="NJ" %}Nicolas Jobs{% endAvatar %}
  {% Avatar src="/assets/img/customer.svg" alt="Customer" %}{% endAvatar %}
  {% AvatarMore count=4 %}
</div>
"""
        expected = """
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </div>
  <div class="nj-avatar nj-avatar--initials">
    <span class="nj-avatar__initials" aria-hidden="true">NJ</span>
    <span class="nj-sr-only">Nicolas Jobs</span>
  </div>
  <div class="nj-avatar">
    <img class="nj-avatar__picture" src="/assets/img/customer.svg" alt="Customer">
  </div>
  <div class="nj-avatar nj-avatar--remaining-count">
    +4
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  {% Avatar size="sm" initial="sm" %}Small avatar{% endAvatar %}
  {% Avatar initial="md" %}Medium avatar{% endAvatar %}
  {% Avatar size="lg" initial="lg" %}Large avatar{% endAvatar %}
  {% Avatar size="xl" initial="xl" %}Extra-large avatar{% endAvatar %}
</div>
"""
        expected = """
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
    <div class="nj-avatar nj-avatar--initials nj-avatar--sm">
      <span class="nj-avatar__initials" aria-hidden="true">sm</span>
      <span class="nj-sr-only">Small avatar</span>
    </div>

    <div class="nj-avatar nj-avatar--initials">
      <span class="nj-avatar__initials" aria-hidden="true">md</span>
      <span class="nj-sr-only">Medium avatar</span>
    </div>

    <div class="nj-avatar nj-avatar--initials nj-avatar--lg">
      <span class="nj-avatar__initials" aria-hidden="true">lg</span>
      <span class="nj-sr-only">Large avatar</span>
    </div>

    <div class="nj-avatar nj-avatar--initials nj-avatar--xl">
      <span class="nj-avatar__initials" aria-hidden="true">xl</span>
      <span class="nj-sr-only">Extra-large avatar</span>
    </div>
  </div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  {% Avatar astag="a" href="#" %}User profile{% endAvatar %}
  {% Avatar astag="a" href="#" initial="NJ" %}Nicolas Jobs{% endAvatar %}
  {% Avatar astag="a" href="#" src="/assets/img/customer.svg" alt="Customer" %}{% endAvatar %}
</div>
"""
        expected = """
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  <a href="#" class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
  </a>
  <a href="#" class="nj-avatar nj-avatar--initials">
    <span class="nj-avatar__initials" aria-hidden="true">NJ</span>
    <span class="nj-sr-only">Nicolas Jobs</span>
  </a>
  <a href="#" class="nj-avatar ">
    <img class="nj-avatar__picture" src="/assets/img/customer.svg" alt="Customer">
  </a>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  {% Avatar clickable=True %}User profile{% endAvatar %}
  {% Avatar initial="NJ" clickable=True %}Nicolas Jobs{% endAvatar %}
  {% Avatar src="/assets/img/customer.svg" alt="Customer" clickable=True %}{% endAvatar %}
</div>
"""
        expected = """
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  <button class="nj-avatar nj-avatar--default-icon nj-avatar--clickable">
    <span class="nj-sr-only">User profile</span>
  </button>
  <button class="nj-avatar nj-avatar--initials nj-avatar--clickable">
    <span class="nj-avatar__initials" aria-hidden="true">NJ</span>
    <span class="nj-sr-only">Nicolas Jobs</span>
  </button>
  <button class="nj-avatar nj-avatar--clickable">
    <img class="nj-avatar__picture" src="/assets/img/customer.svg" alt="Customer">
  </button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  {% Avatar initial="NJ" badge=25 size="sm" %}Nicolas John Doe{% endAvatar %}
  {% Avatar initial="NJ" badge=25 %}Nicolas John Doe{% endAvatar %}
  {% Avatar initial="NJ" badge=25 size="lg" %}Nicolas John Doe{% endAvatar %}
  {% Avatar initial="NJ" badge=25 size="xl" %}Nicolas John Doe{% endAvatar %}
</div>
"""
        expected = """
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  <div class="nj-avatar nj-avatar--initials nj-avatar--sm">
    <span class="nj-avatar__initials" aria-hidden="true">NJ</span>
    <span class="nj-sr-only">Nicolas John Doe</span>
  </div>

  <div class="nj-avatar nj-avatar--initials">
    <span class="nj-avatar__initials" aria-hidden="true">NJ</span>
    <span class="nj-sr-only">Nicolas John Doe</span>
    <div class="nj-badge nj-badge--information">
      <p>25 <span class="nj-sr-only">notifications</span></p>
    </div>
  </div>

  <div class="nj-avatar nj-avatar--initials nj-avatar--lg">
    <span class="nj-avatar__initials" aria-hidden="true">NJ</span>
    <span class="nj-sr-only">Nicolas John Doe</span>
    <div class="nj-badge nj-badge--information">
      <p>25 <span class="nj-sr-only">notifications</span></p>
    </div>
  </div>

  <div class="nj-avatar nj-avatar--initials nj-avatar--xl">
    <span class="nj-avatar__initials" aria-hidden="true">NJ</span>
    <span class="nj-sr-only">Nicolas John Doe</span>
    <div class="nj-badge nj-badge--information nj-badge--lg">
      <p>25 <span class="nj-sr-only">notifications</span></p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  {% Avatar status="offline" size="sm" %}User profile{% endAvatar %}
  {% Avatar status="away" %}User profile{% endAvatar %}
  {% Avatar status="busy" size="lg" %}User profile{% endAvatar %}
  {% Avatar status="online" size="xl" %}User profile{% endAvatar %}
</div>
"""
        expected = """
<div style="display: flex; flex-wrap: wrap; gap: 16px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  <div class="nj-avatar nj-avatar--default-icon nj-avatar--sm">
    <span class="nj-sr-only">User profile</span>
    <div class="nj-status-indicator nj-status-indicator--offline nj-status-indicator--sm">
      <div class="nj-status-indicator__svg">
        <span class="nj-sr-only">Offline</span>
      </div>
    </div>
  </div>

  <div class="nj-avatar nj-avatar--default-icon">
    <span class="nj-sr-only">User profile</span>
    <div class="nj-status-indicator nj-status-indicator--away nj-status-indicator--sm">
      <div class="nj-status-indicator__svg">
        <span class="nj-sr-only">Away</span>
      </div>
    </div>
  </div>

  <div class="nj-avatar nj-avatar--default-icon nj-avatar--lg">
    <span class="nj-sr-only">User profile</span>
    <div class="nj-status-indicator nj-status-indicator--in-progress">
      <div class="nj-status-indicator__svg">
        <span class="nj-sr-only">In progress</span>
      </div>
    </div>
  </div>

  <div class="nj-avatar nj-avatar--default-icon nj-avatar--xl">
    <span class="nj-sr-only">User profile</span>
    <div class="nj-status-indicator nj-status-indicator--online nj-status-indicator--lg">
      <div class="nj-status-indicator__svg">
        <span class="nj-sr-only">Online</span>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  {% AvatarList %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% AvatarMore count=4 clickable=True %}
  {% endAvatarList %}
  {% AvatarList variant="compact" %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% Avatar %}User profile{% endAvatar %}
    {% AvatarMore count=4 clickable=True %}
  {% endAvatarList %}
</div>
"""
        expected = """
<div style="display: flex; flex-direction: column; gap: 24px; background-color: var(--nj-color-background-secondary); padding: 24px;">
  <div class="nj-avatar-list">
    <div class="nj-avatar nj-avatar--default-icon">
      <span class="nj-sr-only">User profile</span>
    </div>
    <div class="nj-avatar nj-avatar--default-icon">
      <span class="nj-sr-only">User profile</span>
    </div>
    <div class="nj-avatar nj-avatar--default-icon">
      <span class="nj-sr-only">User profile</span>
    </div>
    <div class="nj-avatar nj-avatar--default-icon">
      <span class="nj-sr-only">User profile</span>
    </div>
    <button class="nj-avatar nj-avatar--remaining-count nj-avatar--clickable">
      <span aria-hidden="true">+4</span>
      <span class="nj-sr-only">Show 4 more user profiles</span>
    </button>
  </div>

  <div class="nj-avatar-list nj-avatar-list--compact">
    <div class="nj-avatar nj-avatar--default-icon">
      <span class="nj-sr-only">User profile</span>
    </div>
    <div class="nj-avatar nj-avatar--default-icon">
      <span class="nj-sr-only">User profile</span>
    </div>
    <div class="nj-avatar nj-avatar--default-icon">
      <span class="nj-sr-only">User profile</span>
    </div>
    <div class="nj-avatar nj-avatar--default-icon">
      <span class="nj-sr-only">User profile</span>
    </div>
    <button class="nj-avatar nj-avatar--remaining-count nj-avatar--clickable">
      <span aria-hidden="true">+4</span>
      <span class="nj-sr-only">Show 4 more user profiles</span>
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
