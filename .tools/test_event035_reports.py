"""Execute Event 035 report guards from production source.

Native event delivery is recorded, not emulated. These tests cover scheduling
and conservative helper frames, not native popup rendering or delayed delivery.
"""
import unittest
from test_event035_center_projects import (
    Event35Runtime, Scope, country, read_definitions, first,
)


class ReportRuntime(Event35Runtime):
    def _path_container(self, path):
        if "@var:" in path:
            base, target = path.split("@var:", 1)
            path = base + str(int(self._variable(target)))
        return super()._path_container(path)

    def event_body(self, event_id, country_scope, section="immediate"):
        # Native event headers repeat; use the source parser's nodes, not its
        # dictionary's last country_event definition.
        from test_event035_center_projects import ROOT, lex, uncomment, parse_nodes
        path = ROOT / "events/035_great_depression.txt"
        nodes, _ = parse_nodes(lex(uncomment(path.read_text(encoding="utf-8"))), 0, str(path))
        event = next(n.value for n in nodes if isinstance(n.value, list) and first(n.value, "id") == event_id)
        self.root = country_scope
        self.scope_stack = [country_scope]
        trigger = first(event, "trigger", [])
        if not self._conditions(trigger, country_scope):
            return False
        self._effects(first(event, section, []), country_scope)
        return True


def episode(r, actor, episode_id, caller="independent_event_35", source=None):
    actor.values.update({
        "great_depression_active_episode_id": episode_id,
        "great_depression_call_caller_type": r.constants["constant:great_depression_caller." + caller],
        "great_depression_call_started": 1,
        "great_depression_call_report_policy": 1,
        "great_depression_call_news_policy": 1,
    })
    if source:
        actor.values["great_depression_call_source_country_scope"] = source
    r.run_effect("great_depression_initialize_report_chain", actor)


class ReportSchedulingTests(unittest.TestCase):
    def test_worldwide_28_conversions_queue_no_routine_world_news(self):
        r = ReportRuntime()
        r.global_flags.add("great_depression_worldwide_episode_active")
        r.globals["great_depression_global_episode_id"] = 100
        for i in range(28):
            actor = country("W" + str(i))
            episode(r, actor, i + 1, "worldwide_depression_conversion")
            r.run_effect("great_depression_queue_external_surfaces", actor)
            r.event_body("chaosx.nr35.2", actor)
            self.assertEqual(actor.values["great_depression_report_chain_episode"], 100)
        self.assertEqual(len(r.events), 28)
        self.assertTrue(all(e[1] == "chaosx.nr35.2" for e in r.events))

    def test_one_secondary_news_across_all_financial_descendants(self):
        r = ReportRuntime()
        origin = country("AAA")
        episode(r, origin, 1)
        r.run_effect("great_depression_queue_external_surfaces", origin)
        r.event_body("chaosx.nr35.2", origin)
        source = origin
        for i in range(28):
            actor = country("C" + str(i))
            episode(r, actor, i + 2, "financial_contagion_conversion", source)
            r.run_effect("great_depression_queue_external_surfaces", actor)
            r.root = source
            r.scope_stack = [source, actor]
            r._call_effect("great_depression_mark_first_contagion_spread", actor)
            r.event_body("chaosx.nr35.2", actor)
            self.assertEqual(actor.values["great_depression_report_chain_episode"], 1)
            if i % 2:
                source = actor
        self.assertEqual(sum(e[1] == "chaosx.news.40" for e in r.events), 1)
        self.assertEqual(sum(e[1] == "chaosx.nr35.15" for e in r.events), 1)

    def test_deepening_replay_no_extra_report_or_news_and_new_episode_can_report(self):
        r = ReportRuntime()
        a = country("AAA")
        episode(r, a, 1)
        r.run_effect("great_depression_queue_external_surfaces", a)
        self.assertTrue(r.event_body("chaosx.nr35.2", a))
        a.values["great_depression_call_started"] = 0
        for _ in range(30):
            r.run_effect("great_depression_queue_external_surfaces", a)
            self.assertFalse(r.event_body("chaosx.nr35.2", a))
        self.assertEqual(len(r.events), 2)
        episode(r, a, 2)
        r.run_effect("great_depression_queue_external_surfaces", a)
        self.assertTrue(r.event_body("chaosx.nr35.2", a))
        self.assertEqual(len(r.events), 4)

    def test_recipient_aggregates_independent_origins_and_ignores_descendants(self):
        r = ReportRuntime()
        receiver = country("REC")
        r.targets["great_depression_exposure_target"] = receiver
        for i in range(3):
            source = country("S" + str(i))
            episode(r, source, i + 1)
            r.run_effect("great_depression_queue_exposed_partner_report", source)
        self.assertEqual(len(r.events), 1)
        self.assertTrue(r.event_body("chaosx.nr35.14", receiver))
        self.assertEqual(receiver.values["great_depression_exposure_report_other_count"], 2)
        self.assertEqual(receiver.arrays["great_depression_exposure_report_origins"], [])
        descendant = country("DES")
        episode(r, descendant, 4, "financial_contagion_conversion", source)
        r.run_effect("great_depression_queue_exposed_partner_report", descendant)
        self.assertEqual(len(r.events), 1)
        self.assertFalse(r.event_body("chaosx.nr35.14", receiver))
        # A later independent episode is a separate chain and remains visible.
        episode(r, source, 5)
        r.run_effect("great_depression_queue_exposed_partner_report", source)
        self.assertEqual(len(r.events), 2)

    def test_inherited_start_keeps_its_report_and_news(self):
        r = ReportRuntime()
        a = country("AAA")
        episode(r, a, 1, "industrial_boom_collapse")
        r.run_effect("great_depression_queue_external_surfaces", a)
        r.event_body("chaosx.nr35.2", a)
        self.assertEqual([e[1] for e in r.events], ["chaosx.nr35.2", "chaosx.news.40"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
