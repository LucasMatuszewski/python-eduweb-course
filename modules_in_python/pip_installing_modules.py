# PIP is a Python's Package Manager, like NPM in JS or Compose in PHP

# to check PIP version on your computer type in terminal:
#   pip -V
#   pip --version

# We can find modules in Python Package Index:
# https://pypi.org/
# it's like http://npmjs.com/ for JS

# to install an package globally type in console:
#   pip install password-strength

# you will install https://pypi.org/project/password-strength/

# IMPORTANT: if you use Python 3 but have also Python 2 installed on your computer
# you probably need to type "pip3" instead of "pip" (which will install for Python 2):
#   pip3 install password-strength

# To install package just for local user (when we don't have root/sudo access):
#   pip3 install --user password-strength
# It's still installed globally (not only for a project) but just for local user (not for a root)

# To unistall package:
#   pip3 uninstall password-strength

# To install PIP on a computer without Root, for local user:
#   python get-pip.py --user
# it will be installed in .local/bin

from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    length=8,  # min password length
    uppercase=2,  # min 2 uppercase letters
    numbers=1,  # min 1 digit
    special=1,  # min 1 special character
    nonletters=2  # min 2 non-letter characters (digits, special)
)
password = input("Provide a password: ")
tested_pass = policy.password(password)
print(tested_pass.strength())  # score should be more then 0,812
print(tested_pass.test())  # print tests provided password did NOT passed
