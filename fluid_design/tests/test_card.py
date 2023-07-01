# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class CardTest(SimpleTestCase):
    maxDiff = None

    def test_vanilla(self):
        template = """
{% load fluid_design %}
{% Card %}{% endCard %}
"""
        expected = """
<div class="nj-card">
  <div class="nj-card__body">
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example1(self):
        template = """
{% load fluid_design %}
{% Card class="mb-3" %}
  {% Slot 'title' astag="h4" %}
    Card title
  {% endSlot %}

  <p>Some quick example text to build on the card title and make up the bulk of
  the card's content.</p>
  <button class="nj-btn nj-btn--sm">Button</button>
{% endCard %}
{% Card class="mb-3" %}
  {% Slot 'title' %}
    Indicator
  {% endSlot %}
  {% Slot 'number' class="mt-5 mb-1" %}7,234,000{% endSlot %}
  {% Slot 'growth' %}
    <span arian-hidden="true" class="material-icons nj-icon-material nj-icon-material--green mr-1">check_circle</span>
    <span class="nj-sr-only">positive evolution</span> 1,6%
  {% endSlot %}
{% endCard %}
"""
        expected = """
<div class="nj-card mb-3">
  <div class="nj-card__body">
    <h4 class="nj-card__title">Card title</h4>
    <p>Some quick example text to build on the card title and make up the bulk of
  the card's content.</p>

    <button class="nj-btn nj-btn--sm">Button</button>
  </div>
</div>

<div class="nj-card mb-3">
  <div class="nj-card__body">
    <h4 class="nj-card__title">Indicator</h4>
    <p class="nj-card__number mt-5 mb-1">7,234,000</p>
    <p class="nj-card__growth">
      <span arian-hidden="true" class="material-icons nj-icon-material nj-icon-material--green mr-1">check_circle</span>
      <span class="nj-sr-only">positive evolution</span>
      1,6%
    </p>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example2(self):
        template = """
{% load fluid_design %}
{% Grid %}
  {% Row %}
    {% Col md=4 %}
      {% Card class="mb-3" %}
        {% Slot 'title' %}Card title{% endSlot %}

        <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>

        {% Slot 'details' %}
          Category <span aria-hidden="true">|</span> Date
          <span aria-hidden="true">|</span> Author
        {% endSlot %}

        {% Slot 'image' %}
          {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col md=4 %}
      {% Card class="mb-3" border=True %}
        {% Slot 'title' %}Card title{% endSlot %}

        <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>

        {% Slot 'date' %}Updated 24/01/2017{% endSlot %}

        {% Slot 'image' %}
          {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col md=4 %}
      {% Card class="mb-3" %}
        {% Slot 'title' %}Card title{% endSlot %}

        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque
        autem, consequuntur dolorum eius, expedita illo minus molestias natus
        pariatur perferendis, sed tenetur! Cumque magnam qui quis, sequi
        similique suscipit voluptas.</p>

        <div class="mb-2">
          {% Tag color="brand" %}#p{% endTag %}
          {% Tag color="green" %}#p{% endTag %}
          {% Tag color="pink" %}#p{% endTag %}
        </div>
        {% Button size="sm" %}Small button{% endButton%}

        {% Slot 'image' %}
          {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
        {% endSlot %}
      {% endCard %}
    {% endCol %}
  {% endRow %}
{% endGrid %}
"""
        expected = """
<div class="container">
  <div class="row">
    <div class="col-md-4">
      <div class="nj-card mb-3">
        <div class="nj-card__img-wrapper">
            <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
        </div>
        <div class="nj-card__body">
          <p class="nj-card__details">Category <span aria-hidden="true">|</span> Date <span aria-hidden="true">|</span> Author</p>
          <h4 class="nj-card__title">Card title</h4>
          <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="nj-card mb-3 nj-card--border">
        <div class="nj-card__img-wrapper">
            <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
        </div>
        <div class="nj-card__body">
          <h4 class="nj-card__title">Card title</h4>
          <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>
          <p class="nj-card__date">Updated 24/01/2017</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="nj-card mb-3">
        <div class="nj-card__img-wrapper">
            <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
        </div>
        <div class="nj-card__body">
          <h4 class="nj-card__title">Card title</h4>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque
        autem, consequuntur dolorum eius, expedita illo minus molestias natus
        pariatur perferendis, sed tenetur! Cumque magnam qui quis, sequi
        similique suscipit voluptas.</p>
          <div class="mb-2">
            <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">#p</span></div>
            <div class="nj-tag nj-tag--green"><span class="nj-tag__text">#p</span></div>
            <div class="nj-tag nj-tag--pink"><span class="nj-tag__text">#p</span></div>
          </div>
          <button class="nj-btn nj-btn--sm">Small button</button>
        </div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example3(self):
        template = """
{% load fluid_design %}
<div class="mb-4">
  {% Card variant="horizontal" %}
    <div class="mb-2">
      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
    </div>

    {% Slot 'subtitle' %}
      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    {% endSlot %}

    {% Slot 'date' %}15/04/2020{% endSlot %}

    {% Slot 'image' %}
      {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
    {% endSlot %}
  {% endCard %}
</div>
<div class="mb-4">
  {% Card astag="a" href="#" variant="horizontal" %}
    <div class="mb-2">
      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
    </div>

    {% Slot 'subtitle' %}
      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    {% endSlot %}

    {% Slot 'date' %}15/04/2020{% endSlot %}

    {% Slot 'image' %}
      {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
    {% endSlot %}
  {% endCard %}
</div>
"""
        expected = """
<div class="mb-4">
  <div class="nj-card nj-card--horizontal">
      <div class="nj-card__img-wrapper">
        <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
    </div>
    <div class="nj-card__body">
      <div class="mb-2">
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
      </div>
      <h4 class="nj-card__subtitle">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</h4>
      <p class="nj-card__date">15/04/2020</p>
    </div>
  </div>
</div>
<div class="mb-4">
  <a href="#" class="nj-card nj-card--horizontal">
      <div class="nj-card__img-wrapper">
       <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
    </div>
    <div class="nj-card__body">
      <div class="mb-2">
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
      </div>
      <h4 class="nj-card__subtitle">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</h4>
      <p class="nj-card__date">15/04/2020</p>
    </div>
  </a>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example4(self):
        template = """
{% load fluid_design %}
{% Grid %}
  {% Row %}
    {% Col col=12 md=6 lg=3 class="p-2" %}
      {% Card mode="cover" href="#" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);" %}
        {% Slot 'title' %}Villes et collectivités{% endSlot %}
        {% Slot 'description' %}
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Lorem ipsum
          dolor sit amet, consectetur adipisicing elit.
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col col=12 md=6 lg=3 class="p-2" %}
      {% Card mode="cover" href="#" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);" %}
        {% Slot 'title' %}Villes et collectivités{% endSlot %}
        {% Slot 'description' %}
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col col=12 md=6 lg=3 class="p-2" %}
      {% Card mode="cover" href="#" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);" %}
        {% Slot 'title' %}Villes et collectivités{% endSlot %}
        {% Slot 'description' %}
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col col=12 md=6 lg=3 class="p-2" %}
      {% Card mode="cover" href="#" style="background-image:url(https://www.engie.com/sites/default/files/assets/images/2019-11/page_client_particuliers.jpg);" %}
        {% Slot 'title' %}Particuliers{% endSlot %}
        {% Slot 'description' %}
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        {% endSlot %}
      {% endCard %}
    {% endCol %}
  {% endRow %}
{% endGrid %}
"""
        expected = """
<div class="container">
  <div class="row">
    <div class="p-2 col-12 col-md-6 col-lg-3">
      <a href="#" class="nj-card nj-card--cover" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);">
        <div class="nj-card__body">
            <div class="nj-card__overlay">
                <h4 class="nj-card__title">Villes et collectivités</h4>
                <span class="material-icons" aria-hidden="true">arrow_forward</span>
                <p class="nj-card__description">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Lorem ipsum
          dolor sit amet, consectetur adipisicing elit.</p>
            </div>
        </div>
      </a>
    </div>
    <div class="p-2 col-12 col-md-6 col-lg-3">
      <a href="#" class="nj-card nj-card--cover" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);">
        <div class="nj-card__body">
            <div class="nj-card__overlay">
                <h4 class="nj-card__title">Villes et collectivités</h4>
                <span class="material-icons" aria-hidden="true">arrow_forward</span>
                <p class="nj-card__description">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
            </div>
        </div>
      </a>
    </div>
    <div class="p-2 col-12 col-md-6 col-lg-3">
      <a href="#" class="nj-card nj-card--cover" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);">
        <div class="nj-card__body">
            <div class="nj-card__overlay">
                <h4 class="nj-card__title">Villes et collectivités</h4>
                <span class="material-icons" aria-hidden="true">arrow_forward</span>
                <p class="nj-card__description">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
            </div>
        </div>
      </a>
    </div>
    <div class="p-2 col-12 col-md-6 col-lg-3">
      <a href="#" class="nj-card nj-card--cover" style="background-image:url(https://www.engie.com/sites/default/files/assets/images/2019-11/page_client_particuliers.jpg);">
        <div class="nj-card__body">
            <div class="nj-card__overlay">
                <h4 class="nj-card__title">Particuliers</h4>
                <span class="material-icons" aria-hidden="true">arrow_forward</span>
                <p class="nj-card__description">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
            </div>
        </div>
      </a>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example5(self):
        template = """
{% load fluid_design %}
{% CardList variant="deck" %}
  {% Card %}
    {% Slot 'title' %}Card title{% endSlot %}

    <p>This is a longer card with supporting text below as a natural lead-in to
    additional content. This content is a little bit longer.</p>

    <p><small class="text-muted">Last updated 3 mins ago</small></p>

    {% Slot 'image' %}
      {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
    {% endSlot %}
  {% endCard %}

  {% Card %}
    {% Slot 'title' %}Card title{% endSlot %}

    <p>This card has supporting text below as a natural lead-in to additional
    content.</p>

    <p><small class="text-muted">Last updated 3 mins ago</small></p>

    {% Slot 'image' %}
      {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
    {% endSlot %}
  {% endCard %}

  {% Card %}
    {% Slot 'title' %}Card title{% endSlot %}

    <p>This is a wider card with supporting text below as a natural lead-in to
    additional content. This card has even longer content than the first to show
    that equal height action.</p>

    <p><small class="text-muted">Last updated 3 mins ago</small></p>

    {% Slot 'image' %}
      {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
    {% endSlot %}
  {% endCard %}
{% endCardList %}
"""
        expected = """
<div class="nj-card-deck">
  <div class="nj-card">
    <div class="nj-card__img-wrapper">
      <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="">
    </div>
    <div class="nj-card__body">
      <h4 class="nj-card__title">Card title</h4>
      <p>This is a longer card with supporting text below as a natural lead-in to
    additional content. This content is a little bit longer.</p>
      <p><small class="text-muted">Last updated 3 mins ago</small></p>
    </div>
  </div>
  <div class="nj-card">
    <div class="nj-card__img-wrapper">
      <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="">
    </div>
    <div class="nj-card__body">
      <h4 class="nj-card__title">Card title</h4>
      <p>This card has supporting text below as a natural lead-in to additional
    content.</p>
      <p><small class="text-muted">Last updated 3 mins ago</small></p>
    </div>
  </div>
  <div class="nj-card">
    <div class="nj-card__img-wrapper">
      <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="">
    </div>
    <div class="nj-card__body">
      <h4 class="nj-card__title">Card title</h4>
      <p>This is a wider card with supporting text below as a natural lead-in to
    additional content. This card has even longer content than the first to show
    that equal height action.</p>
      <p><small class="text-muted">Last updated 3 mins ago</small></p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example6(self):
        template = """
{% load fluid_design %}
{% Grid %}
  {% CardList variant="columns" %}
    {% Card %}
      {% Slot 'title' %}1 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}2 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}3 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}4 - Card title{% endSlot %}

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis, sed tenetur! Cumque magnam qui quis, sequi similique
      suscipit voluptas.</p>

      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="purple" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="orange" %}tag{% endTag %}

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}5 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}5 Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}6 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}7 - Card title{% endSlot %}

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis, sed tenetur! Cumque magnam qui quis, sequi similique
      suscipit voluptas.</p>

      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="purple" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="orange" %}tag{% endTag %}

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}8 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}9 - Card title{% endSlot %}

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad
      aspernatur dolorum earum harum, hic illum ipsa molestias nam odit quis
      quo quos repellat, repudiandae similique soluta veniam veritatis vero
      voluptatum!</p>

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aspernatur
      dolorum earum harum, hic illum ipsa molestias nam odit quis quo quos
      repellat, repudiandae similique soluta veniam veritatis vero
      voluptatum!</p>

      {% Button size="sm" %}Button{% endButton %}
      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}10 - Card title{% endSlot %}

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis.</p>

      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="purple" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="orange" %}tag{% endTag %}

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="" %}
      {% endSlot %}
    {% endCard %}
  {% endCardList %}
{% endGrid %}
"""
        expected = """
<div class="container">
  <div class="nj-card-columns">
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">1 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">2 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">3 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">4 - Card title</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis, sed tenetur! Cumque magnam qui quis, sequi similique
      suscipit voluptas.</p>
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
        <a href="#" class="nj-tag nj-tag--purple"><span class="nj-tag__text">tag</span></a>
        <a href="#" class="nj-tag nj-tag--orange"><span class="nj-tag__text">tag</span></a>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">5 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">5 Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">6 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">7 - Card title</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis, sed tenetur! Cumque magnam qui quis, sequi similique
      suscipit voluptas.</p>
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
        <a href="#" class="nj-tag nj-tag--purple"><span class="nj-tag__text">tag</span></a>
        <a href="#" class="nj-tag nj-tag--orange"><span class="nj-tag__text">tag</span></a>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">8 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">9 - Card title</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad
      aspernatur dolorum earum harum, hic illum ipsa molestias nam odit quis
      quo quos repellat, repudiandae similique soluta veniam veritatis vero
      voluptatum!</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aspernatur
      dolorum earum harum, hic illum ipsa molestias nam odit quis quo quos
      repellat, repudiandae similique soluta veniam veritatis vero
      voluptatum!</p>
        <button class="nj-btn nj-btn--sm">Button</button>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt=""/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">10 - Card title</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis.</p>
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
        <a href="#" class="nj-tag nj-tag--purple"><span class="nj-tag__text">tag</span></a>
        <a href="#" class="nj-tag nj-tag--orange"><span class="nj-tag__text">tag</span></a>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example7(self):
        template = """
{% load fluid_design %}
{% Grid %}
  {% Row %}
    {% Col md=4 %}
      {% Card class="mb-3" align="center" %}
        {% Slot 'title' %}Card title{% endSlot %}

        <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>

        <button class="nj-btn nj-btn--sm">See profile</button>

        {% Slot 'header' %}
          {% Avatar mode="minimal" size="lg" src="https://design.engie.com/assets/img/customer.svg" alt="Woman" %}
          {% endAvatar %}
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col md=4 %}
      {% Card class="mb-3" align="center" %}
        {% Slot 'header' %}PRO{% endSlot %}

        {% Slot 'price' %}{% endSlot %}

        <ul class="list-unstyled">
          <li>20 users included</li>
          <li>10 of storage</li>
          <li>Priority email support</li>
          <li>Help center access</li>
        </ul>
        <div style="display: flex; flex-direction: column; align-items: center">
          <button class="nj-btn mb-2">Sign for free</button>
          <a href="#" class="nj-link">Offer details</a>
        </div>
      {% endCard %}
    {% endCol %}
  {% endRow %}
{% endGrid %}
"""
        expected = """
<div class="container">
  <div class="row">
    <div class="col-md-4">
      <div class="nj-card mb-3">
        <div class="nj-card__header">
          <div class="nj-avatar nj-avatar--lg">
            <div class="nj-avatar__picture"><img src="https://design.engie.com/assets/img/customer.svg" alt="Woman"></div>
          </div>
        </div>
        <div class="nj-card__body text-center">
          <h4 class="nj-card__title">Card title</h4>
          <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>
          <button class="nj-btn nj-btn--sm">See profile</button>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="nj-card mb-3">
        <div class="nj-card__header">
          PRO
        </div>
        <div class="nj-card__body text-center">
          <div class="nj-card__price"></div>
          <ul class="list-unstyled">
            <li>20 users included</li>
            <li>10 of storage</li>
            <li>Priority email support</li>
            <li>Help center access</li>
          </ul>
          <div style="display: flex; flex-direction: column; align-items: center">
            <button class="nj-btn mb-2">Sign for free</button>
            <a href="#" class="nj-link">Offer details</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example8(self):
        template = """
{% load fluid_design %}
{% Card class="mb-3" %}
  {% Slot 'title' astag="h4" %}
    Card title
  {% endSlot %}

  <p>Some quick example text to build on the card title and make up the bulk of
  the card's content.</p>
  <button class="nj-btn nj-btn--sm">Button</button>
{% endCard %}
{% Card class="mb-3" %}
  <strong>Indicator</strong>
  {% Slot 'number' class="mt-5 mb-1" %}7,234,000{% endSlot %}
  {% Slot 'growth' style="gap: var(--nj-size-space-4);" %}
    <span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--green">check_circle</span>
    1,6%
  {% endSlot %}
{% endCard %}
"""
        expected = """
<div class="nj-card mb-3">
  <div class="nj-card__body">
    <h4 class="nj-card__title">Card title</h4>
    <p>Some quick example text to build on the card title and make up the bulk of
  the card's content.</p>
    <button class="nj-btn nj-btn--sm">Button</button>
  </div>
</div>

<div class="nj-card mb-3">
  <div class="nj-card__body">
    <strong>Indicator</strong>
    <p class="nj-card__number mt-5 mb-1">7,234,000</p>
    <p class="nj-card__growth" style="gap: var(--nj-size-space-4);"><span aria-hidden="true" class="material-icons nj-icon-material nj-icon-material--green">check_circle</span> 1,6%</p>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example9(self):
        template = """
{% load fluid_design %}
{% Grid %}
  {% Row %}
    {% Col md=6 lg=4 %}
      {% Card class="mb-3" %}
        {% Slot 'title' %}Card title{% endSlot %}

        <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>

        {% Slot 'details' %}
          <span class="text-blue-corporate">Category</span>
          | Date | Author
        {% endSlot %}

        {% Slot 'image' %}
          {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col md=6 lg=4 %}
      {% Card class="mb-3" border=True %}
        {% Slot 'title' %}Card title{% endSlot %}

        <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>

        {% Slot 'date' %}Updated 24/01/2017{% endSlot %}

        {% Slot 'image' %}
          {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col md=6 lg=4 %}
      {% Card class="mb-3" %}
        {% Slot 'title' %}Card title{% endSlot %}

        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque
        autem, consequuntur dolorum eius, expedita illo minus molestias natus
        pariatur perferendis, sed tenetur! Cumque magnam qui quis, sequi
        similique suscipit voluptas.</p>

        <div class="mb-2">
          {% Tag color="brand" %}#tag{% endTag %}
          {% Tag color="green" %}#tag{% endTag %}
          {% Tag color="pink" %}#tag{% endTag %}
        </div>
        {% Button size="sm" %}Small button{% endButton%}

        {% Slot 'image' %}
          {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
        {% endSlot %}
      {% endCard %}
    {% endCol %}
  {% endRow %}
{% endGrid %}
"""
        expected = """
<div class="container">
  <div class="row">
    <div class="col-md-6 col-lg-4">
      <div class="nj-card mb-3">
        <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
        </div>
        <div class="nj-card__body">
          <p class="nj-card__details"><span class="text-blue-corporate">Category</span> | Date | Author</p>
          <h4 class="nj-card__title">Card title</h4>
          <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>
        </div>
      </div>
    </div>
    <div class="col-md-6 col-lg-4">
      <div class="nj-card mb-3 nj-card--border">
        <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
        </div>
        <div class="nj-card__body">
          <h4 class="nj-card__title">Card title</h4>
          <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>
          <p class="nj-card__date">Updated 24/01/2017</p>
        </div>
      </div>
    </div>
    <div class="col-md-6 col-lg-4">
      <div class="nj-card mb-3">
        <div class="nj-card__img-wrapper">
          <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
        </div>
        <div class="nj-card__body">
          <h4 class="nj-card__title">Card title</h4>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque
        autem, consequuntur dolorum eius, expedita illo minus molestias natus
        pariatur perferendis, sed tenetur! Cumque magnam qui quis, sequi
        similique suscipit voluptas.</p>
          <div class="mb-2">
            <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">#tag</span></div>
            <div class="nj-tag nj-tag--green"><span class="nj-tag__text">#tag</span></div>
            <div class="nj-tag nj-tag--pink"><span class="nj-tag__text">#tag</span></div>
          </div>
          <button class="nj-btn nj-btn--sm">Small button</button>
        </div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example10(self):
        template = """
{% load fluid_design %}
<div class="mb-4">
  {% Card variant="horizontal" %}
    <div class="mb-2">
      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
    </div>

    {% Slot 'subtitle' %}
      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    {% endSlot %}

    {% Slot 'date' %}15/04/2020{% endSlot %}

    {% Slot 'image' %}
      {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
    {% endSlot %}
  {% endCard %}
</div>
<div class="mb-4">
  {% Card astag="a" href="#" variant="horizontal" %}
    <div class="mb-2">
      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
    </div>

    {% Slot 'subtitle' %}
      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    {% endSlot %}

    {% Slot 'date' %}15/04/2020{% endSlot %}

    {% Slot 'image' %}
      {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
    {% endSlot %}
  {% endCard %}
</div>
"""
        expected = """
<div class="mb-4">
  <div class="nj-card nj-card--horizontal">
    <div class="nj-card__img-wrapper">
      <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
    </div>
    <div class="nj-card__body">
      <div class="mb-2">
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
      </div>
      <h4 class="nj-card__subtitle">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</h4>
      <p class="nj-card__date">15/04/2020</p>
    </div>
  </div>
</div>
<div class="mb-4">
  <a href="#" class="nj-card nj-card--horizontal">
    <div class="nj-card__img-wrapper">
      <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
    </div>
    <div class="nj-card__body">
      <div class="mb-2">
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
      </div>
      <h4 class="nj-card__subtitle">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</h4>
      <p class="nj-card__date">15/04/2020</p>
    </div>
  </a>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example11(self):
        template = """
{% load fluid_design %}
{% Grid %}
  {% Row %}
    {% Col lg=4 class="p-2" %}
      {% Card mode="cover" href="" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);" %}
        {% Slot 'title' %}Villes et collectivités{% endSlot %}
        {% Slot 'description' %}
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Lorem ipsum
          dolor sit amet, consectetur adipisicing elit.
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col lg=4 class="p-2" %}
      {% Card mode="cover" href="#" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);" %}
        {% Slot 'title' %}Villes et collectivités{% endSlot %}
        {% Slot 'description' %}
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col lg=4 class="p-2" %}
      {% Card mode="cover" href="#" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);" %}
        {% Slot 'title' %}Villes et collectivités{% endSlot %}
        {% Slot 'description' %}
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col lg=4 class="p-2" %}
      {% Card mode="cover" href="#" style="background-image:url(https://www.engie.com/sites/default/files/assets/images/2019-11/page_client_particuliers.jpg);" %}
        {% Slot 'title' %}Particuliers{% endSlot %}
        {% Slot 'description' %}
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        {% endSlot %}
      {% endCard %}
    {% endCol %}
  {% endRow %}
{% endGrid %}
"""
        expected = """
<div class="container">
  <div class="row">
    <div class="p-2 col-lg-4">
      <a href="" class="nj-card nj-card--cover" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);">
        <div class="nj-card__body">
            <div class="nj-card__overlay">
                <h4 class="nj-card__title">Villes et collectivités</h4>
                <span aria-hidden="true" class="material-icons">arrow_forward</span>
                <p class="nj-card__description">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Lorem ipsum
          dolor sit amet, consectetur adipisicing elit.</p>
            </div>
        </div>
      </a>
    </div>
    <div class="p-2 col-lg-4">
      <a href="#" class="nj-card nj-card--cover" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);">
        <div class="nj-card__body">
            <div class="nj-card__overlay">
                <h4 class="nj-card__title">Villes et collectivités</h4>
                <span aria-hidden="true" class="material-icons">arrow_forward</span>
                <p class="nj-card__description">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
            </div>
        </div>
      </a>
    </div>
    <div class="p-2 col-lg-4">
      <a href="#" class="nj-card nj-card--cover" style="background-image:url(https://assets.design.digital.engie.com/image/bg-harmonyproject.jpg);">
        <div class="nj-card__body">
            <div class="nj-card__overlay">
                <h4 class="nj-card__title">Villes et collectivités</h4>
                <span aria-hidden="true" class="material-icons">arrow_forward</span>
                <p class="nj-card__description">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
            </div>
        </div>
      </a>
    </div>
    <div class="p-2 col-lg-4">
      <a href="#" class="nj-card nj-card--cover" style="background-image:url(https://www.engie.com/sites/default/files/assets/images/2019-11/page_client_particuliers.jpg);">
        <div class="nj-card__body">
            <div class="nj-card__overlay">
                <h4 class="nj-card__title">Particuliers</h4>
                <span aria-hidden="true" class="material-icons">arrow_forward</span>
                <p class="nj-card__description">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
            </div>
        </div>
      </a>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example12(self):
        template = """
{% load fluid_design %}
{% Grid %}
  {% Row %}
    {% Col lg=6 %}
      {% Card class="mb-3" align="center" %}
        {% Slot 'title' %}Card title{% endSlot %}

        <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>

        <button class="nj-btn nj-btn--sm">See profile</button>

        {% Slot 'header' %}
          {% Avatar mode="minimal" size="lg" src="https://design.engie.com/assets/img/customer.svg" alt="Woman" %}
          {% endAvatar %}
        {% endSlot %}
      {% endCard %}
    {% endCol %}
    {% Col lg=6 %}
      {% Card class="mb-3" align="center" %}
        {% Slot 'header' %}PRO{% endSlot %}

        {% Slot 'price' %}{% endSlot %}

        <ul class="list-unstyled">
          <li>20 users included</li>
          <li>10 of storage</li>
          <li>Priority email support</li>
          <li>Help center access</li>
        </ul>
        <div style="display: flex; flex-direction: column; align-items: center">
          <button class="nj-btn mb-2">Sign for free</button>
          <a href="#" class="nj-link">Offer details</a>
        </div>
      {% endCard %}
    {% endCol %}
  {% endRow %}
{% endGrid %}
"""
        expected = """
<div class="container">
  <div class="row">
    <div class="col-lg-6">
      <div class="nj-card mb-3">
        <div class="nj-card__header">
          <div class="nj-avatar nj-avatar--lg">
            <div class="nj-avatar__picture"><img src="https://design.engie.com/assets/img/customer.svg" alt="Woman"></div>
          </div>
        </div>
        <div class="nj-card__body text-center">
          <h4 class="nj-card__title">Card title</h4>
          <p>Some quick example text to build on the card title and make up the
        bulk of the card's content.</p>
          <button class="nj-btn nj-btn--sm">See profile</button>
        </div>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="nj-card mb-3">
        <div class="nj-card__header">
          PRO
        </div>
        <div class="nj-card__body text-center">
          <div class="nj-card__price"></div>
          <ul class="list-unstyled">
            <li>20 users included</li>
            <li>10 of storage</li>
            <li>Priority email support</li>
            <li>Help center access</li>
          </ul>
          <div style="display: flex; flex-direction: column; align-items: center">
            <button class="nj-btn mb-2">Sign for free</button>
            <a href="#" class="nj-link">Offer details</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_example13(self):
        template = """
{% load fluid_design %}
{% Grid %}
  {% CardList variant="columns" %}
    {% Card %}
      {% Slot 'title' %}1 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}2 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}3 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}4 - Card title{% endSlot %}

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis, sed tenetur! Cumque magnam qui quis, sequi similique
      suscipit voluptas.</p>

      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="purple" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="orange" %}tag{% endTag %}

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}5 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}5 Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}6 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}7 - Card title{% endSlot %}

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis, sed tenetur! Cumque magnam qui quis, sequi similique
      suscipit voluptas.</p>

      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="purple" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="orange" %}tag{% endTag %}

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
      {% endSlot %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}8 - Card title{% endSlot %}

      <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>

      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}9 - Card title{% endSlot %}

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad
      aspernatur dolorum earum harum, hic illum ipsa molestias nam odit quis
      quo quos repellat, repudiandae similique soluta veniam veritatis vero
      voluptatum!</p>

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aspernatur
      dolorum earum harum, hic illum ipsa molestias nam odit quis quo quos
      repellat, repudiandae similique soluta veniam veritatis vero
      voluptatum!</p>

      {% Button size="sm" %}Button{% endButton %}
      {% Button size="sm" %}Button{% endButton %}
    {% endCard %}

    {% Card %}
      {% Slot 'title' %}10 - Card title{% endSlot %}

      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis.</p>

      {% Tag color="brand" %}tag{% endTag %}
      {% Tag color="green" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="purple" %}tag{% endTag %}
      {% Tag mode="anchor" href="#" color="orange" %}tag{% endTag %}

      {% Slot 'image' %}
        {% CardImage src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap" %}
      {% endSlot %}
    {% endCard %}
  {% endCardList %}
{% endGrid %}
"""
        expected = """
<div class="container">
  <div class="nj-card-columns">
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
        <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">1 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">2 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">3 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
        <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">4 - Card title</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis, sed tenetur! Cumque magnam qui quis, sequi similique
      suscipit voluptas.</p>
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
        <a href="#" class="nj-tag nj-tag--purple"><span class="nj-tag__text">tag</span></a>
        <a href="#" class="nj-tag nj-tag--orange"><span class="nj-tag__text">tag</span></a>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
        <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">5 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
        <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">5 Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">6 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
        <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">7 - Card title</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis, sed tenetur! Cumque magnam qui quis, sequi similique
      suscipit voluptas.</p>
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
        <a href="#" class="nj-tag nj-tag--purple"><span class="nj-tag__text">tag</span></a>
        <a href="#" class="nj-tag nj-tag--orange"><span class="nj-tag__text">tag</span></a>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">8 - Card title</h4>
        <p>Some quick example text to build on the card title and make up the
      bulk of the card's content.</p>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__body">
        <h4 class="nj-card__title">9 - Card title</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad
      aspernatur dolorum earum harum, hic illum ipsa molestias nam odit quis
      quo quos repellat, repudiandae similique soluta veniam veritatis vero
      voluptatum!</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aspernatur
      dolorum earum harum, hic illum ipsa molestias nam odit quis quo quos
      repellat, repudiandae similique soluta veniam veritatis vero
      voluptatum!</p>
        <button class="nj-btn nj-btn--sm">Button</button>
        <button class="nj-btn nj-btn--sm">Button</button>
      </div>
    </div>
    <div class="nj-card">
      <div class="nj-card__img-wrapper">
        <img class="nj-card__img" src="https://design.engie.com/assets/img/img-generic.jpg" alt="Card image cap"/>
      </div>
      <div class="nj-card__body">
        <h4 class="nj-card__title">10 - Card title</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque autem,
      consequuntur dolorum eius, expedita illo minus molestias natus pariatur
      perferendis.</p>
        <div class="nj-tag nj-tag--brand"><span class="nj-tag__text">tag</span></div>
        <div class="nj-tag nj-tag--green"><span class="nj-tag__text">tag</span></div>
        <a href="#" class="nj-tag nj-tag--purple"><span class="nj-tag__text">tag</span></a>
        <a href="#" class="nj-tag nj-tag--orange"><span class="nj-tag__text">tag</span></a>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
