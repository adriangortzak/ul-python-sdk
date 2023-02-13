import sys
import os

from ul_sdk import ul

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../ul_sdk/')))


def test_all_stops():
    assert len(ul.all_stops()) > 0


def test_stop_search(search_query):
    pass

def test_journey_search(from_point_id, from_point_type, to_point_id, to_point_type, max_walk_distance=3000):
    pass

def test_journey_parts(route_link_key):
    pass
