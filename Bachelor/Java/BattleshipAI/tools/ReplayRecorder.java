package tools;

import java.io.PrintWriter;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

import heuristic.Markov;
import interfacegraphique.GrilleNavaleGraphique;
import joueurs.Bot;
import joueurs.Joueur;
import joueurs.SmartBot;
import logique.Coordonnee;
import logique.Navire;

/**
 * Enregistre des parties réelles au format JSON pour la page web.
 *
 * Ce runner vit à côté du projet et n'en modifie rien : il instancie les
 * classes de `src/` telles quelles et se contente d'observer. La heatmap
 * n'est pas réimplémentée ici, elle est lue depuis {@link Markov} par
 * réflexion, pour que ce qui est affiché soit exactement ce que le bot a
 * calculé.
 *
 * Comme il utilise la réflexion, il faut l'exécuter sur le classpath et non
 * sur le module path :
 *
 * <pre>
 *   javac -cp bin -d bin-tools tools/ReplayRecorder.java
 *   java  -cp bin:bin-tools -Djava.awt.headless=true tools.ReplayRecorder
 * </pre>
 */
public class ReplayRecorder {

    private static final int TAILLE = 10;
    private static final int[] FLOTTE = {5, 4, 3, 3, 2, 2};

    /** Un tour enregistré : le tir, son résultat, et la heatmap d'avant le tir. */
    private static final class Tour {
        Coordonnee tir;
        int resultat;
        boolean ciblage; // le bot finissait un navire déjà touché
        int[][] heatmap; // null pour les bots sans heatmap
    }

    /**
     * SmartBot qui note ce qu'il fait. Sous-classe plutôt que copie : la
     * décision reste celle du bot d'origine.
     */
    private static final class BotEnregistre extends SmartBot {
        final List<Tour> tours = new ArrayList<>();
        private final boolean avecHeatmap;

        BotEnregistre(GrilleNavaleGraphique grille, String heuristique, boolean avecHeatmap) {
            super(grille, heuristique);
            this.avecHeatmap = avecHeatmap;
        }

        @Override
        public Coordonnee choisirAttaque() {
            List<Integer> restants = lireChamp(this, "naviresRestants");
            List<Coordonnee> touches = lireChamp(this, "currentHits");

            Tour t = new Tour();
            t.ciblage = !touches.isEmpty();
            if (avecHeatmap) {
                t.heatmap = heatmapReelle(TAILLE, this.tirsEnvoyes, restants, touches);
            }
            t.tir = super.choisirAttaque();
            tours.add(t);
            return t.tir;
        }

        /** Expose le retour d'attaque, protégé dans Joueur, pour la boucle à sens unique. */
        void encaisser(Coordonnee c, int etat) {
            retourAttaque(c, etat);
            if (!tours.isEmpty()) tours.get(tours.size() - 1).resultat = etat;
        }
    }

    /* ===================== réflexion ===================== */

    @SuppressWarnings("unchecked")
    private static <T> T lireChamp(Object cible, String nom) {
        try {
            Field f = SmartBot.class.getDeclaredField(nom);
            f.setAccessible(true);
            return (T) f.get(cible);
        } catch (ReflectiveOperationException e) {
            throw new IllegalStateException("champ " + nom + " introuvable dans SmartBot", e);
        }
    }

    private static Method computeProbabilityMatrix;

    /** Appelle la vraie méthode de Markov : rien n'est recalculé à la main. */
    private static int[][] heatmapReelle(int n, boolean[][] tirs, List<Integer> restants, List<Coordonnee> touches) {
        try {
            if (computeProbabilityMatrix == null) {
                computeProbabilityMatrix = Markov.class.getDeclaredMethod(
                        "computeProbabilityMatrix", int.class, boolean[][].class, List.class, List.class);
                computeProbabilityMatrix.setAccessible(true);
            }
            return (int[][]) computeProbabilityMatrix.invoke(new Markov(), n, tirs, restants, touches);
        } catch (ReflectiveOperationException e) {
            throw new IllegalStateException("Markov.computeProbabilityMatrix inaccessible", e);
        }
    }

    /* ===================== parties ===================== */

    /** Relève la flotte d'une grille pour pouvoir la rejouer à l'identique. */
    private static List<Navire> releverFlotte(GrilleNavaleGraphique grille) {
        List<Navire> copie = new ArrayList<>();
        for (Navire n : grille.getNavires()) {
            Coordonnee d = n.getDebut(), f = n.getFin();
            boolean vertical = d.getColonne() == f.getColonne() && d.getLigne() != f.getLigne();
            int longueur = vertical ? (f.getLigne() - d.getLigne() + 1) : (f.getColonne() - d.getColonne() + 1);
            copie.add(new Navire(d, longueur, vertical));
        }
        return copie;
    }

    private static GrilleNavaleGraphique grilleAvec(List<Navire> flotte) {
        GrilleNavaleGraphique g = new GrilleNavaleGraphique(TAILLE);
        for (Navire n : flotte) {
            Coordonnee d = n.getDebut(), f = n.getFin();
            boolean vertical = d.getColonne() == f.getColonne() && d.getLigne() != f.getLigne();
            int longueur = vertical ? (f.getLigne() - d.getLigne() + 1) : (f.getColonne() - d.getColonne() + 1);
            if (!g.ajouteNavire(new Navire(d, longueur, vertical))) {
                throw new IllegalStateException("flotte non rejouable : " + n);
            }
        }
        return g;
    }

    /**
     * Fait attaquer un bot jusqu'à ce que la flotte adverse soit coulée, et
     * renvoie les tours enregistrés. Partie à sens unique : on mesure le
     * nombre de tirs nécessaires, pas un duel.
     */
    private static List<Tour> jouerContre(BotEnregistre attaquant, List<Navire> flotte) {
        Bot defenseur = new Bot(grilleAvec(flotte));
        int garde = TAILLE * TAILLE + 1;
        while (garde-- > 0) {
            Coordonnee c = attaquant.choisirAttaque();
            if (c == null) break;
            int res = defenseur.defendre(c);
            attaquant.encaisser(c, res);
            if (res == Joueur.GAMEOVER) break;
        }
        return attaquant.tours;
    }

    /** Rejoue un bot uniforme sur la même flotte, sans heatmap. */
    private static List<Tour> jouerUniforme(List<Navire> flotte) {
        Bot attaquant = new Bot(new GrilleNavaleGraphique(TAILLE));
        Bot defenseur = new Bot(grilleAvec(flotte));
        List<Tour> tours = new ArrayList<>();
        int garde = TAILLE * TAILLE + 1;
        while (garde-- > 0) {
            Coordonnee c = attaquant.choisirAttaque();
            int res = defenseur.defendre(c);
            Tour t = new Tour();
            t.tir = c;
            t.resultat = res;
            t.ciblage = false;
            tours.add(t);
            if (res == Joueur.GAMEOVER) break;
        }
        return tours;
    }

    /* ===================== sortie JSON ===================== */

    private static void ecrireFlotte(StringBuilder sb, List<Navire> flotte) {
        sb.append("[");
        for (int i = 0; i < flotte.size(); i++) {
            Navire n = flotte.get(i);
            Coordonnee d = n.getDebut(), f = n.getFin();
            boolean vertical = d.getColonne() == f.getColonne() && d.getLigne() != f.getLigne();
            int longueur = vertical ? (f.getLigne() - d.getLigne() + 1) : (f.getColonne() - d.getColonne() + 1);
            if (i > 0) sb.append(",");
            sb.append("{\"r\":").append(d.getLigne())
              .append(",\"c\":").append(d.getColonne())
              .append(",\"len\":").append(longueur)
              .append(",\"v\":").append(vertical).append("}");
        }
        sb.append("]");
    }

    private static void ecrirePartie(StringBuilder sb, String bot, List<Navire> flotte, List<Tour> tours) {
        sb.append("{\"bot\":\"").append(bot).append("\",\"shots_to_sink\":").append(tours.size());
        sb.append(",\"fleet\":");
        ecrireFlotte(sb, flotte);
        sb.append(",\"shots\":[");
        for (int i = 0; i < tours.size(); i++) {
            Tour t = tours.get(i);
            if (i > 0) sb.append(",");
            sb.append("{\"r\":").append(t.tir.getLigne())
              .append(",\"c\":").append(t.tir.getColonne())
              .append(",\"res\":").append(t.resultat)
              .append(",\"t\":").append(t.ciblage ? 1 : 0).append("}");
        }
        sb.append("]");

        boolean aHeatmap = !tours.isEmpty() && tours.get(0).heatmap != null;
        if (aHeatmap) {
            sb.append(",\"heat\":[");
            for (int i = 0; i < tours.size(); i++) {
                int[][] h = tours.get(i).heatmap;
                if (i > 0) sb.append(",");
                sb.append("[");
                for (int r = 0; r < TAILLE; r++) {
                    for (int c = 0; c < TAILLE; c++) {
                        if (r > 0 || c > 0) sb.append(",");
                        sb.append(h == null ? 0 : h[r][c]);
                    }
                }
                sb.append("]");
            }
            sb.append("]");
        }
        sb.append("}");
    }

    public static void main(String[] args) throws Exception {
        int nbParties = args.length > 0 ? Integer.parseInt(args[0]) : 3;

        List<String> parties = new ArrayList<>();
        List<Navire> flotteDeReference = null;
        List<Tour> toursDeReference = null;

        for (int i = 0; i < nbParties; i++) {
            GrilleNavaleGraphique tirage = new GrilleNavaleGraphique(TAILLE);
            tirage.placementAuto(FLOTTE);
            List<Navire> flotte = releverFlotte(tirage);

            BotEnregistre bot = new BotEnregistre(new GrilleNavaleGraphique(TAILLE), "Markov", true);
            List<Tour> tours = jouerContre(bot, flotte);
            verifier(tours);

            StringBuilder sb = new StringBuilder();
            ecrirePartie(sb, "Markov", flotte, tours);
            parties.add(sb.toString());
            System.out.printf("Markov, partie %d : %d tirs%n", i + 1, tours.size());

            if (i == 0) { flotteDeReference = flotte; toursDeReference = tours; }
        }

        // Le duel de la page : le tir aléatoire sur la flotte de la partie 1.
        List<Tour> uniforme = jouerUniforme(flotteDeReference);
        StringBuilder sb = new StringBuilder();
        ecrirePartie(sb, "Uniforme", flotteDeReference, uniforme);
        parties.add(sb.toString());
        System.out.printf("Uniforme, même flotte : %d tirs (Markov : %d)%n",
                uniforme.size(), toursDeReference.size());

        StringBuilder out = new StringBuilder();
        out.append("{\"generated_by\":\"tools/ReplayRecorder.java\",")
           .append("\"board\":").append(TAILLE).append(",")
           .append("\"fleet\":[5,4,3,3,2,2],")
           .append("\"note\":\"Parties reellement jouees par les classes de src/. ")
           .append("La heatmap est celle calculee par Markov, lue par reflexion, pas une reimplementation. ")
           .append("Partie a sens unique : le compte est le nombre de tirs pour couler la flotte.\",")
           .append("\"games\":[");
        for (int i = 0; i < parties.size(); i++) {
            if (i > 0) out.append(",");
            out.append(parties.get(i));
        }
        out.append("]}");

        try (PrintWriter w = new PrintWriter("Results/replays.json", "UTF-8")) {
            w.print(out);
        }
        System.out.println("Ecrit Results/replays.json (" + out.length() / 1024 + " Ko)");
    }

    /**
     * Garde-fou : hors phase de ciblage, le tir doit être un maximum de la
     * heatmap. Si ce n'est pas le cas, le JSON ne décrit pas ce que le bot a
     * fait et la page mentirait.
     */
    private static void verifier(List<Tour> tours) {
        for (int i = 0; i < tours.size(); i++) {
            Tour t = tours.get(i);
            if (t.ciblage || t.heatmap == null) continue;
            int max = Integer.MIN_VALUE;
            for (int r = 0; r < TAILLE; r++)
                for (int c = 0; c < TAILLE; c++)
                    if (t.heatmap[r][c] > max) max = t.heatmap[r][c];
            int valeurDuTir = t.heatmap[t.tir.getLigne()][t.tir.getColonne()];
            if (valeurDuTir != max) {
                throw new IllegalStateException(String.format(
                        "tour %d : tir en (%d,%d) de valeur %d alors que le maximum est %d",
                        i, t.tir.getLigne(), t.tir.getColonne(), valeurDuTir, max));
            }
        }
    }
}
