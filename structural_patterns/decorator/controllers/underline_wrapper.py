from structural_patterns.decorator.controllers.base_wrapper import BaseWrapper


class UnderlineWrapper(BaseWrapper):

    def render(self):
        return f"<u>{self._wrapper.render()}</u>"
