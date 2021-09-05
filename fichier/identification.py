

identifiant = "admin"
mot_de_passe = "password"

print("interface de connexion")

user_name = input("pseudo : ")
user_password = input(" mot de passe : ")

if user_name == identifiant and user_password == mot_de_passe  :
     print(" connexion au compte administrateur reussi" ,user_name )

else: 
 print("connexion perdu ")

