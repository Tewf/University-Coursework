"""Pytest configuration for this exercise.

pytest imports this before any test module, which is the one place a backend can
be chosen early enough: Agg draws into memory, so the tests need no display and
never open a window.
"""
import matplotlib

matplotlib.use("Agg")
