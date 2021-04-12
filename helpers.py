import re
from typing import List, TypedDict

# INFO: The "+" in the character class matches a literal plus
# INFO: It does not act as a metacharacter here
CODE_BLOCK_CONTENT_FINDER = re.compile(r'```([\w+\-]*\n)?([^`]*)```')


class CodeObj(TypedDict):
    code: str
    language: str


def get_language_code(maybe_lang: str):
    langs = {
        'apache': 'text/apache',
        'bash': 'application/x-sh',
        'c': 'text/x-csrc',
        'cpp': 'text/x-c++src',
        'c++': 'text/x-c++src',
        'cs': 'text/x-csharp',
        'csharp': 'text/x-csharp',
        'diff': 'text/x-diff',
        'docker': 'dockerfile',
        'erl': 'erlang',
        'go': 'text/x-go',
        'html': 'htmlmixed',
        'xml': 'htmlmixed',
        'java': 'text/x-java',
        'js': 'javascript',
        'json': 'application/json',
        'kotlin': 'text/x-kotlin',
        'latex': 'stex',
        'lisp': 'commonlisp',
        'md': 'markdown',
        'matlab': 'text/x-octave',
        'mysql': 'text/x-mysql',
        'n-triples': 'application/n-triples',
        'objectivec': 'text/x-objectivec',  # NOSONAR
        'objc': 'text/x-objectivec',
        'obj-c': 'text/x-objectivec',
        'ocaml': 'mllike',
        'fs': 'mllike',
        'fsharp': 'mllike',
        'php': 'text/x-php',
        'ps': 'powershell',
        'py': 'python',
        'scala': 'text/x-scala',
        'sparql': 'application/sparql-query',
        'tex': 'stex',
        'turtle': 'text/turtle',
        'typescript': 'application/typescript',
        'ts': 'application/typescript',
        'tsx': 'application/typescript-jsx',
        'twig': 'text/x-twig',
        'vbnet': 'vb',
    }

    return langs[maybe_lang] if maybe_lang in langs else maybe_lang


def get_code(string: str) -> List[CodeObj]:
    all_code_snippets = map(
        lambda x: {'language': x[0].strip().lower()
                   or 'auto', 'code': x[1].strip()},
        CODE_BLOCK_CONTENT_FINDER.findall(string)
    )

    return list(filter(lambda x: bool(x['code']), all_code_snippets))
