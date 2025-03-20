


import emoji

print('Digite uma frase para ser emojizada!')
print(emoji.emojize(':red_heart:   - '), ':red_heart:')
print(emoji.emojize(':thumbs_up:   - '), ':thumbs_up:')
print(emoji.emojize(':thinking_face:   - '), ':thinking_face:')
print(emoji.emojize(':partying_face:   - '), ':partying_face:')

x = input(': ')

print(emoji.emojize(x))