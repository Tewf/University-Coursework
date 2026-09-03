#include <iostream>
#include <string>
#include <boost/program_options.hpp>
#include "utils.hpp"

namespace po = boost::program_options;

int main(int argc, char* argv[]) {

    // Define and parse the program options
    po::options_description desc("Allowed options");
    desc.add_options()
        ("help,h", "produce help message")
        ("method", po::value<std::string>(), "method to use (e.g. gcd)")
        ("first,f", po::value<float>(), "first number")
        ("second,s", po::value<float>(), "second number");

    // States the order of the positional arguments (the name of the method in first, then the two numbers)
    po::positional_options_description p;
    p.add("method", 1);
    p.add("first", 1);
    p.add("second", 1);

    // vm is map whose keys are the names of the options and the values are the values of these options.
    po::variables_map vm;
    try {
        // Parse command line arguments and stores them in vm (takes into account options and positional arguments)
        po::store(po::command_line_parser(argc, argv).options(desc).positional(p).run(), vm);

        // If help option is specified, display help message and exit
        if (vm.count("help")) {
            std::cout << desc << "\n";
            return EXIT_SUCCESS;
        }

        po::notify(vm); // throws on error, so do after help in case there are any problems
    }
    catch (const po::error &ex) {
        // Prints errors message if command line parsing fails
        std::cerr << "Argument error" << ex.what() << '\n';
        std::cout << desc << "\n";
        return EXIT_FAILURE;
    }

    // We check the method option is correctly provided and retrieve its value
    if(!vm.count("method")){
        std::cerr << "Method not provided. Use --help to see usage." << std::endl;
        return EXIT_FAILURE;
    }
    std::string method = vm["method"].as<std::string>();

    // We fetch the two numbers 
    float fa = vm["first"].as<float>();
    float fb = vm["second"].as<float>();

    if(method == "gcd"){
        // gcd only works with integers, so we do the conversion
        int a = static_cast<int>(fa);
        int b = static_cast<int>(fb);
        std::cout << "The gcd of " << a << " and " << b << " is " << gcd(a, b) << std::endl;
    } else {
        std::cerr << "Unknown method: " << method << ". Use --help to see usage." << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS; 
}