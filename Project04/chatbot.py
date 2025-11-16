def chatbot(inp):
    print("---Welcome to My Personal Simple Chatbot---")
    print("Ask me  anything:")
    chat=str(input("User: ")).lower()
    output="Bot : "
    if chat=="hello":
        output+="Hi!"
    elif chat=="how are you":
        output+="I`m Fine."
    elif chat=="bye":
        output+="Good bye!"
    else:
        output+="I am not trained yet on this type of input"
        
    print(output)
        
    

chatbot("text")



    