from booknlp.booknlp import BookNLP
import os

model_params={
		"pipeline":"entity", 
		"model":"small"
	}
	
booknlp=BookNLP("en", model_params)

# Input file to process

all_files = os.listdir('input_dir')
# input_file="input_dir/pg70123.txt"

# # Output directory to store resulting files in
# # File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
input_dir=[]
output_directory=[]
book_id = []
for i in all_files:
    input_dir.append("input_dir/" + i)
    output_directory.append("output_dir/" + i)
    book_id.append(i.strip(".txt"))

for i in range(len(input_dir)):
    booknlp.process(input_dir[i], output_directory[i], book_id[i])

# booknlp.process(all_files, output_directory, book_id)