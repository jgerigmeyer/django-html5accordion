jQuery html5accordion plugin package for Django
===============================================

django-html5accordion adds JS support to expand/collapse any content, like
HTML5 details/summary elements. It can be called on any element, and accepts
options to set the selector for the ``summary`` contents that should always
remain visible (and act as the link to expand/collapse the hidden content),
the speed of the slideUp/Down animation, the class to be added when the
``details`` element is expanded, and selectors for elements within ``summary``
that should not trigger the expand/collapse.

Dependencies
------------

- `jQuery`_ library

.. _jQuery: http://jquery.com/


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

    $('.details').html5accordion();

Calling the plugin with a variety of options explicitly configured to their
default values::

    $('.details').html5accordion({
      summarySelector: '.summary',                // Selector for summary text
      slideSpeed: 200,                            // Slide animation speed (ms)
      expandedClass: 'open',                      // Class added when details are
                                                    // expanded
      ignoredElements: 'button, a, input, label'  // Elements within `summary` that
                                                    // will not trigger expand/collapse
    });

Note: To expand a ``details`` element on initial load, simply add class
``open`` (or whatever class is passed as option ``expandedClass``), or add
attribute ``open`` (this second method does not work in Firefox 5.0).