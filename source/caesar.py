#Author: javiern_n@ciencias.unam.mx

import sys


class Caesar:

   def superEncryption(self, inputString, k):
      result = ""
      for i in range(len(inputString)):
         char = inputString[i]
         char_or = ord(char)
         if ( char_or >= 65 and char_or <= 90) or ( char_or >= 97 and char_or <= 122 ):
            if (char.isupper()):
               result += chr((char_or + k-65) % 26 + 65)
            else:
               result += chr((char_or + k - 97) % 26 + 97) 
         else:
            result += char
      return result


if __name__ == '__main__':

   if (len(sys.argv) == 2 ):
      string = ""
      k = int(sys.argv[1])
      string = (input("plaintext: "))
      result = Caesar().superEncryption(string, k)
      print ("ciphertext: " + result + "\n")

   else:
      print("Usage: python caesar.py k")
      exit(1)
