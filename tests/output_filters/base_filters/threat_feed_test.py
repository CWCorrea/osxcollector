# -*- coding: utf-8 -*-
import testify as T
from osxcollector.output_filters.base_filters. \
    threat_feed import ThreatFeedFilter
from tests.output_filters.run_filter_test import RunFilterTest


class ThreatFeedFilterTest(RunFilterTest):

    def test_run_output_filter(self):
        with T.assert_raises(NotImplementedError):
            input_blobs = [
                {'fungo': 'dingo', 'bingo': [11, 37], 'banana': {'a': 11}},
                {'span': 'div', 'head': ['tail', 22], 'orange': {'lemmon': 'zits'}}
            ]
            self.run_test(lambda: ThreatFeedFilter('dinky', 'feed_test'), input_blobs, expected_output_blobs=input_blobs)
