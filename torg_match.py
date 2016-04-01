
from fuzzywuzzy import fuzz
import pandas
import progressbar

# Load TORG data.
torg = pandas.read_csv('torg_names.csv')
primary = torg[torg['PRIMARY'] == 1]

# Load Minerva distinct group names data.
with open('post_distinct_uppercase.txt') as f:
	groups = f.read().splitlines()

# Prepare the result matrix.
df = pandas.DataFrame(index=groups, columns=primary['TORG'])
df.index.name = 'Minerva groups'

with progressbar.ProgressBar(max_value=len(df.index)) as bar:
	# Build the matrix of matches
	i = 0
	for minerva_group, rows in bar(df.iterrows()):
		for torg_id, value in rows.iteritems():
			# find the closet match of all TORG groups for this torg_id
			torgs = torg[torg['TORG'] == torg_id]['GROUP']
			ratio = 0
			for torg_group in torgs:
				ratio = max(ratio, fuzz.ratio(minerva_group, torg_group))
			rows[torg_id] = ratio
		i += 1
		bar.update(i)

df.to_pickle('torg_match_dataframe.pickle')
