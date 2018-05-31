"""This is a learning exercise covering many aspects of python from the CodeAcademy course.

The scenario:
A spy deleted important files from a computer. There were a few witnesses at the scene of the crime, but no one is sure who exactly the spy was. Three possible suspects were apprehended based on surveillance video. Each suspect had a sample of DNA taken from them. The computer's keyboard was also swabbed for DNA evidence and, luckily, one small DNA sample was successfully retrieved from the computer's keyboard.

Given the three suspects' DNA and the sample DNA retreived from the keyboard, it's up to you to figure out who the spy is!

The project should have methods for each of the following:
1. Given a file, read in the DNA for each suspect and save it as a string
2. Take a DNA string and split it into a list of codons
3. Iterate through a suspect's codon list to see how many of their codons match the sample codons.
4. Pick the right suspect to continue the investigation on. 

DNA matching based on only 3 codons seems greatly over-simplified... but regardless, here is the program:"""


# Given Information
sample = ['GTA','GGG','CAC']

# Method for reading a suspects DNA sample
"""When used, this method will take in a file, read it, add the file's contents to an empty string, and return the updated string."""
def read_dna(dna_file): 
  dna_data = ""
  with open(dna_file, "r") as f: 
    for line in f: 
      dna_data += line
  return dna_data

# Method for converting the string of all the whole sequence into a list of codons. 
""" Takes a string, creates a list of codons from that string, and returns the list."""
def dna_codons(dna):
  codons = [] 
  for i in range (0, len(dna), 3): 
    if i + 3 < len(dna):  
      codons.append(dna[i:i + 3])
  return codons

# Method to compare the codons to the suspects DNA
"""If there is a match, the match counter goes up by 1. """
def match_dna(dna):
  matches = 0 
  for codon in dna: 
    if codon in sample: 
      matches += 1
  return matches

# Method to determine if a suspect is a criminal. 
"""This method runs the other methods that were previously created."""
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample) 
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3: 
    print("Matches: %s. Verdict: possible suspect!" % num_matches) 
  else: 
    print("Matches: %s. Verdict: innocent." % num_matches)
   
  
# Run the methods on these 3 suspects
print("Suspect 1")
is_criminal('suspect1.txt')
print("")
print("Suspect 2")
is_criminal('suspect2.txt')
print("")
print("Suspect 3")
is_criminal('suspect3.txt')
    

