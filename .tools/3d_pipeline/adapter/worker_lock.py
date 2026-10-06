"""Serialize adapter-owned Blender workers across all repository clients.

The OS releases this advisory lock on process exit, including crashes. A lock
file's existence never proves an active owner, so stale-file deletion is unused.
"""
from contextlib import contextmanager
import os
from pathlib import Path
import time


@contextmanager
def blender_worker_lock(directory, timeout=1800):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / 'blender_worker.lock'
    with path.open('a+b') as stream:
        stream.seek(0, os.SEEK_END)
        if stream.tell() == 0:
            stream.write(b'0')
            stream.flush()
        deadline = time.monotonic() + timeout
        while True:
            stream.seek(0)
            try:
                if os.name == 'nt':
                    import msvcrt
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.monotonic() >= deadline:
                    raise TimeoutError('Another adapter Blender worker holds the repository memory lock.')
                time.sleep(.25)
        try:
            yield path
        finally:
            stream.seek(0)
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
