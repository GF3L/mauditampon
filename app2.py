import streamlit as st

# Fonction pour calculer le nombre d'objets nécessaires pour faire un tampon
def calculer_nombre_objets(dimensions_objet, dimensions_tampon):
    # Séparation des dimensions en largeur et longueur pour l'objet et le tampon
    longueur_objet, largeur_objet = map(float, dimensions_objet.split('x'))
    longueur_tampon, largeur_tampon  = map(float, dimensions_tampon.split('x'))
    
    # Calcul du nombre d'objets nécessaire pour chaque dimension
    nb_objets_largeur = largeur_objet // largeur_tampon
    nb_objets_longueur = longueur_objet // longueur_tampon
    
    # Le nombre d'objets nécessaires est le minimum des deux
    return nb_objets_largeur * nb_objets_longueur

# Fonction pour calculer le coût par objet en fonction des matières premières
def calculer_cout_total(couts, nb_objets_cible):
    # Somme des coûts de tous les objets
    cout_total = sum(couts)
    st.write(f"Cout total : {cout_total}")
    # Calcul du coût par objet
    cout_par_objet = cout_total / nb_objets_cible
    return cout_par_objet

def main():
    st.title("Calculateur de coût d'un produit")

    # Inputs pour l'objet 1 (planche de bois)
    st.header("Objet 1 - Planche de bois")
    dim_objet1 = st.text_input("Dimensions objet 1 (en cm, format: longueur x largeur)", "200x15")
    prix_objet1 = st.number_input("Prix objet 1 (en €)", value=28.0)
    nb_objet1 = st.number_input("Nombre d'objets 1", min_value=1, step=1, value=1)

    # Inputs pour l'objet 2 (caoutchouc)
    st.header("Objet 2 - Caoutchouc")
    dim_objet2 = st.text_input("Dimensions objet 2 (en cm, format: longueur x largeur)", "21x29.7")
    prix_objet2 = st.number_input("Prix objet 2 (en €)", value=18.0)
    nb_objet2 = st.number_input("Nombre d'objets 2", min_value=1, step=1, value=1)

    # Inputs pour l'objet 3 (plaque de mousse)
    st.header("Objet 3 - Plaque de mousse")
    dim_objet3 = st.text_input("Dimensions objet 3 (en cm, format: longueur x largeur)", "21x29.7")
    prix_objet3 = st.number_input("Prix objet 3 (en €)", value=10.0)
    nb_objet3 = st.number_input("Nombre d'objets 3", min_value=1, step=1, value=1)

    # Inputs pour les dimensions de l'objet cible (tampon)
    st.header("Dimensions de l'objet cible - Tampon")
    dim_tampon = st.text_input("Dimensions de l'objet cible (en cm, format: longueur x largeur)", "")

    # Bouton pour calculer le résultat
    if st.button("Calculer"):
        # Calcul du nombre d'objets nécessaires pour faire un tampon
        nb_objets_tampon1 = calculer_nombre_objets(dim_objet1, dim_tampon)
        nb_objets_tampon2 = calculer_nombre_objets(dim_objet2, dim_tampon)
        nb_objets_tampon3 = calculer_nombre_objets(dim_objet3, dim_tampon)
        nb_objets_cible = min(nb_objets_tampon1, nb_objets_tampon2, nb_objets_tampon3)

        # Calcul de la somme globale des coûts
        couts = [prix_objet1, prix_objet2, prix_objet3]

        # Calcul du coût par objet cible
        cout_par_objet_cible = calculer_cout_total(couts, nb_objets_cible)

        # Affichage des résultats
        st.subheader("Résultats")
        st.write(f"Nb Objet tampon a partir d'objet 1 : {nb_objets_tampon1}")
        st.write(f"Nb Objet tampon a partir d'objet 2 : {nb_objets_tampon2}")
        st.write(f"Nb Objet tampon a partir d'objet 3 : {nb_objets_tampon3}")
        st.write(f"Nombre d'objets nécessaires pour faire un tampon : {nb_objets_cible}")
        st.write(f"Coût par objet cible : {cout_par_objet_cible:.2f} €")

if __name__ == "__main__":
    main()
