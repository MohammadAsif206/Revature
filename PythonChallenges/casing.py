import unittest
# write a function that convernts a word into different casings
# assume no spacing
# snake_case example fire_truck OR Fire_Truck  (capitalization does not matter)
# camelCase example fireTruck
# PascalCase example FireTruck
# kebab-case example fire-truck

# casing('registeredUser','camelCase','kebab-case') -> registered-user
def casing(word, initial, target):
    
    letter = []
    for c in word:
        if c.isupper():
            letter.append('_')
            letter.append(c)
        else:
        	letter.append(c)
    #camelCase to PascalCase
    if initial == "camelCase" and target == "PascalCase":
    	print(letter)
    	out = "".join(letter).split("_")
    	a = str(out[0])
    	b = a.capitalize()
    	return (b+out[1])
    #camelCase to kebab-case
    if initial == "camelCase" and target == "kebab-case":
        out = "".join(letter).split("_")
        upperToLower = str(out[1])
        lower_case = upperToLower.lower()
        result = str(out[0]) + "-" + lower_case
        print(result)
        return result
    #camelCase to snake_case
    if initial == "camelCase" and target == "snake_case":
        out = "".join(letter).split("_")
        upperToLower = str(out[1])
        lower_case = upperToLower.lower()
        result = str(out[0]) + "_" + lower_case
        print(result)
        return result
    #word is GreenApple
    letter1 = []
    for p in word:
      if p.isupper():
        letter1.append("_")
        letter1.append(p)
      else:
        letter1.append(p)
    if initial == "PascalCase" and target == "snake_case":
      out1 = "".join(letter1).split("_")
      firstWord = str(out1[1])
      secondWord = str(out1[2])
      result1 = firstWord.lower()+ "_" + secondWord.lower()
      print(result1)
      return result1
    if initial == "PascalCase" and target == "kebab-case":
      out1 = "".join(letter1).split("_")
      firstWord = str(out1[1])
      secondWord = str(out1[2])
      result1 = firstWord.lower()+ "-" + secondWord.lower()
      print(result1)
      return result1
    if initial == "PascalCase" and target == "camelCase":
      out1 = "".join(letter1).split("_")
      firstWord = str(out1[1])
      secondWord = str(out1[2])
      secondWordCapitalized = secondWord.capitalize()
      result1 = firstWord.lower()+ secondWordCapitalized
      print(result1)
      return result1
            
    


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_camel_to_Pascal(self):
        result = casing(word='redSphere',initial='camelCase',target='PascalCase')
        self.assertEquals(result,'RedSphere')

    def test_camel_to_kebab(self):
        result = casing('redSphere','camelCase','kebab-case')
        self.assertEquals(result,'red-sphere')

    def test_camel_to_snake(self):
        result = casing('redSphere','camelCase','snake_case')
        self.assertEquals(result,'red_Sphere')


    def test_Pascal_to_snake(self):
        result = casing('GreenApple','PascalCase','snake_case')
        self.assertEquals(result,'green_apple')

    def test_Pascal_to_kebab(self):
        result = casing('GreenApple','PascalCase','kebab-case')
        self.assertEquals(result,'green-apple')

    def test_Pascal_to_camel(self):
        result = casing('GreenApple','PascalCase','camelCase')
        self.assertEquals(result,'greenApple')
    

    def test_kebab_to_camel(self):
        result = casing('green-apple','kebab-case','camelCase')
        self.assertEquals(result,'greenApple')

    def test_kebab_to_Pascal(self):
        result = casing('green-apple','kebab-case','PascalCase')
        self.assertEquals(result,'GreenApple')   

    def test_kebab_to_snake(self):
        result = casing('green-apple','kebab-case','snake_case')
        self.assertEquals(result,'green_apple') 
    

    def test_snake_to_camel(self):
        result = casing('green_apple','snake_case','camelCase')
        self.assertEquals(result,'greenApple') 
    
    def test_snake_to_Pascal(self):
        result = casing('green_apple','snake_case','PascalCase')
        self.assertEquals(result,'GreenApple') 
    
    def test_snake_to_kebab(self):
        result = casing('green_apple','snake_case','kebab-case')
        self.assertEquals(result,'green-apple') 

if __name__ == '__main__':
    unittest.main()