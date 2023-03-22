from booknlp.booknlp import BookNLP
import os

model_params={
		"pipeline":"entity", 
		"model":"small"
	}
	
booknlp=BookNLP("en", model_params)


all_files = 'input_dir/scwared-14-sample-dataset'

input_dir=[]
output_directory=[]
book_id = []


for subdir in os.listdir(all_files):
    d = {}
    filenames = []

    for filename in os.listdir(os.path.join(all_files, subdir)):

        if filename.endswith('.txt'):
            with open(os.path.join(all_files, subdir, filename), 'r') as f:

                d.update({os.path.splitext(filename[-7:])[0]: f.read()})
        
        input_dir.append(all_files + "/" + subdir +"/"+ filename)

        output_directory.append("output_dir/" + subdir +"|"+ os.path.splitext(filename[-7:])[0])
        book_id.append(subdir +"|"+ os.path.splitext(filename[-7:])[0])

print(input_dir)

for i in range(len(input_dir)):
    booknlp.process(input_dir[i], output_directory[i], book_id[i])
