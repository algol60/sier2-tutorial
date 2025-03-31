from sier2 import Dag, Connection
from ..blocks._example_blocks import RandomNumberBlock, AddBlock, ConfigurableBlock

import param

def example_dag():
    rnga = RandomNumberBlock()
    rngb = RandomNumberBlock()
    add = AddBlock()

    dag = Dag(doc='Demonstrate adding random numbers', site='Example', title='Addition')
    dag.connect(rnga, add, Connection('out_n', 'in_a'))
    dag.connect(rngb, add, Connection('out_n', 'in_b'))

    # rnga.go()
    # rngb.go()

    # dag.execute()

    return dag
