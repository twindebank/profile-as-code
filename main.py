from pathlib import Path

from pyprofile.profile import Profile

p = Profile.from_yamls(Path("legacy/profile"))

print(p)