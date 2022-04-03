from jinja2 import FileSystemLoader, Environment


inp_text = 'Домашнее задание'
way = FileSystemLoader('HW54')
env = Environment(loader=way)
action = env.get_template('hw54main.html')
print(action.render(title=inp_text))
