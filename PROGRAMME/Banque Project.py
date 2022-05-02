infos=[[],[],[],[],[],[]]
cltcompte=[[],[],[],[]]

fichier=open("Banque.txt","r")
contenu=fichier.read()
if contenu=='':
    print("BIENVENUE \n")
    print("Vous n avez pas de compte \n,Veuillez en créer 1,Merci")
    name=input("Veuillez renseignez votre nom...>")
    infos[0].append(name)
    print("\n")
    prenam=input("veuillez renseignez votre prenom...>")
    infos[1].append(prenam)
    print("\n")
    profession=input("Quell est votre Profession...>")
    infos[2].append(profession)
    print("\n")
    tel=int(input("Entrez votre numero de telephone...>"))
    infos[3].append(tel)
    print("\n")
    naissance=input("entrer votre date de naissance...>")
    infos[4].append(naissance)
    print("\n")
    date=input("veuillez renseigner la date d aujourd hui...>")
    infos[5].append(date)
    
    fichier=open("Banque.txt", "w")
    
    fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
    fichier.write("\n")
    fichier.write(str(name))
    fichier.write("\t")
    fichier.write(str(prenam))
    fichier.write("\t")
    fichier.write(str(profession))
    fichier.write("\t")
    fichier.write(str(tel))
    fichier.write("\t")
    fichier.write(str(naissance))
    fichier.write("\t")
    fichier.write("\t")
    fichier.write(str(date))
    
    nom=open("nom.txt", "w")
    prenom=open("prenom.txt", "w")
    num=open("numero.txt", "w")
    naiss=open("naissance.txt","w")
    date2=open("date.txt", "w")
    profession2=open("profession.txt", "w")
    
    nom.write(str(name))
    prenom.write(str(prenam))
    num.write(str(tel))
    date2.write(str(date))
    naiss.write(str(naissance))
    profession2.write(str(profession))
    
    nom.close()
    prenom.close()
    naiss.close()
    date2.close()
    num.close()
    profession2.close()
    fichier.close()

    
    print("\n")
    print("Votre Compte a été crée avec succes \n")
    username=input("Choisisez un Nom d utilisateur...>")
    montant_init=float(input("Veuillez déposer un montant initiale...>"))
    cltcompte[0].append(montant_init)
    compte=open("cltcompte.txt","w")
    compte.write(str(montant_init))
    compte.close()
    
    
    
    print("\n")
    print("Vos informations de compte sont :\n Nom: {}\n Prenom: {}\n Profession: {}\n Numéro de telephone: {}\n Date de Naissance: {}\nVotre compte a été crée le: {}".format((name),(prenam),(profession),(tel),(naissance),(date)))
    from random import randint
    init=0
    password=""                     
    choice="0123456789012005047006000904000320170111054005000050003000870040090"        
    chain=16
    while (init!=chain):
            init+=1
            choice2=randint(0,62)
            password=password+choice[choice2]
    print("Votre Nom d utilisateur est:", username)
    print("Le numero de compte qui vous a été attribué est le: {}".format(password))
    print("Votre solde Actuel est:",montant_init)
    
    print("\n")
    print("Appuyez sur n importe quelle touche pour continuer")   
    print("1-Nouveau Compte")
    print("2-Depot sur compte")
    print("3-retrait sur compte")
    print("4-Informations de compte")
    print("5-Modifier le compte ou et les informations liées au compte/Mettre a jour les informations")
    print("6-Supprimer le compte")
    print("7-Recevoir de transfert")
    print("8-Transferer de l argent")
    print("9-Solde de compte")
    print("10-Reinitialiser l application")
    print("11-Terminer")
    
    user=input("Quelle operation voulez vous effectuer...>")
    
    if user=="1":
        print("votre compte precedent sera supprimeé")
        del(cltcompte)
        del(infos)
        fichier=open("Banque.txt","w")
        fichier.close
        print("BIENVENUE \n")
        choix3=input("Voulez vous vraiment supprimer votre ancien compte..>")
        print("\n")
        if choix3=="oui":
            name=input("Veuillez renseignez votre nom...>")
            infos[0].append(name)
            print("\n")
            prenam=input("veuillez renseignez votre prenom...>")
            infos[1].append(prenam)
            print("\n")
            profession=input("Quell est votre Profession...>")
            infos[2].append(profession)
            print("\n")
            tel=int(input("Entrez votre numero de telephone...>"))
            infos[3].append(tel)
            print("\n")
            naissance=input("entrer votre date de naissance...>")
            infos[4].append(naissance)
            print("\n")
            date=input("veuillez renseigner la date d aujourd hui...>")
            infos[5].append(date)
            
            fichier=open("Banque.txt", "w")
            
            fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
            fichier.write("\n")
            fichier.write(str(name))
            fichier.write("\t")
            fichier.write(str(prenam))
            fichier.write("\t")
            fichier.write(str(profession))
            fichier.write("\t")
            fichier.write(str(tel))
            fichier.write("\t")
            fichier.write(str(naissance))
            fichier.write("\t")
            fichier.write(str(date))
            
            nom=open("nom.txt", "w")
            prenom=open("prenom.txt", "w")
            num=open("numero.txt", "w")
            naiss=open("naissance.txt","w")
            date2=open("date.txt", "w")
            profession2=open("profession.txt", "w")
            
            nom.write(str(name))
            prenom.write(str(prenam))
            num.write(str(tel))
            date2.write(str(date))
            naiss.write(str(naissance))
            profession2.write(str(profession))
            
        else:
            print("ok")

            
            prenom.close()
            naiss.close()
            date2.close()
            num.close()
            profession2.close()
        
    elif user=="2":
        montant=int(input("Entrer la somme a déposer sur le compte...>"))
        montant_init=montant_init+montant
        cltcompte[0]=montant_init
        print("votre compte a ete credité de:",montant,"\nlemontant actuel sur votre compte est de:",montant_init)
        print("Depot effectué avec succes")
        compte=open("cltcompte.txt","w")
        compte.write(str(montant_init))
        compte.close()
    elif user=="3":
        retrait=int(input("Saisisez le montant a retirer...>"))
        print("\n")
        montant_init=montant_init-retrait
        cltcompte[1]=retrait
        compte=open("cltcompte.txt","w")
        compte.write(str(montant_init))
        compte.close()
        print("votre compte a ete debité de:",retrait,"\nlemontant actuel sur votre compte est de:",montant_init)
        print("\n")
        print("Retrait effectué avec succes")
       
    elif user=="4":
        print("Voici les Informations liées a votre compte:")
        print("Vos informations de compte sont :\n Nom: {}\n Prenom: {}\n Profession: {}\n Numéro de telephone: {}\n Date de Naissance: {}\nVotre compte a été crée le: {}".format((name),(prenam),(profession),(tel),(naissance),(date)))
   
        print("Le montant actuel sur votre compte est de:",montant_init)
    elif user=="5":
        print("choisir\na-une seule information\nb-informations completes de Compte")
        print("\n")
        choix1=input("Que voulez vous modifiez? ")
        print("\n")
        if choix1=="a":
            print("nom:modifier le nom\nprenom:modifier le prenom\nprofession: modifier la profession\nnumero:modifier le numero de telephone\ncomptenum:modifier le numéro de compte\nusername:modifier le nom utilisateur")
            print("\n")
            choix2=input("Quelle information voulez vous modifier")
            if choix2=="nom" or choix2=="Nom":
                print("Voici le Nom auquel est actuellement inscrit votre compte:",infos[0])
                print("\n")
                
                choix3=input("Voulez-vous vraiment le remplacer? ")
                print("\n")
                if choix3=="oui":
                    newname=input("Veuillez entrer le nouveau Nom...>")
                    print("\n")
                    infos[0]=newname
                    print("nom modifié",infos[0])
                else:
                    print("super")
                    user=input("Quelle operation voulez vous effectuer...>")
            elif choix2=="prenom":
                print("Voici le Prenom auquel est actuellement inscrit votre compte:",infos[1])
                print("\n")
                choix3=input("Voulez-vous vraiment le remplacer? ")
                print("\n")
                if choix3=="oui":
                    newprename=input("Veuillez entrer le nouveau prénom...>")
                    infos[1]=newprename
                else:
                    print("super")
                    user=input("Quelle operation voulez vous effectuer...>")
            elif choix2=="profession" or choix2=="Profession":
                print("Vous etes actuellement inscrit en tant que:",infos[2])
                print("\n")
                choix3=input("Voulez-vous vraiment la remplacer? ")
                if choix3=="oui":
                    newprof=input("Votre Profession...>")
                    infos[2]=newprof
                else:
                    print("super")
                    user=input("Quelle operation voulez vous effectuer...>")
            elif choix2=="numero" or choix2=="Numero":
                print("Vous etes actuellement inscrit en tant que:",infos[3])
                print("\n")
                choix3=input("Voulez-vous vraiment le remplacer? ")
                if choix3=="oui":
                    newtel=int(input("Entrer le nouveau numéro de telephone...>"))
                    infos[3]=newtel
                else:
                    print("super")
                    user=input("Quelle operation voulez vous effectuer...>")
            elif choix2=="comptenum":
                print("NB:Vous ne pouvez pas vous meme vous attribuer un numero de compte,\nsi vous voulez en changer un nouveau vous sera automatiquement generé")
                print("votre ancien numéro de compte est:",password)
                choix3=input("Voulez-vous vraiment le remplacer? ")
                if choix3=="oui":
                    init=0
                    newpassword=""                     
                    choice="0123456789012005047006000904000320170111054005000050003000870040090"        
                    chain=9
                    while (init!=chain):
                        init+=1
                        choice2=randint(0,62)
                        newpassword=newpassword+choice[choice2]
                        password=newpassword
                    print("Votre Numéro de compte a bien été modifié")
                    print("Voici votre Nouveau numéro de compte:",password)
                else:
                    print("super")
                    user=input("Quelle operation voulez vous effectuer...>")
            elif choix2=="username" or choix2=="Username":
                print("Votre nom d utilisateur actuel est :",username)
                choix3=input("Voulez-vous vraiment le remplacer? ")
                if choix3=="oui":
                    newuser=input("Votre Nouveau nom d utilisateur...>")
                    username=newuser
                    print("Nom d utilisateur modifié")
                    print("Voici votre nouveau nom d utilisateur:",username)
                    
                else:
                    print("super")
                    user=input("Quelle operation voulez vous effectuer...>")
            
        elif choix1=="b":
            newname=input("Veuillez entrer le nouveau Nom...>")
            infos[0]=newname
            newprename=input("Veuillez entrer le nouveau prenom...>")
            infos[1]=newprename
            newprof=input("Votre Profession...>")
            infos[2]=newprof
            newtel=int(input("Entrer le nouveau numéro de telephone...>"))
            infos[3]=newtel
            newuser=input("Votre Nouveau nom d utilisateur...>")
            username=newuser
            print("Voici les Informations liées a votre compte:")
        
            print("Nom: {}\nPrenom: {}\nProfession: {}\nNumero de telephone:{}\nDate de naissance: {}\nDate de création de compte{}".format(infos[0],infos[1],infos[2],infos[3],infos[4],infos[5]))
            print("\n")
            print("Le montant actuel sur votre compte est de:{}".format(cltcompte[0]))
     
    elif user=="6":
        print("choisir\na- supprimer une seule information\n\tb-supprimer les informations completes")
        choix1=input("Que voulez vous supprimer...>")
        if choix1=="a":
            print("nom:supprimer le nom\nprenom:supprimer le prenom\nprofession: supprimer la profession\nnumero:supprimer le numero de telephone\ncomptenum:supprimer le numéro de compte\nusername:supprimer le nom utilisateur")
            choix2=input("Quelle information voulez vous supprimer...>")
            if choix2=="nom" or choix2=="Nom":
                del(infos[0])
                print("information bien supprimée")
            elif choix2=="prenom":
                del(infos[1])
                print("information bien supprimée")

            elif choix2=="profession":
                del(infos[2])
                print("information bien supprimée")
            elif choix2=="numero":
                del(infos[3])
                print("information bien supprimée")
            elif choix2=="comptenum":
                del(password)
                print("information bien supprimée")
            elif choix2=="username":
                del(username)
                print("information bien supprimée")

        elif choix1=="b":
            del(infos[0][0])
            del(infos[1][0])
            del(infos[2][0])
            del(infos[3][0])
            print("Informations bien supprimées")
            
    elif user=="7":
        fichier2=open("recu.txt","r")
        contenu2=fichier2.read()
        if contenu2==" ":
            print("Vous n avez recu aucun transfert")
            
        else:
            print("Vous avez recu un transfert de :",cltcompte[2])
    elif user=="8":
        transfert=int(input("saisisez le montant a transferer...>"))
        receptnum=int(input("saisissez le numero de compte de reception du transfert")) 
        compte=open("cltcompte.txt","w")
        compte.write(str(cltcompte[3]))
        compte.close()
        cltcompte[0]=montant_init-transfert
        print(transfert,"a bien été transféré depuis votre compte vers,:", receptnum)
        print("le montant actuel present sur votre compte s éleve a :",cltcompte[0])
    elif user=="9":
        print("Le montant actuel sur votre compte est de:",montant_init)
    elif user=="10":
        fichier=open("Banque.txt","w")
        fichier.close()
        print("Application reinitialisée")
    elif user=="11":
        inpt=input("Terminer?")
        if inpt=="oui" or inpt=="OUI" or inpt=="Oui" or inpt=="OUi" or inpt=="oUI" or inpt=="oUi":
            while inpt=="oui" or inpt=="OUI" or inpt=="Oui" or inpt=="OUi" or inpt=="oUI" or inpt=="oUi":
                break
        else:
            choix=input("Voulez-vous continuez...>")
            if choix=="oui" or choix=="Oui":
                user=input("Quelle operation voulez vous effectuer...>")  
                                    
                
    while user=="1"or user=="2" or user=="3" or user=="4" or user=="5" or user=="6" or user=="7" or user=="8" or user=="9":
        choix=input("Voulez-vous continuez...>")
        print("\n")
        if choix=="oui" or choix=="Oui":
            user=input("Quelle operation voulez vous effectuer...>")         
            if user=="1":
                print("votre compte precedent sera supprimeé")
                del(cltcompte)
                del(infos)
                fichier=open("Banque.txt","w")
                fichier.close
                print("BIENVENUE \n")
                print("Vous n avez pas de compte ,Veuillez en créer 1,Merci")
                print("\t\tAllez y")
                name=input("Veuillez renseignez votre nom...>")
                infos[0].append(name)
                print("\n")
                prenam=input("veuillez renseignez votre prenom...>")
                infos[1].append(prenam)
                print("\n")
                profession=input("Quell est votre Profession...>")
                infos[2].append(profession)
                print("\n")
                tel=int(input("Entrez votre numero de telephone...>"))
                infos[3].append(tel)
                print("\n")
                naissance=input("entrer votre date de naissance...>")
                infos[4].append(naissance)
                print("\n")
                date=input("veuillez renseigner la date d aujourd hui...>")
                infos[5].append(date)
                
                fichier=open("Banque.txt", "w")
                
                fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
                fichier.write("\n")
                fichier.write(str(name))
                fichier.write("\t")
                fichier.write(str(prenam))
                fichier.write("\t")
                fichier.write(str(profession))
                fichier.write("\t")
                fichier.write(str(tel))
                fichier.write("\t")
                fichier.write(str(naissance))
                fichier.write("\t")
                fichier.write(str(date))
                
                nom=open("nom.txt", "w")
                prenom=open("prenom.txt", "w")
                num=open("numero.txt", "w")
                naiss=open("naissance.txt","w")
                date2=open("date.txt", "w")
                profession2=open("profession.txt", "w")
                
                nom.write(str(name))
                prenom.write(str(prenam))
                num.write(str(tel))
                date2.write(str(date))
                naiss.write(str(naissance))
                profession2.write(str(profession))
                


                nom.close()
                prenom.close()
                naiss.close()
                date2.close()
                num.close()
                profession2.close()

            elif user=="2":
                montant=int(input("Entrer la somme a déposer sur le compte...>"))
                montant_init=montant_init+montant
                cltcompte[0]=montant_init
                print("votre compte a ete credité de:",montant,"\nlemontant actuel sur votre compte est de:",montant_init)
                print("Depot effectué avec succes")
                compte=open("cltcompte.txt","w")
                compte.write(str(montant_init))
                compte.close()
            elif user=="3":
                retrait=int(input("Saisisez le montant a retirer...>"))
                montant_init=montant_init-retrait
                cltcompte[1]=retrait
                compte=open("cltcompte.txt","w")
                compte.write(str(montant_init))
                compte.close()
                print("votre compte a ete debité de:",retrait,"\nlemontant actuel sur votre compte est de:",montant_init)
                print("Retrait effectué avec succes")
       
               
            elif user=="4":
                print("Voici les Informations liées a votre compte:")
                print("Vos informations de compte sont :\n Nom: {}\n Prenom: {}\n Profession: {}\n Numéro de telephone: {}\n Date de Naissance: {}\nVotre compte a été crée le: {}".format((name),(prenam),(profession),(tel),(naissance),(date)))
   
                print("Le montant actuel sur votre compte est de:",montant_init)
            
            elif user=="5":
                print("choisir\na-une seule information\nb-informations completes de Compte")
                choix1=input("Que voulez vous modifiez? ")
                if choix1=="a":
                    print("nom:modifier le nom\nprenom:modifier le prenom\nprofession: modifier la profession\nnumero:modifier le numero de telephone\ncomptenum:modifier le numéro de compte\nusername:modifier le nom utilisateur")
                    choix2=input("Quelle information voulez vous modifier")
                    if choix2=="nom" or choix2=="Nom":
                        print("Voici le Nom auquel est actuellement inscrit votre compte:",infos[0])
                        choix3=input("Voulez-vous vraiment le remplacer? ")
                        if choix3=="oui":
                            newname=input("Veuillez entrer le nouveau Nom...>")
                            infos[0]=newname
                            print("nom modifié",infos[0])
                        else:
                            print("super")
                            user=input("Quelle operation voulez vous effectuer...>")
                    elif choix2=="prenom":
                        print("Voici le Prenom auquel est actuellement inscrit votre compte:",infos[1])
                        choix3=input("Voulez-vous vraiment le remplacer? ")
                        if choix3=="oui":
                            newprename=input("Veuillez entrer le nouveau prénom...>")
                            infos[1]=newprename
                        else:
                            print("super")
                            user=input("Quelle operation voulez vous effectuer...>")
                    elif choix2=="profession" or choix2=="Profession":
                        print("Vous etes actuellement inscrit en tant que:",infos[2])
                        choix3=input("Voulez-vous vraiment la remplacer? ")
                        if choix3=="oui":
                            newprof=input("Votre Profession...>")
                            infos[2]=newprof
                        else:
                            print("super")
                            user=input("Quelle operation voulez vous effectuer...>")
                    elif choix2=="numero" or choix2=="Numero":
                        print("Vous etes actuellement inscrit en tant que:",infos[3])
                        choix3=input("Voulez-vous vraiment le remplacer? ")
                        if choix3=="oui":
                            newtel=int(input("Entrer le nouveau numéro de telephone...>"))
                            infos[3]=newtel
                        else:
                            print("super")
                            user=input("Quelle operation voulez vous effectuer...>")
                    elif choix2=="comptenum":
                        print("NB:Vous ne pouvez pas vous meme vous attribuer un numero de compte,\nsi vous voulez en changer un nouveau vous sera automatiquement generé")
                        print("votre ancien numéro de compte est:",password)
                        choix3=input("Voulez-vous vraiment le remplacer? ")
                        if choix3=="oui":
                            init=0
                            newpassword=""                     
                            choice="0123456789012005047006000904000320170111054005000050003000870040090"        
                            chain=9
                            while (init!=chain):
                                init+=1
                                choice2=randint(0,62)
                                newpassword=newpassword+choice[choice2]
                                password=newpassword
                            print("Votre Numéro de compte a bien été modifié")
                            print("Voici votre Nouveau numéro de compte:",password)
                        else:
                            print("super")
                            user=input("Quelle operation voulez vous effectuer...>")
                    elif choix2=="username" or choix2=="Username":
                        print("Votre nom d utilisateur actuel est :",username)
                        choix3=input("Voulez-vous vraiment le remplacer? ")
                        if choix3=="oui":
                            newuser=input("Votre Nouveau nom d utilisateur...>")
                            username=newuser
                            print("Nom d utilisateur modifié")
                            print("Voici votre nouveau nom d utilisateur:",username)
                            
                        else:
                            print("super")
                            user=input("Quelle operation voulez vous effectuer...>")
                    
                elif choix1=="b":
                    newname=input("Veuillez entrer le nouveau Nom...>")
                    infos[0]=newname
                    newprename=input("Veuillez entrer le nouveau prenom...>")
                    infos[1]=newprename
                    newprof=input("Votre Profession...>")
                    infos[2]=newprof
                    newtel=int(input("Entrer le nouveau numéro de telephone...>"))
                    infos[3]=newtel
                    newuser=input("Votre Nouveau nom d utilisateur...>")
                    username=newuser
                    print("Voici les Informations liées a votre compte:")
                
                    print("Nom: {}\nPrenom: {}\nProfession: {}\nNumero de telephone:{}\nDate de naissance: {}\nDate de création de compte{}".format(infos[0],infos[1],infos[2],infos[3],infos[4],infos[5]))
                    print("\n")
                    print("Le montant actuel sur votre compte est de:{}".format(cltcompte[0]))
             
            elif user=="6":
                print("choisir\na- supprimer une seule information\n \tb-supprimer les informations completes")
                choix1=input("Que voulez vous supprimer...>")
                if choix1=="a":
                    print("nom:supprimer le nom\nprenom:supprimer le prenom\nprofession: supprimer la profession\nnumero:supprimer le numero de telephone\ncomptenum:supprimer le numéro de compte\nusername:supprimer le nom utilisateur")
                    choix2=input("Quelle information voulez vous supprimer...>")
                    if choix2=="nom" or choix2=="Nom":
                        del(infos[0])
                        print("information bien supprimée")
                    elif choix2=="prenom":
                        del(infos[1])
                        print("information bien supprimée")

                    elif choix2=="profession":
                        del(infos[2])
                        print("information bien supprimée")
                    elif choix2=="numero":
                        del(infos[3])
                        print("information bien supprimée")
                    elif choix2=="comptenum":
                        del(password)
                        print("information bien supprimée")
                    elif choix2=="username":
                        del(username)
                        print("information bien supprimée")

                elif choix1=="b":
                    del(infos[0][0])
                    del(infos[1][0])
                    del(infos[2][0])
                    del(infos[3][0])
                    del(password)
                    del(username)
                    print("Informations bien supprimées")
            elif user=="7":
                fichier2=open("recu.txt","r")
                contenu2=fichier2.read()
                if contenu2==" ":
                    print("Vous n avez recu aucun transfert")
                    
                else:
                    print("Vous avez recu un transfert de :",cltcompte[2])
            elif user=="8":
                transfert=int(input("saisisez le montant a transferer...>"))
                montant_init=montant_init-transfert
                cltcompte[3]=transfert
                print("votre compte a ete debité de:",transfert,"\nlemontant actuel sur votre compte est de:",montant_init)
                print("Transfert effectué avec succes")
                receptnum=int(input("saisissez le numero de compte de reception du transfert"))
                compte=open("cltcompte.txt","w")
                compte.write(str(cltcompte[3]))
                compte.close()
                print(transfert,"a bien été transféré depuis votre compte vers,:", receptnum)
                print("le montant actuel present sur votre compte s éleve a :",montant_init)
            elif user=="9":
                print("Le montant actuel sur votre compte est de:",montant_init)
            elif user=="10":
                fichier=open("Banque.txt","w")
                fichier.close()
                print("Application reinitialisée")
            elif user=="11":
                inpt=input("Terminer?")
                if inpt=="oui" or inpt=="OUI" or inpt=="Oui" or inpt=="OUi" or inpt=="oUI" or inpt=="oUi":
                     while inpt=="oui" or inpt=="OUI" or inpt=="Oui" or inpt=="OUi" or inpt=="oUI" or inpt=="oUi":
                        break
                else:
                    choix=input("Voulez-vous continuez...>")
                    if choix=="oui" or choix=="Oui":
                        user=input("Quelle operation voulez vous effectuer...>")  
                                    
                
        else:
            break
else:
    print("Appuyez sur n importe quelle touche pour continuer")   
    print("1-Nouveau Compte")
    print("2-Depot sur compte")
    print("3-retrait sur compte")
    print("4-Informations de compte")
    print("5-Modifier le compte ou et les informations liées au compte/Mettre a jour les informations")
    print("6-Supprimer le compte")
    print("7-Recevoir de transfert")
    print("8-Transferer de l argent")
    print("9-Solde de compte")
    print("10-Reinitialiser l application")
    print("11-Terminer")
    print("\n")
    
    user=input("Quelle operation voulez vous effectuer...>")
    print("\n")
    if user=="1":
        print("votre compte precedent sera supprimeé")
        del(cltcompte)
        del(infos)
        fichier=open("Banque.txt","w")
        fichier.close
        print("BIENVENUE \n")
        print("Vous n avez pas de compte ,Veuillez en créer 1,Merci")
        print("\t\tAllez y")
        name=input("Veuillez renseignez votre nom...>")
        infos[0].append(name)
        print("\n")
        prenam=input("veuillez renseignez votre prenom...>")
        infos[1].append(prenam)
        print("\n")
        profession=input("Quell est votre Profession...>")
        infos[2].append(profession)
        print("\n")
        tel=int(input("Entrez votre numero de telephone...>"))
        infos[3].append(tel)
        print("\n")
        naissance=input("entrer votre date de naissance...>")
        infos[4].append(naissance)
        print("\n")
        date=input("veuillez renseigner la date d aujourd hui...>")
        infos[5].append(date)
        
        fichier=open("Banque.txt", "w")
        
        fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
        fichier.write("\n")
        fichier.write(str(name))
        fichier.write("\t")
        fichier.write(str(prenam))
        fichier.write("\t")
        fichier.write(str(profession))
        fichier.write("\t")
        fichier.write(str(tel))
        fichier.write("\t")
        fichier.write(str(naissance))
        fichier.write("\t")
        fichier.write(str(date))
        
        nom=open("nom.txt", "w")
        prenom=open("prenom.txt", "w")
        num=open("numero.txt", "w")
        naiss=open("naissance.txt","w")
        date2=open("date.txt", "w")
        profession2=open("profession.txt", "w")
        
        nom.write(str(name))
        prenom.write(str(prenam))
        num.write(str(tel))
        date2.write(str(date))
        naiss.write(str(naissance))
        profession2.write(str(profession))
        nom.close()
        prenom.close()
        naiss.close()
        date2.close()
        num.close()
        profession2.close()
    elif user=="2":
        compte=open("cltcompte.txt","r")
        compte2=compte.read()
        compte3=compte2.split(" ")
        montant1=compte3[0]
        montant_init=float(montant1)
        montant=int(input("Entrer la somme a déposer sur le compte...>"))
        montant_init=montant_init+montant
        cltcompte[0]=montant_init
        print("votre compte a ete credité de:",montant,"\nlemontant actuel sur votre compte est de:",montant_init)
        print("Depot effectué avec succes")
        compte=open("cltcompte.txt","w")
        compte.write(str(montant_init))
        compte.close()
    
    elif user=="3":
        compte=open("cltcompte.txt","r")
        compte2=compte.read()
        compte3=compte2.split(" ")
        montant1=compte3[0]
        montant_init=float(montant1)
        retrait=int(input("Saisisez le montant a retirer...>"))
        print("\n")
        montant_init=montant_init-retrait
        cltcompte[1]=retrait
        compte=open("cltcompte.txt","w")
        compte.write(str(montant_init))
        compte.close()
        print("votre compte a ete debité de:",retrait,"\nlemontant actuel sur votre compte est de:",montant_init)
        print("\n")
        print("Retrait effectué avec succes")
    elif user=="4":
        print("Voici les Informations liées a votre compte:")
        compte=open("cltcompte.txt","r")
        compte2=compte.read()
        compte3=compte2.split(" ")
        montant1=compte3[0]
        montant_init=float(montant1)      
        fichier=open("Banque.txt","r")
        contenu=fichier.read()
        print(contenu)
        print("\n")
        print("Le montant actuel sur votre compte est de--->",montant_init)
    elif user=="5":
        print("choisir\na-une seule information\nb-informations completes de Compte")
        choix1=input("Que voulez vous modifiez? ")
        if choix1=="a":
            print("nom:modifier le nom\nprenom:modifier le prenom\nprofession: modifier la profession\nnumero:modifier le numero de telephone")
            print("\n")
            choix2=input("Quelle information voulez vous modifier...>")
            if choix2=="nom" or choix2=="Nom":
                name=input("Veuillez renseignez votre nom...>")
                infos[0].append(name)
                print("\n")
                fichier=open("Banque.txt","a")
                fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
                fichier.write("\n")
                fichier.write(str(name))
                fichier.write("\t")
                nom=open("nom.txt", "w")
                nom.write(str(name))
                nom.close()
                fichier.close()
            elif choix2=="prenom":
                prenom=open("prenom.txt", "w")
                prenom.close()
                fichier=open("Banque.txt","a")
                fichier.write("\t")
                prenom=open("prenom.txt", "w")
                prenam=input("veuillez renseignez votre prenom...>")
                print("\n")
                infos[1].append(prenam)
                print("\n")
                fichier.write(str(prenam))
                prenom.write(str(prenam))
                prenom.close()
                fichier.close()
                print("information bien modifiée ")

            elif choix2=="profession":
                profession2=open("profession.txt", "w")
                profession2.close()
                fichier=open("Banque.txt", "a")
                profession2=open("profession.txt", "w")
                profession=input("Quell est votre Profession...>")
                print("\n")
                profession2.write(str(profession))
                fichier.write(str(profession))
                fichier.write("\t")
                infos[2].append(profession)
                print("\n")
                profession2.close()
                fichier.close()
                print("information bien modifié")
            elif choix2=="numero":
                num=open("numero.txt","w")
                num.close()
                fichier=open("Banque.txt","a")
                num=open("numero.txt", "w")
                tel=int(input("Entrez votre numero de telephone...>"))
                print("\n")
                fichier.write(str(tel))
                num.write(str(tel))
                num.close()
                fichier.close()
                print("information bien supprimée")
        elif choix1=="b":
            infos=[[],[],[],[],[],[]]
            cltcompte=[[],[],[],[]]
            name=input("Veuillez renseignez votre nom...>")
            infos[0].append(name)
            print("\n")
            prenam=input("veuillez renseignez votre prenom...>")
            infos[1].append(prenam)
            print("\n")
            profession=input("Quell est votre Profession...>")
            infos[2].append(profession)
            print("\n")
            tel=int(input("Entrez votre numero de telephone...>"))
            infos[3].append(tel)
            print("\n")
            naissance=input("entrer votre date de naissance...>")
            print("\n")
            infos[4].append(naissance)
            print("\n")
            date=input("veuillez renseigner la date d aujourd hui...>")
            infos[5].append(date)
            
            fichier=open("Banque.txt", "w")
            
            fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
            fichier.write("\n")
            fichier.write(str(name))
            fichier.write("\t")
            fichier.write(str(prenam))
            fichier.write("\t")
            fichier.write(str(profession))
            fichier.write("\t")
            fichier.write(str(tel))
            fichier.write("\t")
            fichier.write(str(naissance))
            fichier.write("\t")
            fichier.write(str(date))
            
            nom=open("nom.txt", "w")
            prenom=open("prenom.txt", "w")
            num=open("numero.txt", "w")
            naiss=open("naissance.txt","w")
            date2=open("date.txt", "w")
            profession2=open("profession.txt", "w")
            
            nom.write(str(name))
            prenom.write(str(prenam))
            num.write(str(tel))
            date2.write(str(date))
            naiss.write(str(naissance))
            profession2.write(str(profession))
            

            fichier.close()
            nom.close()
            prenom.close()
            naiss.close()
            date2.close()
            num.close()
            profession2.close()

            
            print("\n")
            print("Votre Compte a été crée avec succes \n")
            username=input("Choisisez un Nom d utilisateur...>")
            montant_init=float(input("Veuillez déposer un montant initiale...>"))
            cltcompte[0].append(montant_init)
            compte=open("cltcompte.txt","w")
            compte.write(str(montant_init))
            compte.close()
            
            
            
            print("\n")
            print("Vos informations de compte sont :\n Nom: {}\n Prenom: {}\n Profession: {}\n Numéro de telephone: {}\n Date de Naissance: {}\nVotre compte a été crée le: {}".format((name),(prenam),(profession),(tel),(naissance),(date)))
            from random import randint
            init=0
            password=""                     
            choice="0123456789012005047006000904000320170111054005000050003000870040090"        
            chain=16
            while (init!=chain):
                    init+=1
                    choice2=randint(0,62)
                    password=password+choice[choice2]
            print("Votre Nom d utilisateur est:", username)
            print("Le numero de compte qui vous a été attribué est le: {}".format(password))
            print("Votre solde Actuel est:",montant_init)
           
                    
            
    elif user=="6":
        fichier=open("Banque.txt","w")
        fichier.close()
        compte=open("cltcompte.txt","w")
        compte.close()
        nom=open("nom.txt", "w")
        nom.close()
        num=open("numero.txt", "w")
        num.close()
        naiss=open("naissance.txt","w")
        naiss.close()
        date2=open("date.txt", "w")
        date2.close()
        profession2=open("profession.txt", "w")
        profession2.close()
    elif user=="7":
        fichier2=open("recu.txt","r")
        contenu2=fichier2.read()
        if contenu2==" ":
            print("Vous n avez recu aucun transfert")
            
        else:
            print("Vous avez recu un transfert de :",cltcompte[2])
    elif user=="8":
        compte=open("cltcompte.txt","r")
        compte2=compte.read()
        compte3=compte2.split(" ")
        montant1=compte3[0]
        montant_init=float(montant1)
        transfert=int(input("saisisez le montant a transferer...>"))
        montant_init=montant_init-transfert
        cltcompte[3]=transfert
        print("votre compte a ete debité de:",transfert,"\nlemontant actuel sur votre compte est de:",montant_init)
        print("Transfert effectué avec succes")
        receptnum=int(input("saisissez le numero de compte de reception du transfert"))
        compte=open("cltcompte.txt","w")
        compte.write(str(cltcompte[3]))
        compte.close()
        print(transfert,"a bien été transféré depuis votre compte vers,:", receptnum)
        print("le montant actuel present sur votre compte s éleve a :",montant_init)
    elif user=="9":
        print("Le montant actuel sur votre compte est de:",montant_init)
    elif user=="10":
        fichier=open("Banque.txt","w")
        fichier.close()
        print("Application reinitialisée")
    elif user=="11":
        inpt=input("Terminer?")
        if inpt=="oui" or inpt=="OUI" or inpt=="Oui" or inpt=="OUi" or inpt=="oUI" or inpt=="oUi":
            while inpt=="oui" or inpt=="OUI" or inpt=="Oui" or inpt=="OUi" or inpt=="oUI" or inpt=="oUi":
                break
        else:
            choix=input("Voulez-vous continuez...>")
            if choix=="oui" or choix=="Oui":
                user=input("Quelle operation voulez vous effectuer...>")
    while user=="1"or user=="2" or user=="3" or user=="4" or user=="5" or user=="6" or user=="7" or user=="8" or user=="9":
        choix=input("Voulez-vous continuez...>")
        if choix=="oui" or choix=="Oui":
            user=input("Quelle operation voulez vous effectuer...>")
            print("\n")
            if user=="1":
                print("votre compte precedent sera supprimeé")
                del(cltcompte)
                del(infos)
                fichier=open("Banque.txt","w")
                fichier.close
                print("BIENVENUE \n")
                print("\n")
                print("Vous n avez pas de compte ,Veuillez en créer 1,Merci")
                print("\n")
                print("\t\tAllez y")
                name=input("Veuillez renseignez votre nom...>")
                infos[0].append(name)
                print("\n")
                prenam=input("veuillez renseignez votre prenom...>")
                infos[1].append(prenam)
                print("\n")
                profession=input("Quell est votre Profession...>")
                infos[2].append(profession)
                print("\n")
                tel=int(input("Entrez votre numero de telephone...>"))
                infos[3].append(tel)
                print("\n")
                naissance=input("entrer votre date de naissance...>")
                infos[4].append(naissance)
                print("\n")
                date=input("veuillez renseigner la date d aujourd hui...>")
                infos[5].append(date)
                
                fichier=open("Banque.txt", "w")
                
                fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
                fichier.write("\n")
                fichier.write(str(name))
                fichier.write("\t")
                fichier.write(str(prenam))
                fichier.write("\t")
                fichier.write(str(profession))
                fichier.write("\t")
                fichier.write(str(tel))
                fichier.write("\t")
                fichier.write(str(naissance))
                fichier.write("\t")
                fichier.write(str(date))
                
                nom=open("nom.txt", "w")
                prenom=open("prenom.txt", "w")
                num=open("numero.txt", "w")
                naiss=open("naissance.txt","w")
                date2=open("date.txt", "w")
                profession2=open("profession.txt", "w")
                
                nom.write(str(name))
                prenom.write(str(prenam))
                num.write(str(tel))
                date2.write(str(date))
                naiss.write(str(naissance))
                profession2.write(str(profession))
                nom.close()
                prenom.close()
                naiss.close()
                date2.close()
                num.close()
                profession2.close()
            elif user=="2":
                compte=open("cltcompte.txt","r")
                compte2=compte.read()
                compte3=compte2.split(" ")
                montant1=compte3[0]
                montant_init=float(montant1)
                montant=int(input("Entrer la somme a déposer sur le compte...>"))
                print("\n")
                montant_init=montant_init+montant
                cltcompte[0]=montant_init
                print("votre compte a ete credité de:",montant,"\nlemontant actuel sur votre compte est de:",montant_init)
                print("\n")
                print("Depot effectué avec succes")
                compte=open("cltcompte.txt","w")
                compte.write(str(montant_init))
                compte.close()
            
            elif user=="3":
                compte=open("cltcompte.txt","r")
                compte2=compte.read()
                compte3=compte2.split(" ")
                montant1=compte3[0]
                montant_init=float(montant1)
                retrait=int(input("Saisisez le montant a retirer...>"))
                print("\n")
                montant_init=montant_init-retrait
                cltcompte[1]=retrait
                compte=open("cltcompte.txt","w")
                compte.write(str(montant_init))
                compte.close()
                print("votre compte a ete debité de:",retrait,"\nlemontant actuel sur votre compte est de:",montant_init)
                print("\n")
                print("Retrait effectué avec succes")
            elif user=="4":
                print("Voici les Informations liées a votre compte:")
                print("\n")
                compte=open("cltcompte.txt","r")
                compte2=compte.read()
                compte3=compte2.split(" ")
                montant1=compte3[0]
                montant_init=float(montant1)      
                fichier=open("Banque.txt","r")
                contenu=fichier.read()
                print(contenu)
                print("\n")
                print("Le montant actuel sur votre compte est de:",montant_init)
            elif user=="5":
                print("choisir\na-une seule information\nb-informations completes de Compte")
                choix1=input("Que voulez vous modifiez? ")
                if choix1=="a":
                    print("nom:modifier le nom\nprenom:modifier le prenom\nprofession: modifier la profession\nnumero:modifier le numero de telephone")
                    choix2=input("Quelle information voulez vous modifier...>")
                    if choix2=="nom" or choix2=="Nom":
                        name=input("Veuillez renseignez votre nom...>")
                        infos[0].append(name)
                        print("\n")
                        fichier=open("Banque.txt","a")
                        fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
                        fichier.write("\n")
                        fichier.write(str(name))
                        fichier.write("\t")
                        nom=open("nom.txt", "w")
                        nom.write(str(name))
                        nom.close()
                        fichier.close()
                    elif choix2=="prenom":
                        prenom=open("prenom.txt", "w")
                        prenom.close()
                        fichier=open("Banque.txt","a")
                        fichier.write("\t")
                        prenom=open("prenom.txt", "w")
                        prenam=input("veuillez renseignez votre prenom...>")
                        print("\n")
                        infos[1].append(prenam)
                        print("\n")
                        fichier.write(str(prenam))
                        prenom.write(str(prenam))
                        prenom.close()
                        fichier.close()
                        print("information bien modifiée ")

                    elif choix2=="profession":
                        profession2=open("profession.txt", "w")
                        profession2.close()
                        fichier=open("Banque.txt", "a")
                        profession2=open("profession.txt", "w")
                        profession=input("Quell est votre Profession...>")
                        print("\n")
                        profession2.write(str(profession))
                        fichier.write(str(profession))
                        fichier.write("\t")
                        infos[2].append(profession)
                        print("\n")
                        profession2.close()
                        fichier.close()
                        print("information bien modifié")
                    elif choix2=="numero":
                        num=open("numero.txt","w")
                        num.close()
                        fichier=open("Banque.txt","a")
                        num=open("numero.txt", "w")
                        tel=int(input("Entrez votre numero de telephone...>"))
                        print("\n")
                        fichier.write(str(tel))
                        num.write(str(tel))
                        num.close()
                        fichier.close()
                        print("information bien supprimée")
                elif choix1=="b":
                    name=input("Veuillez renseignez votre nom...>")
                    infos[0].append(name)
                    print("\n")
                    prenam=input("veuillez renseignez votre prenom...>")
                    infos[1].append(prenam)
                    print("\n")
                    profession=input("Quell est votre Profession...>")
                    infos[2].append(profession)
                    print("\n")
                    tel=int(input("Entrez votre numero de telephone...>"))
                    infos[3].append(tel)
                    print("\n")
                    naissance=input("entrer votre date de naissance...>")
                    infos[4].append(naissance)
                    print("\n")
                    date=input("veuillez renseigner la date d aujourd hui...>")
                    infos[5].append(date)
                    
                    fichier=open("Banque.txt", "w")
                    
                    fichier.write("Nom\t   prenom\tProfession\tNuméro \tDate de Naissance  Date d' enregistrement")
                    fichier.write("\n")
                    fichier.write(str(name))
                    fichier.write("\t")
                    fichier.write(str(prenam))
                    fichier.write("\t")
                    fichier.write(str(profession))
                    fichier.write("\t")
                    fichier.write(str(tel))
                    fichier.write("\t")
                    fichier.write(str(naissance))
                    fichier.write("\t")
                    fichier.write(str(date))
                    
                    nom=open("nom.txt", "w")
                    prenom=open("prenom.txt", "w")
                    num=open("numero.txt", "w")
                    naiss=open("naissance.txt","w")
                    date2=open("date.txt", "w")
                    profession2=open("profession.txt", "w")
                    
                    nom.write(str(name))
                    prenom.write(str(prenam))
                    num.write(str(tel))
                    date2.write(str(date))
                    naiss.write(str(naissance))
                    profession2.write(str(profession))
                    

                    fichier.close()
                    nom.close()
                    prenom.close()
                    naiss.close()
                    date2.close()
                    num.close()
                    profession2.close()

                    
                    print("\n")
                    print("Votre Compte a été crée avec succes \n")
                    username=input("Choisisez un Nom d utilisateur...>")
                    montant_init=float(input("Veuillez déposer un montant initiale...>"))
                    cltcompte[0].append(montant_init)
                    compte=open("cltcompte.txt","w")
                    compte.write(str(montant_init))
                    compte.close()
                    
                    
                    
                    print("\n")
                    print("Vos informations de compte sont :\n Nom: {}\n Prenom: {}\n Profession: {}\n Numéro de telephone: {}\n Date de Naissance: {}\nVotre compte a été crée le: {}".format((name),(prenam),(profession),(tel),(naissance),(date)))
                    from random import randint
                    init=0
                    password=""                     
                    choice="0123456789012005047006000904000320170111054005000050003000870040090"        
                    chain=16
                    while (init!=chain):
                            init+=1
                            choice2=randint(0,62)
                            password=password+choice[choice2]
                    print("Votre Nom d utilisateur est:", username)
                    print("Le numero de compte qui vous a été attribué est le: {}".format(password))
                    print("Votre solde Actuel est:",montant_init)
                   
                            
                    
            elif user=="6":
                fichier=open("Banque.txt","w")
                fichier.close()
                compte=open("cltcompte.txt","w")
                compte.close()
                nom=open("nom.txt", "w")
                nom.close()
                num=open("numero.txt", "w")
                num.close()
                naiss=open("naissance.txt","w")
                naiss.close()
                date2=open("date.txt", "w")
                date2.close()
                profession2=open("profession.txt", "w")
                profession2.close()
            elif user=="7":
                fichier2=open("recu.txt","r")
                contenu2=fichier2.read()
                if contenu2==" ":
                    print("Vous n avez recu aucun transfert")
                    
                else:
                    print("Vous avez recu un transfert de :",cltcompte[2])
            elif user=="8":
                compte=open("cltcompte.txt","r")
                compte2=compte.read()
                compte3=compte2.split(" ")
                montant1=compte3[0]
                montant_init=float(montant1)
                transfert=int(input("saisisez le montant a transferer...>"))
                montant_init=montant_init-transfert
                cltcompte[3]=transfert
                print("votre compte a ete debité de:",transfert,"\nlemontant actuel sur votre compte est de:",montant_init)
                print("Transfert effectué avec succes")
                receptnum=int(input("saisissez le numero de compte de reception du transfert"))
                compte=open("cltcompte.txt","w")
                compte.write(str(cltcompte[3]))
                compte.close()
                print(transfert,"a bien été transféré depuis votre compte vers,:", receptnum)
                print("le montant actuel present sur votre compte s éleve a :",montant_init)
            elif user=="9":
                print("Le montant actuel sur votre compte est de:",montant_init)
            elif user=="10":
                fichier=open("Banque.txt","w")
                fichier.close()
                print("Application reinitialisée")
            elif user=="11":
                inpt=input("Terminer?")
                if inpt=="oui" or inpt=="OUI" or inpt=="Oui" or inpt=="OUi" or inpt=="oUI" or inpt=="oUi":
                    while inpt=="oui" or inpt=="OUI" or inpt=="Oui" or inpt=="OUi" or inpt=="oUI" or inpt=="oUi":
                        break
                else:
                    choix=input("Voulez-vous continuez...>")
                    if choix=="oui" or choix=="Oui":
                        user=input("Quelle operation voulez vous effectuer...>")
        else:
            break
