#include <gtest/gtest.h>
#include "vector2D.hpp"

TEST(Vector2DInitializationTests, BasicCases){
    Vector2D vec = create_vector2D(2.5, 6.2);
    ASSERT_NEAR(vec.x, 2.5, 0.001);
    ASSERT_NEAR(vec.y, 6.2, 0.001);
}

TEST(Vector2DAdditionTests, BasicCases){
    Vector2D vec1 = create_vector2D(1.0, 2.0);
    Vector2D vec2 = create_vector2D(3.0, 4.0);
    Vector2D result = add(vec1, vec2);
    ASSERT_NEAR(result.x, 4.0, 0.001);
    ASSERT_NEAR(result.y, 6.0, 0.001);
}

TEST(Vector2DSubstractionTests, BasicCases){
    Vector2D vec1 = create_vector2D(5.0, 7.0);
    Vector2D vec2 = create_vector2D(3.0, 4.0);
    Vector2D result = substract(vec1, vec2);
    ASSERT_NEAR(result.x, 2.0, 0.001);
    ASSERT_NEAR(result.y, 3.0, 0.001);
}

TEST(Vector2DDotProductTests, BasicCases){
    Vector2D vec1 = create_vector2D(1.0, 2.0);
    Vector2D vec2 = create_vector2D(3.0, 4.0);
    float result = dotProduct(vec1, vec2);
    ASSERT_NEAR(result, 11.0, 0.001);
}

TEST(Vector2DScalingTests, BasicCases){
    Vector2D vec = create_vector2D(2.0, 3.0);
    float factor = 2.0;
    Vector2D result = scale(vec, factor);
    ASSERT_NEAR(result.x, 4.0, 0.001);
    ASSERT_NEAR(result.y, 6.0, 0.001);
}

TEST(Vector2DAddToTests, BasicCases){
    Vector2D vec1 = create_vector2D(1.0, 2.0);
    Vector2D vec2 = create_vector2D(3.0, 4.0);
    add_to(vec1, vec2);
    ASSERT_NEAR(vec1.x, 4.0, 0.001);
    ASSERT_NEAR(vec1.y, 6.0, 0.001);
}

TEST(Vector2DOperatorOverloadingTests, AdditionOperator){
    Vector2D vec1 = create_vector2D(1.0, 2.0);
    Vector2D vec2 = create_vector2D(3.0, 4.0);
    Vector2D result = vec1 + vec2;
    ASSERT_NEAR(result.x, 4.0, 0.001);
    ASSERT_NEAR(result.y, 6.0, 0.001);
}

TEST(Vector2DOperatorOverloadingTests, UnaryMinusOperator){
    Vector2D vec = create_vector2D(1.0, -2.0);
    Vector2D result = -vec;
    ASSERT_NEAR(result.x, -1.0, 0.001);
    ASSERT_NEAR(result.y, 2.0, 0.001);
}

TEST(Vector2DOperatorOverloadingTests, SubstractionOperator){
    Vector2D vec1 = create_vector2D(5.0, 7.0);
    Vector2D vec2 = create_vector2D(3.0, 4.0);
    Vector2D result = vec1 - vec2;
    ASSERT_NEAR(result.x, 2.0, 0.001);
    ASSERT_NEAR(result.y, 3.0, 0.001);
}

TEST(Vector2DOperatorOverloadingTests, ProductOperator){
    Vector2D vec1 = create_vector2D(2.0, 3.0);
    Vector2D vec2 = create_vector2D(4.0, 5.0);
    float result = dotProduct(vec1, vec2);
    ASSERT_NEAR(result, 23.0, 0.001);
    Vector2D vec3 = vec2 * 2.0;
    ASSERT_NEAR(vec3.x, 8.0, 0.001);
    ASSERT_NEAR(vec3.y, 10.0, 0.001);
}

TEST(Vector2DOperatorOverloadingTests, EqualityOperator){
    Vector2D vec1 = create_vector2D(2.0, 3.0);
    Vector2D vec2 = create_vector2D(2.0, 3.0);
    Vector2D vec3 = create_vector2D(4.0, 5.0);
    ASSERT_TRUE(vec1.x == vec2.x && vec1.y == vec2.y);
    ASSERT_FALSE(vec1.x == vec3.x && vec1.y == vec3.y);
}

TEST(Vector2DStreamOutputTests, BasicCases){
    Vector2D vec = create_vector2D(1.5, -2.5);
    std::ostringstream os;
    os << vec;
    ASSERT_EQ(os.str(), "(1.5, -2.5)");
};
