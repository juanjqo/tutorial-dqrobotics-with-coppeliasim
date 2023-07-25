from pygments.lexers import get_lexer_by_name  # refer LEXERS
from pygments.lexers._mapping import LEXERS
from pygments.lexers.python import PythonLexer
from pygments.lexer import RegexLexer
from pygments.token import *
from pygments.token import Name

class DiffLexer(RegexLexer):
    name = 'Diff'
    aliases = ['diff']
    filenames = ['*.diff']

    tokens = {
        'root': [
            (r' .*\n', Text),
            (r'\+.*\n', Generic.Inserted),
            (r'-.*\n', Generic.Deleted),
            (r'@.*\n', Generic.Subheading),
            (r'Index.*\n', Generic.Heading),
            (r'=.*\n', Generic.Heading),
            (r'.*\n', Text),
        ]
    }



def setup(app):
    # choose one, both ok
    app.add_lexer('my_bash', get_lexer_by_name('py'))
    app.add_lexer('my_bash', DiffLexer)