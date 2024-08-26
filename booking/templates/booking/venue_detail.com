{% extends "base.html" %}

{% block content %}
Venue details go here

{% endblock %}