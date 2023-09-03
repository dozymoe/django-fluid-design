# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class SkeletonTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Skeleton %}{% endSkeleton %}
"""
        expected = """
<div class="nj-skeleton-container">
  <span class="nj-sr-only">Loading...</span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Skeleton style="max-width: 600px;" %}
  {% Bone shape="icon" %}
  <div style="display: flex; gap: 8px;">
    {% Bone shape="circle" %}
    {% Bone shape="rectangle" style="width: 260px;" %}
  </div>
  {% Bone shape="rectangle" height="hecto" style="max-width: 80%;" %}
  {% Bone shape="rectangle" height="base" %}
  {% Bone shape="rectangle" height="base" %}
  {% Bone shape="rectangle" height="base" %}
{% endSkeleton %}
<div aria-busy="true" style="display: none;">
  <p>Your content being loaded (should be hidden)</p>
</div>
"""
        expected = """
<div class="nj-skeleton-container" style="max-width: 600px;">
  <span class="nj-sr-only">Loading...</span>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--area">
    <span class="nj-skeleton__icon material-icons nj-icon-material nj-icon-material--tertiary nj-icon-material--xl">image</span>
  </div>
  <div style="display: flex; gap: 8px;">
    <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle"></div>
    <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle" style="width: 260px;"></div>
  </div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--hecto" style="max-width: 80%;"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--base"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--base"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--base"></div>
</div>
<div aria-busy="true" style="display: none;">
  <p>Your content being loaded (should be hidden)</p>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
<p>Available sizes: <code>"peta", "tera", "giga", "mega", "kilo", "hecto", "deca", "base", "deci", "centi"</code> or custom with <code>style="height: {wantedHeight}px;"</code></p>
{% Skeleton %}
  {% Bone shape="rectangle" %}
  {% Bone shape="rectangle" height="peta" %}
  {% Bone shape="rectangle" height="tera" %}
  {% Bone shape="rectangle" height="giga" %}
  {% Bone shape="rectangle" height="mega" %}
  {% Bone shape="rectangle" height="kilo" %}
  {% Bone shape="rectangle" height="hecto" %}
  {% Bone shape="rectangle" height="deca" %}
  {% Bone shape="rectangle" height="base" %}
  {% Bone shape="rectangle" height="deci" %}
  {% Bone shape="rectangle" height="centi" %}
  {% Bone shape="rectangle" style="height: 120px;" %}
{% endSkeleton %}
"""
        expected = """
<p>Available sizes: <code>"peta", "tera", "giga", "mega", "kilo", "hecto", "deca", "base", "deci", "centi"</code> or custom with <code>style="height: {wantedHeight}px;"</code></p>
<div class="nj-skeleton-container">
  <span class="nj-sr-only">Loading...</span>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--peta"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--tera"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--giga"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--mega"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--kilo"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--hecto"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--deca"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--base"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--deci"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--centi"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle" style="height: 120px;"></div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<p>Available sizes: <code>"sm", "base", "lg", "xl"</code> or custom with <code>style="height: {wantedHeight}px; width: {wantedWidth}px;"</code></p>
{% Skeleton %}
  {% Bone shape="circle" size="sm" %}
  {% Bone shape="circle" %}
  {% Bone shape="circle" size="lg" %}
  {% Bone shape="circle" size="xl" %}
  {% Bone shape="circle" style="height: 200px; width: 200px;" %}
{% endSkeleton %}
"""
        expected = """
<p>Available sizes: <code>"sm", "base", "lg", "xl"</code> or custom with <code>style="height: {wantedHeight}px; width: {wantedWidth}px;"</code></p>
<div class="nj-skeleton-container">
  <span class="nj-sr-only">Loading...</span>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle nj-skeleton--sm"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle nj-skeleton--lg"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle nj-skeleton--xl"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle" style="height: 200px; width: 200px;"></div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
<p>Customize it to your needs: height, width, svg - to give an insight of the type of content being loaded, ...</p>
{% Skeleton %}
  {% Bone shape="icon" %}
  {% Bone shape="svg" style="height: 400px; width: 600px;" %}
{% endSkeleton %}
"""
        expected = """
<p>Customize it to your needs: height, width, svg - to give an insight of the type of content being loaded, ...</p>
<div class="nj-skeleton-container">
  <span class="nj-sr-only">Loading...</span>

  <div aria-hidden="true" class="nj-skeleton nj-skeleton--area">
    <span class="nj-skeleton__icon material-icons nj-icon-material nj-icon-material--tertiary nj-icon-material--xl">image</span>
  </div>

  <div aria-hidden="true" class="nj-skeleton nj-skeleton--area" style="height: 400px; width: 600px;">
    <svg class="nj-skeleton__icon" width="48" height="48" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M36 32V4C36 1.8 34.2 0 32 0H4C1.8 0 0 1.8 0 4V32C0 34.2 1.8 36 4 36H32C34.2 36 36 34.2 36 32ZM11 21L16 27.02L23 18L32 30H4L11 21Z"
        fill="currentColor" />
    </svg>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% Skeleton style="max-width: 600px;" label="Content is loading." %}
  {% Bone shape="icon" %}
  <div style="display: flex; gap: 8px; align-items: center;">
    {% Bone shape="circle" size="lg" %}
    {% Bone shape="rectangle" height="giga" style="width: 260px;" %}
  </div>
    {% Bone shape="rectangle" height="hecto" style="max-width: 80%;" %}
    {% Bone shape="rectangle" height="base" %}
    {% Bone shape="rectangle" height="base" %}
    {% Bone shape="rectangle" height="base" %}
{% endSkeleton %}
  
<div aria-busy="true" style="display: none;">
  <!-- Your content being loaded goes here (hidden) -->
</div>
"""
        expected = """
<div class="nj-skeleton-container" style="max-width: 600px;">
  <span class="nj-sr-only">Content is loading.</span>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--area">
    <span class="nj-skeleton__icon material-icons nj-icon-material nj-icon-material--tertiary nj-icon-material--xl">image</span>
  </div>
  <div style="display: flex; gap: 8px; align-items: center;">
    <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle nj-skeleton--lg"></div>
    <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--giga" style="width: 260px;"></div>
  </div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--hecto" style="max-width: 80%;"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--base"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--base"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--base"></div>
</div>
  
<div aria-busy="true" style="display: none;">
  <!-- Your content being loaded goes here (hidden) -->
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Skeleton label="Content is loading." %}
  {% Bone shape="rectangle" %}
  {% Bone shape="rectangle" height="peta" %}
  {% Bone shape="rectangle" height="tera" %}
  {% Bone shape="rectangle" height="giga" %}
  {% Bone shape="rectangle" height="mega" %}
  {% Bone shape="rectangle" height="kilo" %}
  {% Bone shape="rectangle" height="hecto" %}
  {% Bone shape="rectangle" height="deca" %}
  {% Bone shape="rectangle" height="base" %}
  {% Bone shape="rectangle" height="deci" %}
  {% Bone shape="rectangle" height="centi" %}
  {% Bone shape="rectangle" style="height: 120px;" %}
{% endSkeleton %}
"""
        expected = """
<div class="nj-skeleton-container">
  <span class="nj-sr-only">Content is loading.</span>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--peta"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--tera"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--giga"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--mega"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--kilo"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--hecto"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--deca"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--base"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--deci"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle nj-skeleton--centi"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--rectangle" style="height: 120px;"></div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Skeleton label="Content is loading." %}
  {% Bone shape="circle" size="sm" %}
  {% Bone shape="circle" %}
  {% Bone shape="circle" size="lg" %}
  {% Bone shape="circle" size="xl" %}
  {% Bone shape="circle" style="height: 200px; width: 200px;" %}
{% endSkeleton %}
"""
        expected = """
<div class="nj-skeleton-container">
  <span class="nj-sr-only">Content is loading.</span>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle nj-skeleton--sm"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle nj-skeleton--lg"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle nj-skeleton--xl"></div>
  <div aria-hidden="true" class="nj-skeleton nj-skeleton--circle" style="height: 200px; width: 200px;"></div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Skeleton label="Content is loading" %}
  {% Bone shape="icon" %}
  {% Bone shape="svg" style="height: 400px; width: 600px;" %}
{% endSkeleton %}
"""
        expected = """
<div class="nj-skeleton-container">
  <span class="nj-sr-only">Content is loading</span>

  <div aria-hidden="true" class="nj-skeleton nj-skeleton--area">
    <span class="nj-skeleton__icon material-icons nj-icon-material nj-icon-material--tertiary nj-icon-material--xl">image</span>
  </div>

  <div aria-hidden="true" class="nj-skeleton nj-skeleton--area" style="height: 400px; width: 600px;">
    <svg class="nj-skeleton__icon" width="48" height="48" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M36 32V4C36 1.8 34.2 0 32 0H4C1.8 0 0 1.8 0 4V32C0 34.2 1.8 36 4 36H32C34.2 36 36 34.2 36 32ZM11 21L16 27.02L23 18L32 30H4L11 21Z"
        fill="currentColor" />
    </svg>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
