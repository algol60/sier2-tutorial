from sier2 import Connection, Library
from sier2.panel import PanelDag

print('Loading ui ...')
UiBlock = Library.get_block('sier2_examples.tutorial_3b.UserInput')
ui = UiBlock(name='User input', user_input=True)

print('Loading translator ...')
TrBlock = Library.get_block('sier2_examples.tutorial_3b.Translate')
tr = TrBlock(name='Translation')

print('Loading display ...')
DiBlock = Library.get_block('sier2_examples.tutorial_3b.Display')
di = DiBlock(name='Display output')

dag = PanelDag(doc='Translation', title='translate text')
dag.connect(ui, tr, Connection('out_text', 'in_text'), Connection('out_flag', 'in_flag'))
dag.connect(tr, di, Connection('out_text', 'in_text'))

dag.show()