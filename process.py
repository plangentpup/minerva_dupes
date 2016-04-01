import pandas

# Load TORG data.
torg = pandas.read_csv('torg_names.csv')
primary = torg[torg['PRIMARY'] == 1]

results = pandas.read_pickle('torg_match_dataframe.pickle')
results['HighScore'] = results.max(axis=1)
results.sort('HighScore', inplace=True, ascending=0)
results.drop('HighScore', axis=1, inplace=True)

for minerva_group, row in results.iterrows():
	clean = row.dropna()
	clean.sort(inplace=True,ascending=False)
	i = 0
	if len(clean):
		print ""
		print str(minerva_group)
		for torg_id, ratio in clean.iteritems():
			if i < 3:
				print ""
				torgs = torg[torg['TORG'] == torg_id].sort('PRIMARY', ascending=0)
				prime = torgs[torgs['PRIMARY'] == 1].iloc[0]['GROUP']
				torgs = torgs['GROUP'].tolist()
				print "    {} | {}".format(str(ratio).rjust(3), str(torgs.pop(0)))
				for name in torgs:
					print "        | {}".format(name)
				print ''
				print '          UPDATE clean SET group1_torg = "{}", group1 = "{}" WHERE group1 = "{}";'.format(str(torg_id), str(prime), str(minerva_group))
				print '          UPDATE clean SET group2_torg = "{}", group2 = "{}" WHERE group2 = "{}";'.format(str(torg_id), str(prime), str(minerva_group))
				i += 1
		print ""
		print ""
		print "----------------------------------------------------------------------------------------------"
		print ""
