"""Guard regressions. Run in WSL with unittest; never attach to a real game."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('bridge', Path(__file__).with_name('clausewitz_linux.py'))
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


class GuardTests(unittest.TestCase):
    def test_wrong_build_refuses_launch_before_lease_or_prctl(self):
        with patch.object(bridge, 'check_checkout'), patch.object(bridge, 'build_id', return_value='wrong'), \
             patch.object(bridge, 'require_lease') as lease, patch.object(bridge.ctypes, 'CDLL') as native, \
             patch.object(bridge.os, 'execv') as execute:
            with self.assertRaisesRegex(RuntimeError, 'Unsupported HOI4 ELF build'):
                bridge.launch('test', [])
            lease.assert_not_called()
            native.assert_not_called()
            execute.assert_not_called()

    def test_other_lease_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            lease = Path(temp) / 'lease'
            lease.write_text('other_job\n')
            with patch.object(bridge, 'LOCK', lease):
                with self.assertRaisesRegex(RuntimeError, 'other_job'):
                    bridge.require_lease('test')
            self.assertEqual(lease.read_text(), 'other_job\n')

    def test_no_lease_is_not_permission(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(bridge, 'LOCK', Path(temp) / 'missing'):
            with self.assertRaisesRegex(RuntimeError, 'lease belongs to None'):
                bridge.require_lease('test')

    def test_matching_lease(self):
        with tempfile.TemporaryDirectory() as temp:
            lease = Path(temp) / 'lease'
            lease.write_text('test\n')
            with patch.object(bridge, 'LOCK', lease):
                bridge.require_lease('test')

    def test_screenshot_never_focuses_desktop(self):
        with patch.object(bridge.subprocess, 'run') as run, patch.object(bridge, 'owned_pid') as pid:
            with self.assertRaisesRegex(RuntimeError, 'focusing is disabled'):
                bridge.screenshot('test', focus=True)
            run.assert_not_called()
            pid.assert_not_called()

    def test_capture_failure_has_no_desktop_fallback(self):
        with patch.object(bridge, 'owned_pid', return_value=123), \
             patch.object(bridge.subprocess, 'check_output', return_value='456\n'), \
             patch.object(bridge.subprocess, 'run', side_effect=bridge.subprocess.TimeoutExpired('import', 45)) as run:
            with self.assertRaises(bridge.subprocess.TimeoutExpired):
                bridge.screenshot('test')
            self.assertEqual(run.call_count, 1)
            self.assertEqual(run.call_args.args[0][0], 'import')
            self.assertIn(':91', run.call_args.args[0])

    def test_modified_checkout_is_refused(self):
        with patch.object(bridge, 'command_output', side_effect=[bridge.PIN, ' M calling/offsets.py']):
            with self.assertRaisesRegex(RuntimeError, 'tracked files have changed'):
                bridge.check_checkout()

    def test_wrong_commit_is_refused(self):
        with patch.object(bridge, 'command_output', return_value='wrong'):
            with self.assertRaisesRegex(RuntimeError, 'not the reviewed commit'):
                bridge.check_checkout()


if __name__ == '__main__':
    unittest.main()
