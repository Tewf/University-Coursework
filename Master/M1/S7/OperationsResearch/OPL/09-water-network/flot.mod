/*********************************************
 * OPL 12.6.0.0 Model
 * Gestion d'un reseau d'eau
 * Auteurs : Hadrien Cambazard, Maxime Ogier
 *********************************************/

//Donnees
// Vous ne devez pas modifier le code existant pour charger les donnees, 
// mais vous pouvez ajouter le code que vous voulez
int nbS = ...;      // nombre de sources
int nbD = ...;      // nombre de destinations
int nbK = ...;      // nombre de stations intermediaires
range sources = 1..nbS;                         // ensemble des sources
range destinations = nbS+nbK+1..nbS+nbK+nbD;    // ensemble des destinations
range stations = nbS+1..nbS+nbK;                // ensemble des stations
range points = 1..nbS+nbK+nbD;                  // ensemble de tous les points
int O[sources] = ...;               // quantite maximale fournie par les sources    
int R[destinations] = ...;          // demande aux destinations
int pRest[stations] = ...;          // probabilite de restitution de l'eau par les stations
int capa[points][points] = ...;     // capacites du reseau : definie pour toute paire de points
                                    // 0 signifie que l'arc n'existe pas
{int} deltaPlus[points] = ...;      // ids des sucesseurs de chaque point
{int} deltaMoins[points] = ...;     // ids des predecesseurs de chaque point


//Variables


//Objectif
minimize ;

//Contraintes
subject to {

}

/* Affichage de la solution */
execute {
    writeln("Post-traitement: ");
    writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 