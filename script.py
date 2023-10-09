file=open("input.txt.txt",'r')
all_lines=file.readlines()
cleaned_lines = [line.strip() for line in all_lines]
search_word=['PYTHON','C','OOP','HELLO','JAVA','C++']
matched_list=[0]*len(search_word)
for line in cleaned_lines:
    for i,word in enumerate(search_word):
         if line == word:
            matched_list[i]=matched_list[i]+1

for i,word in enumerate(search_word):
    print(word,"->",matched_list[i])


