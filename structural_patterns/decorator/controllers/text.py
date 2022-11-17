from structural_patterns.decorator.controllers.base_wrapper import BaseWrapper


class Text(BaseWrapper):

    def render(self):
        return self._wrapper
