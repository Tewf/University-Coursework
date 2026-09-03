/**
 * @file vector2D.hpp
 * @author Ernest Foussard (ernest.foussard@univ-grenoble-alpes.fr)
 * @brief Implementation of 2D vectors
 * @version 0.1
 * @date 2026-01-19
 * 
 * @copyright CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
 * 
 */

#pragma once
#include <iostream>
#include <stdexcept>

/**
 * @brief Structure for 2D vectors
 * 
 * To create a new vector: 
 *     Vector2D myVector;
 * 
 * To access its components
 *     myVector.x
 *  
 */
struct Vector2D{
    float x;
    float y;
};

/**
 * @brief Create a vector2D object
 * 
 * @param x first element of the vector
 * @param y second element of the vector
 * @return the newly created vector
 */
Vector2D create_vector2D(float x, float y);


/**
 * @brief print a vector2D object in the standard output
 * 
 * @param vec the vector to be printed
 */
void print_vector(const Vector2D& vec);

/**
 * @brief Overload of operator << 
 * 
 * Overloading this operator will allow to use streams 
 * to print to vectors e.g.
 *    std::cout << my_vector;
 * 
 * @param os output stream in which the contents of the vector will be printed 
 * @param vec vector to be printed
 * @return std::ostream& the output stream passed as input
 */
std::ostream& operator<<(std::ostream& os, const Vector2D& vec);


/* Basic operations on vectors */

/**
 * @brief Compute the sum of two vector
 * 
 * @param vec1 first vector
 * @param vec2 second vector
 * @return sum of the two vectors
 */
Vector2D add(const Vector2D& vec1, const Vector2D& vec2);

/**
 * @brief Adds vec2 to vec1
 * 
 * @param vec1 target vector to which vec2 will be added
 * @param vec2 vector to add to vec1
 */
void add_to(Vector2D& vec1, const Vector2D& vec2);

/**
 * @brief Substract two vectors
 * 
 * @param vec1 left operand of the substraction
 * @param vec2 right operand
 * @return substraction of the two vectors
 */
Vector2D substract(const Vector2D& vec1, const Vector2D& vec2);

/**
 * @brief Scales the vector by the factor
 * 
 * @param vec vector to be scaled
 * @param factor scaling factor
 * @return scaled vector
 */
Vector2D scale(const Vector2D& vec, float factor);

/**
 * @brief Computes the dot product of two vectors
 * 
 * @param vec1 first vector
 * @param vec2 second vector
 * @return dot product of the two vectors
 */
float dotProduct(const Vector2D& vec1, const Vector2D& vec2);

/* Operator overloading */

/**
 * @brief Overload of operator +
 * 
 * @param vec1 first vector
 * @param vec2 second vector
 * @return sum of the two vectors
 */
Vector2D operator+(const Vector2D& vec1, const Vector2D& vec2);

/**
 * @brief Overload of unary operator -
 * 
 * @param vec the vector
 * @return opposite of the vector given as a parameter 
 */
Vector2D operator-(const Vector2D& vec);

/**
 * @brief Overload of binary operator -
 * 
 * @param vec1 left operand of the substraction
 * @param vec2 right operand of the substraction
 * @return 
 */
Vector2D operator-(const Vector2D& vec1, const Vector2D& vec2);

/**
 * @brief Overload of binary operator * for scaling product
 * 
 * @param vec vector to scale
 * @param factor scaling factor
 * @return scaled vector
 */
Vector2D operator*(const Vector2D& vec, float factor);

/**
 * @brief Overload of binary operator * for dot product
 *  
 * @param vec1 first vector 
 * @param vec2 second vector
 * @return dot product of the two vectors
 */
float operator*(const Vector2D& vec1, const Vector2D& vec2);

/**
 * @brief Overload of equality operator == for vectors
 * 
 * @param vec1 left operand
 * @param vec2 right operand
 * @return true if all components of the vectors are equal
 * @return false otherwise
 */
bool operator==(const Vector2D& vec1, const Vector2D& vec2);