from CL701G import *

def main():
  try:
    people = []
    with open("data/prog701g.dat", 'r') as f:
      num = int(f.readline()) # 'f.' to read one line at a time
      while num != 99:
        fn = f.readline()
        ln = f.readline()
        if num == 1:
          gpa = float(f.readline())
          p = Student(fn, ln, gpa)
          people.append(p)
        elif num == 2:
          numStu = int(f.readline())
          p = Teacher(fn, ln, numStu)
          people.append(p)
        if num == 3:
          favW = f.readline().strip() # strip off line breaks
          p = Admin(fn, ln, favW)
          people.append(p)
        num = int(f.readline())

      tot = 0.0
      cnt = 0
      totstus = 0
      large = ""
      sm = "oaiwhfoiwahioohqfohfuhewqaiufeaygfeauhgafuhfauhfawuihaufjygwvwaiuygdwaugdwaiugwayffigawdiuhdwaiuygdwaiygdwaiygdwaiuydwauhwadugdwaigdwaygfgidwiugwadiugdwiugiuwaiudgwiuagdogqgdwaou"

      for Person in people:
        if isinstance(Person, Student): # if my person is an instance of a student
          tot += Person.gpa
          cnt += 1
        if isinstance(Person, Teacher):
          totstus += Person.numStudents
        if isinstance(Person, Admin):
          favW = Person.favWord
          if len(favW) > len(large):
            large = favW
          if len(favW) < len(sm):
            sm = favW

    print("Average sudents GPA: ", round(tot/cnt, 2))
    print("Total number of students taught: ", totstus)
    print("Smallest favorite admin word:", sm)
    print("Largest Favorite admin word: ", large)

  except Exception as e:
    print("Error: ", e)


if __name__ == "__main__":
  main()
