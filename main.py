from translate import translate

while True:
  try:
    translate()
  except KeyboardInterrupt:
    print("\nBye")
    exit()
