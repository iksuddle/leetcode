from .solution import *


def test_basic():
    counter = HitCounter()

    counter.hit(1)
    counter.hit(2)
    counter.hit(3)

    assert counter.getHits(4) == 3

    counter.hit(300)

    assert counter.getHits(300) == 4
    assert counter.getHits(301) == 3


def test_same_timestamp():
    counter = HitCounter()

    counter.hit(1)
    counter.hit(1)
    counter.hit(1)

    assert counter.getHits(1) == 3
    assert counter.getHits(300) == 3
    assert counter.getHits(301) == 0


def test_exact_300_second_boundary():
    counter = HitCounter()

    counter.hit(100)

    assert counter.getHits(399) == 1
    assert counter.getHits(400) == 0


def test_hits_on_boundary():
    counter = HitCounter()

    counter.hit(1)
    counter.hit(2)
    counter.hit(300)

    assert counter.getHits(300) == 3

    counter.hit(301)

    assert counter.getHits(301) == 3
    assert counter.getHits(302) == 2
    assert counter.getHits(600) == 1
    assert counter.getHits(601) == 0


def test_large_gap():
    counter = HitCounter()

    counter.hit(1)
    counter.hit(50)
    counter.hit(100)

    assert counter.getHits(1000) == 0

    counter.hit(1000)
    assert counter.getHits(1000) == 1


def test_many_hits_same_and_different_times():
    counter = HitCounter()

    for _ in range(5):
        counter.hit(1)

    for _ in range(3):
        counter.hit(100)

    for _ in range(7):
        counter.hit(300)

    assert counter.getHits(300) == 15
    assert counter.getHits(301) == 10
    assert counter.getHits(400) == 7
    assert counter.getHits(600) == 0
