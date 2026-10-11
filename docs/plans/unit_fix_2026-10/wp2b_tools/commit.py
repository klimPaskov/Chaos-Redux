"""Shared-tree commit of fully owned paths: temp index from HEAD, commit-tree, CAS update-ref, restore real index entries."""
import os, subprocess, sys, tempfile
REPO = r"<mod root>"
class Fail(Exception): pass
def git(*a, env=None, inp=None, check=True):
    r = subprocess.run(['git', '-C', REPO, *a], capture_output=True, env=env, input=inp)
    if check and r.returncode:
        raise Fail(f"git {a[:2]} failed: {r.stderr.decode(errors='replace')}")
    return r.stdout.decode(errors='replace').strip()
msg, paths = sys.argv[1], sys.argv[2:]
def attempt():
    head = git('rev-parse', 'HEAD')
    tmp = tempfile.mktemp(prefix='wp3idx_')
    env = dict(os.environ, GIT_INDEX_FILE=tmp)
    git('read-tree', head, env=env)
    git('add', '--', *paths, env=env)
    print(git('diff', '--cached', '--stat', head, env=env))
    tree = git('write-tree', env=env)
    mf = tempfile.mktemp(prefix='wp3msg_')
    open(mf, 'w', encoding='utf-8', newline='\n').write(msg.rstrip() + "\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\n")
    new = git('commit-tree', tree, '-p', head, '-F', mf)
    git('update-ref', 'HEAD', new, head)
    git('restore', '--staged', f'--source={new}', '--', *paths)
    os.remove(tmp); os.remove(mf)
    print('committed', new)

for i in range(6):
    try:
        attempt(); break
    except Fail as e:
        print('retry', i, str(e)[:200])
        if 'update_ref' not in str(e) and 'update-ref' not in str(e): raise SystemExit(1)
else:
    raise SystemExit('gave up')
