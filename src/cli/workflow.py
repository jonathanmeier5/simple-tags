

class BreakLoop(Exception):
    pass


class Workflow:

    def __init__(self, *args, **kwargs):
        base_callable_mapping = {
            'q': self.quit,
        }

        self.callable_mapping = base_callable_mapping
        self.callable_mapping.update(kwargs.get('callable_mapping', {}))
        self.training_set = kwargs.get('training_set')

        assert self.training_set, 'training_set is a required keyword argument'

    def init_loop(self):

        while True:
            prompt = self.get_prompt()
            input_str = input(prompt)
            try:
                self.handle_input(input_str)
            except BreakLoop:
                break

    def handle_input(self, input_str: str):
        """Handle input from prompt"""
        f = self.callable_mapping.get(input_str)
        if not f:
            raise InvalidInput(input_str)
        else:
            f()

    def get_prompt(self):
        menu_items = []
        for k, v in sorted(self.callable_mapping.items(), key=lambda pair: pair[0]):
            menu_item = f'[{k}] {v.__doc__}:\n'
            menu_items.append(menu_item)

        return ''.join(menu_items)

    def quit(self):
        """exit program"""
        raise BreakLoop
