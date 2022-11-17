from structural_patterns.decorator.controllers.base_wrapper import BaseWrapper


class BoldWrapper(BaseWrapper):

    def render(self):
        return f"<b>{self._wrapper.render()}</b>"
