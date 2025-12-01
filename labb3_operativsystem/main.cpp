// New[]
// try, catch
// sizeof()
//fixed width integer types like int64_t

#include "malloc.h"
#include <cstdlib>
#include <iostream>



int main() {

	bool running = true;
	size_t chunkSize = 0;
	size_t GiB = 1073741824;
	size_t MiB = 1048576;
	size_t KiB = 1024;
	size_t valueMiB = 0;
	while (running) {

		int chunkChoice = 0;
		std::cout << "Choose chunksize for each allocation" << std::endl;
		std::cout << "[1] - 1 Gibibyte." << std::endl;
		std::cout << "[2] - 1 Kibibyte." << std::endl;
		std::cout << "Choice: ";
		std::cin >> chunkChoice;
		if (chunkChoice == 1) {
			chunkSize = GiB;
			valueMiB = 1024;
		}
		else if (chunkChoice == 2) {
			chunkSize = KiB;
			valueMiB = 1;
		}
		else {
			continue;
		}
		try {
			size_t sizeCounter = 0;
			size_t counterMiB = 0;
			running = false;

			for (size_t i = 0; ; i++) {

				int* myArr = new int[chunkSize / 4];
				sizeCounter += chunkSize;

				std::cout << sizeCounter % MiB << std::endl;
				if (sizeCounter % MiB == 0) {
					counterMiB += valueMiB;
					std::cout << ("1) size of allocated memory: ") << counterMiB << "MiB" << std::endl;
				}
			}

			std::cout << ("2) size of total allocated memory: ") << sizeCounter / 1024 * 1024 << "MiB" << std::endl;
		}
		catch (std::exception const& e) {
			std::cout << "Exception caught: " << e.what() << std::endl;
		}
	}



	return 0;
}