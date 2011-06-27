jQuery html5accordion plugin package for Django
===============================================

django-html5accordion adds JS support to expand/collapse any content, like HTML5 details/summary elements. It can be called on any element, and takes as an argument a selector for the `summary` contents that should always remain visible (and act as the link to expand/collapse the hidden content).

Dependencies
------------

- jQuery library (http://jquery.com/)

Installation
------------

In your Django project settings, add "html5accordion" to your INSTALLED_APPS.

Usage
-----

Linking the JS::

    <script src="{{ STATIC_URL }}html5accordion/jquery.html5accordion.js"></script>

Sample HTML::

    <article class="details">
      <header class="summary">
        <p>This content will always be visible</p>
      </header>
      <div>
        <p>This content will expand/collapse when `.summary` is clicked</p>
      </div>
    </article>

Calling the plugin::

    $('.details').html5accordion('.summary');