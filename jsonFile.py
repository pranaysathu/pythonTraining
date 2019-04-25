data = {
	"Name": {
		"fIRSTNAME": "PRANAY",
		"lASTNAME":"sathu"
	}
}

import json

wf = open("data_File.json","w")
json.dump(data,wf)