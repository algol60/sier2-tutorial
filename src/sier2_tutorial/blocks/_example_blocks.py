#

# Blocks provided by a builtin library.
# These are here to demonstrate building a dag from a data structure.
#

from sier2 import Block
import param
import random

class RandomNumberBlock(Block):
    """Produce a random number.

    Uses random.randint() to produce an integer in 1 .. 100 inclusive.
    """

    out_n = param.Integer(
        label='An integer',
        doc='A random number between 1 and 100 inclusive',
        default=None
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def prime(self):
        """A convenience method to prime the dag."""

        n = random.randint(1, 100)
        print(f'Random: {n}')
        self.out_n = n

class ConstantNumberBlock(Block):
    """Produce a constant number specified when the block is created."""

    out_constant = param.Number(
        label='A constant number',
        doc='A number determined at block creation time'
    )

    def __init__(self, x, name=None, *args, **kwargs):
        """Use our own name instead of one provided by param.

        Use id(self) to allow two blocks with the same constant.
        """

        if name is None:
            name = f'Number{x}-{id(self)}'

        super().__init__(name=name, *args, **kwargs)
        self.x = x

    def prime(self):
        """A convenience method to prime the dag."""

        self.out_constant = self.x

class AddBlock(Block):
    """Add two numbers.

    The action does not happen if either of the inputs is None.
    """

    in_a = param.Number(label='First number', default=None, doc='First number')
    in_b = param.Number(label='Second number', default=None, doc='Second number')
    out_result = param.Number(label='Result', default=None, doc='Result of addding in_a and in_b')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def execute(self):
        # If any arg isn't set, don't do anything.
        #
        if any(arg is None for arg in (self.in_a, self.in_b)):
            return

        self.out_result = self.in_a+self.in_b
        # print(f'{self.in_a} + {self.in_b} = {self.out_result}')

class ConfigurableBlock(Block):
    """The output of this block is the value of the key ``output`` in its config."""

    out_output = param.String(label='Output', doc='Output from config file', allow_None=True)

    def __init__(self):
        super().__init__(block_pause_execution=True)

    def execute(self):
        self.out_output = self.get_config_value('output')
