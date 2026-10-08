from pathlib import Path
import re, json

def parse(text):
    tokens = list(re.finditer(r'#[^\n]*|"(?:\\.|[^"\\])*"|[^\s{}=<>!#"]+|[{}=<>!]', text))
    tokens = [t for t in tokens if not t.group().startswith('#')]
    cursor = 0
    def body():
        nonlocal cursor
        nodes = []
        while cursor < len(tokens) and tokens[cursor].group() != '}':
            key = tokens[cursor]; cursor += 1
            if key.group() == '{':
                children = body()
                if cursor < len(tokens): cursor += 1
                nodes.append(('$anonymous', children, key.start(), tokens[cursor-1].end()))
                continue
            if cursor >= len(tokens) or tokens[cursor].group() not in ('=', '<', '>'):
                continue
            op = tokens[cursor].group(); cursor += 1
            if cursor >= len(tokens): break
            value = tokens[cursor]; cursor += 1
            if value.group() == '{':
                children = body()
                if cursor < len(tokens): cursor += 1
                end = tokens[cursor-1].end()
                nodes.append((key.group(), children, key.start(), end))
            else:
                nodes.append((key.group(), value.group(), key.start(), value.end()))
        return nodes
    return body()
