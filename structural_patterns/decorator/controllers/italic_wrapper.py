from structural_patterns.decorator.controllers.base_wrapper import BaseWrapper


class ItalicWrapper(BaseWrapper):

    def render(self):
        return f"<i>{self._wrapper.render()}</i>"
