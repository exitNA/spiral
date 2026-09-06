"""Regression coverage for scheduling signals derived from task outcomes."""
import importlib.util
from pathlib import Path
import unittest

RUNTIME = Path(__file__).resolve().parents[1] / 'loop/skills/loop/scripts/loop_runtime.py'
spec = importlib.util.spec_from_file_location('loop_runtime', RUNTIME)
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


class FirstPassSuccessTests(unittest.TestCase):
    def summarize(self, outcomes):
        events = []
        for index, (status, rework) in enumerate(outcomes):
            events.extend([
                dict(type='task_start', task=str(index), ts=index * 10, kind='implement'),
                dict(type='task_end', task=str(index), ts=index * 10 + 5,
                     status=status, rework=rework),
            ])
        return runtime.task_summary(events)

    def test_failures_reduce_success_rate_and_trigger_adaptation(self):
        tasks, stats = self.summarize([('success', 0)] + [('failed', 0)] * 3)
        self.assertEqual(stats['first_pass_success_rate'], 0.25)
        hints = runtime.policy_hints({'tasks': stats, 'events': {}}, tasks)
        self.assertTrue(any('earlier contract/reproduction checks' in hint for hint in hints))

    def test_all_failed_or_blocked_is_zero(self):
        _, stats = self.summarize([('failed', 0), ('blocked', 0)])
        self.assertEqual(stats['first_pass_success_rate'], 0)

    def test_repaired_success_is_not_first_pass(self):
        _, stats = self.summarize([('success', 0), ('success', 1)])
        self.assertEqual(stats['first_pass_success_rate'], 0.5)

    def test_all_first_pass_successes(self):
        _, stats = self.summarize([('success', 0)] * 3)
        self.assertEqual(stats['first_pass_success_rate'], 1)

    def test_empty_run_has_no_rate(self):
        _, stats = self.summarize([])
        self.assertIsNone(stats['first_pass_success_rate'])


if __name__ == '__main__':
    unittest.main()
