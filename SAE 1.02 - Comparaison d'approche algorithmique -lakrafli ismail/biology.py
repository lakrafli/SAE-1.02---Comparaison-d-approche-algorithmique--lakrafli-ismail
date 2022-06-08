#1

def est_base(nom_parametre):
    z="ATGC"
    if nom_parametre in z:
        return True
    else:
        return False


        #2
        def est_adn(tab):
            lettres="TAGC"
            i=0
            a=0

            while i<len(tab):

                if tab[i] in lettres:
                    return True

                else:
                    return False


                    #3
                    def arn(ADN):
                        incre=0
                        t="T"
                        unit=""

                        while incre <len(ADN):

                            if ADN[incre] in t:
                                unit=ADN.replace("T","U")

                            incre=incre +1



                        return unit



                    arn("ATTTGCC")

                    #4
                    def arn_to_codons(bbb):
                        i=0
                        nom=""
                        le_tableau=[]
                        a=0

                        while i < len(bbb):

                            nom=nom+bbb[i]
                            a=a+1

                            if a ==3:

                                le_tableau.append(nom)
                                a=0
                                nom=""


                            i=i+1

                        return le_tableau
                    arn_to_codons('AJNDQSGFBSF')





                    #5
                    from json import *
                    import copy


                    def load_dico_codons_aa(chemin):
                        dossier=open(chemin,"r")
                        a=dossier.read()
                        dossier.close()
                        marche= loads(a)

                        return marche



                        #5
                        def codons_stop(dico):
                            test="zz"
                            letters='AUGC'
                            zzzz=[]
                            tableau=[]
                            keywords = []
                            for A in letters:
                                for U in letters:
                                    for G in letters:
                                        keywords.append(A+U+G)
                            i=0
                            a=list(dico.keys())
                            while i<len(a):
                                zzzz.append(a[i])
                                i+=1

                            # nbr de différence entre les combinaisons et le dico
                            b= len(keywords)-len(zzzz)
                            i=0
                            compt=0
                            while compt<len(zzzz):
                                if keywords[compt] in zzzz :
                                    compt+=1
                                else:
                                    tableau.append(keywords[compt])
                                    compt+=1
                            return tableau





                        #6
                        def codons_to_aa(tableau,dictionnaiiree):
                            i=0
                            a=[]
                            b=list(dictionnaiiree)
                            c=list(dictionnaiiree.values())



                            while i < len(tableau):
                                if tableau[i]in b:
                                    a.append(c[i])

                                i=i+1


                            return a
