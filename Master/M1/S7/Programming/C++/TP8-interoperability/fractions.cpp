#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>

namespace py=pybind11;

class Fraction{

    public:

        Fraction(int integer_value);
        Fraction(int num, int den);

        float as_float() const;
        bool is_integer() const;

        Fraction operator+(const Fraction& other) const;
        Fraction operator+(int other) const;
        Fraction operator-() const;
        Fraction operator-(const Fraction& other) const;
        Fraction operator-(int other) const;
        Fraction operator*(const Fraction& other) const;
        Fraction operator*(int other) const;

        friend std::ostream& operator<<(std::ostream& os, const Fraction& frac);

    private:

        int _num;
        int _den;

        void simplify();
};

Fraction::Fraction(int integer_value): _num(integer_value), _den(1)
{
}

Fraction::Fraction(int num, int den) : _num(num), _den(den)
{
    if(den==0){
        throw std::runtime_error("Denominator cannot be zero");
    }
    simplify();
}

float Fraction::as_float() const
{
    return _num/_den;
}

bool Fraction::is_integer() const
{
    return (_den == 1);
}

Fraction Fraction::operator+(const Fraction &other) const
{
    Fraction tmp = Fraction(_num * other._den + _den * other._num, _den * other._den);
    tmp.simplify();
    return tmp;
}

Fraction Fraction::operator+(int other) const
{
    return *this + Fraction(other);
}

Fraction Fraction::operator-() const
{
    return Fraction(-_num, _den);
}

Fraction Fraction::operator-(const Fraction &other) const
{
    return *this + (-other);
}

Fraction Fraction::operator-(int other) const
{
    return *this + (-other);
}

Fraction Fraction::operator*(const Fraction &other) const
{
    Fraction tmp = Fraction(_num * other._num, _den * other._den);
    tmp.simplify();
    return tmp;
}

Fraction Fraction::operator*(int other) const
{
    return *this * Fraction(other);
}

void Fraction::simplify()
{
    int a = abs(_num);
    int b = abs(_den);
    int tmp;
    while(b > 0){
        tmp = b;
        b = a % b;
        a = tmp;
    }
    _num = _num/a;
    _den = _den/a;
}

std::ostream &operator<<(std::ostream &os, const Fraction &frac)
{
    os << frac._num << "/" << frac._den;
    return os;
}

// TODO : add the missing constructor, methods (only the public ones) and operator overloads

PYBIND11_MODULE(fractions, m, py::mod_gil_not_used()) {
    py::class_<Fraction>(m, "Fraction")
        .def(py::init<int>())                    // constructor Fraction(int)
        .def("as_float", &Fraction::as_float)    // method      bool as_float() const
        .def(py::self + py::self)                // operator +  for two fractions   (py::self refers to members of the class Fraction)
        .def(py::self + int())                  // operator +  for a fraction (on the left) and an integer (on the right) 
        .def("__str__", [](const Fraction &frac){                    // overloading the special method __str__, to the convertion of a fraction
                                std::stringstream ss;         // into a str representation in python, e.g. when using print()
                                ss << frac;                  // Here we create an anonymous function that converts a fraction into a string
                                return ss.str();                // using the << overload
                            });
}


