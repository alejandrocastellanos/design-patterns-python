from structural_patterns.decorator.controllers.bold_wrapper import BoldWrapper
from structural_patterns.decorator.controllers.italic_wrapper import ItalicWrapper
from structural_patterns.decorator.controllers.text import Text
from structural_patterns.decorator.controllers.underline_wrapper import UnderlineWrapper


def test_decorators():
    text = 'Hello world!'

    basic_text = Text(text)
    bold_text = BoldWrapper(basic_text)
    bold_italix_underline_text = UnderlineWrapper(ItalicWrapper(BoldWrapper(basic_text)))

    assert basic_text.render() == 'Hello world!'
    assert bold_text.render() == '<b>Hello world!</b>'
    assert bold_italix_underline_text.render() == '<u><i><b>Hello world!</b></i></u>'
