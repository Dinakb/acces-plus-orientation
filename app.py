import streamlit as st

st.set_page_config(page_title="Accès+ Orientation", layout="centered")
st.title("🎓 Accès+ – Ta boussole pour l’avenir")

st.markdown("""
Bienvenue sur **Accès+**, la plateforme qui t'aide à mieux te connaître, découvrir des parcours ambitieux, et surtout à oser croire en toi. 

🧭 Réponds aux questions ci-dessous pour recevoir des conseils adaptés à ton profil, découvrir des études que tu ne connais peut-être pas, et construire ton propre plan pour avancer vers ce que TU veux vraiment.
""")

niveau = st.selectbox("Quelle est ta classe actuelle ?", ["Seconde", "Première", "Terminale"])

if niveau == "Seconde":
    matieres = st.multiselect("Quelles matières préfères-tu ?", ["Maths", "Français", "Histoire-Géo", "SVT / Physique", "SES", "Langues", "Autre"])
    activite = st.radio("Que fais-tu facilement, sans te forcer ?", ["Résoudre des problèmes", "Écrire ou argumenter", "Travailler en équipe", "Aider les autres", "Créer ou inventer"])
    connais_prepa = st.radio("As-tu déjà entendu parler de la prépa ou des grandes écoles ?", ["Oui", "Non", "Pas vraiment"])
    if connais_prepa != "Oui":
        st.info("📘 Une prépa, c’est une formation publique (souvent gratuite), exigeante mais très encadrée, qui ouvre vers les grandes écoles comme HEC, l’ENS, Sciences Po, Polytechnique… Et c’est accessible, même pour toi !")

elif niveau == "Première":
    specialites = st.multiselect("Quelles spécialités as-tu choisies ?", ["Maths", "SES", "HGGSP", "HLP", "SVT", "Physique-Chimie", "Langues", "Autre"])
    importance = st.radio("Tu accordes quelle importance à ton orientation aujourd’hui ?", ["Très importante", "Moyenne", "Pas encore réfléchi"])
    vision = st.radio("Tu te verrais faire des études longues ?", ["Oui", "Je ne sais pas", "Non"])
    connais_filiere = st.multiselect("Tu connais ces filières ?", ["Prépa", "Sciences Po", "BUT", "BTS", "Licence", "Je ne sais pas ce que c’est"])

elif niveau == "Terminale":
    idee = st.radio("Tu sais déjà ce que tu veux faire après le bac ?", ["Oui", "Un peu", "Pas du tout"])
    attirance = st.multiselect("Quels types de formations t’attirent ?", ["Prépa", "BTS", "BUT", "Licence", "École post-bac", "Je ne sais pas"])
    freins = st.multiselect("Qu’est-ce qui te freine aujourd’hui dans tes choix ?", ["Manque d’informations", "Peur d’échouer", "Pas confiance en moi", "Personne pour m’aider", "Rien, je suis prêt(e)"])

if st.button("👉 Voir mes pistes et conseils"):
    st.success("Bravo d’avoir pris le temps de réfléchir à ton orientation !")
    st.markdown("### 🎯 Ce que tu peux faire maintenant :")
    st.markdown("- **Explorer des filières qui te correspondent** (en fonction de tes réponses)")
    st.markdown("- **Découvrir des études ambitieuses expliquées simplement** : prépa, BUT, BTS, fac, etc.")
    st.markdown("- **Lire des fiches fiables issues de l’ONISEP, Parcoursup et du Ministère**")
    st.markdown("- **Télécharger un plan d’action simple pour avancer dès cette semaine**")

    with st.expander("📘 Exemple : Qu’est-ce qu’une prépa ?"):
        st.markdown(\"\"\"
        Une prépa (CPGE) est une formation gratuite et exigeante, qui prépare en 2 ans aux concours des grandes écoles (commerce, ingénieur, ENS, etc.). Elle s’adresse aux élèves motivés, curieux et prêts à travailler sérieusement.

        Il existe plusieurs types de prépas : 
        - ECG (économique & commerciale, pour les élèves venant de spécialités SES/Maths par exemple)
        - MPSI, PCSI, BCPST (scientifiques)
        - Lettres (hypokhâgne/khâgne)
        - TSI (prépa technologique, pour STI2D notamment)

        Et surtout : il n’est pas nécessaire d’être « un génie » pour y arriver. Ce qu’il faut, c’est du travail, de l’envie, de la méthode. Et tu peux être accompagné(e) !
        \"\"\")

st.markdown(\"\\n---\\n👩‍🎓 Projet imaginé par **Dina Klabi**, étudiante en prépa ECG au lycée Michelet\")

