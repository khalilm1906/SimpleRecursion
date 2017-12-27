def find_character_index(character, index=0):
  i = index
  c = str.upper(character)
  alphabet = [chr(x) for x in range(65, 91)]

  if i < 26:
      if alphabet[i] == c:
          print("FOUND CHARACTER %s in English Alphabet at %d" % (character, i+1))
          return i+1
      else:
          print("count %d does not equal %s so recursing" % (i+1, character))
          i += 1
          find_character_index(character,i)
  else:
      print("CHARACTER %s Not Found in English Alphabet" % character)
      return -1
