from pathlib import Path
import re, json, collections

root = Path.cwd()
issues = []
categories = collections.defaultdict(list)
count = 0
for path in sorted((root / 'common/script_constants').glob('*.txt')):
    text = path.read_text(encoding='utf-8-sig')
    tokens = []
    last_offset, current_line = 0, 1
    for match in re.finditer(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>#]+', text):
        current_line += text.count('\n', last_offset, match.start())
        last_offset = match.start()
        if not match.group().startswith('#'): tokens.append((match.group(), current_line))
    pos = 0
    def block():
        global pos
        result = []
        while pos < len(tokens) and tokens[pos][0] != '}':
            key, line = tokens[pos]; pos += 1
            if key == '{':
                result.append((None, block(), line)); continue
            if pos >= len(tokens) or tokens[pos][0] != '=':
                result.append((None, key, line)); continue
            pos += 1
            val, _ = tokens[pos]; pos += 1
            result.append((key, block() if val == '{' else val, line))
        if pos < len(tokens): pos += 1
        return result
    try:
        data = block()
    except (ValueError, IndexError) as error:
        issues.append(str(error)); continue
    for category, entries, line in data:
        count += 1
        where = f'{path.relative_to(root)}:{line}:{category}'
        categories[category].append(where)
        if not isinstance(entries, list):
            issues.append(where + ': category is scalar'); continue
        schemas = [e for e in entries if e[0] == 'schema']
        if len(schemas) != 1 or entries[0][0] != 'schema':
            issues.append(where + ': missing, duplicated or non-first schema'); continue
        schema = dict((k,v) for k,v,_ in schemas[0][1])
        if ('key' in schema) == ('any_key' in schema): issues.append(where + ': ambiguous/missing key selector')
        typ = schema.get('data')
        if schema.get('array') in ('country', 'state'): continue
        if isinstance(typ, list): continue
        if typ not in ('int', 'fixed_point'): issues.append(where + ': unsupported scalar type ' + str(typ))
        seen = set()
        for key, value, entryline in entries[1:]:
            location = f'{path.relative_to(root)}:{entryline}:{category}.{key}'
            if key in seen: issues.append(location + ': duplicate key')
            seen.add(key)
            if isinstance(value, list) or not re.fullmatch(r'-?\d+(?:\.\d+)?', value): issues.append(location + ': nonnumeric scalar ' + str(value))
            if typ == 'int' and isinstance(value,str) and '.' in value: issues.append(location + ': fractional integer')
for name, locations in categories.items():
    if len(locations) > 1: issues.append({'duplicate_category':name,'locations':locations})
print(json.dumps({'category_count':count,'issues':issues}, indent=2))
