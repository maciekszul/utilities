import os
import datetime
import pandas
import unittest

class files():


	def __init__(self):
		self.sep = os.path.sep


	def getFoFis(self, path, wp=True):
		"""
		Returns lists of files and folders from directory
		path - folder address
		wp - BOOL, list with path
		"""
		files = []
		folders = []
		for (dirpath, dirnames, filenames) in os.walk(path):
	        files.extend(filenames)
	        folders.extend(dirnames)
	        break
	    if wp:
	    	files = [path + self.sep + i for i in files]
	    	folders = [path + self.sep + i for i in folders]

	   return (folders, files)


	def getFiles(self, path, prefix, extension, wp=True):
		"""
		Returns lists of files within folder with specific
		prefix, extension and both.
		path - folder address
		wp - BOOL, list with path
		prefix - string, beginning of the filename
		extension - string, extension w/o dot
		"""
		ext = []
	    prfx = []
	    intersect = []
	    files = self.getFoFi(path)
	    for i in files[1]:
	        if i.startswith(prefix):
	            prfx.append(i)
	        if i.endswith(extension):
	            ext.append(i)
	        if i.endswith(extension) and i.startswith(prefix):
	            intersect.append(i)
	    if wp:
	    	ext = [path + self.sep + i for i in ext]
        	prfx = [path + self.sep + i for i in prfx]
        	intersect = [path + self.sep + i for i in intersect]

        return (ext, prfx, intersect)


    def csvMerge(self, path, filename):
    	"""
	    merges all csvs in the directory without unnecessary headers, unnamed
	    columns
	    """

	    now = datetime.datetime.now()
	    day = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
	    hour = str(now.hour) + "_" + str(now.minute) + "_" + str(now.second)

	    all_files = self.getFiles(path, '', 'csv', wp=True)[2]

	    dataframes = [pd.read_csv(i) for i in all_files]

	    data = pd.concat(dataframes, ignore_index=True)
	    headers = list(data)
	    data = data[headers[:-1]]

	    data.to_csv('{0}{1}{2}_{3}_{4}.csv'.format(path, self.sep, filename, day, hour))


class testVA(unittest.TestCase):
	pass