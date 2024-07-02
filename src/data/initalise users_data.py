import json

def main():
  """ Pour initialisation users file and admins file
  saved in ./data/).
  """

  users_filename = './data/users.json'
  admins_filename = './data/admins.json'

  users = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine",
    "admin": "4dm1N" 
  }

  admins = {
    "admin": "4dm1N" 
  }

  # save users_file and admins_file
  with open(users_filename, 'w', encoding='utf8') as f:
      json.dump(users,f)

  with open(admins_filename, 'w', encoding='utf8') as f:
      json.dump(admins,f)

main()