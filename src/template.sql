{% import 'macros.sql' as macros %}

{% call macros.connect(c.connections.main, c.users.superdb) %}{% endcall %}
