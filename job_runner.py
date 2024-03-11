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



def run(name, jobs, runs: set):

    job = jobs.get(name)
    # run
    if job:
        if not (name in runs):
            job["function"]()
            job["runs"] += 1

        # all children
        for i in set(job.get("dependants")):
            run(i, jobs, runs)

        runs.add(name)



run('A', j, set())
run('A', j, set())
assert j["A"]["runs"] == 3
assert j["B"]["runs"] == 3
assert j["C"]["runs"] == 3
assert j["D"]["runs"] == 3
assert j["X"]["runs"] == 1
assert j["Z"]["runs"] == 1
