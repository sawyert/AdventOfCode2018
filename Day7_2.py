input="""
Step Q must be finished before step O can begin.
Step Z must be finished before step G can begin.
Step W must be finished before step V can begin.
Step C must be finished before step X can begin.
Step O must be finished before step E can begin.
Step K must be finished before step N can begin.
Step P must be finished before step I can begin.
Step X must be finished before step D can begin.
Step N must be finished before step E can begin.
Step F must be finished before step A can begin.
Step U must be finished before step Y can begin.
Step M must be finished before step H can begin.
Step J must be finished before step B can begin.
Step B must be finished before step E can begin.
Step S must be finished before step L can begin.
Step A must be finished before step L can begin.
Step E must be finished before step L can begin.
Step L must be finished before step G can begin.
Step D must be finished before step I can begin.
Step Y must be finished before step I can begin.
Step I must be finished before step G can begin.
Step G must be finished before step R can begin.
Step V must be finished before step T can begin.
Step R must be finished before step H can begin.
Step H must be finished before step T can begin.
Step S must be finished before step E can begin.
Step C must be finished before step E can begin.
Step P must be finished before step T can begin.
Step I must be finished before step H can begin.
Step O must be finished before step P can begin.
Step M must be finished before step L can begin.
Step S must be finished before step D can begin.
Step P must be finished before step D can begin.
Step P must be finished before step R can begin.
Step I must be finished before step R can begin.
Step Y must be finished before step G can begin.
Step Q must be finished before step L can begin.
Step N must be finished before step R can begin.
Step J must be finished before step E can begin.
Step N must be finished before step T can begin.
Step B must be finished before step V can begin.
Step Q must be finished before step B can begin.
Step J must be finished before step H can begin.
Step F must be finished before step B can begin.
Step W must be finished before step X can begin.
Step S must be finished before step T can begin.
Step J must be finished before step G can begin.
Step O must be finished before step R can begin.
Step K must be finished before step B can begin.
Step Z must be finished before step O can begin.
Step Q must be finished before step S can begin.
Step K must be finished before step V can begin.
Step B must be finished before step R can begin.
Step J must be finished before step T can begin.
Step E must be finished before step T can begin.
Step G must be finished before step V can begin.
Step D must be finished before step Y can begin.
Step M must be finished before step Y can begin.
Step F must be finished before step G can begin.
Step C must be finished before step P can begin.
Step V must be finished before step R can begin.
Step R must be finished before step T can begin.
Step J must be finished before step Y can begin.
Step U must be finished before step R can begin.
Step Z must be finished before step F can begin.
Step Q must be finished before step V can begin.
Step U must be finished before step M can begin.
Step J must be finished before step R can begin.
Step L must be finished before step V can begin.
Step W must be finished before step K can begin.
Step B must be finished before step Y can begin.
Step O must be finished before step N can begin.
Step D must be finished before step V can begin.
Step P must be finished before step B can begin.
Step U must be finished before step I can begin.
Step O must be finished before step T can begin.
Step S must be finished before step G can begin.
Step X must be finished before step A can begin.
Step U must be finished before step T can begin.
Step A must be finished before step I can begin.
Step B must be finished before step G can begin.
Step N must be finished before step Y can begin.
Step Z must be finished before step J can begin.
Step M must be finished before step D can begin.
Step U must be finished before step A can begin.
Step S must be finished before step R can begin.
Step Z must be finished before step A can begin.
Step Y must be finished before step R can begin.
Step E must be finished before step Y can begin.
Step N must be finished before step G can begin.
Step Z must be finished before step X can begin.
Step P must be finished before step X can begin.
Step Z must be finished before step T can begin.
Step Z must be finished before step P can begin.
Step V must be finished before step H can begin.
Step P must be finished before step L can begin.
Step L must be finished before step H can begin.
Step X must be finished before step V can begin.
Step W must be finished before step G can begin.
Step N must be finished before step D can begin.
Step Z must be finished before step U can begin.
"""

testdata = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""

from time import sleep

def available_jobs(dependencies, complete, workers):
  for stepComplete in complete:
    for step in dependencies.keys():
      value = dependencies[step]
      try:
        value.remove(stepComplete)
      except ValueError:
        pass

  result = ""
  keys = sorted(dependencies.keys())
  for key in keys:
    #print ("Looking at key %s, result is %s" % (key, result))
    value = dependencies[key]
    #print ("Dependencies %s" % value)
    if len(value) == 0:
      #print("Length of value is 0")
      #print("Looking for %s in %s, result is %d" % (key, result, result.find(key)))
      if complete.find(key) == -1:
        try:
          seconds = workers[key]
        except KeyError:
          result += key
  return result

def Day7_2(input, delay, max_workers):
  inputProcessed = input.replace('Step ','').replace(' must be finished before step ','>').replace(' can begin.','');
  print (inputProcessed)
  dependencies = {}
  for line in inputProcessed.split('\n'):
    if len(line.strip()) == 0: continue
    linesplit = line.split('>')
    dependency = linesplit[0]
    step = linesplit[1]
    try:
      existing = dependencies[step]
    except KeyError:
      dependencies[step] = []
    try:
      existing = dependencies[dependency]
    except KeyError:
      dependencies[dependency] = []
    
    dependencies[step].append(dependency)
    
  keys = sorted(dependencies.keys())
  print (keys)
  print (dependencies)
  
  workers = {}
  tick = 0
  letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  complete = ""
  while(True):
    available = available_jobs(dependencies, complete, workers)
    if len(available) == 0:
      print ("No jobs available")
      if len(workers.keys()) == 0:
        print("No workers executing, stopping")
        break
      
    print("Available jobs %s" % available)      
    while len(workers.keys()) < max_workers and len(available) > 0:
      job_key = available[0]
      print ("Assigning job %s to worker" % job_key)
      workers[job_key] = delay + letters.find(job_key)
      available = available[1:]
    print ("%d\t%s\t%s\t%s" % (tick, available, workers, complete))
    
    for worker_key in workers.keys():
      workers[worker_key] -= 1
      print ("%s is now %d" % (worker_key, workers[worker_key]))
      if workers[worker_key] == 0:
        complete += worker_key
        workers[worker_key] = None

    workers = {k: v for k, v in workers.items() if v is not None}

    tick += 1
  return tick
  
assert(Day7_2(testdata, 0, 2)==15)
print (Day7_2(input, 60, 5))