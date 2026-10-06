"""Small read-only asset parser preserving repeated keys and source lines.

Handles assignment blocks, anonymous lists, quoted strings, and comments.
Unsupported or truncated input raises instead of silently losing event blocks.
"""
from dataclasses import dataclass
import re

TOKEN = re.compile(r'\s+|\#[^\n]*|"(?:\\.|[^"\\])*"|[{}=]|[^\s{}=\#"]+')


@dataclass
class Node:
    key: str
    value: object
    line: int

    def children(self, key=None):
        rows = self.value if isinstance(self.value, list) else []
        return [n for n in rows if key is None or n.key == key]

    def scalar(self, key, default=None):
        rows = self.children(key)
        return rows[0].value if rows and not isinstance(rows[0].value, list) else default


def parse(text):
    tokens = []
    line = 1
    offset = 0
    for match in TOKEN.finditer(text):
        if match.start() != offset:
            raise ValueError('Unsupported asset text at line ' + str(line))
        value = match.group()
        if not value.isspace() and not value.startswith('#'):
            tokens.append((value, line))
        line += value.count('\n')
        offset = match.end()
    if offset != len(text):
        raise ValueError('Unparsed asset suffix')
    index = 0

    def atom(value):
        return value[1:-1].replace('\\"', '"').replace('\\\\', '\\') if value.startswith('"') else value

    def block(nested=False):
        nonlocal index
        rows = []
        while index < len(tokens):
            token, source_line = tokens[index]
            if token == '}':
                if not nested:
                    raise ValueError('Unexpected } at line ' + str(source_line))
                index += 1
                return rows
            if token in {'=', '{'}:
                raise ValueError('Unexpected token at line ' + str(source_line))
            index += 1
            if index < len(tokens) and tokens[index][0] == '=':
                index += 1
                if index >= len(tokens):
                    raise ValueError('Missing assignment value')
                value = tokens[index][0]
                index += 1
                rows.append(Node(atom(token), block(True) if value == '{' else atom(value), source_line))
            else:
                rows.append(Node('', atom(token), source_line))
        if nested:
            raise ValueError('Unclosed asset block')
        return rows

    return Node('', block(), 1)


def walk(node):
    yield node
    for child in node.children():
        yield from walk(child)
