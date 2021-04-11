from typing import List

import re

CODE_BLOCK_CONTENT_FINDER = re.compile(r'```(\w*\n)?([^`]*)```')


def get_code(string: str) -> List[str]:
    return list(filter(lambda x: bool(x), map(
        lambda x: x[1].strip(),
        CODE_BLOCK_CONTENT_FINDER.findall(string)
    )))
