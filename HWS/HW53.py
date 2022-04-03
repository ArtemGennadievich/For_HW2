from jinja2 import Template


val = '''
<ul>
{% for i,j in ren.items() %}
{%- if i == "/index" -%}
<li><a href="{{i}}" class="active">{{j}}</a></li>
{%- else -%}
    <li><a href="{{i}}">{{j}}</a></li>
{%- endif %}
{% endfor -%}
</ul>
'''
ren = {
    '/index': 'Главная',
    '/news': 'Новости',
    '/about': 'О компании',
    '/shop': 'Магазин',
    '/contacts': 'Контакты'
}

tm = Template(val)
print(tm.render(ren=ren))

