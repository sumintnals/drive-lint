import unittest
from pathlib import Path

from drivelint.checkers import grid, list as list_checker, long_message, message, pane, signin, tab

FIXTURES = Path(__file__).parent / "fixtures"


def _read(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


class GridCheckerTest(unittest.TestCase):
    def test_flags_more_than_six_items(self):
        violations = grid.check(_read("grid_fail.kt"), "grid_fail.kt")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "GRID-003")

    def test_allows_six_or_fewer_items(self):
        violations = grid.check(_read("grid_pass.kt"), "grid_pass.kt")
        self.assertEqual(violations, [])


class PaneCheckerTest(unittest.TestCase):
    def test_flags_more_than_four_rows(self):
        violations = pane.check(_read("pane_fail_too_many.kt"), "pane_fail_too_many.kt")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "PANE-010")

    def test_flags_zero_rows(self):
        violations = pane.check(_read("pane_fail_empty.kt"), "pane_fail_empty.kt")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "PANE-009")

    def test_allows_one_to_four_rows(self):
        violations = pane.check(_read("pane_pass.kt"), "pane_pass.kt")
        self.assertEqual(violations, [])


class TabCheckerTest(unittest.TestCase):
    def test_flags_fewer_than_two_tabs(self):
        violations = tab.check(_read("tab_fail_too_few.kt"), "tab_fail_too_few.kt")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "TAB-013")

    def test_flags_more_than_four_tabs(self):
        violations = tab.check(_read("tab_fail_too_many.kt"), "tab_fail_too_many.kt")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "TAB-013")

    def test_allows_two_to_four_tabs(self):
        violations = tab.check(_read("tab_pass.kt"), "tab_pass.kt")
        self.assertEqual(violations, [])


class ListCheckerTest(unittest.TestCase):
    def test_flags_empty_section_header(self):
        violations = list_checker.check(_read("list_fail_no_header.kt"), "list_fail_no_header.kt")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "LIST-001")

    def test_allows_section_with_header(self):
        violations = list_checker.check(_read("list_pass_with_header.kt"), "list_pass_with_header.kt")
        self.assertEqual(violations, [])


class MessageCheckerTest(unittest.TestCase):
    def test_flags_empty_message(self):
        violations = message.check(_read("message_fail_empty.kt"), "message_fail_empty.kt")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "MESSAGE-006")

    def test_allows_non_empty_message(self):
        violations = message.check(_read("message_pass.kt"), "message_pass.kt")
        self.assertEqual(violations, [])


class LongMessageCheckerTest(unittest.TestCase):
    def test_flags_empty_message(self):
        violations = long_message.check(
            _read("long_message_fail_empty.kt"), "long_message_fail_empty.kt"
        )
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "LONG-MESSAGE-005")

    def test_allows_non_empty_message(self):
        violations = long_message.check(_read("long_message_pass.kt"), "long_message_pass.kt")
        self.assertEqual(violations, [])


class SignInCheckerTest(unittest.TestCase):
    def test_flags_unknown_signin_method(self):
        violations = signin.check(
            _read("signin_fail_unknown_method.kt"), "signin_fail_unknown_method.kt"
        )
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "SIGNIN-014")

    def test_allows_known_signin_method(self):
        violations = signin.check(_read("signin_pass.kt"), "signin_pass.kt")
        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
