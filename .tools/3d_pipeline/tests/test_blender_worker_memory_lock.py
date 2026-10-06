"""Check exclusive worker serialization and OS release after a crash."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ADAPTER = Path(__file__).resolve().parents[1] / 'adapter'
sys.path.insert(0, str(ADAPTER))
from worker_lock import blender_worker_lock


class WorkerLockTests(unittest.TestCase):
    def test_second_client_waits_and_does_not_remove_lock_file(self):
        with tempfile.TemporaryDirectory() as directory:
            with blender_worker_lock(directory):
                with self.assertRaises(TimeoutError):
                    with blender_worker_lock(directory, timeout=.05):
                        self.fail('Two workers acquired the memory lock')
            self.assertTrue((Path(directory) / 'blender_worker.lock').is_file())
            with blender_worker_lock(directory, timeout=.05):
                pass

    def test_crashed_owner_does_not_leave_permanent_lock(self):
        with tempfile.TemporaryDirectory() as directory:
            code = "import sys,os;sys.path.insert(0,sys.argv[1]);from worker_lock import blender_worker_lock;\nwith blender_worker_lock(sys.argv[2]): os._exit(17)"
            result = subprocess.run([sys.executable, '-c', code, str(ADAPTER), directory], check=False)
            self.assertEqual(result.returncode, 17)
            with blender_worker_lock(directory, timeout=.05):
                pass


if __name__ == '__main__':
    unittest.main()
