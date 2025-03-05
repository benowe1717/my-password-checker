# my-password-checker
A secure password checker using haveibeenpwned.com

Provide any number of passwords as command-line arguments to this program and it will check each password's hash
against the haveibeenpwned.com list of hashes. If the hash is found, you will be informed. If there is no output,
your password is safe!

![Quick GIF tutorial on using this program](https://github.com/benowe1717/my-password-checker/blob/write-docs/docs/usage.gif)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10.12+
- An internet connection

## Installing

To install <my-password-checker>, follow these steps:

1. Check out the repository on a machine with `Python 3.10.12+` installed:
`git clone https://github.com/benowe1717/my-password-checker.git`

2. Create a python virtual environment:
`python3.10 -m venv .venv`

3. Activate the newly created virtual environment:
`source .venv/bin/activate`

4. Install any required dependencies:
`python3 -m pip install -r requirements.txt`

For more information on virtual environments, see below:
- https://docs.python.org/3/library/venv.html
- https://www.pythonguis.com/tutorials/python-virtual-environments/

## Using

To use <my-password-checker>, simply execute the `main.py` script and provide at least one password:
`python3 main.py -p Password123`

You can also specify multiple passwords, as long as they are space-separated:
`python3 main.py --password Password123 Password1! HelloWorld`

## Contributing to <my-password-checker>

To contribute to <my-password-checker>, follow these steps:

1. Fork this repository
2. Create a branch: `git checkout -b <branch_name>`
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the Pull Request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

- [@benowe1717](https://github.com/benowe1717)

## Contact

For help or support on this repository, follow these steps:

- [Create an issue](https://github.com/benowe1717/my-password-checker/issues)

## License

This project uses the following license: GNU GPLv3.

## Sources

- https://github.com/scottydocs/README-template.md/blob/master/README.md
- https://choosealicense.com/
- https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
