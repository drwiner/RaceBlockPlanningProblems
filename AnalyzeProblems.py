from collections import defaultdict

FILENAME = "RaceBlockWorld3_{}_problem.txt"

def IsBlank(line):
	if (line == "\n" or line == "" or line == None):
		return True
	return False

def parseEverything(filename):
	boids = 0
	locs = 0
	blocks = 0


	found = False
	for i, line in enumerate(filename):
		if not found and line.split()[0] == "Objects":
			found = True
			continue

		if found:
			if line[0] == "L" and line[-2] != "A":
				locs += 1
			elif line[0] == "L" and line[-2] == "A":
				continue
			elif line[0:5] == "block":
				blocks += 1
			else:
				boids += 1


		if (IsBlank(line)):
			break

	return (locs, boids, blocks)



if __name__ == "__main__":

	'''
	A problem is unique relative to its number of locations, boids, and blocks
	'''
	probDict = defaultdict(int)
	probList = defaultdict(list)
	for i in range(40):
		fname = FILENAME.format(str(i))
		with open(fname, 'r') as open_file:
			prob_spec = parseEverything(open_file)
			probDict[prob_spec] += 1
			probList[prob_spec].append(i)

	sumo = 0
	for k, v in probDict.items():
		print(k, v)
		print(probList[k])
		sumo += v
		print()

	print('total', sumo)