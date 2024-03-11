from collections import OrderedDict


j = {
  "A": {
    "function": lambda: print('A'),
    "runs": 1,  # -> 2
    "dependants": ["B", "B", "B", "C", "E"],
  },
  "B": {
    "function": lambda: print('B'),
    "runs": 1,  # -> 2
    "dependants": ["D"],
  },
  "C": {
    "function": lambda: print('C'),
    "runs": 1,  # -> 2
    "dependants": ["D", "F"],
  },
  "D": {
    "function": lambda: print('D'),
    "runs": 1,  # -> 2
    "dependants": [],
  },
  "X": {
    "function": lambda: print('X'),
    "runs": 1,
    "dependants": ["Y", "W"],
  },
  "Z": {
    "function": lambda: print('Z'),
    "runs": 1,
    "dependants": ["A"],
  }
}


def get_dependencies(name, jobs, dependencies: OrderedDict):
    """ Get all distinct existing dependant jobs.
    We need to use OrderedDict here to keep order and make the search faster.
    """
    # Check that job actually exists
    job = jobs.get(name)
    if job:
        if not (name in dependencies):
            dependencies.update({name: True})
        for dependant_name in set(job.get("dependants")):
            get_dependencies(dependant_name, jobs, dependencies)
    return dependencies


def run(name, jobs):
    dependencies = OrderedDict()
    for job_name in get_dependencies(name, jobs, dependencies):
        job = jobs[job_name]
        job["function"]()
        job["runs"] += 1


run('A', j)
run('A', j)
assert j["A"]["runs"] == 3
assert j["B"]["runs"] == 3
assert j["C"]["runs"] == 3
assert j["D"]["runs"] == 3
assert j["X"]["runs"] == 1
assert j["Z"]["runs"] == 1
