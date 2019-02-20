import urllib

def read_text():
    quotes=open("D:\DN_Renesas-update at 26Aug16\Personal\check_profanity_file.txt")
    contents_of_file=quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+text_to_check)
    output=connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print(" This doucment has no curse words!")
    else:
        print(" Could not scan the document properly.")
    
read_text()
