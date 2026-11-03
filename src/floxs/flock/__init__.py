"""
Flock mult-agent environment

Multi-agent environment inspired by Reynolds boid model. Agents
aim to stay close to other agents without colliding.
"""

from floxs.flock import env as env
from floxs.flock import generator as generator
from floxs.flock import observations as observations
from floxs.flock import rewards as rewards
from floxs.flock import types as types
from floxs.flock import viewer as viewer
from floxs.flock.env import Flock as Flock
