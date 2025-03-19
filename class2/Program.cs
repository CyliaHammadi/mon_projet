/*using System;

public class Livre
{
    // Champs publics
    public string Titre;
    public string Auteur;
    public int AnneePublication;

    // Constructeur pour initialiser les champs
    public Livre(string titre, string auteur, int anneePublication)
    {
        Titre = titre;
        Auteur = auteur;
        AnneePublication = anneePublication;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // Création d'une instance de Livre via le constructeur
        Livre monLivre = new Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943);

        // Affichage des informations du livre
        Console.WriteLine("Titre: " + monLivre.Titre);
        Console.WriteLine("Auteur: " + monLivre.Auteur);
        Console.WriteLine("Année de publication: " + monLivre.AnneePublication);
    }
}*/

/*
using System;

public class Livre
{
    // Champs privés
    private string titre;
    private string auteur;
    private int anneePublication;

    // Propriété pour accéder au champ 'titre'
    public string Titre
    {
        get { return titre; }
        set { titre = value; }
    }

    // Propriété pour accéder au champ 'auteur'
    public string Auteur
    {
        get { return auteur; }
        set { auteur = value; }
    }

    // Propriété pour accéder au champ 'anneePublication'
    public int AnneePublication
    {
        get { return anneePublication; }
        set { anneePublication = value; }
    }

    // Constructeur qui initialise les champs privés
    public Livre(string titre, string auteur, int anneePublication)
    {
        this.titre = titre;
        this.auteur = auteur;
        this.anneePublication = anneePublication;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // Création d'une instance de Livre via le constructeur
        Livre monLivre = new Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943);
        monLivre.Titre ="cylia";
        // Affichage des informations du livre
        Console.WriteLine("Titre: " + monLivre.Titre);
        Console.WriteLine("Auteur: " + monLivre.Auteur);
        Console.WriteLine("Année de publication: " + monLivre.AnneePublication);
    }
}



using System;

public class JeuPierrePapierCiseaux
{
    // Options possibles
    private string[] options = { "Pierre", "Papier", "Ciseaux" };
    private Random random = new Random();

    // Méthode pour démarrer le jeu
    public void Jouer()
    {
        Console.WriteLine("Bienvenue dans le jeu Pierre-Papier-Ciseaux !");
        Console.WriteLine("Entrez votre choix (Pierre, Papier ou Ciseaux) :");

        // Saisie utilisateur
        string choixUtilisateur = Console.ReadLine();

        // Choix aléatoire pour l'ordinateur
        int indexOrdi = random.Next(options.Length);
        string choixOrdi = options[indexOrdi];

        Console.WriteLine("Vous avez choisi : " + choixUtilisateur);
        Console.WriteLine("L'ordinateur a choisi : " + choixOrdi);

        // Comparaison pour déterminer le gagnant
        if (choixUtilisateur.Equals(choixOrdi, StringComparison.OrdinalIgnoreCase))
        {
            Console.WriteLine("Match nul !");
        }
        else if ((choixUtilisateur.Equals("Pierre", StringComparison.OrdinalIgnoreCase) && choixOrdi == "Ciseaux") ||
                 (choixUtilisateur.Equals("Papier", StringComparison.OrdinalIgnoreCase) && choixOrdi == "Pierre") ||
                 (choixUtilisateur.Equals("Ciseaux", StringComparison.OrdinalIgnoreCase) && choixOrdi == "Papier"))
        {
            Console.WriteLine("Vous gagnez !");
        }
        else
        {
            Console.WriteLine("L'ordinateur gagne !");
        }
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // Création de l'instance du jeu et démarrage
        JeuPierrePapierCiseaux jeu = new JeuPierrePapierCiseaux();
        jeu.Jouer();
    }
}

*/
using System;

public class Vehicule
{
    // Propriétés de base
    public string Marque;
    public int VitesseMax;

    // Constructeur de la classe Vehicule
    public Vehicule(string marque, int vitesseMax)
    {
        Marque = marque;
        VitesseMax = vitesseMax;
    }

    // Méthode pour afficher les informations du véhicule
    public void AfficherInfos()
    {
        Console.WriteLine("Marque: " + Marque);
        Console.WriteLine("Vitesse maximale: " + VitesseMax + " km/h");
    }
}

public class Voiture : Vehicule
{
    // Propriété spécifique à la classe Voiture
    public int NombrePortes;

    // Constructeur de la classe Voiture qui appelle le constructeur de la classe de base
    public Voiture(string marque, int vitesseMax, int nombrePortes)
        : base(marque, vitesseMax)
    {
        NombrePortes = nombrePortes;
    }

    // Méthode pour afficher toutes les informations de la voiture
    public void AfficherInfosVoiture()
    {
        // Affiche d'abord les informations de base du véhicule
        AfficherInfos();
        // Affiche l'information spécifique à la voiture
        Console.WriteLine("Nombre de portes: " + NombrePortes);
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // Création d'une instance de Voiture
        Voiture maVoiture = new Voiture("Renault", 220, 5);
        
        // Affichage des informations de la voiture
        maVoiture.AfficherInfosVoiture();
    }
}