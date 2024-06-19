letter = ''' Dear <|Name|>, 
    You are selected! 
    <|Date|> ''' 

print(letter.replace("<|Name|>", "Rahul").replace("<|Date|>", "28th July"))