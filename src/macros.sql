{% macro a(name, value='', type='rt', size=20) -%}
  Soy a, con name {{name}}, value {{value}}, type {{type}} y size {{size}}.
  {{ caller() }}
{%- endmacro %}


{% macro connect(conn, user) -%}
\c {{conn.dbname}} {{user.user}} {{conn.host}} {{conn.port}} {{caller()}}
{%- endmacro %}
