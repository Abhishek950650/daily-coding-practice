#demonstrate template string function
from string import Template

def main():

    str1 = "You are Learning {0} by {1}".format('Python', 'Abhishek')

    print(str1)

    # create a template with placeholder
    templ = Template("You are Learning ${title} by ${author}")
    str2 = templ.substitute(title='Python', author='Abhishek')
    print(str2)

    data = {
        'title': 'Python',
        'author': 'Abhishek'
    }
    str3 = templ.substitute(data)
    print(str3)

if __name__ == "__main__":
    main()
